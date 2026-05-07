from datapizza.agents import Agent
from .config import WikiConfig
from .schemas import QUERY_PROMPT
from .tools import file_tools


class QueryAgent:
    """Agent that navigates the wiki and retrieves ground-truth answers from source documents."""

    def __init__(self, config: WikiConfig):
        self.config = config

        tools = [
            file_tools.read_wiki_page,
            file_tools.list_wiki_pages,
            file_tools.search_wiki,
            file_tools.read_document_around_anchors,
            file_tools.read_source_document,
        ]

        self._agent = Agent(
            name="wiki_query",
            client=config.create_client(),
            system_prompt=QUERY_PROMPT,
            tools=tools,
            max_steps=15,
        )

    @property
    def agent(self) -> Agent:
        return self._agent

    def ask(self, question: str) -> str:
        """Ask a question and get a cited answer from source documents."""
        result = self._agent.run(question)
        return _extract_text(result)


def _extract_text(result):
    if result is None:
        return ""
    if hasattr(result, "text"):
        return result.text
    if isinstance(result, str):
        return result
    return str(result)
