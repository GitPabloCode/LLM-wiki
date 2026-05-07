from datapizza.agents import Agent
from datapizza.tools import tool
from .config import WikiConfig
from .schemas import CHUNK_SUMMARIZE_PROMPT, WIKI_GENERATE_PROMPT
from .tools import file_tools, index_tools


class IngestAgent:
    """Agent that reads processed documents and creates/updates wiki pages via Map-Reduce."""

    def __init__(self, config: WikiConfig):
        self.config = config
        self._extract_text = _extract_text

        # Stage 1 summarizer: no tools, just reads chunk and outputs summary
        self._summarizer = Agent(
            name="chunk_summarizer",
            client=config.create_client(),
            system_prompt=CHUNK_SUMMARIZE_PROMPT,
            tools=[],
            max_steps=1,
        )

        # Build the ingestion pipeline tool (captures config + summarizer)
        ingest_pipeline = _make_ingestion_pipeline(config, self._summarizer, self._extract_text)

        # Stage 2 agent: receives summaries, writes wiki pages
        wiki_tools = [
            file_tools.read_wiki_page,
            file_tools.write_wiki_page,
            file_tools.list_wiki_pages,
            index_tools.update_index,
            index_tools.append_log,
            index_tools.update_overview,
            ingest_pipeline,
        ]

        self._agent = Agent(
            name="wiki_ingest",
            client=config.create_client(),
            system_prompt=WIKI_GENERATE_PROMPT,
            tools=wiki_tools,
            max_steps=30,
        )

    @property
    def agent(self) -> Agent:
        return self._agent

    def ingest(self, doc_name: str) -> str:
        """Run the full Map-Reduce ingestion pipeline for a document."""
        result = self._agent.run(
            f"Ingest document '{doc_name}'. "
            f"First call run_ingestion_pipeline(doc_name=\"{doc_name}\") to summarize all chunks, "
            f"then generate all wiki pages. "
            f"Pass doc_name=\"{doc_name}\" to every write_wiki_page call. "
            f"Log format: \"ingest | {doc_name} — completed (N chunks)\""
        )
        return self._extract_text(result)


def _extract_text(result):
    if result is None:
        return ""
    if hasattr(result, "text"):
        return result.text
    if isinstance(result, str):
        return result
    return str(result)


def _make_ingestion_pipeline(config: WikiConfig, summarizer: Agent, extract):
    @tool
    def run_ingestion_pipeline(doc_name: str) -> str:
        """Stage 1 Map: chunk a document and summarize every chunk.

        Returns the combined chunk summaries as a single markdown document
        for the Stage 2 Reduce phase.
        """
        from .chunking import chunk_document

        doc_path = config.processed_dir / doc_name / "document.md"
        if not doc_path.exists():
            return f"Error: document '{doc_name}' not found"

        chunks = chunk_document(doc_path, config.chunk_target_tokens, config.token_encoding)

        summaries = []
        for chunk in chunks:
            task = (
                f"Chunk {chunk['index'] + 1}/{chunk['total']} of document '{doc_name}' "
                f"({chunk['token_count']} tokens):\n\n{chunk['content']}"
            )
            result = summarizer.run(task)
            summary = extract(result)
            summaries.append(f"## Chunk {chunk['index'] + 1}/{chunk['total']}\n\n{summary}")

        summaries_md = f"# Chunk Summaries: {doc_name}\n\n" + "\n\n---\n\n".join(summaries)

        summaries_path = config.processed_dir / doc_name / "chunk_summaries.md"
        summaries_path.write_text(summaries_md, encoding="utf-8")

        return summaries_md

    return run_ingestion_pipeline
