# Plan: Implement Documentation Skills as Repository Standards

## Context

The organvm-pactvm planning corpus has no README.md, no LICENSE, no `.github/` community health files, and 80+ files at root level. Three documentation skills exist that codify best practices for GitHub repos:

- **github-profile-architect** — profile-level branding (deferred for now)
- **github-repo-curator** — repo audit, curation, visibility strategy
- **github-repository-standards** — root hygiene, README quality, community health

The user wants to: (1) create a standalone standards document synthesizing these skills for all ~44 repos, (2) add CLAUDE.md references so AI agents always load them, and (3) apply full treatment to THIS directory as the first exemplar.

## Skill Source Paths

```
/Users/4jp/world/realm/operate/org/liminal/repo/a-i-skills/skills/documentation/github-profile-architect/
/Users/4jp/world/realm/operate/org/liminal/repo/a-i-skills/skills/documentation/github-repo-curator/
/Users/4jp/world/realm/operate/org/liminal/repo/a-i-skills/skills/documentation/github-repository-standards/
```

## Existing Documents to Preserve / Complement

- `01-README-AUDIT-FRAMEWORK.md` — 100-point scoring rubric (Existence 20 + Content 40 + Accuracy 20 + Portfolio 20)
- `03-PER-ORGAN-README-TEMPLATES.md` — 7 organ-specific README templates with YAML frontmatter
- `04-PER-ORGAN-VALIDATION-CHECKLISTS.md` — per-organ validation checklists
- `08-CANONICAL-ACTION-PLAN.md` D-07 — tiered repo classification (Flagship/Standard/Stub/Archive)

The new work **enhances** these, adding root hygiene, community health, curation strategy, and badge standards that the existing docs don't cover.

---

## Deliverables (5 items)

### 1. `10-REPOSITORY-STANDARDS.md` (NEW — ~2,000-2,500 words)

Standalone standards document synthesizing all three skills into organvm-specific standards. Sections:

1. **Purpose & Scope** — What this document covers, relationship to `01`/`03`/`04`
2. **Root Hygiene Standard** — Adapted from repository-standards skill
   - Required root files: README.md, LICENSE, .gitignore, CLAUDE.md
   - Required directories: `.github/`, `docs/` (for repos with documentation)
   - Config migration: tool configs → `.config/` where tooling supports it
   - Root file count target: <20 for code repos, flexible for documentation repos
3. **README Standard** — Progressive disclosure pattern from repository-standards
   - Three tiers aligned with `08` D-07: Flagship (12 sections, 3,000+ words), Standard (8 sections, 1,000+ words), Stub (4 sections, 200+ words)
   - Hero section pattern: title + badge row + one-line hook + quick start
   - Cross-references to `03-PER-ORGAN-README-TEMPLATES.md` for organ-specific sections
   - Badge ordering convention: Status → Metadata → Social → Activity
4. **Community Health Files** — `.github/` directory standard
   - `SECURITY.md` — vulnerability reporting process
   - `CONTRIBUTING.md` — contribution workflow (adapted per repo type)
   - `ISSUE_TEMPLATES/` — bug report + feature request templates
   - `PULL_REQUEST_TEMPLATE.md` — PR checklist
   - `CODE_OF_CONDUCT.md` — standard Contributor Covenant
5. **Curation & Visibility Strategy** — From repo-curator skill
   - Visibility decision matrix: Public / Private / Archive / Delete
   - Topics/tags taxonomy aligned with organ model: organ tag + domain tag + type tag + status tag
   - Pinned repo strategy per org (max 6 pins per org)
6. **Badge & Shield Standards** — From all three skills
   - Per-organ badge color scheme (consistent with branding)
   - Required badges by tier (Flagship: 4+, Standard: 2+, Stub: 1)
   - shields.io style: `flat-square` (consistent across all repos)
7. **Compliance Checklist** — Quick-reference checklist for validating any repo

### 2. `README.md` (NEW — this directory)

A proper README for the planning corpus itself. Structure:

- **Title + badge row** — "Seven-Organ System: Planning & Governance Corpus"
- **One-line description** — What this repo contains
- **Quick navigation** — Document reading order (adapted from CLAUDE.md §Reading Order)
- **Document architecture diagram** — The layer model (Genesis → Planning → Execution → v2 Active)
- **Current status** — Phase -1 complete, Bronze Sprint next
- **The Seven-Organ Model** — Table from CLAUDE.md
- **How to use this corpus** — For human readers and AI agents
- **License** — reference to LICENSE file
- **Author** — @4444j99

This replaces CLAUDE.md as the human entry point (CLAUDE.md remains as the AI agent entry point).

### 3. `LICENSE` (NEW)

CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike) — appropriate for a documentation/planning corpus. Not code, so MIT/Apache don't apply. CC BY-SA allows reuse with attribution and share-alike, which fits the "building in public" philosophy (ORGAN-V).

### 4. `.github/` directory (NEW)

```
.github/
├── CONTRIBUTING.md          — How to contribute to this planning corpus
├── SECURITY.md              — Vulnerability disclosure (lightweight for docs repo)
├── CODE_OF_CONDUCT.md       — Contributor Covenant v2.1
├── ISSUE_TEMPLATES/
│   ├── document-correction.md   — Report factual errors in planning docs
│   └── planning-suggestion.md   — Suggest changes to strategy/execution
└── PULL_REQUEST_TEMPLATE.md — PR checklist for doc changes
```

Adapted for a documentation corpus (not code-centric templates).

### 5. `CLAUDE.md` updates

Add a new section after the existing "Working With This Corpus" section:

```markdown
## Repository Standards (Skills Framework)

This project enforces repository standards derived from three documentation skills:

- **github-profile-architect** — `~/world/realm/operate/org/liminal/repo/a-i-skills/skills/documentation/github-profile-architect/SKILL.md`
- **github-repo-curator** — `~/world/realm/operate/org/liminal/repo/a-i-skills/skills/documentation/github-repo-curator/SKILL.md`
- **github-repository-standards** — `~/world/realm/operate/org/liminal/repo/a-i-skills/skills/documentation/github-repository-standards/SKILL.md`

### Key Standards (enforced across all 7 orgs)

1. **Root hygiene:** README.md, LICENSE, .gitignore, CLAUDE.md at root. Tool configs in `.config/` where supported.
2. **README progressive disclosure:** Hero → Value → Quick Start → Docs in <30 seconds.
3. **Community health:** `.github/` with CONTRIBUTING.md, SECURITY.md, issue templates, PR template.
4. **Badge convention:** `flat-square` style, order: Status → Metadata → Social → Activity.
5. **Tiered README depth:** Flagship (12 sections), Standard (8 sections), Stub (4 sections) per `08` D-07.
6. **Topics taxonomy:** `organ-{i..vii}` + domain tag + type tag + status tag on every repo.
7. **Visibility strategy:** Every repo has an explicit Public/Private/Archive decision in `registry-v2.json`.

See `10-REPOSITORY-STANDARDS.md` for full specification. When working on ANY repo in the seven-organ system, reference these standards.
```

---

## Execution Order

1. Write `10-REPOSITORY-STANDARDS.md`
2. Write `README.md`
3. Write `LICENSE` (CC BY-SA 4.0 full text)
4. Create `.github/` directory and all 5 files within it
5. Update `CLAUDE.md` (add Repository Standards section)
6. Update `ANNOTATED-MANIFEST.md` (add entries for new files)

## Files Modified

| File | Action | Description |
|------|--------|-------------|
| `10-REPOSITORY-STANDARDS.md` | NEW | Standalone standards document (~2,000-2,500 words) |
| `README.md` | NEW | Human-facing entry point for the planning corpus |
| `LICENSE` | NEW | CC BY-SA 4.0 full text |
| `.github/CONTRIBUTING.md` | NEW | Contribution guidelines for docs corpus |
| `.github/SECURITY.md` | NEW | Lightweight security disclosure |
| `.github/CODE_OF_CONDUCT.md` | NEW | Contributor Covenant v2.1 |
| `.github/ISSUE_TEMPLATES/document-correction.md` | NEW | Issue template for doc errors |
| `.github/ISSUE_TEMPLATES/planning-suggestion.md` | NEW | Issue template for strategy changes |
| `.github/PULL_REQUEST_TEMPLATE.md` | NEW | PR checklist template |
| `CLAUDE.md` | EDIT | Add Repository Standards section with skill paths + key principles |
| `ANNOTATED-MANIFEST.md` | EDIT | Add entries for all new files |

**Total: 9 new files + 2 edits**

## Verification

1. Confirm all new files exist: `ls README.md LICENSE .github/ 10-REPOSITORY-STANDARDS.md`
2. Confirm `.github/` has all 5 expected files
3. Grep CLAUDE.md for `Repository Standards` section
4. Grep ANNOTATED-MANIFEST.md for `10-REPOSITORY-STANDARDS`
5. Read `10-REPOSITORY-STANDARDS.md` end-to-end for coherence with existing `01`/`03`/`04` documents
6. Confirm no contradictions between new standards and `08-CANONICAL-ACTION-PLAN.md` decisions
