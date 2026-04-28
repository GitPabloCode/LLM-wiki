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
- **Citations to sources:** `[¶N](viewer.html#N)` where the viewer is under `processed_documents/{doc}/`.
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

## Query workflow

1. User asks a question
2. Read `wiki/index.md` to find relevant pages
3. Read those pages, follow cross-references
4. If wiki-level synthesis is enough: answer with citations to wiki pages
5. If source-level detail is needed: search `citations.json` in the relevant `processed_documents/{doc}/` folder, or use `qa_agent.py`:
   ```
   python qa_agent.py -d processed_documents/{doc} -q "question" -m bm25
   ```
6. Synthesize answer with `[¶N]` citations pointing to the source viewer
7. If the user says "file this", create a new wiki page with the answer and update the index

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

- Source documents use `[¶N]` anchors generated by docling_converter.py
- In wiki pages, cite sources as: `[¶42](../../processed_documents/{doc}/viewer.html#42)`
- Each citation links to viewer.html showing the page with a yellow bounding box on the cited paragraph
- `citations.json` provides O(1) lookup: `citations["¶42"]` → `{page_id, type, content, bbox}`
