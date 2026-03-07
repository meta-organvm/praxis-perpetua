# SOP: Promotion & State Transitions

## 1. Ontological Purpose

This SOP governs the execution of promotion state transitions for repositories in the ORGANVM system. The promotion state machine (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED) is the primary lifecycle governance mechanism. Each transition has preconditions, execution steps, edge validation requirements, and post-transition verification.

This is not a checklist of aspirational goals — it is a governed procedure. No transition may be executed without satisfying all preconditions. No precondition may be waived without a documented exception in the decision log.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 3: Governance & Lifecycle)
**Cross-reference:** `SOP--repo-onboarding-and-habitat-creation.md` (new repos enter at LOCAL), `SOP--structural-integrity-audit.md` (audit gates at promotion), `SOP--stranger-test-protocol.md` (required for GRADUATED), Standard `12-habitat-governance-lifecycle.md` (artifact requirements per stage)
**Canonical source:** `governance-rules.json` state_machine and promotion_criteria

---

## 2. Phase I: Precondition Verification

### Process

1. **Identify the current state and target state.** Valid transitions (from `governance-rules.json`):

   | From | To (valid targets) |
   |------|--------------------|
   | LOCAL | CANDIDATE, ARCHIVED |
   | CANDIDATE | PUBLIC_PROCESS, LOCAL (demotion), ARCHIVED |
   | PUBLIC_PROCESS | GRADUATED, CANDIDATE (demotion), ARCHIVED |
   | GRADUATED | ARCHIVED |
   | ARCHIVED | (terminal — no transitions) |

2. **Verify preconditions for the target state:**

   **LOCAL -> CANDIDATE:**
   - [ ] `seed.yaml` exists with correct organ, tier
   - [ ] `README.md` explains what this is and why it exists
   - [ ] `.gitignore` is language-appropriate
   - [ ] `LICENSE` selected
   - [ ] `CLAUDE.md` provides AI agent context
   - [ ] GitHub repo has description and topics set
   - [ ] Dependency audit clean (no critical vulnerabilities)

   **CANDIDATE -> PUBLIC_PROCESS:**
   - [ ] All CANDIDATE requirements satisfied
   - [ ] `ci_workflow` is not null (CI pipeline running)
   - [ ] `implementation_status` is ACTIVE
   - [ ] README passes portfolio gate (2,500+ words for relevant repos)
   - [ ] `SECURITY.md` with disclosure policy
   - [ ] `CONTRIBUTING.md` with setup and PR process
   - [ ] `CODE_OF_CONDUCT.md`
   - [ ] At least 1 ADR documenting major architectural decision
   - [ ] First E2G review completed
   - [ ] **If financial/PII:** 2+ ADRs, validation gates, 2-reviewer policy

   **PUBLIC_PROCESS -> GRADUATED:**
   - [ ] All PUBLIC_PROCESS requirements satisfied
   - [ ] `platinum_status` is true
   - [ ] Stranger test or peer review completed
   - [ ] No critical audit findings
   - [ ] ADR set covers all major decisions (3+)
   - [ ] SLA documented
   - [ ] Incident response notes exist
   - [ ] Changelog established

3. **Check dependency graph:** No promotion may create a back-edge violation. Run:
   ```bash
   organvm governance check-deps
   ```

### Starter Research Questions
- What is the repo's current state and when was it last validated?
- Which preconditions are already met vs. need work?
- Does promoting this repo create any new dependency edges?
- Are there any outstanding audit findings blocking promotion?
- Does the repo handle money or PII (triggering additional requirements)?

---

## 3. Phase II: State Transition Execution

### Process

1. **Update `seed.yaml`:**
   ```yaml
   promotion_status: <TARGET_STATE>
   last_validated: <ISO-DATE>
   ```

2. **Update `registry-v2.json`:**
   ```bash
   organvm registry update <repo> promotion_status <TARGET_STATE>
   ```
   Or edit directly, updating the `promotion_status` field.

3. **If cross-organ promotion** (Theory->Art, Art->Commerce, Any->PublicProcess):
   - Create the destination repo per `SOP--repo-onboarding-and-habitat-creation.md`
   - Add dependency edge from new repo to source repo
   - Follow naming conventions from `governance-rules.json`:
     - Theory->Art: `art-from--<source>`
     - Art->Commerce: `<source>`
     - Any->PublicProcess: `essay-from--<source>`

4. **Run registry validation:**
   ```bash
   organvm registry validate
   ```

### Starter Research Questions
- Is this a same-repo promotion or a cross-organ promotion?
- If cross-organ, does the destination repo already exist?
- Are all registry counts still accurate after the update?
- Does the seed.yaml match the registry entry?

---

## 4. Phase III: Edge Validation

### Process

1. **Verify dependency graph integrity:**
   ```bash
   organvm governance check-deps
   organvm seed graph
   ```

2. **Check for back-edge violations.** The I-II-III chain is unidirectional:
   - ORGAN-I -> ORGAN-II (allowed)
   - ORGAN-II -> ORGAN-III (allowed)
   - ORGAN-I -> ORGAN-III (allowed)
   - ORGAN-II -> ORGAN-I (FORBIDDEN)
   - ORGAN-III -> ORGAN-II (FORBIDDEN)
   - ORGAN-III -> ORGAN-I (FORBIDDEN)

3. **Verify ORGAN-IV constraint satisfaction.** ORGAN-IV may reference any organ. ORGAN-V observes (read-many). ORGAN-VII is pure consumer.

4. **Check produces/consumes edges** in the promoted repo's seed.yaml resolve to existing repos.

### Starter Research Questions
- Does this promotion introduce any new cross-organ edges?
- Are all forward edges declared in both source and consumer seed.yaml files?
- Does the dependency graph remain a DAG (no cycles)?
- Are ORGAN-VI and ORGAN-VII edges correctly declared?

---

## 5. Phase IV: Post-Promotion Verification

### Process

1. **Run full validation suite:**
   ```bash
   organvm registry validate
   organvm governance audit
   organvm seed validate
   ```

2. **Regenerate context files:**
   ```bash
   organvm context sync --dry-run
   organvm context sync
   ```

3. **Regenerate pitch deck** (if promotion to PUBLIC_PROCESS or above):
   ```bash
   organvm pitch generate --repo <name>
   ```

4. **Refresh dashboard:**
   ```bash
   organvm metrics refresh
   ```

5. **Update the omega scorecard** if the promotion affects any of the 17 criteria.

### Starter Research Questions
- Do all validation commands pass cleanly?
- Did context sync produce any unexpected changes?
- Is the pitch deck current with the new state?
- Does the dashboard reflect the updated promotion status?

---

## 6. Output Artifacts

- Updated `seed.yaml` with new `promotion_status` and `last_validated`
- Updated `registry-v2.json` entry
- Validated dependency graph (no violations)
- Regenerated context files and pitch deck
- Decision log entry (if exceptions were granted)

---

## Appendix A: Valid Transitions Table

```
LOCAL ---------> CANDIDATE ---------> PUBLIC_PROCESS ---------> GRADUATED ---------> ARCHIVED
  |                 |                       |                                           ^
  |                 v                       v                                           |
  +------------> ARCHIVED             CANDIDATE (demotion)                              |
                                            |                                           |
                                            v                                           |
                                        ARCHIVED  ------------------------------------>-+
```

## Appendix B: Precondition Matrix

| Requirement | L->C | C->PP | PP->G |
|-------------|------|-------|-------|
| seed.yaml | REQ | REQ | REQ |
| README | REQ | PORTFOLIO | PORTFOLIO |
| LICENSE | REQ | REQ | REQ |
| CLAUDE.md | REQ | REQ | REQ |
| CI pipeline | — | REQ | REQ |
| SECURITY.md | — | REQ | REQ |
| CONTRIBUTING.md | — | REQ | REQ |
| CODE_OF_CONDUCT.md | — | REQ | REQ |
| ADR (1+) | — | REQ | REQ (3+) |
| E2G review | — | REQ | REQ |
| platinum_status | — | — | REQ |
| Stranger test | — | — | REQ |
| SLA docs | — | — | REQ |
| Changelog | — | — | REQ |

## Appendix C: Cross-Organ Naming Conventions

| Path | Naming Pattern | Destination Org |
|------|---------------|-----------------|
| Theory -> Art | `art-from--{source}` | `organvm-ii-poiesis` |
| Art -> Commerce | `{source}` | `organvm-iii-ergon` |
| Any -> Public Process | `essay-from--{source}` | `organvm-v-logos` |

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
