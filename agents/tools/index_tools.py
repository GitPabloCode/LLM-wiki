import json
import os
from datetime import datetime
from pathlib import Path
from datapizza.tools import tool


def _get_project_paths():
    from dotenv import load_dotenv
    project_root = Path(__file__).resolve().parent.parent.parent
    load_dotenv(project_root / ".env")
    wiki_dir = project_root / os.getenv("WIKI_DIR", "wiki")
    return project_root, wiki_dir


@tool
def update_index(entries_json: str) -> str:
    """Update wiki/index.md with new or updated page entries.

    Args:
        entries_json: JSON string describing pages to add/update. Format:
          {
            "add_summaries": [{"name": "subset40", "path": "summaries/subset40.md", "desc": "...", "date": "2026-05-07"}],
            "add_entities": [{"name": "stm", "path": "entities/stm.md", "desc": "...", "sources": "subset35, subset58"}],
            "add_concepts": [...],
            "add_comparisons": [...],
            "add_lint_reports": [...]
          }
        All keys are optional. Missing keys are skipped.

    Returns confirmation.
    """
    _, wiki_dir = _get_project_paths()
    index_path = wiki_dir / "index.md"

    today = datetime.now().strftime("%Y-%m-%d")

    if index_path.exists():
        content = index_path.read_text(encoding="utf-8")
    else:
        content = f"# Wiki Index\n\n*Last updated: {today}*\n"

    content = content.replace("*Last updated:*", f"*Last updated: {today}*\n<!-- previous update -->")

    try:
        entries = json.loads(entries_json)
    except json.JSONDecodeError as e:
        return f"Error parsing entries_json: {e}"

    section_map = {
        "add_summaries": "## Summaries",
        "add_entities": "## Entities",
        "add_concepts": "## Concepts",
        "add_comparisons": "## Comparisons",
        "add_lint_reports": "## Lint Reports",
    }

    changes = []
    for key, section_header in section_map.items():
        items = entries.get(key, [])
        if not items:
            continue

        # ensure section exists
        if section_header not in content:
            content += f"\n{section_header}\n"

        for item in items:
            name = item.get("name", "")
            path = item.get("path", "")
            desc = item.get("desc", "")
            date = item.get("date", today)
            sources = item.get("sources", "")

            line = f"- [{name}]({path}) — {desc}"
            if sources:
                line += f" | sources: {sources}"
            if date and key in ("add_summaries", "add_comparisons", "add_lint_reports"):
                line += f" | {date}"

            # check if already present
            existing_pattern = f"[{name}]({path})"
            if existing_pattern in content:
                lines = content.split("\n")
                new_lines = []
                for l in lines:
                    if existing_pattern in l:
                        new_lines.append(line)
                        changes.append(f"updated: {name}")
                    else:
                        new_lines.append(l)
                content = "\n".join(new_lines)
            else:
                # insert after section header
                content = content.replace(
                    section_header + "\n",
                    section_header + "\n" + line + "\n"
                )
                changes.append(f"added: {name}")

    index_path.write_text(content, encoding="utf-8")
    return f"OK: index updated ({', '.join(changes) if changes else 'no changes'})"


@tool
def append_log(entry: str) -> str:
    """Append an entry to the operation log (wiki/log.md).

    Args:
        entry: The log entry text. Date prefix is added automatically.
               Examples: "ingest | subset40 — s/1, e/3, c/4", "query | what is STM?"

    Returns confirmation.
    """
    _, wiki_dir = _get_project_paths()
    log_path = wiki_dir / "log.md"

    today = datetime.now().strftime("%Y-%m-%d")
    line = f"## [{today}] {entry}\n"

    if log_path.exists():
        current = log_path.read_text(encoding="utf-8")
        log_path.write_text(current.rstrip() + "\n" + line + "\n", encoding="utf-8")
    else:
        log_path.write_text("# Operation Log\n\n" + line + "\n", encoding="utf-8")

    return f"OK: logged '{entry}'"


@tool
def update_overview(content: str) -> str:
    """Replace the overview page (wiki/overview.md) with new content.

    Args:
        content: The full markdown content for the overview page.

    Returns confirmation.
    """
    _, wiki_dir = _get_project_paths()
    overview_path = wiki_dir / "overview.md"
    overview_path.write_text(content, encoding="utf-8")
    return f"OK: overview updated ({len(content)} chars)"
