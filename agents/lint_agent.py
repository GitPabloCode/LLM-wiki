from datapizza.agents import Agent
from .config import WikiConfig
from .schemas import LINT_PROMPT
from .tools import file_tools, index_tools


class LintAgent:
    """Standalone lint agent for orchestrator-initiated full-wiki health checks.

    Created fresh per lint by the orchestrator — no persistent state.
    """

    def __init__(self, config: WikiConfig):
        self.config = config

    def lint(self) -> str:
        """Create a fresh lint agent and check the entire wiki."""
        lint_agent = Agent(
            name="wiki_lint_worker",
            client=self.config.create_client(self.config.model_lint),
            system_prompt=LINT_PROMPT,
            tools=[
                file_tools.read_wiki_page,
                file_tools.write_wiki_page,
                file_tools.delete_wiki_page,
                file_tools.list_wiki_pages,
                file_tools.search_wiki,
                index_tools.update_index,
            ],
            max_steps=20,
        )

        result = lint_agent.run(
            "Run a complete health check on the wiki. "
            "Read index.md and overview.md first, then systematically check "
            "all pages across all categories for issues. "
            "Fix issues you can fix directly. "
            "Save a lint report to lint_reports/ with today's date in the filename. "
            "Update the index after saving the lint report."
        )
        return _extract_text(result)


def _extract_text(result):
    if result is None:
        return ""
    if hasattr(result, "text"):
        return result.text
    if isinstance(result, str):
        return result
    return str(result)
