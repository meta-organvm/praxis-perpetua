---
sop: true
name: completeness-verification
scope: system
phase: hardening
triggers:
  - context:pre-promotion
  - context:pre-release
  - context:milestone-complete
complements:
  - structural-integrity-audit
  - session-self-critique
overrides: null
---
# SOP: Completeness Verification

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** End-to-end sweep to verify that a deliverable, repo, or milestone is genuinely complete — "wrapped with a beautiful bow, eat off the floor."

---

## 1. Ontological Purpose

Completeness is not perfection — it is the absence of unfinished edges. A project that works but has broken links, placeholder comments, missing tests, or undocumented features is not complete. This SOP codifies the final sweep that catches what working memory forgets: the TODO comments left behind, the edge case untested, the config file still pointing to localhost.

This is the complement to `SOP--structural-integrity-audit.md` (which checks *structure*) — this SOP checks *completion*.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--structural-integrity-audit.md` (structural soundness), `SOP--session-self-critique.md` (per-session review)

---

## 2. Trigger

Execute this SOP when:
- A milestone is declared "done" (before closing)
- A repo is being promoted from CANDIDATE to PUBLIC_PROCESS
- A release is being tagged
- A deliverable is being presented to an external audience
- The phrase "beautiful bow" appears in your inner monologue

**Exception:** In-progress work and exploratory branches do not require completeness verification.

---

## 3. Phase I: Artifact Inventory

**Goal:** Know everything that was supposed to be delivered.

### Process

1. **Retrieve the governing plan** from `.claude/plans/` or the task tracker
2. **List all planned deliverables:**
   - Code files (new modules, modified files)
   - Documentation (README, CLAUDE.md, inline docs)
   - Tests (unit, integration, E2E)
   - Configuration (CI, deployment, env vars)
   - Registry updates (seed.yaml, registry-v2.json)
3. **Cross-reference against actual output:**
   - `git log --since=<start>` for all commits
   - `git status` for uncommitted work
   - Plan file task checkboxes

### Output
A checklist: `Planned | Delivered | Status (done/partial/missing)`

---

## 4. Phase II: Loose End Sweep

**Goal:** Find everything that was started but not finished.

### Process

1. **Search for TODO/FIXME/HACK markers:**
   ```bash
   grep -rn "TODO\|FIXME\|HACK\|XXX\|TEMP\|PLACEHOLDER" src/ tests/
   ```
2. **Search for placeholder content:**
   - `<!-- ... -->` comments that were meant to be replaced
   - Empty function bodies or `pass` statements
   - `raise NotImplementedError`
   - Hardcoded test values that should be parameterized
3. **Check for orphaned files:**
   - Files created during development but not imported/used anywhere
   - Test fixtures that are no longer referenced
4. **Check for broken references:**
   - Internal links in markdown files
   - Import statements that reference moved/renamed modules
   - Cross-references to other repos that may have changed

### Output
A loose ends list with severity: `MUST FIX | SHOULD FIX | ACCEPTABLE`

---

## 5. Phase III: Test & Lint Verification

**Goal:** Confirm all quality gates pass.

### Process

1. **Run the full test suite:** `pytest tests/ -v`
2. **Run the linter:** `ruff check src/`
3. **Run the type checker** (if configured): `pyright` or `tsc --noEmit`
4. **Run any project-specific checks:**
   - Schema validation: `organvm-validate`
   - Registry validation: `organvm registry validate`
   - Seed validation: `organvm seed validate`
5. **Verify CI would pass** — check that local results match CI expectations

### Output
All quality gates green, or a list of failures to fix.

---

## 6. Phase IV: External Review

**Goal:** Verify the deliverable works from an outsider's perspective.

### Process

1. **Fresh clone test:** Would a `git clone` + documented setup steps produce a working system?
2. **README accuracy:** Does every feature described in the README actually work?
3. **CLI help accuracy:** Do `--help` outputs match actual behavior?
4. **Stranger test:** Apply `SOP--stranger-test-protocol.md` — could someone unfamiliar use this?

### Output
External review notes with any discrepancies between documentation and reality.

---

## 7. Starter Research Questions

- What was promised in the plan that hasn't been checked off?
- Are there any "I'll come back to this" notes left in the code?
- Would the test suite catch a regression in the features just built?
- Does the documentation describe the system as it is, or as it was planned to be?

---

## 8. Output Artifacts

- Completeness checklist (planned vs. delivered)
- Loose ends inventory
- Quality gate results
- External review notes

---

## 9. Verification

- [ ] All planned deliverables are accounted for
- [ ] No TODO/FIXME markers remain in shipped code
- [ ] All tests pass
- [ ] Linter and type checker pass
- [ ] README matches current reality
- [ ] No orphaned files or broken references

---

## 10. Prompt Examples

Representative prompts from clipboard history that trigger this pattern:

### Example 1

> devise plan to elevate repo to perfection;

### Example 2

> Add a prompt schema (if prompts are introduced) to fully match the original Phase 6
> structure. Do a final sweep to remove or relocate archived chatmodes once you
> confirm none are in use.
