# SOP: Document Audit & Feature Extraction

## 1. Purpose & Scope

This SOP codifies the process for exhaustively auditing a repository's documentation and extracting actionable product features, architectural improvements, and behavioral insights as GitHub issues.

**When to run:**
- New repo with substantial `docs/` content that has never been triaged
- After a major documentation addition (research library, thesis, brainstorm transcripts)
- Quarterly review of repos with >20 unread documents
- Post-acquisition of external reference material (books, papers, competitor analyses)

**Applicable to:** Any repo in any organ with a `docs/` directory, `specs/`, `rfcs/`, `adrs/`, or equivalent documentation structure.

**Origin:** Codified from the Styx audit (2026-03-04) which produced 74 GitHub issues from 147 documents across 6 categories.

**Cross-reference:** `SOP--source-evaluation-and-bibliography.md` Phase II (CRAAP test) applies to evaluating external reference material encountered during document audits. `SOP--repo-onboarding-and-habitat-creation.md` governs post-audit repo creation when extracted features warrant a new repository.

---

## 2. Prerequisites

### Required Artifacts
- **Feature backlog or issue tracker:** `FEATURE-BACKLOG.md`, GitHub Issues, or equivalent. The audit cross-references against this to avoid duplicates.
- **Document manifest (optional):** `MANIFEST.md` or `docs/README.md` listing all documents. If absent, the audit generates one in Phase 1.

### Required Tools
- `gh` CLI (GitHub issue creation, label management)
- Claude Code or equivalent AI agent (for exhaustive reading at scale)
- `pandoc` (format conversion: epub, docx, HTML to plain text)
- `calibre` CLI tools (for `.azw3`, `.mobi` formats if applicable)

### Required Access
- Repository write access (issue creation, file commits)
- Familiarity with the project's domain (to assess feature relevance)

### Pre-Audit Checklist
1. Read the project's `CLAUDE.md` / `GEMINI.md` / `AGENTS.md` for conventions
2. Read `seed.yaml` for organ membership, tier, and declared edges
3. Run `gh issue list --state open | wc -l` to baseline existing issue count
4. Scan `FEATURE-BACKLOG.md` (if present) for existing tracked features

---

## 3. Phase 1: Inventory & Triage

**Goal:** Map all documents before reading any of them.

### Process
1. **List all `docs/` subdirectories and files** recursively. Record path, format, and approximate size.
2. **Classify by format:**
   - Markdown (`.md`) — directly readable
   - PDF (`.pdf`) — readable via tool with page ranges
   - EPUB/DOCX (`.epub`, `.docx`) — convert with `pandoc -t plain`
   - AZW3/MOBI (`.azw3`, `.mobi`) — convert with Calibre (`ebook-convert`)
   - Binary/media — note as unreadable, skip
3. **Identify format conversion gaps.** Note any documents that cannot be converted. Flag for manual review.
4. **Build or update a document manifest.** If `MANIFEST.md` doesn't exist, create it with: path, title, format, author (if known), date, read status.

### Output
A manifest table and a reading plan ordered by priority (brainstorm > research > architecture > reference > legal > misc).

---

## 4. Phase 2: Exhaustive Read & Extraction

**Goal:** Read every document word-for-word and extract actionable items.

### Process
1. **Read each document completely.** Do not skim. Do not summarize. The value is in the details that summaries miss.
2. **Extract every actionable item:**
   - Product features or feature ideas
   - Architectural suggestions or design patterns
   - Behavioral insights (user psychology, motivation, game theory)
   - Competitive intelligence (features competitors have that this product doesn't)
   - Research findings with product implications
   - Legal or compliance requirements that need engineering work
3. **Tag each extraction with:**
   - Source document (path)
   - Section or page reference
   - Verbatim quote or close paraphrase
   - Category: `feature`, `architecture`, `behavioral`, `competitive`, `research`, `legal`, `infrastructure`
4. **For reference books and external sources:** Note the theoretical framework, then extract product-applicable implications. A behavioral economics textbook yields feature ideas; a legal analysis yields compliance requirements.
5. **Organize by document folder** (e.g., all `docs/brainstorm/` extractions together, all `docs/research/` together).

### Parallelization Guide (16GB RAM constraint)
- Use up to 3 parallel agents for independent document reads
- Each agent reads one folder/category at a time
- Merge extractions after each batch completes
- Do not parallelize the deduplication phase (Phase 3)

---

## 5. Phase 3: Deduplication

**Goal:** Eliminate duplicates and identify genuinely new items.

### Cross-Reference Against
1. **Existing feature backlog** (`F-*` IDs or equivalent feature identifiers)
2. **All open GitHub issues** (`gh issue list --state open --limit 500`)
3. **Codebase** (grep for implemented but untracked features — functions, routes, components that exist but have no corresponding issue or backlog entry)
4. **Other documents' extractions** (two brainstorm transcripts may describe the same feature in different terms)

### Classification
- **Already tracked:** Skip. Note the existing issue/feature ID for cross-reference.
- **Partially tracked:** Enhance the existing issue with new details from the extraction. Add a comment rather than creating a duplicate.
- **Genuinely new:** Proceed to Phase 4 for issue creation.
- **Contradictory:** Flag when two documents propose incompatible approaches to the same problem. Create a single issue that frames the decision.

---

## 6. Phase 4: Issue Creation

**Goal:** Convert deduplicated extractions into structured GitHub issues.

### Issue Format
```markdown
**Title:** `feat: {descriptive title}` or `docs:` / `chore:` / `refactor:` as appropriate

**Body:**
## Source
- Document(s): `docs/research/competitor-analysis--beeminder.md`
- Author(s): (if attributed)
- Key quote: "> ..."

## Problem
What gap or opportunity this extraction addresses.

## Proposed Feature
1. Numbered requirements or design sketch
2. Include API surface, schema changes, or UI components if evident
3. Note dependencies on other features

## Cross-References
- Related feature IDs: F-042, F-067
- Related issues: #45, #89
- Code paths: `src/modules/stakes/`
```

### Labels
- Always include: `enhancement` (or `documentation`, `chore` as appropriate)
- Domain labels: match the project's existing label taxonomy
- Add `unimplemented-plan` if the extraction comes from a plan file that was never executed

### Batch Strategy
- Create issues in thematic groups (all behavioral-science extractions together, all infrastructure together)
- Maintain a running tally: "Issues created: 0→12 (brainstorm), 12→28 (research), ..."
- Number ranges help audit the process later

---

## 7. Phase 5: Post-Audit Artifacts

**Goal:** Update project records and commit the audit results.

### Deliverables
1. **Update `FEATURE-BACKLOG.md`** with new `F-*` entries (if the project uses this system)
2. **Update `MANIFEST.md`** with any new documents discovered or created during the audit
3. **Create a syllabus** (if reference library was audited): structured reading list with chapter/section recommendations for further research
4. **Write audit summary:** `docs/planning/planning--document-audit--YYYY-MM-DD.md` containing:
   - Folders audited and document count per folder
   - Issues created (with GitHub issue number ranges)
   - Format conversion failures or gaps noted
   - Observations about document quality, coverage, or organization
5. **Commit all artifacts and push**

### Post-Audit System Commands
```bash
organvm context sync --dry-run   # preview context file updates
organvm context sync --write     # propagate if changes needed
```

---

## Appendix A: Format Conversion Reference

| Format | Command | Notes |
|--------|---------|-------|
| EPUB to text | `pandoc -t plain input.epub -o output.txt` | Preserves structure |
| DOCX to text | `pandoc -t plain input.docx -o output.txt` | |
| PDF | Read directly with tool (page ranges) | Large PDFs: read 20 pages at a time |
| AZW3/MOBI | `ebook-convert input.azw3 output.txt` | Requires Calibre |
| HTML | `pandoc -t plain input.html -o output.txt` | Or read directly |

## Appendix B: Issue Body Template

Copy-paste skeleton for rapid issue creation:

```markdown
## Source
- Document(s):
- Key quote: "> ..."

## Problem


## Proposed Feature
1.

## Cross-References
- Issues:
- Code:
```

## Appendix C: Adaptation for Non-Docs Repos

For repos that use `specs/`, `rfcs/`, `adrs/`, or `design/` instead of `docs/`:
- Apply the same 5-phase process to whatever documentation directory exists
- ADRs: each ADR is a micro-document; extract unresolved "consequences" sections as issues
- RFCs: extract "open questions" and "future work" sections
- Specs: compare spec requirements against implementation; gaps become issues

## Appendix D: Cross-Reference to Governance

- Constitution: `organvm-corpvs-testamentvm/docs/memory/constitution.md`
- Key workflows: `organvm-corpvs-testamentvm/docs/operations/key-workflows.md`
- Operational cadence: `organvm-corpvs-testamentvm/docs/operations/operational-cadence.md`
- Governance rules: `organvm-corpvs-testamentvm/governance-rules.json`
- This SOP: `praxis-perpetua/standards/SOP--document-audit-feature-extraction.md`
