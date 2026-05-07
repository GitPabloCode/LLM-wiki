import re
from pathlib import Path
import tiktoken


def count_tokens(text: str, encoding: str = "cl100k_base") -> int:
    enc = tiktoken.get_encoding(encoding)
    return len(enc.encode(text))


def parse_sections(markdown: str) -> list[dict]:
    """Split markdown into sections at heading boundaries.

    Each section is {heading, level, content}. The heading line is included
    in content. Text before the first heading becomes a preamble section
    with heading=None, level=0.
    """
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
    matches = list(heading_re.finditer(markdown))

    if not matches:
        return [{"heading": None, "level": 0, "content": markdown}]

    sections = []
    first_match_start = matches[0].start()

    # Preamble: everything before the first heading
    if first_match_start > 0:
        preamble = markdown[:first_match_start].rstrip()
        if preamble:
            sections.append({"heading": None, "level": 0, "content": preamble})

    for i, m in enumerate(matches):
        heading_text = m.group(0)
        level = len(m.group(1))
        title = m.group(2)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        content = markdown[start:end].rstrip()

        sections.append({
            "heading": title,
            "level": level,
            "content": content,
        })

    return sections


def chunk_document(doc_path: Path, target_tokens: int = 60000, encoding: str = "cl100k_base") -> list[dict]:
    """Split a markdown document into chunks of approximately target_tokens.

    Sections are never split. A single section that exceeds target_tokens
    becomes its own chunk.
    """
    markdown = doc_path.read_text(encoding="utf-8")
    sections = parse_sections(markdown)

    chunks = []
    current_sections = []
    current_tokens = 0

    for sec in sections:
        sec_tokens = count_tokens(sec["content"], encoding)

        if current_sections and current_tokens + sec_tokens > target_tokens:
            chunks.append(_build_chunk(current_sections, len(chunks), encoding))
            current_sections = []
            current_tokens = 0

        current_sections.append(sec)
        current_tokens += sec_tokens

    if current_sections:
        chunks.append(_build_chunk(current_sections, len(chunks), encoding))

    # Number chunks after building
    total = len(chunks)
    for i, chunk in enumerate(chunks):
        chunk["index"] = i
        chunk["total"] = total

    return chunks


def _build_chunk(sections: list[dict], index: int, encoding: str) -> dict:
    content = "\n\n".join(sec["content"] for sec in sections)
    return {
        "index": index,
        "total": 0,
        "sections": sections,
        "token_count": count_tokens(content, encoding),
        "content": content,
    }
