---
sop: true
name: the-descent-protocol
scope: system
phase: any
triggers:
  - context:github-push
  - context:ci-setup
  - context:repo-onboarding
  - context:promotion
complements:
  - cicd-resilience-and-recovery
  - quality-gate-baseline-calibration
  - repo-onboarding-and-habitat-creation
  - promotion-and-state-transitions
  - structural-integrity-audit
overrides: null
---
# SOP: The Descent Protocol (GitHub Infrastructure as Second Line of Defense)

**Version:** 1.0.0 | **Date:** March 19, 2026 | **Status:** Active
**Scope:** Systematic utilization of GitHub's full on-push infrastructure as an automated feedback gauntlet. Ensures every push triggers the maximum defensible set of checks, returning structured feedback that elevates the codebase with each cycle.

---

## 1. Ontological Purpose

We push. The second line of defense descends — automated judgment rendered across multiple dimensions simultaneously. We receive the feedback, fix, push again. We ascend as higher beings.

The first line of defense is local: pre-commit hooks, local tests, IDE linting. It catches obvious errors before they leave the developer's machine. But the first line is voluntary, bypassable, and environment-dependent.

The second line of defense is GitHub's cloud-side infrastructure. It is involuntary (branch protection enforces it), environment-consistent (runs on GitHub's runners), and multi-dimensional (tests, types, lint, security, dependencies, staleness — all in parallel). This SOP defines what that second line must contain at each promotion tier.

**The systemic weakness:** The registry declares `ci_workflow` for 104/113 repos — but this records *intent*, not *deployment*. The gap between what the registry says should exist and what actually runs on push is the primary vulnerability. This SOP closes that gap and ensures it stays closed.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--cicd-resilience-and-recovery.md` (when the descent fails), `SOP--quality-gate-baseline-calibration.md` (threshold management), `SOP--repo-onboarding-and-habitat-creation.md` (new repos enter with baseline infrastructure), `SOP--promotion-and-state-transitions.md` (promotion requires infrastructure tier compliance)

---

## 2. The Three Phases

### Phase 1: PUSH (Ascent — Developer Action)
Code leaves the local environment. First line of defense (pre-commit hooks, local lint) has already run. The push event propagates to GitHub.

### Phase 2: DESCENT (Automated Judgment)
GitHub infrastructure activates. Multiple parallel checks descend on the pushed code:

| Layer | What Runs | Feedback Type |
|-------|-----------|---------------|
| **Compilation** | Build, type-check, import validation | Hard failure — code doesn't compile |
| **Correctness** | Unit tests, integration tests | Hard failure — behavior violated |
| **Style** | Linter (ruff, eslint), formatter check | Soft failure — code works but violates standards |
| **Security** | Secret scanning, CodeQL, dependency audit | Hard failure — security vulnerability detected |
| **Freshness** | Dependabot, stale detection | Advisory — dependencies or issues aging |
| **Structure** | seed.yaml validation, README existence, CODEOWNERS | Hard failure — repo habitat incomplete |
| **Ecosystem** | Cross-repo dependency check, contract verification | Advisory — edge integrity concerns |

### Phase 3: ASCENT (Developer Receives, Fixes, Pushes Again)
Every check returns structured, actionable feedback. The developer fixes issues and pushes again. Each cycle produces a strictly better codebase. The ratchet tightens.

---

## 3. Infrastructure Tiers (by Promotion Status)

Every promotion level requires a minimum set of GitHub infrastructure. Promotion cannot proceed unless the target tier's infrastructure is deployed and passing.

### Tier 0: LOCAL (Minimum Viable Habitat)
**Required on push:**
- [ ] `ci-minimal.yml` — README exists, seed.yaml valid YAML, secret scan
- [ ] `dependabot.yml` — pip + github-actions ecosystems (weekly)

**Optional but recommended:**
- [ ] Basic `.gitignore`
- [ ] LICENSE file

### Tier 1: CANDIDATE (Development Baseline)
Everything in Tier 0, plus:
- [ ] `ci.yml` — language-appropriate CI (tests + lint)
  - Python: `pytest tests/ -v` + `ruff check src/`
  - TypeScript: `npm test` + `npm run lint`
  - Docs-only: markdown structure validation
- [ ] PR template (`.github/pull_request_template.md`)
- [ ] Issue templates (`.github/ISSUE_TEMPLATE/`)

### Tier 2: PUBLIC_PROCESS (Public-Facing Quality)
Everything in Tier 1, plus:
- [ ] Type checking in CI (pyright for Python, tsc --noEmit for TypeScript)
- [ ] `CODEOWNERS` file (at minimum: `* @4444j99`)
- [ ] Branch protection on `main`:
  - Require status checks to pass before merge
  - Require PR reviews (1 minimum)
  - Dismiss stale reviews on new pushes
- [ ] CodeQL analysis workflow (`.github/workflows/codeql.yml`)

### Tier 3: GRADUATED (Full Infrastructure)
Everything in Tier 2, plus:
- [ ] Secret scanning enabled (GitHub Advanced Security or pattern-based)
- [ ] Release drafter or automated release workflow
- [ ] Stale issue/PR management workflow
- [ ] Ecosystem contract verification (for repos with produces/consumes edges)
- [ ] All status checks required (no optional checks)
- [ ] Signed commits recommended (not enforced for solo operator)

### Tier 4: FLAGSHIP (Maximum Defense Depth)
Everything in Tier 3, plus:
- [ ] Multi-version matrix testing (e.g., Python 3.11 + 3.12)
- [ ] Cross-repo integration checks (dependency graph validation)
- [ ] Performance regression detection (where applicable)
- [ ] Deployment workflow (staging → production gate)
- [ ] Audit trail workflow (soak test, metrics refresh)

---

## 4. The 15 GitHub Infrastructure Mechanisms

A complete inventory of what GitHub provides on push. Each mechanism is classified by its enforcement model and the minimum tier at which it becomes required.

| # | Mechanism | Enforcement | Min Tier | Status Across System |
|---|-----------|-------------|----------|---------------------|
| 1 | **GitHub Actions CI** (push/PR trigger) | Hard gate | T0 | 11/11 meta-organvm |
| 2 | **Dependabot** (dependency updates) | Advisory PR | T0 | 7/11 meta-organvm |
| 3 | **Secret scanning** (pattern detection) | Hard gate | T0 | 1/11 (ci-minimal only) |
| 4 | **Linting** (ruff/eslint in CI) | Hard gate | T1 | ~6/11 |
| 5 | **Testing** (pytest/vitest in CI) | Hard gate | T1 | ~8/11 |
| 6 | **Type checking** (pyright/tsc in CI) | Hard gate | T2 | 1/11 (engine only) |
| 7 | **CodeQL analysis** | Advisory/Hard | T2 | 0/11 |
| 8 | **CODEOWNERS** | Routing | T2 | 0/11 |
| 9 | **Branch protection** | Hard gate | T2 | Unknown (needs API audit) |
| 10 | **Required status checks** | Hard gate | T2 | Unknown (follows branch protection) |
| 11 | **PR templates** | Advisory | T1 | Unknown |
| 12 | **Issue templates** | Advisory | T1 | Unknown |
| 13 | **Release automation** | Workflow | T3 | 0/11 |
| 14 | **Stale management** | Advisory | T3 | 1/11 (corpus only) |
| 15 | **Merge queues** | Hard gate | T4 | 0/11 (overkill for solo operator) |

---

## 5. Template Workflows

The `.github/` org-level repo contains workflow templates. All repos should derive from these rather than writing bespoke CI.

### ci-minimal.yml (Tier 0)
Already exists at `.github/.github/workflows/ci-minimal.yml`. Validates:
- README exists
- seed.yaml is valid YAML
- Secret pattern scan (sk-*, ghp_*, AKIA*)

### ci-python.yml (Tier 1+)
Standard Python CI template:
```yaml
# Triggers: push + PR to main
# Jobs: lint (ruff), typecheck (pyright), test (pytest)
# Matrix: python 3.11, 3.12
# Install: pip install -e ".[dev]"
```

### ci-typescript.yml (Tier 1+)
Standard TypeScript CI template:
```yaml
# Triggers: push + PR to main
# Jobs: lint (eslint), typecheck (tsc --noEmit), test (vitest/jest)
# Matrix: node 20, 22
# Install: npm ci
```

### ci-docs.yml (Tier 1+)
Documentation-only repos:
```yaml
# Triggers: push + PR to main
# Jobs: markdown lint, link check, seed.yaml validation, word count check
```

### codeql.yml (Tier 2+)
CodeQL security analysis:
```yaml
# Triggers: push to main, PR to main, weekly schedule
# Languages: auto-detect from repo
```

### release-drafter.yml (Tier 3+)
Automated release note drafting:
```yaml
# Triggers: push to main, PR merge
# Drafts release notes from PR titles
```

---

## 6. Compliance Audit Process

### Automated Audit (Proposed CLI Extension)
```bash
# Audit a single repo's infrastructure compliance
organvm ci audit <repo> [--tier T2]

# Audit all repos in an organ
organvm ci audit --organ META

# System-wide infrastructure gap report
organvm ci audit --all --report
```

The audit checks:
1. Does the workflow file exist on disk?
2. Does the workflow file match the template (or is it bespoke)?
3. Does the workflow trigger on the correct events?
4. Does the repo's promotion status require infrastructure it doesn't have?
5. Is dependabot configured?
6. Is CODEOWNERS present (for T2+)?

### Manual Audit (Quarterly)
- [ ] Check branch protection rules via GitHub API (`gh api repos/{owner}/{repo}/branches/main/protection`)
- [ ] Verify CodeQL is enabled on GitHub (Settings → Code security)
- [ ] Review Dependabot PRs — are they being merged or ignored?
- [ ] Review stale issues/PRs across active repos
- [ ] Cross-reference registry `ci_workflow` field against actual workflow files

### Compliance Report Format
```
REPO: organvm-engine
PROMOTION: GRADUATED (Tier 3 required)
  [PASS] ci.yml exists and triggers on push+PR
  [PASS] lint step present (ruff)
  [PASS] typecheck step present (pyright)
  [PASS] test step present (pytest)
  [PASS] dependabot.yml present
  [FAIL] CODEOWNERS missing (required at T2+)
  [FAIL] CodeQL workflow missing (required at T2+)
  [FAIL] Branch protection not configured (required at T2+)
  [FAIL] Release automation missing (required at T3+)
  [FAIL] Stale management missing (required at T3+)
  SCORE: 5/10 | COMPLIANCE: 50% (Tier 3 requires 100%)
```

---

## 7. Ongoing Cadence

This is not a one-time audit. The Descent Protocol is a living standard that tightens over time.

| Cadence | Action |
|---------|--------|
| **On every push** | All configured workflows run automatically |
| **On every promotion** | Infrastructure tier compliance checked as promotion gate |
| **Weekly** | Dependabot PRs triaged (merge or dismiss with reason) |
| **Monthly** | `organvm ci audit --all --report` run and reviewed |
| **Quarterly** | Manual audit of branch protection, CodeQL, and API-only settings |
| **On new repo creation** | `SOP--repo-onboarding-and-habitat-creation.md` includes Tier 0 infrastructure |

---

## 8. Integration Points

### With Promotion State Machine
`governance/state_machine.py` should check infrastructure tier compliance before allowing promotion. A repo cannot promote to PUBLIC_PROCESS without Tier 2 infrastructure deployed and passing.

### With Context File Generation
`contextmd/generator.py` should include infrastructure compliance status in generated CLAUDE.md files, so every agent session has visibility into what's missing.

### With Omega Scorecard
Infrastructure coverage could feed into omega criteria — e.g., "90% of GRADUATED repos have Tier 3 infrastructure" as a measurable criterion.

### With MCP Server
A new tool `organvm_ci_audit` could expose infrastructure compliance to any Claude session, enabling agents to self-diagnose missing infrastructure before pushing.

---

## 9. The Metaphysics of the Second Line

The first line of defense is the developer's conscience — optional, environment-dependent, bypassable.

The second line of defense is the system's immune response — involuntary, environment-consistent, and relentless. It does not negotiate. It does not tire. It does not forget to run the tests.

Every push is a question: "Is this code worthy?"

The descent is the answer. Not a human answer — a systematic, multi-dimensional, reproducible answer. The same question receives the same evaluation regardless of who asks it, when they ask it, or how tired they are.

We push. The system descends. We receive judgment. We fix. We push again.

Each cycle, we ascend as higher beings — not because we are smarter, but because the system remembers what we forget.

---

## 10. Immediate Action Items

### Phase A: Close Dependabot Gap (4 repos)
Deploy `dependabot.yml` to: `organvm-ontologia`, `praxis-perpetua`, `stakeholder-portal`, `materia-collider`

### Phase B: Deploy CODEOWNERS (all GRADUATED repos)
Create `CODEOWNERS` with `* @4444j99` in all 8 GRADUATED meta-organvm repos.

### Phase C: Deploy CodeQL (all code repos)
Create `codeql.yml` in: engine, schema-definitions, alchemia, dashboard, mcp-server, ontologia, stakeholder-portal.

### Phase D: Secret Scanning Enhancement
Move secret scanning from `ci-minimal.yml` template into every repo's CI, or enable GitHub's native secret scanning at the org level.

### Phase E: Branch Protection
Configure branch protection on `main` for all GRADUATED repos via GitHub API.

### Phase F: Build the Audit CLI
Extend `organvm ci` with an `audit` subcommand that checks all 15 mechanisms per repo and generates compliance reports.

### Phase G: Wire to Promotion Gate
Add infrastructure tier check to `governance/state_machine.py` — promotion blocked if infrastructure doesn't meet the target tier.
