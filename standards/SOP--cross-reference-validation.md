---
sop: true
name: cross-reference-validation
scope: system
phase: hardening
triggers:
  - context:ci-setup
  - context:data-integration
complements:
  - verification-loop
overrides: null
---
# SOP: Cross-Reference Validation

**Version:** 1.0.0 | **Date:** March 9, 2026 | **Status:** Active
**Scope:** Procedure for validating that identifiers referenced across system boundaries (slugs, repo names, component IDs) resolve to real entities in their canonical source.

---

## 1. Ontological Purpose

When system A references system B by slug or ID, there is no compiler to catch a typo. A portfolio PrismNav component referencing `repoSlug: "my-knowlege-base"` (note the typo) will silently fail to link to the repo. A registry `dependencies` entry pointing to `"nonexistent-repo"` will pass validation but break dependency graph traversal.

Cross-reference validation is the type-checker for inter-system contracts. Without it, every rename, every slug change, and every new identifier creates a potential phantom reference that silently degrades system behavior.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 2: Quality & Integrity)
**Cross-reference:** `SOP--quality-gate-baseline-calibration.md` (Phase IV: Cross-Reference Validation), `SOP--structural-integrity-audit.md`
**Precedent:** Portfolio PrismNav repo slugs hardcoded wrong, didn't match canonical manifest (2026-03-08).

---

## 2. Trigger

Execute this SOP when:
- A new integration between two systems is created
- Identifiers are renamed in a canonical source
- A cross-system validation failure is discovered
- Setting up CI for a project that references external data sources

---

## 3. Phase I: Identify Cross-Reference Boundaries

### Process

1. **Map every point where one system references another by identifier:**

   | Referencing System | Referenced System | Identifier Type | Canonical Source |
   |-------------------|-------------------|-----------------|-----------------|
   | Portfolio PrismNav | Route manifest | `repoSlug` | `route-manifest.ts` |
   | Registry | Registry | `dependencies[]` | `registry-v2.json` repo names |
   | seed.yaml | Registry | `produces`/`consumes` targets | `registry-v2.json` repo names |
   | Dashboard | Registry | repo names in queries | `registry-v2.json` |
   | CLAUDE.md auto-sections | Registry | sibling repo names | `registry-v2.json` |
   | SOP cross-references | Filesystem | file paths | Actual files on disk |

2. **For each boundary, identify:**
   - Who is the authority? (Which system is the canonical source?)
   - How often does the canonical source change?
   - What is the blast radius of a phantom reference?

### Deliverables
- Cross-reference boundary map

---

## 4. Phase II: Build Validation Checks

### Process

1. **For each boundary, create a validation check:**

   **Type A — Script validation (preferred):**
   ```bash
   # Example: validate PrismNav slugs against route manifest
   node scripts/validate-slugs.js

   # Example: validate registry dependency references
   organvm registry validate  # already checks dependency resolution

   # Example: validate seed.yaml edge targets
   organvm seed validate  # checks produces/consumes targets
   ```

   **Type B — CI step:**
   ```yaml
   - name: Validate cross-references
     run: |
       node scripts/validate-slugs.js
       organvm registry validate
       organvm seed validate
   ```

   **Type C — Pre-commit hook (for high-frequency references):**
   ```bash
   # In .husky/pre-commit or .git/hooks/pre-commit
   node scripts/validate-slugs.js || exit 1
   ```

2. **Validation check requirements:**
   - Must load the canonical source (not a cached copy)
   - Must report the specific phantom reference, not just "validation failed"
   - Must exit with non-zero code on failure
   - Must be runnable locally (not CI-only)

3. **For references that can't be validated automatically** (e.g., external URLs, cross-repo file paths):
   - Add a manual checklist item to the PR template
   - Document the reference in a `CROSS_REFS.md` file that humans can audit

### Deliverables
- Validation script per boundary
- CI integration for automated boundaries
- Manual checklist for non-automatable boundaries

---

## 5. Phase III: Rename Protocol

### Process

1. **When renaming an identifier in a canonical source:**
   - Search all known referencing systems for the old identifier
   - Update all references before or simultaneously with the rename
   - Run all validation checks to confirm zero phantom references

2. **Search commands by identifier type:**
   ```bash
   # Repo name rename
   grep -rn "old-repo-name" ~/Workspace/ --include="*.json" --include="*.yaml" --include="*.ts" --include="*.md"

   # Route slug rename
   grep -rn "old-slug" src/ --include="*.ts" --include="*.tsx"

   # Component name rename
   grep -rn "OldComponent" src/ --include="*.tsx" --include="*.ts"
   ```

3. **Commit the rename and all reference updates in a single atomic commit** (or PR) to prevent intermediate states with broken references.

### Deliverables
- All references updated
- Validation checks pass after rename

---

## 6. Output Artifacts

- Cross-reference boundary map
- Validation scripts per boundary
- CI configuration for automated validation
- `CROSS_REFS.md` for non-automatable references (if applicable)

---

## 7. Success Criteria

- Zero phantom references in production
- Every rename triggers a reference search
- Validation checks run in CI and block merge on failure
- New cross-reference boundaries are documented when created

---

## 8. Cross-References

- `SOP--quality-gate-baseline-calibration.md` — cross-reference validation is a quality gate component
- `SOP--structural-integrity-audit.md` — phantom references are structural defects
- `SOP--repo-onboarding-and-habitat-creation.md` — new repos create cross-reference boundaries
- `organvm registry validate` — built-in registry reference validation
- `organvm seed validate` — built-in seed edge target validation

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
