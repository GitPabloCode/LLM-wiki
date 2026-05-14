from datapizza.agents import Agent
from .config import WikiConfig
from .chunking import count_tokens, chunk_document
from .schemas import INGEST_PROMPT, CHUNK_AGENT_PROMPT, INGEST_ORCHESTRATOR_PROMPT, POST_INGEST_LINT_PROMPT
from .tools import file_tools, index_tools


class IngestAgent:
    """Document ingestion with automatic two-agent pipeline for large documents.

    Small docs (<= chunk_target_tokens): single-pass agent with full tools.
    Large docs (> chunk_target_tokens): chunk agent (no tools, no wiki) per chunk,
    then ingestion orchestrator synthesizes all analyses into wiki pages.
    """

    def __init__(self, config: WikiConfig):
        self.config = config

    def ingest(self, doc_name: str) -> str:
        config = self.config

        doc_path = config.processed_dir / doc_name / "document.md"
        if not doc_path.exists():
            return f"Error: document not found at {doc_path}"

        content = doc_path.read_text(encoding="utf-8")
        token_count = count_tokens(content, config.token_encoding)
        print(f"\n[ingest] {doc_name} — {token_count:,} token — {config.model_main_ingest}")

        if token_count <= config.chunk_target_tokens:
            return self._ingest_small(doc_name, content, token_count)
        else:
            return self._ingest_large(doc_name, doc_path, token_count)

    # ── Small document: single agent ────────────────────────────────────────

    def _ingest_small(self, doc_name: str, content: str, token_count: int) -> str:
        config = self.config

        main_agent = Agent(
            name="wiki_ingest_main",
            client=config.create_client(config.model_main_ingest),
            system_prompt=INGEST_PROMPT,
            tools=[
                file_tools.read_source_document,
                file_tools.read_wiki_page,
                file_tools.write_wiki_page,
                file_tools.list_wiki_pages,
                index_tools.update_index,
                index_tools.append_log,
                index_tools.update_overview,
            ],
            max_steps=30,
        )

        task = (
            f"Ingest document '{doc_name}'. Full document text below.\n\n"
            f"{content}\n\n"
            f"Pass doc_name=\"{doc_name}\" to every write_wiki_page call. "
            f"Log format: \"ingest | {doc_name} — completed\""
        )
        main_agent.run(task)

        return self._run_lint(doc_name)

    # ── Large document: chunk agents → orchestrator ─────────────────────────

    def _ingest_large(self, doc_name: str, doc_path, token_count: int) -> str:
        config = self.config

        chunks = chunk_document(
            doc_path,
            target_tokens=config.chunk_target_tokens,
            encoding=config.token_encoding,
        )
        print(f"[ingest] {doc_name} — {token_count:,} token → {len(chunks)} chunk")

        # Phase 1: run chunk agent on each chunk, no tools, no wiki, context reset each time
        chunk_responses: list[str] = []
        for i, chunk in enumerate(chunks):
            response = self._run_chunk_agent(doc_name, chunk, i)
            chunk_responses.append(response)
            print(f"[ingest] chunk {i + 1}/{len(chunks)} completato ({chunk['token_count']:,} token)")

        # Phase 2: orchestrator synthesizes all chunk analyses into wiki
        print(f"[ingest] avvio orchestrator con {len(chunk_responses)} analisi chunk...")
        orchestrator_result = self._run_orchestrator(doc_name, chunk_responses)
        print(f"[ingest] orchestrator completato.")

        # Phase 3: deterministic post-ingestion lint
        return self._run_lint(doc_name)

    def _run_chunk_agent(self, doc_name: str, chunk: dict, index: int) -> str:
        """Run a single chunk agent with NO tools and NO wiki access.

        Returns the raw text response, saved in a Python variable for later
        aggregation by the orchestrator.
        """
        config = self.config
        agent = Agent(
            name=f"wiki_chunk_{index}",
            client=config.create_client(config.model_main_ingest),
            system_prompt=CHUNK_AGENT_PROMPT,
            tools=[],  # NO tools, NO wiki access
            max_steps=1,
        )

        task = (
            f"Analyze this chunk ({index + 1} of the document). "
            f"Use doc_name=\"{doc_name}\" for all citations.\n\n"
            f"{chunk['content']}"
        )
        result = agent.run(task)
        return _extract_text(result)

    def _run_orchestrator(self, doc_name: str, chunk_responses: list[str]) -> str:
        """Synthesize all chunk analyses into wiki pages with full tool access."""
        config = self.config

        agent = Agent(
            name="wiki_ingest_orchestrator",
            client=config.create_client(config.model_main_ingest),
            system_prompt=INGEST_ORCHESTRATOR_PROMPT,
            tools=[
                file_tools.read_source_document,
                file_tools.read_wiki_page,
                file_tools.write_wiki_page,
                file_tools.list_wiki_pages,
                index_tools.update_index,
                index_tools.append_log,
                index_tools.update_overview,
            ],
            max_steps=30,
        )

        analyses = "\n\n---\n\n".join(
            f"=== CHUNK {i + 1} ANALYSIS ===\n\n{resp}"
            for i, resp in enumerate(chunk_responses)
        )

        task = (
            f"Synthesize all chunk analyses below into wiki pages for document '{doc_name}'.\n\n"
            f"Pass doc_name=\"{doc_name}\" to every write_wiki_page call. "
            f"Log format: \"ingest | {doc_name} — completed\"\n\n"
            f"{analyses}"
        )
        result = agent.run(task)
        return _extract_text(result)

    # ── Post-ingestion lint ─────────────────────────────────────────────────

    def _run_lint(self, doc_name: str) -> str:
        config = self.config
        print(f"[ingest] lint finale...")
        lint_agent = Agent(
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
        lint_result = lint_agent.run(
            f"Post-ingestion lint check for document '{doc_name}'. "
            f"Scan all wiki pages related to {doc_name} for duplicates, broken links, missing citations, format issues."
        )
        print(f"[ingest] completato.")
        return _extract_text(lint_result)


def _extract_text(result):
    if result is None:
        return ""
    if hasattr(result, "text"):
        return result.text
    if isinstance(result, str):
        return result
    return str(result)
