# Plan: Complete Repository Standards Deliverables

## Context

Last session wrote `README.md` (136 lines) and `10-REPOSITORY-STANDARDS.md` (346 lines) successfully but hit an API content filtering error on the README write response. **The file did persist on disk** — the error was on the API response, not the file write. Three deliverables remain incomplete.

## Current State

| File | Status |
|------|--------|
| `README.md` | DONE (136 lines on disk) |
| `10-REPOSITORY-STANDARDS.md` | DONE (346 lines on disk) |
| `LICENSE` | MISSING |
| `.github/` directory | MISSING |
| `CLAUDE.md` update | NOT DONE |
| `ANNOTATED-MANIFEST.md` update | NOT DONE |

## Tasks

### 1. Write `LICENSE` (CC BY-SA 4.0)

Write the standard CC BY-SA 4.0 legal text. This is the Creative Commons license recommended in `10-REPOSITORY-STANDARDS.md` (§2.3) for documentation repos.

- **File:** `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/LICENSE`
- **Content:** Standard CC BY-SA 4.0 legalcode text
- **Note:** If full legalcode triggers content filter, use the short-form deed text with a link to the full license

### 2. Create `.github/` community health files

Per `10-REPOSITORY-STANDARDS.md` §4, create these files:

- `.github/CONTRIBUTING.md` — Documentation repo variant (correction process, suggestion process, editorial standards)
- `.github/SECURITY.md` — Documentation-only scope (no deployed code)
- `.github/CODE_OF_CONDUCT.md` — Contributor Covenant v2.1
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist for documentation changes

**Files to create:**
- `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/.github/CONTRIBUTING.md`
- `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/.github/SECURITY.md`
- `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/.github/CODE_OF_CONDUCT.md`
- `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/.github/PULL_REQUEST_TEMPLATE.md`

### 3. Update `CLAUDE.md`

Add a brief section referencing `10-REPOSITORY-STANDARDS.md` to the Document Layers or Working With This Corpus section.

- **File:** `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/CLAUDE.md`
- **Change:** Add `10-REPOSITORY-STANDARDS.md` to the Document Layers list under a new category, and mention it in the reading order
- **Approach:** Use Edit tool to insert into existing sections (lines ~51-57 for Document Layers, line ~47 for reading order)

### 4. Update `ANNOTATED-MANIFEST.md`

Add entries for all new files to both the detailed manifest (Section II) and the Quick Reference Table (Section VI).

- **File:** `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/ANNOTATED-MANIFEST.md`
- **New entries needed:**
  - `README.md` — corpus entry point (Layer 5: Standards)
  - `LICENSE` — CC BY-SA 4.0 license (Layer 5: Standards)
  - `10-REPOSITORY-STANDARDS.md` — Repository standards (Layer 1: Phase 1 Planning, numbered `10`)
  - `.github/CONTRIBUTING.md` — Contributing guidelines
  - `.github/SECURITY.md` — Security policy
  - `.github/CODE_OF_CONDUCT.md` — Code of conduct
  - `.github/PULL_REQUEST_TEMPLATE.md` — PR template
- **Also update:** File count in the header (line 4), and add rows to the Quick Reference Table (lines 1101-1143)

### 5. Verify all deliverables

After all writes, verify:
- All files exist via Glob
- README.md links point to real files
- ANNOTATED-MANIFEST.md file count is updated
- No broken cross-references

## Content Filter Mitigation

If any write hits the content filter:
1. Try writing in smaller chunks using Edit to build up the file
2. Remove any content that might be triggering the filter (e.g., specific phrases about vulnerabilities, security contacts)
3. Use more generic phrasing where possible

## Execution Order

1. `LICENSE` (independent)
2. `.github/` files (independent, can be parallel)
3. `CLAUDE.md` update (independent)
4. `ANNOTATED-MANIFEST.md` update (depends on knowing final file list from steps 1-3)
5. Verification (depends on all above)
