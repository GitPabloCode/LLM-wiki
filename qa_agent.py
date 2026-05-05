#!/usr/bin/env python3
"""
qa_agent.py — Agente Q&A che risponde citando i paragrafi con anchor [¶N].

Utilizzo:
  python qa_agent.py --doc-dir processed_documents/subset40
  python qa_agent.py -d processed_documents/subset40 -q "domanda"
"""
import argparse
import json
import re
import sys
import textwrap
from pathlib import Path

from datapizza.clients.openai_like import OpenAILikeClient

# ---------------------------------------------------------------------------
# Agente Q&A
# ---------------------------------------------------------------------------

SYSTEM_PROMPT_FULL = textwrap.dedent("""\
    Sei un assistente specializzato nell'analisi di documenti tecnici.
    Rispondi alla domanda dell'utente basandoti ESCLUSIVAMENTE sul documento fornito.

    FORMATO CITAZIONI:
    - Ogni paragrafo del documento è seguito da un anchor nel formato [¶N] (es. [¶42]).
    - DEVI citare l'anchor di ogni paragrafo da cui prendi un'informazione.
    - Le citazioni vanno messe DOPO la frase che le usa. Esempio:
      "Il treno deve fermarsi entro 50 metri [¶42]."
    - Se usi più paragrafi, cita ciascuno separatamente.
    - Se il documento non contiene la risposta, dillo esplicitamente.

    FORMATO RISPOSTA:
    - Risposta chiara e concisa.
    - Ogni affermazione deve avere il suo [¶N].
    - Alla fine, elenca le fonti in formato compatto:
      "Fonti: ¶42, ¶58, ¶103"
    """)

class QAAgent:
    """Agente Q&A con citazione dei paragrafi tramite anchor Docling [¶N].

    Supporta uno o più subset di documenti. Con più subset, gli anchor
    vengono prefissati con il numero del subset (es. ¶35-1, ¶40-1, ¶58-1).
    """

    def __init__(
        self,
        doc_dirs: list[str],
        model: str = "deepseek-v4-flash:cloud",
    ):
        self.doc_dirs = [Path(d) for d in doc_dirs]
        self.model = model

        self._citations: dict[str, dict] = {}
        self._markdown: str = ""
        self._client: OpenAILikeClient | None = None
        self._anchor_to_doc_dir: dict[str, Path] = {}
        # Primo doc_dir per retrocompatibilità
        self.doc_dir = self.doc_dirs[0]

    # ── Inizializzazione ─────────────────────────────────────────────────

    def load(self) -> "QAAgent":
        """Carica document.md e citations.json da tutti i subset."""
        md_parts: list[str] = []
        multi = len(self.doc_dirs) > 1

        for doc_dir in self.doc_dirs:
            md_path = doc_dir / "document.md"
            citations_path = doc_dir / "citations.json"

            if not md_path.exists():
                raise FileNotFoundError(f"Markdown non trovato: {md_path}")
            if not citations_path.exists():
                raise FileNotFoundError(f"Citations non trovato: {citations_path}")

            md_text = md_path.read_text(encoding="utf-8")
            raw = json.loads(citations_path.read_text(encoding="utf-8"))
            subset_citations = raw.get("citations", {})

            if multi:
                prefix = re.sub(r"(?i)^subset[_-]?", "", doc_dir.name).replace(" v360", "")
                # Rinomina anchor nel markdown: [¶N] → [¶{prefix}-N]
                md_text = re.sub(r"\[¶(\d+)\]", rf"[¶{prefix}-\1]", md_text)
                # Rinomina chiavi nelle citations
                subset_citations = {
                    f"¶{prefix}-{k.lstrip('¶')}": v
                    for k, v in subset_citations.items()
                }

            md_parts.append(md_text)
            self._citations.update(subset_citations)

            # Mappa anchor → doc_dir per i link al viewer
            for anchor in subset_citations:
                self._anchor_to_doc_dir[anchor] = doc_dir

        self._markdown = "\n\n".join(md_parts)

        self._init_client()
        return self

    def _init_client(self):
        self._client = OpenAILikeClient(
            api_key="ollama",
            model=self.model,
            base_url="http://localhost:11434/v1",
        )

    # ── Chiamata LLM ────────────────────────────────────────────────────

    def _call_llm(self, system_prompt: str, user_prompt: str) -> tuple[str, dict[str, int]]:
        """Restituisce (testo_risposta, {prompt_tokens, completion_tokens, total_tokens})."""
        response = self._client.invoke(
            input=user_prompt,
            system_prompt=system_prompt,
            temperature=0.1,
        )
        text = response.text or ""
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.prompt_tokens + response.usage.completion_tokens,
        }
        return text, usage

    # ── Lookup fonti ────────────────────────────────────────────────────

    def _extract_anchors(self, text: str) -> list[str]:
        """Estrae tutti gli anchor ¶N o ¶{prefix}-N unici dal testo, ordinati."""
        found = re.findall(r"¶(?:(\d+)-)?(\d+)", text)
        seen: set[str] = set()
        unique: list[str] = []
        for prefix, num in found:
            anchor = f"¶{prefix}-{num}" if prefix else f"¶{num}"
            if anchor not in seen and anchor in self._citations:
                seen.add(anchor)
                unique.append(anchor)
        return unique

    def _lookup_sources(self, anchors: list[str]) -> list[dict]:
        result = []
        for a in anchors:
            c = self._citations[a]
            doc_dir = self._anchor_to_doc_dir.get(a, self.doc_dir)
            source = {
                "anchor": a,
                "page": c["page_id"],
                "type": c["type"],
                "content": c["content"],
                "doc_dir": str(doc_dir),
            }
            if c.get("bbox"):
                source["bbox"] = c["bbox"]
            result.append(source)
        return result

    # ── Modalità Full-Context ───────────────────────────────────────────

    def _ask_full(self, question: str) -> dict:
        user_prompt = (
            f"DOCUMENTO:\n\n{self._markdown}\n\n"
            f"DOMANDA: {question}"
        )

        answer, tokens = self._call_llm(SYSTEM_PROMPT_FULL, user_prompt)
        anchors = self._extract_anchors(answer)
        sources = self._lookup_sources(anchors)
        return {"answer": answer, "sources": sources, "mode": "full", "tokens": tokens}

    # ── API pubblica ────────────────────────────────────────────────────

    def ask(self, question: str) -> dict:
        return self._ask_full(question)


# ---------------------------------------------------------------------------
# Formattazione output
# ---------------------------------------------------------------------------

def format_answer(result: dict) -> str:
    lines = [
        f"{'─' * 60}",
        f"Modalità: {result['mode']}",
        f"{'─' * 60}",
        "",
        result["answer"].rstrip(),
    ]

    if result["sources"]:
        lines.append("")
        lines.append("─" * 60)
        lines.append("FONTI VERIFICATE:")
        lines.append("")
        for i, src in enumerate(result["sources"], 1):
            content_preview = src["content"][:200].replace("\n", " ")
            if len(src["content"]) > 200:
                content_preview += "…"
            lines.append(f"  [{src['anchor']}] pagina {src['page']}, {src['type']}")
            lines.append(f"      {content_preview}")
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Agente Q&A con citazione dei paragrafi via anchor Docling [¶N].",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            esempi:
              python qa_agent.py -d processed_documents/subset40
              python qa_agent.py -d processed_documents/subset35 processed_documents/subset40 -q "domanda"
        """),
    )
    p.add_argument("-d", "--doc-dir", required=True, nargs="+",
                   help="Cartella/e con document.md e citations.json")
    p.add_argument("-q", "--question", default=None,
                   help="Domanda singola")
    p.add_argument("--model", default="deepseek-v4-flash:cloud",
                   help="Modello LLM (default: deepseek-v4-flash:cloud)")
    return p.parse_args()


def _expand_doc_dirs(doc_dirs: list[str]) -> list[str]:
    """Se una directory è la root 'processed_documents', la espande in tutte le sottocartelle."""
    expanded: list[str] = []
    for d in doc_dirs:
        p = Path(d).resolve()
        if (p / "document.md").exists():
            expanded.append(d)
        else:
            subs = sorted(
                str(sub) for sub in p.iterdir()
                if sub.is_dir() and (sub / "document.md").exists()
            )
            if not subs:
                raise FileNotFoundError(
                    f"Né {d} né le sue sottocartelle contengono document.md"
                )
            expanded.extend(subs)
    return expanded


def main() -> None:
    args = parse_args()
    args.doc_dir = _expand_doc_dirs(args.doc_dir)

    try:
        agent = QAAgent(
            doc_dirs=args.doc_dir,
            model=args.model,
        ).load()
    except FileNotFoundError as e:
        print(f"❌ {e}")
        sys.exit(1)

    if args.question:
        result = agent.ask(args.question)
        print(format_answer(result))
    else:
        print(f"\n🤖 Q&A Agent — subset: {', '.join(d.name for d in agent.doc_dirs)}")
        print(f"   Modello: {agent.model}")
        print(f"   Documento combinato: {len(agent._markdown):,} char")
        print(f"   Paragrafi citabili: {len(agent._citations)}")
        print("\n   Scrivi 'fine' o 'quit' per uscire.\n")

        while True:
            try:
                question = input("❯ ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n")
                break

            if not question:
                continue

            if question.lower() in ("fine", "quit", "exit", "q"):
                break

            result = agent.ask(question)
            print(format_answer(result))
            print()


if __name__ == "__main__":
    main()
