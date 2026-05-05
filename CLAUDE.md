# LLM-Wiki Schema

You are the maintainer of this wiki. Every wiki page is owned by you — you create, update, cross-reference, and keep them consistent. This document defines the conventions and workflows.

## Directory structure

```
raw_sources/               Immutable source PDFs — read from, never modify
processed_documents/       Docling output: one folder per PDF with document.md, citations.json, viewer.html, pages/
wiki/
  index.md                 Catalog of every wiki page (title, link, one-line summary, metadata)
  log.md                   Append-only chronological record of all operations
  overview.md              Cross-source synthesis connecting all sources
  summaries/               One page per ingested source
  entities/                Key objects, systems, components, people, locations
  concepts/                Ideas, theories, rules, processes, definitions
  comparisons/             Side-by-side analyses across sources or entities
  lint_reports/            Periodic health-check reports
```

## Page format conventions

Every wiki page follows this template:

```markdown
# Page Title

**Source:** [source-name](summaries/source-name.md) | **Date:** YYYY-MM-DD | **Type:** entity|concept|summary|comparison|overview|lint

Content here. Written in clear, concise English.

## Cross-references
- [Related Page](path.md) — one-line explanation of relationship
- [Another Page](path.md) — one-line explanation of relationship
```

Rules:
- **One page = one topic.** Don't cram multiple entities into one page.
- **Cross-references footer is mandatory.** Every page links to related pages.
- **Links are pure markdown:** `[text](relative/path.md)`. Relative to `wiki/`.
- **Citations to sources:** Every `[¶N]` in wiki page body text MUST be a clickable markdown link with the source document prefix: `[¶N](http://localhost:8765/go.html#{doc}-N)` (es. `go.html#subset40-42` per ¶42 di subset40). Plain-text `[¶N]` is not acceptable. Ranges like `[¶A-B]` link to the first paragraph in the range.
- **No frontmatter.** Metadata goes in a bold line under the title.
- **Keep pages focused.** Entity pages describe one thing. Concept pages explain one idea.

## Index format (wiki/index.md)

```markdown
# Wiki Index

## Summaries
- [subset35](summaries/subset35.md) — Description of the document | 2026-04-28

## Entities
- [balise](entities/balise.md) — Trackside transmission device | subset35, subset40

## Concepts
- [braking-curve](concepts/braking-curve.md) — How trains compute stopping distance | subset35, subset58

## Comparisons
- [balise-vs-eurobalise](comparisons/balise-vs-eurobalise.md) — 2026-04-28
```

Update it on every ingest and whenever a new page is created during queries.

## Log format (wiki/log.md)

```markdown
# Operation Log

## [2026-04-28] ingest | subset35 — pages: s/1, e/3, c/2 (summaries/entities/concepts created or updated)
## [2026-04-28] query | "What are the braking distance requirements?" — filed as concepts/braking-distance.md
## [2026-04-28] lint | full pass — 3 issues found, see lint_reports/2026-04-28.md
```

Append-only. Each entry starts with `## [YYYY-MM-DD] operation-type | details`. This makes it grep-able: `grep "^## \[" wiki/log.md | tail -5`.

## Ingest workflow

### Prerequisites (user does these)
1. Place PDF in `raw_sources/`
2. Run: `python docling_converter.py raw_sources/doc.pdf --output-dir processed_documents`
   - This creates `processed_documents/{doc_name}/` with `document.md`, `citations.json`, `viewer.html`, `pages/`
3. Start the citation viewer HTTP server (do this once per session):
   ```bash
   cd processed_documents && python3 -m http.server 8765 &
   ```
   This makes all `[¶N]` citation links clickable in-browser.

### Supervised mode (one source at a time, recommended)
1. User says: "ingest processed_documents/{doc_name}"
2. Read `processed_documents/{doc_name}/document.md`
3. Identify the 5-10 most important takeaways or facts
4. Discuss key takeaways with the user — ask what to emphasize
5. Write `wiki/summaries/{doc_name}.md`:
   - Title, source metadata
   - Executive summary (2-3 sentences)
   - Key points (bullet list, each with `[¶N]` citation to source)
   - Notable entities and concepts found
   - Cross-references to related pages
6. For each **new entity** discovered: create `wiki/entities/{name}.md`
7. For each **new concept** discovered: create `wiki/concepts/{name}.md`
8. For each **existing entity/concept page** that this source touches: update it with new information and add a link back to `summaries/{doc_name}.md`
9. Update `wiki/overview.md` if the new source shifts the overall picture
10. Update `wiki/index.md`: add summary entry, add new entity/concept entries, update metadata on changed pages
11. Append to `wiki/log.md`: `## [DATE] ingest | {doc_name} — s/1, e/N, c/M`

### Batch mode (multiple sources, less supervision)
1. User says: "batch-ingest processed_documents/subset35 processed_documents/subset40"
2. Process each source through steps 3-10 of supervised mode, with minimal user interaction
3. At the end, report what was created/updated
4. Append one log entry per source

## Direct Research Query Workflow

This is the **default workflow** for answering questions. You, the Claude Code
agent, perform all research inline.

**Protocol — follow every step in order. Do not skip.**

### Step 1: Orient via wiki
Read `wiki/index.md`. Identify candidate pages whose titles or summaries match
the user's question. Also read `wiki/overview.md` for cross-source synthesis.

**If zero candidates are found:** Proceed to "No wiki coverage" below.

### Step 2: Extract citations from wiki pages
For each candidate page found in Step 1:
- Read the full page.
- From the `**Source:**` metadata line, extract the source document name(s).
  Example: `**Source:** [subset35](../summaries/subset35.md)` means this page
  draws from the `subset35` processed document.
- Collect every `[¶N]` and `[¶A-B]` anchor appearing in the page body.
- Group anchors by source document. A page with a single source means all its
  anchors belong to that source. For multi-source pages, use the paragraph
  content surrounding each anchor to infer which document it references.

### Step 3: Read primary-source paragraphs from document.md
For each source document identified in Step 2:
- The file is `processed_documents/{doc}/document.md`.
- For every `[¶N]` anchor collected from wiki pages, use `grep` to locate
  that anchor in document.md, then read the surrounding context (~20 lines
  before and after the anchor). Do NOT read the entire file unless it is small.
- For range anchors `[¶A-B]`: sample the first, middle, and last paragraphs
  in the range. Read each individually using the same grep approach.
- When reading large ranges, prioritize paragraphs that appear most relevant
  to the specific question.

### Step 4: Expand search if needed
If the paragraphs from Step 3 are insufficient to answer the question:
- Search document.md for keywords from the question:
  `grep -n -i "keyword" processed_documents/{doc}/document.md`
- Read surrounding context of any matches.
- Repeat until you have enough information for a complete answer.

### Step 5: Synthesize the answer with mandatory citations
Compose a clear, concise answer. **Every factual claim MUST carry an inline
citation.** Use **reference-style markdown links**: the inline text is just
`[¶N]`, and the URL is defined once at the bottom of the answer.

Example — inline in body text:
```
The STM has eight defined states [¶238-274].
```

Example — URL definitions at the bottom of the answer:
```
[¶238-274]: http://localhost:8765/go.html#subset35-238
[¶42]: http://localhost:8765/go.html#subset40-42
```

Rules (mandatory):
- Inline citations are bare `[¶N]` or `[¶A-B]` — no parenthesized URL inline.
- Every `[¶N]` used inline MUST have a corresponding reference definition.
- `go.html#{doc}-N` prefixed format ensures the correct document's viewer is opened. Bare `#N` anchors are resolved by go.html searching all documents, but prefixed anchors guarantee the correct document.
- For range anchors `[¶A-B]`: link to the first paragraph in the range.
- **No claim may appear without a citation.**
- If a claim draws from multiple documents, include all relevant citations.

### Step 6: Format the answer
Structure every answer like this:

```
[Concise answer text with [¶N] citations inline.]

**Sources:**
- [¶N] — one-line description
- [¶M] — one-line description

**Consulted wiki pages:**
- [Page Name](path/to/page.md)

[¶N]: http://localhost:8765/go.html#subset35-N
[¶M]: http://localhost:8765/go.html#subset40-M
```

### No wiki coverage
If Step 1 finds no relevant wiki pages, respond:
"The wiki does not yet have pages covering this topic. I can search the
processed documents directly — tell me which document(s) to consult, or I
can suggest based on overview.md."

Then:
- Read `wiki/overview.md` to suggest candidate documents.
- Or ask the user to specify.
- Once document(s) are chosen, search document.md by keyword (Step 4) and
  proceed to Steps 5-6. Citations are still mandatory.

### Filing the answer
If the user says "file this":
- Create the page under `wiki/concepts/` or `wiki/entities/` as appropriate.
- Follow the page format conventions. All citations in the filed page MUST
  be clickable links, not plain text.
- Update `wiki/index.md`.
- Append to `wiki/log.md`:
  `## [DATE] query | "question" — filed as {path}`

## Query workflow (qa_agent.py — external LLM fallback)

This is a **secondary/fallback** tool. Use `qa_agent.py` only when:
- The user explicitly asks to use the qa_agent
- The Direct Research Query Workflow cannot find sufficient information in the wiki
- You need to generate an HTML report from multiple Q&A results

1. User asks a question requiring qa_agent
2. Read `wiki/index.md` and identify which `processed_documents/` folders are relevant
3. Launch `qa_agent.py` on the relevant documents:
   ```
   python qa_agent.py -d processed_documents/{doc1} processed_documents/{doc2} -q "user's question" --model {model}
   ```
4. Synthesize the answer using qa_agent's response as the base.
   Always cite with `[¶N](http://localhost:8765/go.html#{doc}-N)` with the correct document prefix.

## Multi-Question Batch Workflow

When the user provides multiple questions and asks for qa_agent or an HTML report:

### Step 1: Identify relevant documents
Read `wiki/index.md` and `wiki/overview.md`. Identify which `processed_documents/` folders are relevant.

### Step 2: Run qa_agent for each question
For each individual question, run:
```
python qa_agent.py -d processed_documents/{doc1} [processed_documents/{doc2} ...] -q "question" --model {model}
```

### Step 3: Generate HTML report
Collect all results and generate the report:
```python
from qa_agent import generate_report

results = [
    {"question": "...", "answer": "...", "sources": [...], "tokens": {...}, "duration": 2.34},
    ...
]

generate_report(
    results=results,
    doc_dirs=["processed_documents/subset35", ...],
    output_path="domande_excel/report_batch_{timestamp}.html",
    model="deepseek-v4-flash:cloud",
    title="Report Q&A Batch",
)
```

### Step 4: Report path
Tell the user where the HTML report was saved.

## Lint workflow

When the user asks to lint, check:

1. **Contradictions** — Read pairs of pages that discuss the same topic. Flag contradictory claims.
2. **Staleness** — Check if newer source summaries contain information that older entity/concept pages lack.
3. **Orphans** — Use the index to find pages with no inbound cross-references from other pages.
4. **Missing pages** — Scan source summaries for important entities/concepts mentioned but lacking their own page.
5. **Cross-reference gaps** — Check that related pages actually link to each other.
6. **Data gaps** — Identify questions the wiki can't answer yet; suggest sources to look for.

Write findings to `wiki/lint_reports/YYYY-MM-DD.md`. Append log entry.

## Citation system

- Source documents (document.md) use single `[¶N]` anchors generated by
  docling_converter.py. There are no range anchors in document.md — ranges
  exist only in wiki pages as shorthand (e.g., `[¶78-79, 238-274]`).
- In wiki pages and in answers, cite sources with document-prefixed anchors:
  `[¶42](http://localhost:8765/go.html#subset40-42)`
- Each citation links to viewer.html showing the page with a yellow bounding
  box on the cited paragraph.
- `citations.json` provides O(1) lookup: `citations["¶42"]` → `{page_id, type, content, bbox}`
- Path convention: citations use `http://localhost:8765/` URLs pointing to a local
  HTTP server serving the `processed_documents/` directory. Start it once with:
  `cd processed_documents && python3 -m http.server 8765 &`
  The format is `http://localhost:8765/go.html#{doc}-N` (e.g., `go.html#subset40-42` for ¶42 of subset40).
