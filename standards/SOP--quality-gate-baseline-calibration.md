---
sop: true
name: quality-gate-baseline-calibration
scope: system
phase: hardening
triggers:
  - context:ci-setup
  - context:quality-gate
complements:
  - verification-loop
  - coding-standards-enforcer
overrides: null
---
# SOP: Quality Gate Baseline Calibration

**Version:** 1.0.0 | **Date:** March 9, 2026 | **Status:** Active
**Scope:** Procedure for establishing, calibrating, and tightening quality gate thresholds (bundle size, Lighthouse scores, test coverage, lint rules) from measured baselines.

---

## 1. Ontological Purpose

Quality gates are ratchets — they only tighten, never loosen. But a ratchet set aspirationally rather than empirically is a guarantee of CI failure. Setting a bundle budget of 200KB when the actual bundle is 340KB does not enforce quality — it blocks all merges until someone loosens the gate, defeating its purpose.

This SOP ensures that every quality gate starts from a measured baseline and tightens on a predictable cadence. The gate exists to prevent regression, not to enforce aspirational targets that were never met.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 2: Quality & Integrity)
**Cross-reference:** `SOP--cicd-resilience-and-recovery.md` (quality gates are CI components), `SOP--structural-integrity-audit.md`
**Precedent:** Portfolio GitHub Actions 4-commit fix cycle (2026-03-08): aspirational Lighthouse thresholds, full-site scanning, formatter violations, slug mismatch.

---

## 2. Trigger

Execute this SOP when:
- Adding a new quality gate to CI (bundle budget, Lighthouse, coverage threshold, lint rule set)
- Migrating a project to a new formatter or linter
- A quality gate is failing on merge and no one knows what the "correct" value is

---

## 3. Phase I: Measure the Baseline

### Process

1. **Run the gate locally** against the current codebase in its current state:
   - Bundle size: `npm run build && du -sh dist/`
   - Lighthouse: `lhci collect --url=<local-url>` on 6 representative pages (see sampling below)
   - Test coverage: `pytest --cov --cov-report=term-missing`
   - Lint: `ruff check . --statistics` or `biome check . --reporter=summary`

2. **Record the raw measurements** in a table:

   | Gate | Measured Value | Unit | Date |
   |------|---------------|------|------|
   | Bundle size | 342KB | KB gzipped | 2026-03-09 |
   | Lighthouse performance | 78 | score | 2026-03-09 |
   | Test coverage | 67% | percentage | 2026-03-09 |
   | Lint violations | 12 | count | 2026-03-09 |

3. **Representative page sampling** (for Lighthouse and similar per-page gates):
   - Do NOT scan all pages. Select 6 archetypes:
     1. Home / landing page
     2. A content-heavy page (long text, many images)
     3. A data-heavy page (tables, lists, dynamic content)
     4. A minimal page (about, contact)
     5. A page with interactive components (forms, modals)
     6. A page with third-party embeds (if any)
   - Document the selected pages and why they represent the full surface.

### Deliverables
- Baseline measurement table
- Representative page list (if applicable)

---

## 4. Phase II: Set Initial Thresholds

### Process

1. **Set initial threshold at measured value + 10% headroom:**
   - Bundle: 342KB → threshold = 376KB
   - Lighthouse: 78 → threshold = 70 (round down to nearest 5 for scores)
   - Coverage: 67% → threshold = 60% (round down to nearest 5)
   - Lint: 12 → threshold = 15 (round up)

2. **Split thresholds by environment:**
   - **CI floor** (in CI config): tolerant — the value above. Merge is blocked only if regression is severe.
   - **Local target** (in docs or pre-commit): aspirational — where you want to be (e.g., bundle 250KB, Lighthouse 90).

3. **Document the calibration decision:**
   ```markdown
   ## Quality Gate Calibration — 2026-03-09
   | Gate | Measured | CI Floor | Local Target | Tighten Cadence |
   |------|---------|----------|--------------|----------------|
   | Bundle | 342KB | 376KB | 250KB | Monthly |
   | Lighthouse | 78 | 70 | 90 | Monthly |
   ```

4. **Run formatter/linter in fix mode BEFORE committing thresholds:**
   - `biome check --write .` or `ruff check --fix .`
   - Commit the fixes first, then commit the gate configuration
   - Never introduce a gate that immediately fails on the current codebase

### Deliverables
- CI gate configuration committed
- Calibration table in project docs or `CONTRIBUTING.md`

---

## 5. Phase III: Tightening Cadence

### Process

1. **Monthly review:** Re-measure actual values. If the codebase has improved, tighten the CI floor:
   - New floor = max(current measurement, old floor - improvement increment)
   - Never tighten past the actual measured value

2. **Improvement increment guidelines:**
   - Bundle size: tighten by 5-10% per month
   - Lighthouse: tighten by 5 points per month
   - Test coverage: tighten by 3-5% per month
   - Lint violations: tighten by 20% per month (violations should trend to zero)

3. **Ratchet log:** Append each tightening to the calibration table with the date and measured value that justified it.

4. **Emergency loosening:** If a legitimate architectural change (new dependency, feature flag) causes a threshold breach:
   - Re-measure the baseline with the new architecture
   - Set a new floor from the new measurement + headroom
   - Document why the loosening is justified (not a regression)
   - Resume the tightening cadence from the new baseline

### Deliverables
- Updated calibration table (appended, not overwritten)

---

## 6. Phase IV: Cross-Reference Validation

### Process

1. **When a quality gate references identifiers from another system, validate them:**
   - Route slugs in PrismNav → validate against `route-manifest.ts`
   - Repo names in dependency arrays → validate against `registry-v2.json`
   - Component names in style guides → validate against component directory

2. **Add a validation step to CI** that cross-checks referenced identifiers:
   ```bash
   # Example: validate all repoSlug values exist in route manifest
   node scripts/validate-slugs.js
   ```

3. **If automated validation is not feasible**, add a manual checklist item to the PR template.

### Deliverables
- Cross-reference validation script or checklist
- No phantom references in quality gate configuration

---

## 7. Output Artifacts

- Baseline measurement table (dated)
- CI gate configuration with calibrated thresholds
- Calibration documentation in project docs
- Cross-reference validation mechanism
- Ratchet tightening log (living document)

---

## 8. Success Criteria

- Quality gates pass on the first CI run after configuration
- Zero aspirational-threshold failures (gate was set from measurement, not hope)
- Ratchet tightening occurs at documented cadence
- All cross-referenced identifiers resolve to real entities

---

## 9. Cross-References

- `SOP--cicd-resilience-and-recovery.md` — quality gates are CI pipeline components
- `SOP--structural-integrity-audit.md` — gates form part of structural quality
- `SOP--cross-reference-validation.md` — detailed cross-reference validation procedure
- `lessons/derived-principles.md` — Principle C4 (test coverage ≠ correctness)

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
