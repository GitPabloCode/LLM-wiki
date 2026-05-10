from datapizza.agents import Agent
from datapizza.tools import tool
from .config import WikiConfig
from .schemas import CHUNK_ANALYZE_PROMPT, INGEST_AGENT_PROMPT, POST_INGEST_LINT_PROMPT
from .tools import file_tools, index_tools


class IngestAgent:
    """Two-level ingestion: Chunk Analyzer (per-chunk extraction) + Main Agent (merge + write).

    Created fresh per ingestion by the orchestrator — no persistent state.
    """

    def __init__(self, config: WikiConfig):
        self.config = config

    def ingest(self, doc_name: str) -> str:
        """Create fresh agents and run the two-level ingestion pipeline.

        Small docs (≤200K tokens): read full document, process directly.
        Large docs (>200K tokens): chunk, extract per chunk, merge analyses.
        Final step: post-ingestion lint.
        """
        config = self.config

        analyze_chunks = _make_analyze_chunks(config)

        post_ingest_lint = Agent(
            name="wiki_post_ingest_lint",
            client=config.create_client(config.model_lint),
            system_prompt=POST_INGEST_LINT_PROMPT,
            tools=[
                file_tools.read_wiki_page,
                file_tools.write_wiki_page,
                file_tools.delete_wiki_page,
                file_tools.list_wiki_pages,
            ],
            max_steps=15,
        )

        main_agent = Agent(
            name="wiki_ingest_main",
            client=config.create_client(config.model_main_ingest),
            system_prompt=INGEST_AGENT_PROMPT,
            tools=[
                file_tools.get_document_info,
                file_tools.read_source_document,
                analyze_chunks,
                file_tools.read_wiki_page,
                file_tools.write_wiki_page,
                file_tools.list_wiki_pages,
                index_tools.update_index,
                index_tools.append_log,
                index_tools.update_overview,
            ],
            can_call=[post_ingest_lint],
            max_steps=30,
        )

        result = main_agent.run(
            f"Ingest document '{doc_name}'. "
            f"First call get_document_info(doc_name=\"{doc_name}\") to check size "
            f"and decide between direct-read and chunked path. "
            f"Pass doc_name=\"{doc_name}\" to every write_wiki_page call. "
            f"When you finish ALL wiki pages, as FINAL step call wiki_post_ingest_lint "
            f"with the list of pages you created or updated. "
            f"Log format: \"ingest | {doc_name} — completed\""
        )
        return _extract_text(result)


def _make_analyze_chunks(config: WikiConfig):
    @tool
    def analyze_document_chunks(doc_name: str) -> str:
        """Chunk a large document and extract structured analyses from each chunk.

        Use this when get_document_info shows the document exceeds 200,000 tokens.
        Each chunk is ~85,000 tokens. A fresh Chunk Analyzer agent processes each
        chunk independently, extracting entities, concepts, and key claims with
        paragraph citations.

        Returns combined structured analyses for all chunks as markdown.
        """
        from .chunking import chunk_document

        doc_path = config.processed_dir / doc_name / "document.md"
        if not doc_path.exists():
            return f"Error: document '{doc_name}' not found at {doc_path}"

        chunks = chunk_document(doc_path, config.chunk_analyze_target_tokens, config.token_encoding)

        analyses = []
        for chunk in chunks:
            chunk_agent = Agent(
                name="chunk_analyzer",
                client=config.create_client(config.model_chunk_analyzer),
                system_prompt=CHUNK_ANALYZE_PROMPT,
                tools=[],
                max_steps=1,
            )

            task = (
                f"Chunk {chunk['index'] + 1}/{chunk['total']} of document '{doc_name}' "
                f"({chunk['token_count']} tokens):\n\n{chunk['content']}"
            )
            result = chunk_agent.run(task)
            analysis = _extract_text(result)
            analyses.append(f"## Chunk {chunk['index'] + 1}/{chunk['total']}\n\n{analysis}")

        combined = f"# Structured Analyses: {doc_name}\n\n" + "\n\n---\n\n".join(analyses)
        return combined

    return analyze_document_chunks


def _extract_text(result):
    if result is None:
        return ""
    if hasattr(result, "text"):
        return result.text
    if isinstance(result, str):
        return result
    return str(result)
