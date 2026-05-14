import os
import json
from pathlib import Path
import tiktoken
from datapizza.tools import tool


def _get_project_paths():
    from dotenv import load_dotenv
    project_root = Path(__file__).resolve().parent.parent.parent
    load_dotenv(project_root / ".env")
    wiki_dir = project_root / os.getenv("WIKI_DIR", "wiki")
    processed_dir = project_root / os.getenv("PROCESSED_DIR", "processed_documents")
    citation_base = os.getenv("CITATION_BASE_URL", "http://localhost:8765/go.html")
    return project_root, wiki_dir, processed_dir, citation_base


@tool
def list_source_documents() -> str:
    """List all available source documents in processed_documents/.

    Returns the names of all available documents with their sizes.
    Call this FIRST when you need to search source documents from scratch.
    """
    _, _, processed_dir, _ = _get_project_paths()
    if not processed_dir.exists():
        return "No processed_documents/ directory found."

    docs = []
    for d in sorted(processed_dir.iterdir()):
        if d.is_dir() and not d.name.startswith("."):
            md = d / "document.md"
            if md.exists():
                size_kb = md.stat().st_size // 1024
                lines = md.read_text(encoding="utf-8").count("\n")
                docs.append(f"  - {d.name} ({size_kb}KB, {lines} linee)")
            else:
                docs.append(f"  - {d.name} (no document.md)")

    if not docs:
        return "Nessun documento trovato in processed_documents/."
    return "Documenti disponibili in processed_documents/:\n" + "\n".join(docs)


@tool
def read_source_document(
    doc_name: str,
    anchors: list[int] | None = None,
    context_lines: int = 50,
) -> str:
    """Read a processed source document.

    Two modes:
    - anchors=[59, 60]: read context_lines above and below each anchor.
      Start with context_lines=50. If you need more context, call again
      with larger context_lines (100, 200, 400...). Stop when you have
      enough information to answer.
    - anchors=None: read the full document from the beginning.

    Args:
        doc_name: The document name (e.g., "subset40").
        anchors: List of paragraph numbers to look up, or None for full read.
        context_lines: Lines of context above and below each anchor (default 50).

    Returns the document text.
    """
    _, _, processed_dir, _ = _get_project_paths()
    doc_path = processed_dir / doc_name / "document.md"
    if not doc_path.exists():
        return f"Error: document not found at {doc_path}"

    lines = doc_path.read_text(encoding="utf-8").split("\n")

    if anchors is None:
        return "\n".join(lines)

    out = [f"# {doc_name} — anchor: {anchors}, contesto: ±{context_lines} righe\n"]
    seen = set()

    for anchor_num in anchors:
        if anchor_num in seen:
            continue
        seen.add(anchor_num)

        anchor_str = f"[¶{anchor_num}]"
        found_line = None
        for i, line in enumerate(lines):
            if anchor_str in line:
                found_line = i
                break

        if found_line is None:
            out.append(f"## ¶{anchor_num} — NON TROVATO\n")
            continue

        start = max(0, found_line - context_lines)
        end = min(len(lines), found_line + context_lines + 1)
        snippet = "\n".join(lines[start:end])

        out.append(f"## ¶{anchor_num} (righe {start+1}-{end})")
        out.append("```markdown")
        out.append(snippet)
        out.append("```\n")

    return "\n".join(out)


@tool
def get_document_info(doc_name: str, token_budget: int = 0) -> str:
    """Get document statistics: line count, tokens, number of citable anchors.

    Args:
        doc_name: The document name (e.g., "subset40").
        token_budget: Optional token budget for fit-check.

    Returns formatted document statistics.
    """
    _, _, processed_dir, _ = _get_project_paths()
    doc_path = processed_dir / doc_name / "document.md"
    cit_path = processed_dir / doc_name / "citations.json"

    if not doc_path.exists():
        return f"Error: document not found at {doc_path}"

    content = doc_path.read_text(encoding="utf-8")
    total_chars = len(content)
    total_lines = content.count("\n")
    enc = tiktoken.get_encoding("cl100k_base")
    token_count = len(enc.encode(content))
    avg_chars_per_line = total_chars / max(total_lines, 1)

    num_anchors = 0
    if cit_path.exists():
        try:
            cit_data = json.loads(cit_path.read_text(encoding="utf-8"))
            num_anchors = len(cit_data.get("citations", {}))
        except Exception:
            num_anchors = 0

    lines = [
        f"Document: {doc_name}",
        f"Total lines: {total_lines}",
        f"Total characters: {total_chars}",
        f"Tokens (tiktoken): {token_count}",
        f"Number of citable anchors: {num_anchors}",
        f"Average characters per line: {avg_chars_per_line:.1f}",
    ]

    if token_budget > 0:
        fits = token_count <= token_budget
        budget_lines = int((token_budget / token_count) * total_lines) if token_count > 0 else 0
        lines.append("")
        lines.append(
            f"Fits in budget ({token_budget} tokens): {'YES' if fits else 'NO'}"
        )
        if not fits and num_anchors > 0:
            lines.append(f"Available lines: {budget_lines}")
            lines.append("Lines per anchor at different selection sizes:")
            for n in [5, 10, 15, 20, 30, 50]:
                if n <= num_anchors:
                    lpa = max(3, budget_lines // n)
                    cl = max(1, (lpa - 1) // 2)
                    lines.append(
                        f"  {n} anchors -> {lpa} lines/anchor (context_lines={cl})"
                    )

    return "\n".join(lines)


@tool
def grep_source_document(doc_name: str, pattern: str, context_lines: int = 3) -> str:
    """Search for a pattern/regex in a source document. Like grep.

    Returns matching lines with the closest [¶N] anchor and line numbers.
    Use this to quickly locate specific information in large documents
    (e.g., searching for a message name in a 26K-line document).

    Args:
        doc_name: The document name (e.g., "subset26").
        pattern: Text or regex to search for (case-insensitive).
        context_lines: Lines of context around each match (default 3).

    Returns matching lines with anchor references and line numbers.
    """
    import re
    _, _, processed_dir, _ = _get_project_paths()
    doc_path = processed_dir / doc_name / "document.md"
    if not doc_path.exists():
        return f"Error: document not found at {doc_path}"

    lines = doc_path.read_text(encoding="utf-8").split("\n")

    try:
        regex = re.compile(pattern, re.IGNORECASE)
    except re.error as e:
        return f"Invalid regex pattern: {e}"

    matches = []
    for i, line in enumerate(lines):
        if regex.search(line):
            # Find closest [¶N] anchor before or at this line
            anchor = None
            for j in range(i, max(-1, i - 50), -1):
                anchor_m = re.search(r'\[¶(\d+)\]', lines[j])
                if anchor_m:
                    anchor = int(anchor_m.group(1))
                    break
            if anchor is None:
                for j in range(i + 1, min(len(lines), i + 50)):
                    anchor_m = re.search(r'\[¶(\d+)\]', lines[j])
                    if anchor_m:
                        anchor = int(anchor_m.group(1))
                        break

            start = max(0, i - context_lines)
            end = min(len(lines), i + context_lines + 1)
            snippet = "\n".join(f"  {ln}: {lines[ln]}" for ln in range(start, end))

            matches.append({
                "line": i + 1,
                "anchor": anchor,
                "snippet": snippet,
            })

    if not matches:
        return f"No matches for '{pattern}' in {doc_name}"

    out = [f"Grep results for '{pattern}' in {doc_name} ({len(matches)} matches):\n"]
    for m in matches[:30]:  # max 30 matches
        anchor_str = f"¶{m['anchor']}" if m['anchor'] else "nessun anchor"
        out.append(f"### Linea {m['line']} — anchor {anchor_str}")
        out.append("```")
        out.append(m["snippet"])
        out.append("```\n")

    if len(matches) > 30:
        out.append(f"...e altre {len(matches) - 30} occorrenze. Raffina il pattern.")

    return "\n".join(out)


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
    """Write or overwrite a wiki page.

    Args:
        page_path: Path relative to wiki/ (e.g., "entities/stm.md").
        content: The markdown content of the page. Use [doc_name ¶N] format for
                 citations (e.g., [subset35 ¶59]). These become clickable links
                 automatically when displayed to the user.
        doc_name: Source document name. Kept for backwards compatibility.

    Returns confirmation of the write operation.
    """
    _, wiki_dir, _, _ = _get_project_paths()
    full_path = wiki_dir / page_path
    full_path.parent.mkdir(parents=True, exist_ok=True)

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
def delete_wiki_page(page_path: str) -> str:
    """Delete a wiki page.

    Args:
        page_path: Path relative to wiki/ (e.g., "entities/old_page.md").

    Returns confirmation of the delete operation.
    """
    _, wiki_dir, _, _ = _get_project_paths()

    if page_path in ("index.md", "log.md", "overview.md"):
        return f"Error: cannot delete system page '{page_path}'"

    full_path = wiki_dir / page_path
    if not full_path.exists():
        return f"Page not found: {page_path}"

    full_path.unlink()
    return f"OK: deleted {page_path}"
