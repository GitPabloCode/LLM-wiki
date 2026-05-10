from datapizza.agents import Agent
from datapizza.memory import Memory
from datapizza.tools import tool
from .config import WikiConfig
from .query_agent import _is_useless_report
from .schemas import ORCHESTRATOR_PROMPT


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
            """Ingest a document: chunk, extract knowledge, write/update wiki pages."""
            from .ingest_agent import IngestAgent
            agent = IngestAgent(config)
            return agent.ingest(doc_name)

        @tool
        def wiki_query(question: str) -> str:
            """Answer a question by researching the wiki ONLY (no source documents).

            Call FIRST when the user asks a question.
            The result is stored and returned directly to the user — the orchestrator
            MUST NOT modify or add to it. If the report shows no results, call
            wiki_deepen immediately.
            """
            from .query_agent import QueryAgent
            agent = QueryAgent(config)
            result = agent.ask_wiki(question)
            orchestrator_self._last_report = result
            orchestrator_self._last_question = question

            # Add deepen hint if wiki found results
            if not _is_useless_report(result):
                result += "\n\n---\n*Scrivi \"approfondisci\" per leggere i documenti originali.*"

            orchestrator_self._direct_response = result
            return result  # LLM sees this to decide if auto-deepen is needed

        @tool
        def wiki_deepen() -> str:
            """Read source documents to give a deeper answer.

            Call when wiki_query returned no results OR user asks to deepen.
            Uses stored wiki context. Result goes directly to user.
            """
            if not orchestrator_self._last_report:
                return "Nessuna ricerca wiki precedente da approfondire."
            from .query_agent import QueryAgent
            agent = QueryAgent(config)
            result = agent.ask_deep(
                orchestrator_self._last_question,
                orchestrator_self._last_report,
            )
            orchestrator_self._direct_response = result
            return result  # LLM sees this but user gets _direct_response

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
