import re
import os
from pathlib import Path
from datapizza.tools import tool


def _get_citation_base() -> str:
    from dotenv import load_dotenv
    project_root = Path(__file__).resolve().parent.parent.parent
    load_dotenv(project_root / ".env")
    return os.getenv("CITATION_BASE_URL", "http://localhost:8765/go.html")


def transform_anchors_deterministic(text: str, citation_base_url: str = "") -> str:
    """Convert [doc_name ¶N] and [doc_name ¶N, ¶M] to clickable go.html links.

    Applied deterministically to every agent response — no tool delegation needed.
    Format expected from agents: [subset35 ¶59] or [subset35 ¶59, ¶60].
    """
    if not citation_base_url:
        citation_base_url = _get_citation_base()

    pattern = r'\[([a-zA-Z0-9_]+)\s+(¶\d+(?:-\d+)?(?:\s*,\s*¶\d+(?:-\d+)?)*)\]'

    def replace_match(m: re.Match) -> str:
        doc = m.group(1)
        anchors_str = m.group(2)
        parts = [p.strip() for p in anchors_str.split(",")]
        transformed = []
        for part in parts:
            m2 = re.match(r"¶(\d+)(?:-(\d+))?", part)
            if m2:
                a = m2.group(1)
                b = m2.group(2)
                if b:
                    transformed.append(f"[¶{a}-{b}]({citation_base_url}#{doc}-{a})")
                else:
                    transformed.append(f"[¶{a}]({citation_base_url}#{doc}-{a})")
            else:
                transformed.append(part)
        return ", ".join(transformed)

    return re.sub(pattern, replace_match, text)


# Legacy — kept for ingest agent's write_wiki_page which still uses [¶N] bare format
def transform_anchors_in_text(text: str, doc_name: str, citation_base_url: str = "http://localhost:8765/go.html") -> str:
    """Replace all bare [paragraph_N] and [paragraph_A-B] with clickable go.html links."""

    def replace_match(m: re.Match) -> str:
        inner = m.group(1)
        parts = [p.strip() for p in inner.split(",")]
        transformed = []
        for part in parts:
            m2 = re.match(r"(\d+)(?:-(\d+))?", part)
            if m2:
                a = m2.group(1)
                b = m2.group(2)
                if b:
                    transformed.append(f"[¶{a}-{b}]({citation_base_url}#{doc_name}-{a})")
                else:
                    transformed.append(f"[¶{a}]({citation_base_url}#{doc_name}-{a})")
            else:
                transformed.append(part)
        return ", ".join(transformed)

    return re.sub(r"\[¶(\d+(?:-\d+)?(?:,\s*\d+(?:-\d+)?)*)\]", replace_match, text)


@tool
def transform_anchors(text: str, doc_name: str) -> str:
    """Convert bare [paragraph_N] citations to clickable links pointing to the citation viewer.

    Args:
        text: The text containing [paragraph_N] markers to convert.
        doc_name: The source document name (e.g., "subset40").

    Returns the text with all [paragraph_N] replaced by clickable markdown links.
    """
    return transform_anchors_in_text(text, doc_name, _get_citation_base())
