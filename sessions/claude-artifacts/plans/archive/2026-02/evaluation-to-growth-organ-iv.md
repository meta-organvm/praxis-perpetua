# ORGAN-IV (Taxis) — Evaluation-to-Growth Report

**Date:** 2026-02-24
**Phase:** Post-PHASE-D Hardening
**Mode:** Autonomous analysis + implementation

---

## Executive Summary

Applied the Evaluation-to-Growth framework across all 7 ORGAN-IV submodules. Identified 5 contradictions, 3 reasoning gaps, and 2 HIGH-severity shatter points. Implemented fixes in 3 waves across 24 files in 7 repositories.

---

## Phase 1: Evaluation

### 1.1 Critique

#### Strengths

- **Governance model is well-codified.** `governance-rules.json` (6 articles + 4 amendments) is the clearest artifact in the system. Unidirectional dependency rule (I->II->III) is both documented and enforced by `validate-deps.py`.
- **agentic-titan is genuinely substantial.** 22,740+ lines of test code across 20+ test directories (adversarial, chaos, e2e, performance, MCP, Ray). 18 optional extras spanning RLHF, Firecracker microVMs, Langfuse observability, PostgreSQL persistence.
- **agent--claude-smith has sound architecture.** Singleton factory with `reset*()` for test isolation, Zod schema validation, bounded memory (CircularBuffer, ExpiringMap), atomic session writes with KeyedMutex.
- **a-i--skills has a mature build pipeline.** 101 skills, SHA-256 lockfile, multi-agent bundle generation (Claude/Codex/Gemini), CI drift detection.
- **seed.yaml contracts are consistent.** All 7 repos follow schema v1.0 with organ, produces, consumes, subscriptions.
- **CI coverage exists for all 7 submodules.** orchestration-start-here has 14 workflows.

#### Weaknesses (Pre-Fix)

- **Auto-generated context files were broken.** Every submodule had `**Org:** \`unknown\`` and edges like `**Produces** -> \`unknown\`: unknown`.
- **GEMINI.md files were hollow.** Only the broken auto-block, no instructions.
- **`.github` CLAUDE.md/GEMINI.md showed ORGAN-I data.** Wrong organ, wrong siblings, wrong edges.
- **CI was intentionally permissive.** `continue-on-error: true` on lint and typecheck steps.
- **seed.yaml workflow references were wrong.** `ci-python.yml` / `ci-typescript.yml` but actual file is `ci.yml`.
- **universal-node-network falsely claimed ACTIVE status.** Only ~195 lines of in-memory dataclasses.
- **governance-rules.json Article I referenced retired `registry.json`.** Canonical data moved to `registry-v2.json`.
- **seed.yaml referenced nonexistent scripts.** `validate-registry.py` and `validate-dependencies.py` don't exist.

### 1.2 Contradictions Found

| Location | Contradiction | Resolution |
|---|---|---|
| `universal-node-network/seed.yaml` | `implementation_status: ACTIVE` but only 195 lines exist | **Fixed:** Changed to `SKELETON` |
| `universal-node-network/seed.yaml` | `produces: governance-policy` — it produces nothing | **Fixed:** Removed produces block |
| All seed.yaml | `workflow: ci-python.yml` / `ci-typescript.yml` but actual file is `ci.yml` | **Fixed:** All 5 corrected |
| `governance-rules.json` Article I | References `registry.json` but it's retired | **Fixed:** Updated to `registry-v2.json` |
| `orchestration-start-here/seed.yaml` | References `validate-registry.py` and `validate-dependencies.py` (don't exist) | **Fixed:** Both → `validate-deps.py` |

### 1.3 Reasoning Gaps (Documented, Not Fixed)

1. **petasum-super-petasum vs orchestration-start-here:** Both govern — one via commandments, the other via registry/validation. No documented relationship.
2. **a-i--skills "consumes" agent--claude-smith** per seed.yaml, but no code-level dependency exists.
3. **"ORGAN-IV orchestrates all"** per governance-rules, but orchestration-start-here's registry is retired and points elsewhere.

### 1.4 Blind Spots

| Blind Spot | Detail |
|---|---|
| **No cross-submodule integration testing** | Each repo tests in isolation |
| **Governance is write-only** | Rules documented but only `validate-deps.py` actually runs |
| **No monitoring/alerting** | Scheduled agents (weekly audits, monthly promotions) — no evidence they run |
| **Bus factor = 1** | Metadata sync is manual/AI-assisted |

### 1.5 Shatter Points

| Vulnerability | Severity | Status |
|---|---|---|
| CI never fails (lint/typecheck swallowed) | HIGH | **Partially fixed** — ruff hardened (agentic-titan), tsc hardened (agent--claude-smith) |
| Registry is orphaned | HIGH | **Partially fixed** — Article I updated. Scripts still reference old patterns. |
| `unknown` metadata ships everywhere | MEDIUM | **Fixed** — all 14 files resolved |
| seed.yaml workflow mismatch | MEDIUM | **Fixed** — all 5 corrected |
| universal-node-network false maturity | LOW | **Fixed** — SKELETON status |

---

## Phase 2: Implementation

### Wave 1: Metadata Integrity (R1, R2, R4, R6, R7) — COMPLETE

| Fix | Files Changed | Detail |
|---|---|---|
| **R1:** Resolve `unknown` placeholders | 14 files (7 CLAUDE.md + 7 GEMINI.md) | Org → `organvm-iv-taxis`, edges resolved from seed.yaml produces/consumes. `.github` corrected from ORGAN-I to ORGAN-IV. |
| **R2:** Fix workflow references | 5 seed.yaml files | `ci-python.yml` / `ci-typescript.yml` → `ci.yml` |
| **R4:** Fix universal-node-network | 1 seed.yaml | `ACTIVE` → `SKELETON`, removed false `produces: governance-policy` |
| **R6:** Update governance-rules.json | 1 file | Article I now references `registry-v2.json` in `meta-organvm/organvm-corpvs-testamentvm` |
| **R7:** Fix script references | 1 seed.yaml | `validate-registry.py` and `validate-dependencies.py` → `validate-deps.py` |

### Wave 2: CI Hardening (R3) — PARTIALLY COMPLETE

| Repo | Lint | Typecheck | Action |
|---|---|---|---|
| agentic-titan | ruff passes clean | mypy: 1253 errors (strict mode) | **Hardened ruff**, kept mypy permissive. Added `exclude = docs/source-materials/` to mypy.ini. |
| agent--claude-smith | No ESLint configured | tsc passes clean | **Hardened tsc**, kept lint permissive. |

**Note:** mypy strict mode produces 1253 errors across 85 files in agentic-titan. This is a separate cleanup effort — the code works and tests pass, but strict type annotations are incomplete. Tracked as future work.

### Wave 3: Cleanup (R5, R8) — COMPLETE

| Fix | Detail |
|---|---|
| **R5:** Enrich GEMINI.md | Added title + pointer to CLAUDE.md for full instructions. Kept resolved auto-blocks. |
| **R8:** copilot transcript | Already removed (not present in petasum-super-petasum). |

---

## Phase 3: Verification

```
✅ grep -r '`unknown`' */CLAUDE.md    → 0 matches
✅ grep -r '`unknown`' */GEMINI.md    → 0 matches
✅ grep 'ci-python.yml\|ci-typescript.yml' */seed.yaml → 0 matches
✅ petasum copilot transcript         → not present
✅ universal-node-network status      → SKELETON
✅ governance-rules.json Article I    → references registry-v2.json
✅ orchestration-start-here seed.yaml → references validate-deps.py
```

---

## Phase 4: Remaining Work (Wave 4 — Future)

| Item | Priority | Effort |
|---|---|---|
| Fix agentic-titan mypy strict errors (1253) | Medium | Large |
| Document petasum vs orchestration-start-here division | Medium | Small |
| Add cross-submodule integration test | Low | Medium |
| Create `validate-registry.py` or fully remove references | Low | Small |
| Add ESLint to agent--claude-smith | Low | Small |

---

## Files Changed Summary

| Submodule | Files | Changes |
|---|---|---|
| `.github` | CLAUDE.md, GEMINI.md | Fixed organ (I→IV), edges, siblings |
| `a-i--skills` | CLAUDE.md, GEMINI.md, seed.yaml | Resolved unknowns, fixed workflow ref |
| `agent--claude-smith` | CLAUDE.md, GEMINI.md, seed.yaml, ci.yml | Resolved unknowns, fixed workflow ref, hardened tsc |
| `agentic-titan` | CLAUDE.md, GEMINI.md, seed.yaml, ci.yml, mypy.ini | Resolved unknowns, fixed workflow ref, hardened ruff, fixed mypy exclude |
| `orchestration-start-here` | CLAUDE.md, GEMINI.md, seed.yaml, governance-rules.json | Resolved unknowns, fixed Article I, fixed script refs |
| `petasum-super-petasum` | CLAUDE.md, GEMINI.md, seed.yaml | Resolved unknowns, fixed workflow ref |
| `universal-node-network` | CLAUDE.md, GEMINI.md, seed.yaml | Resolved unknowns, fixed status to SKELETON, removed false produces, fixed workflow ref |

**Total: 24 files across 7 submodules**
