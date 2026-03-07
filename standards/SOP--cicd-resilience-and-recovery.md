# SOP: CI/CD Pipeline Resilience & Recovery

## 1. Ontological Purpose

This SOP defines the systematic protocol for diagnosing, unclogging, and structurally hardening CI/CD pipelines across the ORGANVM system. CI failures are not random events — they are symptoms of structural weaknesses. This procedure treats the structure, not the symptom.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--product-deployment-and-revenue-activation.md` (CI must pass before deployment), `SOP--structural-integrity-audit.md` (CI failures may indicate deeper structural issues)

---

**Created:** 2026-03-06
**Author:** @4444j99 (AI-conductor model)
**Status:** ACTIVE
**Canonical location:** `praxis-perpetua/standards/SOP--cicd-resilience-and-recovery.md`
**Companions:** [`emergency-procedures.md`](../../organvm-corpvs-testamentvm/docs/operations/emergency-procedures.md), [`key-workflows.md`](../../organvm-corpvs-testamentvm/docs/operations/key-workflows.md)
**Precedent:** Portfolio pipeline blockage (Feb 17 - Mar 6, 2026) — 17 days, 10 commits, 4 push-watch-fix cycles, 5 failure categories

---

## 2. Foundational Principles

### Thesis — What mature quality systems do well
1. **Comprehensive gate coverage** catches real regressions, not theater
2. **Monotonic ratchets** (date-based, phase-based) create sustainable improvement trajectories
3. **Separating generation from validation** catches generator bugs before they poison downstream checks
4. **Build-first gating** prevents phantom passes — stale artifacts produce false greens
5. **"Plan all fixes, push once"** is orders of magnitude faster than serial fix-push-watch cycles

### Antithesis — Structural failure modes
1. **Drift magnets** — Manually maintained lists that mirror filesystem structure will drift. `P(drift) -> 1` as `t -> inf`
2. **Sequential discovery tax** — N hidden failures cost `N * cycle_time` when found serially
3. **CI-only validation gap** — Checks that only run in CI create irreducible feedback delay
4. **Invisible coupling** — Changing file A requires changing file B, but nothing tells you
5. **Environment-blind thresholds** — A threshold that works locally but flakes in CI is a coin flip
6. **No local pre-flight** — If nothing runs before `git push`, every mistake costs a full CI cycle

### Synthesis — Universal structural principles
1. **Derive, don't duplicate.** Generate lists from filesystem/data at runtime
2. **Preflight locally.** Single command runs all locally-reproducible checks
3. **Document coupling.** Human-readable coupling map: "if you change X, also change Y"
4. **Split thresholds by environment.** CI floors (tolerant) vs local targets (aspirational)
5. **Diagnose fully before fixing.** Collect entire failure surface before writing code

---

## 3. Phase I: Triage (5 min)

### Process

1. **Pull failed run details:**
   ```bash
   gh run list --limit 1 --status failure --repo OWNER/REPO
   gh run view RUN_ID --repo OWNER/REPO
   gh run view RUN_ID --repo OWNER/REPO --log-failed | tail -100
   ```
2. **Output:** Complete list of all failing jobs + error messages. Do NOT fix anything yet.

### Starter Research Questions
- How many distinct failures are there?
- Are failures in the same job or different jobs?
- When was the last green run?
- What changed between last green and this failure?

---

## 4. Phase II: Classify (10 min)

### Process

Categorize each failure:

| Category | Pattern | Fix archetype |
|----------|---------|---------------|
| Drift | Hardcoded list != filesystem | Make dynamic |
| Threshold | Score too strict for CI | Relax to env-appropriate value |
| Formatter | Generated file fails lint | Exclude from formatter |
| Stale artifact | Old manifest/summary | Regenerate |
| Missing dep | Tool not installed in CI | Add install step |
| Code bug | Invalid HTML, broken link | Fix the code |

### Starter Research Questions
- Is this a real regression or an environmental flake?
- Could this failure have been caught locally?
- Is this a new failure category not in the table above?
- What structural change would prevent this class of failure?

---

## 5. Phase III: Reproduce Locally (15 min)

### Process

1. **Run project-specific preflight:**
   ```bash
   npm run preflight        # or quality:local:no-lh, or pytest, etc.
   # Generic fallback:
   <lint> && <typecheck> && <build> && <test>
   ```
2. **Fix all locally-reproducible failures in a single batch.** Do not push partial fixes.

### Starter Research Questions
- Does a preflight command exist for this project?
- Which failures reproduce locally and which are CI-only?
- Can I create a preflight command if one doesn't exist?

---

## 6. Phase IV: Fix CI-Only Failures

### Process

1. **Extract exact values from CI logs** (not just "failed")
2. **Distinguish environmental flake from real regression**
3. **Fix regressions; adjust environmental thresholds** with documented rationale

### Starter Research Questions
- What exact value did the CI environment produce vs. what was expected?
- Is this threshold appropriate for the CI runner's resources?
- Can this check be made reproducible locally?

---

## 7. Phase V: Single Push, Full Watch

### Process

1. **Stage all fixes:**
   ```bash
   git add <specific files>
   git commit -m "fix: unclog CI — [all fixes summarized]"
   git push origin main
   gh run watch $(gh run list --limit 1 --json databaseId -q '.[0].databaseId') --exit-status
   ```
2. **If it fails:** Return to Phase I with fresh triage. Never push partial fixes.

---

## 8. Phase VI: Post-Mortem Audit

### Process

1. **Review every change as if someone else made it** — find flaws
2. **For each fix, ask:** "What structural change prevents this class of failure?"
3. **Implement structural fixes** as a separate commit

---

## 9. Phase VII: Feed Back

### Process

If this incident revealed a new failure category, coupling point, or principle, update this document. Version as `SOP--cicd-resilience-and-recovery-v2.md` (never overwrite).

---

## 10. Output Artifacts

- Green CI run
- Coupling map (`.quality/GOVERNANCE-COUPLING.md`) for the project
- Updated preflight command
- Post-mortem notes (if structural changes made)

---

## Appendix A: Project Instantiation Template

Each project that adopts this SOP should create `.quality/GOVERNANCE-COUPLING.md`:

```markdown
## Coupling Map
| If you change... | Also update... | Enforced by |
|-----------------|----------------|-------------|

## Preflight Command
`npm run preflight` / `make preflight` / etc.

## CI-Only Checks
- (list checks requiring CI environment)

## Environment-Split Thresholds
| Metric | CI floor (error) | Local target (warn) |
|--------|------------------|---------------------|
```

## Appendix B: Precedent Timeline

Portfolio pipeline (Feb-Mar 2026): 10 commits, 4 push-watch-fix cycles, 5 failure categories, 17 days blocked.
**Lesson:** A single `npm run preflight` would have caught 8 of 10 failures locally, reducing 17 days to ~2 hours.

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
