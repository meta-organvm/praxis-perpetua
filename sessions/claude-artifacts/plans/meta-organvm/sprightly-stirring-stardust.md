# Plan: Enterprise SOP — Document Audit & Feature Extraction

**Date:** 2026-03-04
**Context:** We systematically audited every folder in `peer-audited--behavioral-blockchain/docs/` (brainstorm, legal, research, reference-library), reading every document word-for-word, extracting product/feature ideas, deduplicating against the codebase + feature backlog + existing GitHub issues, and creating 74 new GitHub issues (#46–#119). The user wants this codified as a reusable SOP for all ~111 repos across 8 organs.

---

## What to Create

**One SOP document** placed in the enterprise governance corpus:

```
meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md
```

This follows the existing pattern:
- `key-workflows.md` (6 step-by-step procedures) — same directory
- `operational-cadence.md` (weekly/monthly rhythm) — same directory
- Double-hyphen kebab-case naming convention
- "Audience: competent developer with no prior system knowledge" tone

## SOP Structure

The document will have **7 sections** mirroring the actual process we executed:

### 1. Purpose & Scope
- What this SOP does (exhaustive document audit → GitHub issues)
- When to run it (new repo, major doc additions, quarterly review)
- Applicable to any repo in any organ with a `docs/` directory

### 2. Prerequisites
- Required artifacts: `FEATURE-BACKLOG.md` (or equivalent), `MANIFEST.md`
- Required tools: `gh` CLI, Claude Code (or manual), pandoc (for format conversion)
- Required access: GitHub repo write access, issue creation permissions
- Pre-audit checklist: read project CLAUDE.md, read seed.yaml, inventory existing issues

### 3. Phase 1 — Inventory & Triage
- List all `docs/` subdirectories and files
- Classify by format (markdown, PDF, epub, azw3, binary)
- Identify unreadable formats — note gaps, convert where possible (pandoc)
- Build a document manifest if one doesn't exist (reference Styx `MANIFEST.md` as template)

### 4. Phase 2 — Exhaustive Read & Extraction
- Read every document **word-for-word** (not skim, not summarize)
- Extract every product idea, feature concept, architectural suggestion, or behavioral insight
- Tag each extraction with: source document, page/section, verbatim quote or paraphrase
- Organize extractions by document folder (brainstorm, research, legal, architecture, etc.)
- For reference books/external sources: read in full, note the theoretical framework, extract actionable product implications

### 5. Phase 3 — Deduplication
- Cross-reference extractions against:
  1. Existing feature backlog (`F-*` IDs if available)
  2. All open GitHub issues
  3. Codebase (grep for implemented but untracked features)
- Merge overlapping extractions across documents into consolidated candidates
- Flag items that are already tracked (skip) vs. partially tracked (enhance existing issue) vs. genuinely new (create issue)

### 6. Phase 4 — Issue Creation
- Issue title format: `feat: {descriptive title}`
- Issue body template (structured markdown):
  - **Source**: Document(s) and author(s) cited
  - **Problem**: What gap or opportunity the extraction addresses
  - **Proposed Feature**: Numbered requirements/design sketch
  - **Cross-References**: Related `F-*` IDs, issue numbers, code paths
- Labels: `enhancement` + domain labels (e.g., `behavioral-science`, `contracts`, `ux`)
- Batch creation strategy: create in thematic groups, not document order
- Running tally: track issues created per folder, maintain cumulative count

### 7. Phase 5 — Post-Audit Artifacts
- Update `FEATURE-BACKLOG.md` with new `F-*` entries (if project uses this system)
- Update `MANIFEST.md` with any new documents discovered/created
- Create a **syllabus** (if reference library audit): structured reading list for further research
- Write audit summary: folders audited, issues created (with ranges), gaps noted, format conversion failures
- Commit all new artifacts and push

### Appendices
- **A. Format Conversion Reference**: pandoc commands for epub→txt, PDF reading tips, azw3 limitations (needs Calibre)
- **B. Issue Body Template**: Copy-pasteable markdown skeleton
- **C. Claude Code Parallelization Guide**: How to use parallel agents for multi-document reads (5 agents max on 16GB RAM)
- **D. Adapting for Non-Docs Repos**: How to apply this to repos that have specs, RFCs, ADRs, or design docs instead of a `docs/` folder
- **E. Cross-Reference to Governance**: Links to constitution, governance-rules.json, key-workflows.md, operational-cadence.md

## Files to Modify

| File | Action |
|------|--------|
| `meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md` | **CREATE** — the SOP |
| `meta-organvm/organvm-corpvs-testamentvm/docs/operations/key-workflows.md` | **EDIT** — add entry #7 linking to the new SOP |

## Verification

1. Read the SOP end-to-end and confirm every step of the actual Styx audit is captured
2. Confirm the SOP is generic enough to apply to any repo (not Styx-specific)
3. Confirm naming convention matches existing governance docs
4. Confirm cross-references to constitution, key-workflows, operational-cadence are accurate
