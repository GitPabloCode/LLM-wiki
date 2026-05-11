from datapizza.agents import Agent
from .config import WikiConfig
from .chunking import count_tokens
from .schemas import INGEST_PROMPT, POST_INGEST_LINT_PROMPT
from .tools import file_tools, index_tools


class IngestAgent:
    """Single-pass ingestion. Large documents must be pre-split via docling_converter.split_large_document().

    Each (sub)document is ingested in one pass: main agent reads content,
    checks existing wiki pages, writes/updates pages, then lint runs deterministically.
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

        # Main agent: process document, write wiki pages
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

        # Deterministic lint
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
