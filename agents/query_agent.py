from datapizza.agents import Agent
from .config import WikiConfig
from .schemas import WIKI_ROUTER_PROMPT, SOURCE_RESEARCH_PROMPT, SOURCE_DEEP_DIVE_PROMPT
from .tools import file_tools
from .tools.transform_tools import transform_anchors_deterministic


class QueryAgent:
    """Two-agent pipeline: Wiki Router finds sources, Source Agent researches.

    - Wiki Router (wiki/ only, max 4 steps): collects document anchors
    - Source Agent (processed_documents/ only): researches from anchors, produces answer
    - Source Deep Dive (fallback): autonomous exploration when wiki has nothing
    """

    def __init__(self, config: WikiConfig):
        self.config = config

        self._wiki_router = Agent(
            name="wiki_router",
            client=config.create_client(config.model_query),
            system_prompt=WIKI_ROUTER_PROMPT,
            tools=[
                file_tools.read_wiki_page,
                file_tools.list_wiki_pages,
                file_tools.search_wiki,
            ],
            max_steps=4,
        )

        self._source_agent = Agent(
            name="source_agent",
            client=config.create_client(config.model_query),
            system_prompt=SOURCE_RESEARCH_PROMPT,
            tools=[
                file_tools.read_source_document,
                file_tools.get_document_info,
            ],
            max_steps=8,
        )

        self._source_deep_dive = Agent(
            name="source_deep_dive",
            client=config.create_client(config.model_query),
            system_prompt=SOURCE_DEEP_DIVE_PROMPT,
            tools=[
                file_tools.list_source_documents,
                file_tools.read_source_document,
                file_tools.get_document_info,
                file_tools.grep_source_document,
            ],
            max_steps=10,
        )

    def route(self, question: str) -> str:
        """Stage 1: Wiki Router finds relevant documents and anchors."""
        result = self._wiki_router.run(
            f"Domanda dell'utente: {question}\n\n"
            f"Trova i documenti e gli anchor rilevanti. NON rispondere alla domanda."
        )
        return transform_anchors_deterministic(_extract_text(result))

    def research(self, question: str, routing_report: str) -> str:
        """Stage 2: Source Agent researches from routing anchors, produces full answer."""
        has_anchors = _has_anchors(routing_report)

        if has_anchors:
            prompt = (
                f"Domanda dell'utente: {question}\n\n"
                f"Routing report dal Wiki Router:\n\n{routing_report}\n\n"
                f"Parti dagli anchor forniti. Inizia la risposta con il preambolo (Overview) del routing report."
            )
            result = self._source_agent.run(prompt)
        else:
            prompt = (
                f"Domanda dell'utente: {question}\n\n"
                f"Il Wiki Router non ha trovato anchor specifici, ma ecco il contesto che ha raccolto:\n\n"
                f"{routing_report}\n\n"
                f"Usa queste informazioni per orientare la ricerca: quali documenti esplorare, quali termini cercare."
            )
            result = self._source_deep_dive.run(prompt)

        return transform_anchors_deterministic(_extract_text(result))

    def ask_wiki(self, question: str) -> str:
        """Legacy alias for route()."""
        return self.route(question)

    def ask_deep(self, question: str, routing_report: str) -> str:
        """Legacy alias for research()."""
        return self.research(question, routing_report)


def _has_anchors(report: str) -> bool:
    """Check if the routing report contains usable anchors."""
    import re
    return bool(re.search(r'\[(\w[\w-]*)\s+¶\d', report))


def _needs_source_lookup(report: str) -> bool:
    """Always True: the pipeline always does wiki→source for substantive questions."""
    return True


# Backward compatibility
_is_useless_report = _needs_source_lookup


def _extract_text(result):
    if result is None:
        return ""
    if hasattr(result, "text"):
        return result.text
    if isinstance(result, str):
        return result
    return str(result)
