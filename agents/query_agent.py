from datapizza.agents import Agent
from .config import WikiConfig
from .schemas import WIKI_RESEARCH_PROMPT, SOURCE_WITH_ANCHORS_PROMPT, SOURCE_DEEP_DIVE_PROMPT
from .tools import file_tools
from .tools.transform_tools import transform_anchors_deterministic


class QueryAgent:
    """Three independent agents with deterministic tool separation.

    - Wiki Agent (wiki/ only): answers from wiki pages
    - Source Agent A (processed_documents/ only): starts from wiki anchors, explores outward
    - Source Agent B (processed_documents/ only): deep dive from scratch, no wiki hints
    """

    def __init__(self, config: WikiConfig):
        self.config = config

        # Wiki Agent — wiki/ tools ONLY
        self._wiki_agent = Agent(
            name="wiki_agent",
            client=config.create_client(config.model_query),
            system_prompt=WIKI_RESEARCH_PROMPT,
            tools=[
                file_tools.read_wiki_page,
                file_tools.list_wiki_pages,
                file_tools.search_wiki,
            ],
            max_steps=12,
        )

        # Source Agent A — has wiki anchors, explores outward from them
        self._source_agent_a = Agent(
            name="source_agent_anchors",
            client=config.create_client(config.model_query),
            system_prompt=SOURCE_WITH_ANCHORS_PROMPT,
            tools=[file_tools.read_source_document],
            max_steps=8,
        )

        # Source Agent B — no wiki hints, deep dives autonomously
        self._source_agent_b = Agent(
            name="source_agent_deep_dive",
            client=config.create_client(config.model_query),
            system_prompt=SOURCE_DEEP_DIVE_PROMPT,
            tools=[
                file_tools.list_source_documents,
                file_tools.read_source_document,
                file_tools.get_document_info,
            ],
            max_steps=10,
        )

    def ask_wiki(self, question: str) -> str:
        """Stage 1: Wiki Agent answers from wiki pages only."""
        result = self._wiki_agent.run(
            f"Domanda dell'utente: {question}\n\n"
            f"Rispondi usando SOLO le pagine wiki. Usa il formato Risposta/Fonti richiesto."
        )
        return transform_anchors_deterministic(_extract_text(result))

    def ask_deep(self, question: str, wiki_report: str) -> str:
        """Stage 2 with wiki anchors: Source Agent A explores from anchors outward."""
        useless = _is_useless_report(wiki_report)

        if useless:
            # No wiki anchors — use Agent B for autonomous deep dive
            prompt = (
                f"Domanda dell'utente: {question}\n\n"
                f"Il Wiki Agent non ha trovato nulla. Fai un deep dive autonomo "
                f"tra tutti i documenti in processed_documents/ per trovare la risposta."
            )
            result = self._source_agent_b.run(prompt)
        else:
            # Has wiki anchors — use Agent A to explore from anchors
            prompt = (
                f"Domanda dell'utente: {question}\n\n"
                f"Rapporto del Wiki Agent con gli anchor da cui partire:\n\n{wiki_report}\n\n"
                f"Parti dagli anchor nella sezione 'Ancora per approfondimento'. "
                f"Usa read_source_document con context_lines=50, poi allarga se serve."
            )
            result = self._source_agent_a.run(prompt)

        return transform_anchors_deterministic(_extract_text(result))


def _is_useless_report(report: str) -> bool:
    """Check if the wiki report indicates no useful results were found."""
    no_results_markers = [
        "nessuna informazione trovata",
        "fonti: nessuna",
        "no results found",
        "nessun risultato",
        "non ho trovato",
    ]
    report_lower = report.lower()
    return any(marker in report_lower for marker in no_results_markers)


def _extract_text(result):
    if result is None:
        return ""
    if hasattr(result, "text"):
        return result.text
    if isinstance(result, str):
        return result
    return str(result)
