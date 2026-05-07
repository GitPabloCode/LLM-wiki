import os
import json
from pathlib import Path
from datapizza.tools import tool
from .transform_tools import transform_anchors_in_text


def _get_project_paths():
    from dotenv import load_dotenv
    project_root = Path(__file__).resolve().parent.parent.parent
    load_dotenv(project_root / ".env")
    wiki_dir = project_root / os.getenv("WIKI_DIR", "wiki")
    processed_dir = project_root / os.getenv("PROCESSED_DIR", "processed_documents")
    citation_base = os.getenv("CITATION_BASE_URL", "http://localhost:8765/go.html")
    return project_root, wiki_dir, processed_dir, citation_base


@tool
def read_source_document(doc_name: str, max_lines: int = 0) -> str:
    """Read a processed source document. Use max_lines to limit output size.

    Args:
        doc_name: The document name (e.g., "subset40").
        max_lines: If > 0, read only the first N lines. Use 150-300 for a quick overview.
                   If 0, read the entire document.

    Returns the document.md content.
    """
    _, _, processed_dir, _ = _get_project_paths()
    doc_path = processed_dir / doc_name / "document.md"
    if not doc_path.exists():
        return f"Error: document not found at {doc_path}"

    if max_lines > 0:
        lines = doc_path.read_text(encoding="utf-8").split("\n")
        return "\n".join(lines[:max_lines])
    return doc_path.read_text(encoding="utf-8")


@tool
def read_citations(doc_name: str) -> str:
    """Read the citations.json for a processed document. Returns summary + first 30 entries.

    Args:
        doc_name: The document name (e.g., "subset40").

    Returns summary with source_file, total_citable, and 30 sample entries.
    """
    _, _, processed_dir, _ = _get_project_paths()
    cit_path = processed_dir / doc_name / "citations.json"
    if not cit_path.exists():
        return f"Error: citations.json not found at {cit_path}"

    data = json.loads(cit_path.read_text(encoding="utf-8"))
    citable = data.get("citations", {})

    types_count = {}
    samples = []
    for i, (key, val) in enumerate(citable.items()):
        t = val.get("type", "unknown")
        types_count[t] = types_count.get(t, 0) + 1
        if i < 15:
            samples.append(f"  {key}: [{val.get('type')}] {val.get('content', '')[:120]}")

    lines = [
        f"source_file: {data.get('source_file')}",
        f"total_citable: {data.get('total_citable')}",
        f"anchor_format: {data.get('anchor_format')}",
        f"types: {json.dumps(types_count)}",
        "",
        "Sample entries:",
    ] + samples

    return "\n".join(lines)


@tool
def read_wiki_page(page_path: str) -> str:
    """Read an existing wiki page.

    Args:
        page_path: Path relative to wiki/ (e.g., "entities/stm.md").

    Returns the page content, or an error message if not found.
    """
    _, wiki_dir, _, _ = _get_project_paths()
    full_path = wiki_dir / page_path
    if not full_path.exists():
        return f"Page not found: {page_path}"
    return full_path.read_text(encoding="utf-8")


@tool
def write_wiki_page(page_path: str, content: str, doc_name: str = "") -> str:
    """Write or overwrite a wiki page. Automatically transforms bare [paragraph_N] citations into clickable links.

    Args:
        page_path: Path relative to wiki/ (e.g., "entities/stm.md").
        content: The markdown content of the page.
        doc_name: Source document name for anchor transformation (e.g., "subset40"). Required if content has [paragraph_N] anchors.

    Returns confirmation of the write operation.
    """
    _, wiki_dir, _, citation_base = _get_project_paths()
    full_path = wiki_dir / page_path
    full_path.parent.mkdir(parents=True, exist_ok=True)

    if doc_name and "[¶" in content:
        content = transform_anchors_in_text(content, doc_name, citation_base)

    full_path.write_text(content, encoding="utf-8")
    return f"OK: wrote {page_path} ({len(content)} chars)"


@tool
def list_wiki_pages(category: str = "all") -> str:
    """List existing wiki pages by category.

    Args:
        category: One of "summaries", "entities", "concepts", "comparisons", "lint_reports", or "all".

    Returns a JSON list of relative page paths.
    """
    _, wiki_dir, _, _ = _get_project_paths()

    categories = ["summaries", "entities", "concepts", "comparisons", "lint_reports"]
    if category != "all":
        categories = [category]

    result = {}
    for cat in categories:
        cat_dir = wiki_dir / cat
        if cat_dir.exists():
            pages = sorted(p.name for p in cat_dir.glob("*.md"))
            result[cat] = pages

    return json.dumps(result, indent=2)


@tool
def search_wiki(query: str, max_results: int = 10) -> str:
    """Full-text search across all wiki pages. Returns matching snippets with file paths.

    Args:
        query: The search query. Supports multiple words (AND logic).
        max_results: Maximum number of snippets to return (default 10).

    Returns formatted search results with file paths and matching lines.
    """
    _, wiki_dir, _, _ = _get_project_paths()

    terms = query.lower().split()
    all_md = list(wiki_dir.rglob("*.md"))
    results = []

    for md_file in all_md:
        rel_path = str(md_file.relative_to(wiki_dir))
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        lines = content.split("\n")
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if all(t in line_lower for t in terms):
                # Get surrounding context (±2 lines)
                start = max(0, i - 2)
                end = min(len(lines), i + 3)
                snippet = "\n".join(lines[start:end])
                results.append({
                    "file": rel_path,
                    "line": i + 1,
                    "snippet": snippet[:300],
                })

        if len(results) >= max_results * 3:
            break

    # Deduplicate and limit
    seen_files = set()
    filtered = []
    for r in results:
        if r["file"] not in seen_files:
            seen_files.add(r["file"])
            filtered.append(r)
        if len(filtered) >= max_results:
            break

    if not filtered:
        return f"No results found for '{query}'"

    out = [f"Search results for '{query}' ({len(filtered)} files):\n"]
    for r in filtered:
        out.append(f"\n### {r['file']} (line {r['line']})")
        out.append(f"```\n{r['snippet']}\n```")

    return "\n".join(out)


@tool
def read_document_around_anchors(doc_name: str, anchors: list[int], context_lines: int = 30) -> str:
    """Read the original source document around specific paragraph anchor numbers.

    Use this after navigating the wiki to get the exact original text. The wiki
    tells you WHERE to look; this tool gives you the GROUND TRUTH.

    Args:
        doc_name: The document name (e.g., "subset40").
        anchors: List of paragraph numbers to look up (e.g., [59, 60, 62]).
        context_lines: Number of lines of context before and after each anchor (default 30).

    Returns the original document text surrounding each requested anchor.
    """
    import re

    _, _, processed_dir, _ = _get_project_paths()
    doc_path = processed_dir / doc_name / "document.md"
    if not doc_path.exists():
        return f"Error: document not found at {doc_path}"

    lines = doc_path.read_text(encoding="utf-8").split("\n")

    out = [f"# Source document: {doc_name}\n"]

    for anchor_num in anchors:
        anchor_str = f"[¶{anchor_num}]"
        found_line = None

        for i, line in enumerate(lines):
            if anchor_str in line:
                found_line = i
                break

        if found_line is None:
            out.append(f"## ¶{anchor_num} — NOT FOUND\n")
            continue

        start = max(0, found_line - context_lines)
        end = min(len(lines), found_line + context_lines + 1)
        snippet = "\n".join(lines[start:end])

        out.append(f"## ¶{anchor_num} (lines {start+1}-{end})")
        out.append("```markdown")
        out.append(snippet)
        out.append("```\n")

    return "\n".join(out)
