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
- **Citations to sources:** Every `[¶N]` in wiki page body text MUST be a clickable markdown link: `[¶N](http://localhost:8765/{doc}/go.html#N)` where `{doc}` is the source document folder name (e.g. `subset40`). Plain-text `[¶N]` is not acceptable. Ranges like `[¶A-B]` link to the first paragraph in the range.
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

## Query Workflow

For EVERY user question, the answer MUST be generated by `qa_agent.py`.
Claude Code never answers directly: it explores the wiki to decide which
document to pass to qa_agent.py.

### Step 1: Find the document (exhaust the wiki before grep)
1. ALWAYS start by reading `wiki/index.md`. Look for pages matching the
   question, including partial and related matches — not just exact titles.
2. Read any promising wiki page. Follow its cross-references to other pages.
   Extract the source document from `**Source:**` metadata.
3. ONLY if no wiki page (direct or related) points to a relevant document:
   search with grep across `processed_documents/*/document.md`.
4. If grep also finds nothing: ask the user.

### Step 2: Run qa_agent.py (MANDATORY)
```
python qa_agent.py -d processed_documents/{doc} -q "user's exact question"
```
qa_agent.py reads the full document.md, passes it to the LLM, and returns
the answer with `[¶N]` citations.

### Step 3: Show the answer
Report qa_agent.py's output. Citations must be linked with the document
folder name: `[¶N](http://localhost:8765/{doc}/go.html#N)`

### Filing
If the user says "file this": create a wiki page, update index.md and log.md.

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
- In wiki pages and in answers, cite sources with the document folder:
  `[¶42](http://localhost:8765/{doc}/go.html#42)`
- Each citation links to viewer.html showing the page with a yellow bounding
  box on the cited paragraph.
- `citations.json` provides O(1) lookup: `citations["¶42"]` → `{page_id, type, content, bbox}`
- Path convention: citations use `http://localhost:8765/` URLs pointing to a local
  HTTP server serving the `processed_documents/` directory. Start it once with:
  `cd processed_documents && python3 -m http.server 8765 &`
  The format is `http://localhost:8765/{doc}/go.html#N` (e.g. `http://localhost:8765/subset40/go.html#42`).
