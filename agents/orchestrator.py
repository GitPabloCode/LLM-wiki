from datapizza.agents import Agent
from datapizza.memory import Memory
from datapizza.tools import tool
from .config import WikiConfig
from .query_agent import QueryAgent
from .schemas import WIKI_CONVENTIONS


ORCHESTRATOR_PROMPT = f"""You are the Orchestrator of LLM Wiki, a system that maintains a personal knowledge base using specialized AI agents.

Your role:
1. Talk to the user naturally and helpfully in Italian or English (match the user's language)
2. When the user requests something that requires a specialized agent, delegate silently
3. When the sub-agent finishes, synthesize the result and continue the conversation

DELEGATION RULES:
- **INGEST**: user asks to process/ingest/add a document, do ingestion, "aggiungi il documento X", "processa il documento Y", etc.
  → Delegate to wiki_ingest with the document name

- **QUERY**: user asks substantive questions about document content, "cos'è X?", "spiegami Y", "che numero ha X?", "quali sono i componenti di...?"
  → Delegate to wiki_query with the question. The pipeline (Wiki Router → Source Agent) runs automatically.
  → After wiki_query returns, do NOT add any text. Just stop.
  → If the user asks to go deeper ("approfondisci", "vai più a fondo") → call wiki_deepen.

- **LINT**: user asks to check/verify/health-check the wiki, "controlla il wiki", "ci sono contraddizioni?", "il wiki è aggiornato?", "fai un health check"
  → Delegate to wiki_lint

- **NORMAL CHAT**: greetings, "quali documenti abbiamo?", "mostrami l'indice", "come funziona il sistema?"
  → Answer directly without delegating

IMPORTANT:
- For INGEST and LINT: after delegation, present the result clearly and ask if the user wants to explore further.
- For QUERY: the response already includes research from source documents. Present it to the user as received.
- wiki_deepen uses the stored wiki research context — do NOT pass the question again.
- Do NOT say "I'm delegating to..." — activate the sub-agent transparently.
- CRITICAL: NEVER modify, remove, rewrite, or reformat [doc_name ¶N] references in the agent's response. Output them EXACTLY as the agent wrote them. These are citations that must reach the user unchanged.

Wiki conventions for your reference:
{WIKI_CONVENTIONS}
"""


class OrchestratorAgent:
    """Interactive chatbot that routes user requests to specialized sub-agents.

    Query responses bypass the orchestrator LLM deterministically:
    wiki_query and wiki_deepen store their result in _direct_response.
    chat() returns _direct_response directly, ignoring LLM text output.
    This guarantees [doc_name ¶N] references reach the user unmodified.
    """

    def __init__(self, config: WikiConfig):
        self.config = config
        self._last_report: str | None = None
        self._last_question: str | None = None
        self._direct_response: str | None = None

    def start(self):
        config = self.config
        orchestrator_self = self

        @tool
        def wiki_ingest(doc_name: str) -> str:
            """Ingest a document: study it and create/update wiki pages. Documents are pre-split at conversion time."""
            print(f"\n[orchestrator] avvio ingest per '{doc_name}'...")
            from .ingest_agent import IngestAgent

            doc_path = config.processed_dir / doc_name / "document.md"
            if not doc_path.exists():
                return f"Error: document not found at {doc_path}"

            agent = IngestAgent(config)
            return agent.ingest(doc_name)

        @tool
        def wiki_query(question: str) -> str:
            """Answer a question: Wiki Router finds sources, Source Agent researches.

            Always call FIRST for user questions. The pipeline is always:
            wiki_router → source_agent, never wiki-only.
            """
            agent = QueryAgent(config)

            # Stage 1: Wiki Router collects anchors
            routing_report = agent.route(question)
            orchestrator_self._last_report = routing_report
            orchestrator_self._last_question = question

            # Stage 2: Source Agent researches from anchors (always)
            final_answer = agent.research(question, routing_report)
            orchestrator_self._direct_response = final_answer
            return final_answer

        @tool
        def wiki_deepen() -> str:
            """Re-research source documents with expanded context.

            Call when the user asks to go deeper on the previous answer.
            Uses stored routing context.
            """
            if not orchestrator_self._last_report:
                return "Nessuna ricerca wiki precedente da approfondire."
            agent = QueryAgent(config)
            result = agent.research(
                orchestrator_self._last_question,
                orchestrator_self._last_report,
            )
            orchestrator_self._direct_response = result
            return result

        @tool
        def wiki_lint() -> str:
            """Run a full wiki health check."""
            from .lint_agent import LintAgent
            agent = LintAgent(config)
            return agent.lint()

        self._agent = Agent(
            name="wiki_orchestrator",
            client=config.create_client(config.model_orchestrator),
            system_prompt=ORCHESTRATOR_PROMPT,
            tools=[wiki_ingest, wiki_query, wiki_deepen, wiki_lint],
            stateless=False,
            memory=Memory(),
        )

    def chat(self, message: str) -> str:
        """Send a message to the orchestrator and get the response.

        Query responses bypass the LLM: _direct_response is set by wiki_query/wiki_deepen
        and returned directly, guaranteeing citations reach the user unmodified.
        """
        if not hasattr(self, "_agent"):
            return "Error: orchestrator not started. Call start() first."

        self._direct_response = None
        result = self._agent.run(message)

        if self._direct_response is not None:
            return self._direct_response

        if result is None:
            return ""
        if hasattr(result, "text"):
            return result.text
        return str(result)
