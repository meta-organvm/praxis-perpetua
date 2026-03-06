# ORGAN-IV (Taxis) — Evaluation-to-Growth Review

## Context

Project-wide review of the ORGAN-IV (Taxis/Orchestration) superproject and its 7 submodules using the Evaluation-to-Growth framework. ORGAN-IV is the coordination layer of the eight-organ ORGANVM system — it governs dependency flow, promotion pipelines, multi-agent orchestration, and AI skill distribution across ~101 repos.

**Scope:** All 7 submodules + superproject-level metadata. Focus on structural health, governance consistency, code maturity, documentation quality, and growth vectors.

---

## Phase 1: Evaluation

### 1.1 Critique

**Strengths:**
- **Governance is codified, not informal.** `governance-rules.json` encodes 6 articles + 4 amendments with machine-readable enforcement levels. The dependency DAG, promotion state machine, and quality gates are all explicit — not tribal knowledge.
- **Strong documentation culture.** Every repo has a substantial README (346–699 lines). The superproject CLAUDE.md is thorough and accurate. GEMINI.md provides cross-AI context.
- **seed.yaml contracts are universal.** All 7 submodules declare organ membership, tier, produces/consumes edges, and CI agents. This enables automated cross-organ reasoning.
- **agentic-titan is genuinely substantial.** 228 source files, 90 test files, 24+ top-level packages, adversarial/auth/chaos/e2e test suites, 18 optional extras. This is a real framework, not a scaffold.
- **agent--claude-smith is architecturally clean.** Singleton factory pattern, explicit reset functions for test isolation, security validation layer, bounded-memory data structures, 80% coverage thresholds enforced.
- **a-i--skills has a mature build pipeline.** 101 skills across 12 categories, SHA-256 lockfile, multi-agent bundles (Claude/Codex/Gemini), CI validation with drift detection.
- **CI coverage is broad.** orchestration-start-here alone has 15 workflows. agentic-titan has CodeQL. a-i--skills has secret detection.
- **Org profile (`profile/README.md`) is high quality.** Greek etymology, clear architectural explanation, proper eight-organ context table.

**Weaknesses:**
- **Auto-generated context blocks use `unknown` throughout.** Every submodule CLAUDE.md has `**Org:** \`unknown\`` and edges like `**Produces** → \`unknown\`: unknown`. This degrades trustworthiness of the auto-sync output.
- **AGENTS.md is auto-generated stub only.** Contains only the organ map block — no actual agent instructions, no behavioral guidance. It exists but is hollow.
- **universal-node-network is near-empty.** Described as "minimal/early stage" but has a full README (346 lines), seed.yaml, pyproject.toml, and tests — the gap between documentation ambition and implementation substance is a credibility concern.
- **orchestration-start-here has no tests directory.** The central governance hub — the most critical repo for system integrity — has zero automated tests for its scripts.
- **registry.json is a redirect stub.** Points to `registry-v2.json` in another org, but the seed.yaml still references local validation scripts (`validate-registry.py`) that don't exist in `scripts/`.
- **petasum-super-petasum contains a raw `copilot-chat-response-transcript`.** A 34KB chat log committed to the repo root. This is debris, not governance documentation.
- **`_local/` in agentic-titan was accumulating untracked.** Now gitignored (this session), but signals that the working boundary between committed and scratch content needs guardrails.
- **No superproject-level README-superproject.md content audit performed.** File exists but wasn't verified for accuracy post-changes.

### 1.2 Logic Check

| Issue | Severity | Detail |
|-------|----------|--------|
| **seed.yaml `produces` edge mismatch** | Medium | `a-i--skills` seed says it `consumes` from `agent--claude-smith`, but `agent--claude-smith` seed does NOT list `a-i--skills` as a consumer in its `produces`. The edge is one-sided. |
| **Promotion status naming inconsistency** | Low | seed.yaml uses `promotion_status: LOCAL/PUBLIC_PROCESS`. The promotion-recommender agent description uses `DESIGN_ONLY→SKELETON→PROTOTYPE→PRODUCTION`. These are different state machines for different concerns (promotion vs implementation) but the naming overlap creates confusion. |
| **Governance articles skip III, IV, V** | Low | Articles are numbered I, II, III, IV, V, VI but only I, II, III, V, VI appear in the JSON. Article IV ("Documentation Precedes Deployment") exists but article numbering suggests missing articles or non-sequential numbering. |
| **`validate-deps.py` vs `validate-dependencies.py`** | Medium | seed.yaml references `validate-dependencies.py` as a quality gate check, but the actual script is `validate-deps.py`. The workflow file is `validate-dependencies.yml` — the naming is inconsistent. |
| **Stale repo count** | Low | org profile says "9 repositories", superproject tracks 7 submodules, CLAUDE.md says 7 repos. The discrepancy suggests the org has repos not in the superproject. |
| **Boilerplate subscriptions on non-orchestrator repos** | Low | `agentic-titan`, `a-i--skills` seed.yaml files have `repo.created` and `ci.passed` subscriptions copied from `orchestration-start-here`. These subscriptions don't make sense on framework/skills repos — they're orchestrator-level concerns. |

### 1.3 Logos Review (Rational Appeal)

- **The eight-organ model is well-argued** in the org profile. The Greek etymology, functional decomposition, and dependency DAG provide a clear rational framework.
- **governance-rules.json is the strongest artifact.** Machine-readable, enforceable, with clear articles. The amendments (Bronze Tier, Coordination Budget, AI Non-Determinism) show learning and adaptation.
- **The promotion state machine is sound** in concept but undertested — no repos have reached GRADUATED or ARCHIVED, so the upper transitions are theoretical.
- **Weakness:** The gap between aspirational documentation (elaborate READMEs, seed.yaml contracts, CI workflow definitions) and actual running automation is the biggest logical vulnerability. Many workflows reference scripts/infrastructure that may not exist or run successfully.

### 1.4 Pathos Review (Emotional Resonance)

- **Strong identity and naming.** The Greek organ names, double-hyphen convention, and deliberate etymology create a sense of intentional design. This feels like a system built with care, not a random collection of repos.
- **The "nervous system" metaphor** in the org profile is effective — it positions ORGAN-IV as essential infrastructure rather than bureaucratic overhead.
- **Risk of alienation:** The complexity is intimidating. A newcomer encountering 7 repos, seed.yaml contracts, governance articles, and promotion state machines may feel the system is over-engineered for its current scale (5 of 7 repos at LOCAL status).
- **The copilot transcript in petasum is jarring.** It breaks the carefully cultivated tone of intentional design.

### 1.5 Ethos Review (Credibility)

- **Positive signals:** CodeQL enabled, security test suites, SECURITY.md files, 1Password integration, command validation, adversarial tests, secret detection in CI. These demonstrate security consciousness.
- **Credibility gap:** The `unknown` values in auto-generated blocks undermine the "automated governance" narrative. If the auto-sync can't resolve its own org names, the automation story weakens.
- **Missing tests in orchestration-start-here** is the most serious credibility issue. The repo whose entire purpose is "validate the system" has no automated validation of its own scripts.
- **universal-node-network's 346-line README for what appears to be minimal implementation** risks looking like documentation theater.

---

## Phase 2: Reinforcement

### Priority actions to resolve contradictions and strengthen coherence:

1. **Fix auto-sync `unknown` values** — The sync script that generates `<!-- ORGANVM:AUTO:START -->` blocks needs to resolve org names from seed.yaml's `org` field instead of outputting `unknown`. This is a meta-organvm issue but impacts ORGAN-IV presentation.

2. **Add tests to orchestration-start-here** — At minimum: test `validate-deps.py` with known-good and back-edge-violating inputs, test `calculate-metrics.py` output format, test `organ-audit.py` with mock registry data.

3. **Reconcile seed.yaml edge symmetry** — If `a-i--skills` consumes from `agent--claude-smith`, then `agent--claude-smith` should list `a-i--skills` as a consumer. Audit all produce/consume pairs for bidirectional consistency.

4. **Clean petasum-super-petasum** — Remove or move `copilot-chat-response-transcript` to a `docs/archive/` or delete it entirely.

5. **Align script naming** — Either rename `validate-deps.py` → `validate-dependencies.py` or update seed.yaml references. Pick one convention.

6. **Remove boilerplate subscriptions** — Strip `repo.created` and `ci.passed` subscriptions from repos that aren't the orchestrator.

7. **Write substantive AGENTS.md** — Define what AI agents should know about working across the superproject. Currently it's just the auto-generated map.

---

## Phase 3: Risk Analysis

### 3.1 Blind Spots

- **No integration testing across submodules.** Each repo tests in isolation, but nothing validates that `agentic-titan` can actually consume from `orchestration-start-here`'s governance rules, or that `agent--claude-smith` can resolve skills from `a-i--skills`.
- **Workflow execution status is unknown.** 15+ GitHub Actions workflows are defined in orchestration-start-here. Whether they actually run successfully, or are disabled/failing, isn't tracked in any visible artifact.
- **The registry redirect is a dead end locally.** `registry.json` points to another repo's `registry-v2.json`. Local scripts that try to read the registry need network access to another org — this is a hidden coupling.
- **Missing CONTRIBUTING.md and SECURITY.md in universal-node-network.** Community health files are inherited from `.github` at org level, but explicit files signal maturity.

### 3.2 Shatter Points

| Vulnerability | Severity | Impact |
|---------------|----------|--------|
| **orchestration-start-here scripts are untested** | High | A bug in `validate-deps.py` could silently allow back-edge violations, breaking the core architectural invariant |
| **Auto-sync produces incorrect organ mappings** | Medium | Already seen: `.github/CLAUDE.md` was mapped to ORGAN-I. Any new submodule could get wrong context, leading AI agents to make incorrect architectural decisions |
| **Superproject pointer drift** | Medium | If submodule commits aren't synced to the superproject, `git submodule update --init` checks out stale code. No CI enforces pointer freshness. |
| **Single maintainer** | Medium | `@4444j99` is the sole maintainer across all 7 repos. No bus-factor mitigation. |

---

## Phase 4: Growth

### 4.1 Bloom (Emergent Insights)

- **The seed.yaml schema is the most portable innovation.** It could become a standalone specification for multi-repo governance — "seed contracts for federated organizations." Worth extracting into its own reference implementation.
- **agentic-titan's topology diversity (9 patterns, 22 archetypes)** is a differentiator. Most orchestration frameworks offer 1-2 patterns. Publishing a topology comparison guide would strengthen the project's authority.
- **The skills pipeline (`a-i--skills`)** with its multi-agent bundles (Claude/Codex/Gemini) is ahead of the market. Most skill/prompt libraries target a single LLM. The cross-agent portability story is compelling but under-marketed.
- **The governance-as-code pattern** (JSON articles + automated enforcement + promotion state machine) could be a standalone open-source contribution.

### 4.2 Evolve (Recommended Actions)

Concrete implementation plan, ordered by impact:

#### A. orchestration-start-here: Add test suite
- **Files:** Create `orchestration-start-here/tests/` with `test_validate_deps.py`, `test_calculate_metrics.py`, `test_organ_audit.py`
- **Approach:** Use pytest with fixture-based mock registries. Test both valid and invalid dependency graphs.
- **Why first:** Credibility of the entire governance layer depends on this.

#### B. Fix auto-generated `unknown` org values across all CLAUDE.md files
- **Files:** All 6 submodule CLAUDE.md files (`.github` already fixed)
- **Approach:** The auto-sync script lives in meta-organvm; the fix is upstream. In the meantime, manually correct the `**Org:**` line and edge descriptions in each file using seed.yaml as source of truth.
- **Scope:** 5 files to edit (agent--claude-smith, a-i--skills, agentic-titan, orchestration-start-here, petasum-super-petasum, universal-node-network)

#### C. Clean up petasum-super-petasum
- **File:** Delete `petasum-super-petasum/copilot-chat-response-transcript`
- **Why:** 34KB of raw chat log in the repo root undermines governance credibility.

#### D. Reconcile seed.yaml edge symmetry
- **Files:** `agent--claude-smith/seed.yaml` (add `a-i--skills` as consumer), audit all other pairs
- **Approach:** For each `consumes` entry in any seed.yaml, verify a corresponding `produces` entry exists in the source repo's seed.yaml.

#### E. Remove boilerplate subscriptions from non-orchestrator repos
- **Files:** `agentic-titan/seed.yaml`, `a-i--skills/seed.yaml`
- **Action:** Remove `repo.created` and `ci.passed` subscriptions (these are orchestrator concerns, not framework concerns)

#### F. Substantive AGENTS.md at superproject level
- **File:** `AGENTS.md`
- **Action:** Replace auto-generated stub with actual guidance: submodule navigation protocol, commit rules, testing commands, cross-repo dependency awareness.

#### G. Add community health files to universal-node-network
- **Files:** Create `CONTRIBUTING.md`, `SECURITY.md` (can be minimal, pointing to org-level defaults)

---

## Verification

After implementation:
1. `git submodule foreach 'git status --short'` — all submodules clean
2. `grep -r 'unknown' */CLAUDE.md` — no `unknown` values in auto-generated blocks
3. `cd orchestration-start-here && pytest tests/ -v` — new test suite passes
4. `ls petasum-super-petasum/copilot-chat-response-transcript` — file deleted
5. Manual review: each seed.yaml `consumes` edge has a matching `produces` edge in the source repo
