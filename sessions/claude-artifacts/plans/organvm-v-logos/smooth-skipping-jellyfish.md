# Plan: Publish Dissertation to Public-Process Site + Create Dissertation SOP

**Date:** 2026-03-04
**Context:** The application-pipeline project has a ~50K word doctoral dissertation (`docs/thesis/`, 8 chapter files + 1 unified). The user wants to: (1) publish it on the ORGAN-V essay site with a new "dissertations" section, and (2) create an SOP for producing doctoral dissertations across all ORGANVM projects.

---

## Part 1: Publish Dissertation to Public-Process Site

### 1.1 Add `dissertations` Jekyll collection

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/_config.yml`

- Add `dissertations` collection with `output: true` and permalink `/dissertations/:title/`
- Add defaults block assigning `layout: dissertation` to the collection
- Keep existing essay/log collections untouched

### 1.2 Create `dissertation` layout

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/_layouts/dissertation.html`

- Based on the existing `essay.html` layout but adapted for long-form academic content
- Add chapter navigation (prev/next chapter links within the dissertation)
- Add a "Back to dissertation overview" link
- Add table of contents support for each chapter
- Display additional academic metadata (abstract excerpt, word count, chapter number)

### 1.3 Create dissertation content directory + chapter files

**Directory:** `/Users/4jp/Workspace/organvm-v-logos/public-process/dissertations/`

Publish the unified thesis as **chapter-per-page** (matches the existing separate chapter files). Each chapter becomes a collection item:

| Source (application-pipeline) | Destination (public-process) |
|------|------|
| `00-preliminary-pages.md` | `dissertations/precision-pipeline/00-preliminary-pages.md` |
| `01-introduction.md` | `dissertations/precision-pipeline/01-introduction.md` |
| `02-literature-review.md` | `dissertations/precision-pipeline/02-literature-review.md` |
| `03-methodology.md` | `dissertations/precision-pipeline/03-methodology.md` |
| `04-results.md` | `dissertations/precision-pipeline/04-results.md` |
| `05-discussion.md` | `dissertations/precision-pipeline/05-discussion.md` |
| `06-references.md` | `dissertations/precision-pipeline/06-references.md` |
| `07-appendices.md` | `dissertations/precision-pipeline/07-appendices.md` |

Each file gets Jekyll frontmatter added:
```yaml
---
title: "Chapter N: Title"
dissertation: "precision-pipeline"
dissertation_title: "Precision Over Volume"
chapter: N
author: "@4444J99"
date: "2026-03-04"
tags: [mcda, career-pipeline, network-theory, portfolio-optimization, precision-hiring]
category: "dissertation"
word_count: NNNN
reading_time: "NN min"
related_repos:
  - 4444J99/application-pipeline
---
```

### 1.4 Create dissertation landing page

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/dissertations.md`

- Title, abstract, full table of contents linking to each chapter
- Metadata: total word count, date, author
- Stat grid (similar to index.md pattern) showing chapters, total words, references

### 1.5 Add `_posts/` entry for the dissertation

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/_posts/2026-03-04-precision-over-volume-doctoral-thesis.md`

- Short announcement post linking to the dissertations landing page
- Follows existing blog post pattern so it appears in the RSS feed and main index

### 1.6 Update navigation

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/_includes/header.html`

- Add "Dissertations" link between existing nav items

### 1.7 Update data index

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/data/essays-index.json`

- Update stats to include dissertation count (or create separate `dissertations-index.json`)

### 1.8 Update index.md

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/index.md`

- Add a "Dissertations" section below the essays section linking to the dissertations landing page

---

## Part 2: Create Dissertation SOP

**File:** `/Users/4jp/Workspace/organvm-v-logos/public-process/docs/sop-doctoral-dissertation.md`

This SOP codifies the process used to create the precision-pipeline thesis, abstracted for reuse across all ORGANVM projects.

### SOP Structure

1. **Purpose & Scope** — What this SOP covers; target: one doctoral dissertation per major ORGANVM project
2. **Prerequisites** — What must exist before starting (mature codebase, production data, 6+ months of documented decisions)
3. **Phase 1: Research Notes** — Systematic literature review organized by domain; output: dated plan file (like the v1 plan)
4. **Phase 2: Mathematical Foundations** — Formal mathematical treatment with proofs/derivations; output: v2 plan file (like the v2 plan)
5. **Phase 3: Thesis Drafting** — Chapter-by-chapter composition following standard academic structure (prelim → intro → lit review → methodology → results → discussion → refs → appendices)
6. **Phase 4: Integration** — Wire the thesis into the project's `docs/thesis/` directory; create both unified and chapter-split versions
7. **Phase 5: Publication** — Push to public-process site using the dissertations collection pattern
8. **Quality Gates** — Word count targets (~50K), citation count, chapter completeness checklist
9. **Naming Convention** — `docs/thesis/` in source project; `dissertations/{project-slug}/` on the site
10. **Template** — Frontmatter template, chapter file template, landing page template

### Candidate Projects for Future Dissertations

The SOP will include a table of ORGANVM projects ready for dissertation treatment, based on maturity:

| Project | Organ | Dissertation Topic |
|---------|-------|----|
| `recursive-engine--generative-entity` | I | Recursive Epistemological Computing |
| `metasystem-master` | II | Generative Art Systems Architecture |
| `public-record-data-scrapper` | III | Web-Scale Data Collection Pipelines |
| `agentic-titan` | IV | Multi-Topology AI Agent Orchestration |
| `public-process` | V | Public Discourse as Creative Practice |
| (this site itself) | V | — |

---

## Execution Order

1. Create dissertation layout (`_layouts/dissertation.html`)
2. Update `_config.yml` with new collection
3. Create `dissertations/precision-pipeline/` directory with all 8 chapter files (copy from source, add frontmatter)
4. Create `dissertations.md` landing page
5. Create `_posts/` announcement entry
6. Update `header.html` navigation
7. Update `index.md` with dissertations section
8. Create SOP document
9. Build locally (`bundle exec jekyll serve`) to verify
10. Commit in public-process repo and push

---

## Key Files Modified

### public-process repo (all changes)
- `_config.yml` — add dissertations collection
- `_layouts/dissertation.html` — new layout (based on essay.html)
- `_includes/header.html` — add nav link
- `index.md` — add dissertations section
- `dissertations.md` — new landing page
- `dissertations/precision-pipeline/*.md` — 8 chapter files (new)
- `_posts/2026-03-04-precision-over-volume-doctoral-thesis.md` — new announcement post
- `docs/sop-doctoral-dissertation.md` — new SOP document

### Source files (read-only, content copied from)
- `/Users/4jp/Workspace/4444J99/application-pipeline/docs/thesis/*.md` — 8 chapter files

---

## Verification

1. `cd /Users/4jp/Workspace/organvm-v-logos/public-process && bundle exec jekyll build` — site builds without errors
2. Verify `/dissertations/` index page renders with table of contents
3. Verify each chapter page renders with proper navigation
4. Verify header nav includes "Dissertations" link
5. Verify `_posts/` announcement appears in the main index
6. Verify SOP is complete and actionable
