#!/usr/bin/env python3
"""LLM Wiki — Interactive chatbot with specialized sub-agents.

Usage:
    python run_wiki.py [--no-citation-server]

The orchestrator is an interactive chatbot. Tell it what you want:
    - "fai l'ingestion di subset40"  → delegates to Ingest Agent
    - "cos'è l'STM?"                 → delegates to Query Agent
    - "controlla il wiki"            → delegates to Lint Agent
    - "ciao!"                        → normal chat (no delegation)

Type /exit to quit, /help for available commands.
"""

import sys
import os
import subprocess
import time
import signal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agents.config import WikiConfig
from agents.ingest_agent import IngestAgent
from agents.query_agent import QueryAgent
from agents.orchestrator import OrchestratorAgent


CITATION_PORT = 8765
citation_server = None


def start_citation_server():
    """Start the HTTP server in processed_documents/ for citation go.html links."""
    global citation_server
    project_root = Path(__file__).resolve().parent
    processed_dir = project_root / os.getenv("PROCESSED_DIR", "processed_documents")

    if not processed_dir.exists():
        print(f"[warn] processed_documents/ not found, citation server not started")
        return

    citation_server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(CITATION_PORT), "--bind", "127.0.0.1"],
        cwd=str(processed_dir),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(0.3)
    ok = citation_server.poll() is None
    if ok:
        print(f"[ok] Citation server running at http://localhost:{CITATION_PORT}/")
    else:
        print(f"[warn] Could not start citation server (port {CITATION_PORT} may be in use)")


def stop_citation_server():
    global citation_server
    if citation_server and citation_server.poll() is None:
        citation_server.terminate()
        citation_server.wait(timeout=2)
        print("[ok] Citation server stopped")


def check_ollama(config: WikiConfig) -> bool:
    """Check if Ollama is running and the configured model is available."""
    import urllib.request, json
    try:
        req = urllib.request.Request("http://localhost:11434/api/tags")
        data = json.loads(urllib.request.urlopen(req, timeout=5).read())
        models = [m["name"] for m in data.get("models", [])]
        if config.model in models:
            print(f"[ok] Ollama model '{config.model}' available")
            return True
        else:
            print(f"[warn] Model '{config.model}' not found in Ollama. Available: {', '.join(models[:8])}")
            return False
    except Exception:
        print("[warn] Cannot reach Ollama at http://localhost:11434 — is it running?")
        return False


def print_help():
    print("""
LLM Wiki Commands:
  /help        — show this help
  /exit        — quit
  /docs        — list available documents in processed_documents/
  /pages       — list all wiki pages

Examples:
  "fai l'ingestion di subset40"
  "cos'è l'STM?"
  "controlla che non ci siano contraddizioni nel wiki"
""")


def list_available_docs(config: WikiConfig):
    processed = config.processed_dir
    if not processed.exists():
        print("  No processed_documents/ directory found.")
        return
    docs = [d.name for d in sorted(processed.iterdir()) if d.is_dir() and not d.name.startswith(".")]
    if docs:
        print("  Available documents:")
        for d in docs:
            md = processed / d / "document.md"
            size = f"{md.stat().st_size // 1024}KB" if md.exists() else "N/A"
            print(f"    - {d} ({size})")
    else:
        print("  No documents found.")


def main():
    config = WikiConfig()

    print("=" * 55)
    print("LLM Wiki — Orchestrator")
    print("=" * 55)

    # Check prerequisites
    if not check_ollama(config):
        print("[warn] Proceeding anyway — LLM calls may fail")

    # Start citation server
    start_citation_server()

    # Build agents
    print("[ok] Initializing Ingest Agent...")
    ingest_agent = IngestAgent(config)

    print("[ok] Initializing Query Agent...")
    query_agent = QueryAgent(config)

    # For now, Lint agent is not available
    lint_agent = None

    print("[ok] Starting Orchestrator...")
    orchestrator = OrchestratorAgent(config)
    orchestrator.start(
        ingest_agent=ingest_agent,
        query_agent=query_agent,
        lint_agent=lint_agent,
    )

    print("\nChat with the Orchestrator. Type /help for commands, /exit to quit.\n")

    # Interactive chat loop
    try:
        while True:
            user_input = input("\nTu > ").strip()
            if not user_input:
                continue

            # Handle commands
            if user_input.startswith("/"):
                cmd = user_input.lower()
                if cmd in ("/exit", "/quit", "/q"):
                    print("Ciao!")
                    break
                elif cmd == "/help":
                    print_help()
                    continue
                elif cmd == "/docs":
                    list_available_docs(config)
                    continue
                elif cmd == "/pages":
                    from agents.tools.file_tools import list_wiki_pages
                    print(list_wiki_pages("all"))
                    continue
                else:
                    print(f"Unknown command: {cmd}")
                    continue

            # Route to orchestrator
            print("\nWiki > ", end="", flush=True)
            response = orchestrator.chat(user_input)
            print(response)

    except KeyboardInterrupt:
        print("\n\nInterrupted.")
    finally:
        stop_citation_server()


if __name__ == "__main__":
    main()
