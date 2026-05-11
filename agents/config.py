import os
from pathlib import Path
from dataclasses import dataclass, field
from dotenv import load_dotenv


@dataclass
class WikiConfig:
    project_root: Path = field(default_factory=lambda: Path(__file__).resolve().parent.parent)
    wiki_dir: Path | None = None
    processed_dir: Path | None = None

    # Model per role (overridable via env var: LLM_MODEL_ORCHESTRATOR, LLM_MODEL_MAIN_INGEST, etc.)
    model_orchestrator: str = "qwen3.5:4b"
    model_main_ingest: str = "deepseek-v4-flash:cloud"
    model_lint: str = "deepseek-v4-flash:cloud"
    model_query: str = "deepseek-v4-flash:cloud"

    base_url: str = "http://localhost:11434/v1"
    api_key: str = "ollama"
    citation_base_url: str = "http://localhost:8765/go.html"
    chunk_target_tokens: int = 60000
    token_encoding: str = "cl100k_base"

    def __post_init__(self):
        load_dotenv(self.project_root / ".env")

        self.model_orchestrator = os.getenv("LLM_MODEL_ORCHESTRATOR", self.model_orchestrator)
        self.model_main_ingest = os.getenv("LLM_MODEL_MAIN_INGEST", self.model_main_ingest)
        self.model_lint = os.getenv("LLM_MODEL_LINT", self.model_lint)
        self.model_query = os.getenv("LLM_MODEL_QUERY", self.model_query)

        self.base_url = os.getenv("LLM_BASE_URL", self.base_url)
        self.api_key = os.getenv("LLM_API_KEY", self.api_key)
        self.citation_base_url = os.getenv("CITATION_BASE_URL", self.citation_base_url)
        self.chunk_target_tokens = int(os.getenv("CHUNK_TARGET_TOKENS", str(self.chunk_target_tokens)))
        self.token_encoding = os.getenv("TOKEN_ENCODING", self.token_encoding)

        wiki_rel = os.getenv("WIKI_DIR", "wiki")
        processed_rel = os.getenv("PROCESSED_DIR", "processed_documents")
        self.wiki_dir = self.project_root / wiki_rel
        self.processed_dir = self.project_root / processed_rel

    def create_client(self, model: str | None = None):
        from datapizza.clients.openai import OpenAIClient
        return OpenAIClient(
            api_key=self.api_key,
            base_url=self.base_url,
            model=model or self.model_orchestrator,
        )
