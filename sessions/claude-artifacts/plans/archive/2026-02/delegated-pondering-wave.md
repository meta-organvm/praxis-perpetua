# meta-organvm: Evaluation-to-Growth Report

## Context

Full codebase review of the `meta-organvm` superproject (7 submodules, ~4,500 lines of Python across 5 packages) using the Evaluation-to-Growth framework. The goal: identify what's working, what's fragile, what's missing, and where the system should grow — producing an actionable implementation plan for strengthening the entire organ.

---

## Phase 1: Evaluation

### 1.1 Critique

**Strengths**

- **Consistent architecture across subprojects.** All Python packages follow `src/` layout, use `pyproject.toml`, have `seed.yaml`, and share a common dependency on `registry-v2.json`. The pattern is learnable and reproducible.
- **The `organvm` CLI is comprehensive and well-organized.** 7 command groups (~25 subcommands), clean argparse dispatch pattern, consistent `(ok, msg)` return tuples for error reporting.
- **Governance enforcement is real code, not just documentation.** Back-edge detection, cycle detection, promotion state machine, and dependency graph validation are all implemented and tested.
- **MCP server cleanly wraps the engine.** 13 tools across 5 groups with proper JSON schemas. The `get_context` tool is genuinely useful for cross-repo awareness.
- **Context sync system (`contextmd/`) is the most operationally valuable feature.** Auto-generating CLAUDE.md/GEMINI.md/AGENTS.md across 100+ repos from a single registry is high-leverage.
- **Metrics propagator (`propagator.py`) is sophisticated.** Regex-based metric injection across markdown files with skip markers for historical content, cross-repo manifest support, and portfolio transforms.
- **Test fixtures are minimal and focused.** `registry-minimal.json` and `governance-rules-test.json` let tests run without touching real data.

**Weaknesses**

- **`omega_status()` in MCP server is hardcoded stub** (`organvm-mcp-server/src/organvm_mcp/tools/health.py:69-108`). Returns static data with a TODO comment. This is the most prominent incomplete feature.
- **`impact.py` has string literal `\n` in f-string** (`organvm-engine/src/organvm_engine/governance/impact.py:26-27,33-34,48-49`). The `summary()` method uses `"` at line boundaries causing literal backslash-n instead of newlines.
- **No `__init__.py` exports** in most module packages (registry/, seed/, metrics/, dispatch/ — they exist but are empty or minimal). This forces verbose imports everywhere.
- **Three separate `ORGANVM_CORPUS_DIR` resolution patterns:**
  - `organvm-engine/registry/loader.py` — inline `os.environ.get()`
  - `organvm-engine/governance/rules.py` — same pattern, duplicated
  - `organvm-engine/metrics/timeseries.py` — same pattern, duplicated
  - `organvm-mcp-server/data/paths.py` — centralized (correct approach)
  - `system-dashboard/data/loader.py` — yet another inline resolution
- **Dashboard data loader (`system-dashboard/data/loader.py`) duplicates engine logic.** It reimplements `load_registry`, `load_governance_rules`, `load_soak_snapshots` instead of importing from `organvm_engine`.
- **`alchemia review` command raises `sys.exit(1)` with "Not yet implemented"** (`alchemia-ingestvm/src/alchemia/cli.py:233`). This is a dead endpoint.
- **No tests for `organvm-mcp-server` tools** beyond a stub `test_tools.py`. The 13 tools are untested.
- **No tests for `git/` or `contextmd/` modules** in organvm-engine despite being the most operationally critical.
- **`generate_workspace_section()` has hardcoded `omega_met=8`** (`contextmd/generator.py:234`). Should read from actual omega evidence.

### 1.2 Logic Check

| Issue | Location | Severity |
|-------|----------|----------|
| **Back-edge logic is inverted in `dependency_graph.py`** | Line 106: `if from_level < to_level` flags I→II as a back-edge, but this is the CORRECT flow direction. The condition should be `from_level > to_level` (higher-numbered organ depending on lower). However, this matches the comment "I→II→III" suggesting levels go from 1→3 and lower depends on higher... Actually, re-reading: `ORGAN_LEVELS` maps I=1, II=2, III=3. A back-edge would be III depending on I (from_level=3 > to_level=1). The code checks `from_level < to_level` which flags I depending on II — this IS correct since I should never depend on II. **The logic is correct, naming is confusing.** | Low (naming) |
| **`validator.py` back-edge check differs from `dependency_graph.py`** | `validator.py:120` checks `organ_num < dep_num` for back-edges. `dependency_graph.py:106` checks `from_level < to_level`. These are equivalent but use different variable names and mapping constants (`organ_num` vs `ORGAN_LEVELS`). | Medium (duplication) |
| **`check_dependency()` in MCP graph tools has inverted level comparison** | `organvm-mcp-server/tools/graph.py:153` — `s_lv >= t_lv` returns "allowed" meaning "source organ has higher-or-equal level than target". But ORGAN-I=1, II=2, III=3. If ORGAN-III (level 3) depends on ORGAN-I (level 1), that's `s_lv=3 >= t_lv=1`, which is allowed. If ORGAN-I depends on ORGAN-III, that's `s_lv=1 >= t_lv=3`, which is NOT allowed. **Logic is correct.** | None |
| **`propagator.py` patterns could match unintended content** | Regex like `r"(\b)\d+( repositor(?:ies\|y) across\b)"` will match ANY number followed by "repositories across" — including unrelated content. The `SKIP_MARKERS` list mitigates this but is brittle. | Medium |
| **Dashboard duplicates registry loading without engine import** | `system-dashboard/data/loader.py` vs `organvm_engine.registry.loader`. If the registry format changes, two loaders need updating. | Medium |
| **MCP `query_registry()` passes `promotion_status` as `status` kwarg** to `list_repos()` | `organvm-mcp-server/tools/registry.py:38` — `list_repos(registry, ..., status=promotion_status)`. The engine's `list_repos` filters on `implementation_status` when `status=` is passed. This is a **semantic mismatch**: the MCP tool promises to filter by `promotion_status` but actually filters by `implementation_status`. | **High** |

### 1.3 Logos Review (Rational/Factual)

- **Arguments for the architecture are well-supported.** The unidirectional flow (I→II→III) is enforced in code, not just declared. Promotion state machine has clear transitions. Registry is validated before context sync.
- **The system's complexity is justified by its scope.** Managing ~100 repos across 8 organs with automated context propagation, metrics injection, and governance enforcement requires this level of tooling.
- **Weak point: no runtime metrics or telemetry.** The system computes metrics from static registry data but has no way to measure actual usage, build times, or operational health dynamically.
- **The MCP server makes a strong case for cross-repo AI awareness** — but the `get_context()` tool's CWD resolution logic (`context.py:38-42`) is fragile. It assumes exactly 2 levels of nesting (`Workspace/<organ>/<repo>`) and breaks for deeper or shallower paths.

### 1.4 Pathos Review (Emotional/Engagement)

- **The naming system creates strong identity.** "Alchemical Forge," "Aesthetic Nervous System," "taste.yaml cascades," "Omega criteria" — these are memorable and motivating.
- **CLI output is functional but stark.** Plain text with manual `─` dividers. No color, no progress indicators, no rich formatting.
- **Error messages are helpful.** `check_transition()` tells you both what failed and what your valid options are. `validate_registry()` reports specific field names.
- **Missing: success celebration.** After syncing 327 files or passing all governance checks, the output is matter-of-fact. A brief "System is healthy" or similar would reinforce positive behavior.

### 1.5 Ethos Review (Credibility/Authority)

- **Code quality is consistent and professional.** Type hints on most public functions, docstrings with Args/Returns, dataclass result types.
- **Test coverage is uneven.** Engine registry/governance/seed/metrics/dispatch all have tests. But git/, contextmd/, MCP tools, dashboard routes, and alchemia pipeline stages have minimal or no tests.
- **No CI workflows exist in the superproject.** CLAUDE.md previously claimed CI runs on push/PR but there are no `.github/workflows/` files. This undermines trust.
- **The `impact.py` module has a visible bug** (string literal newlines) that suggests it hasn't been exercised much.
- **Version pinning is minimal.** `pyyaml>=6.0`, `fastapi>=0.104`, `mcp>=1.0` — no upper bounds. This is fine for early development but fragile for reproducibility.

---

## Phase 2: Reinforcement

### 2.1 Synthesis — Issues to Resolve

**P0 (Breaking bugs):**
1. Fix `impact.py` string literal `\n` → actual newlines in `ImpactReport.summary()`
2. Fix MCP `query_registry()` semantic mismatch: `status=promotion_status` should filter by `promotion_status`, not `implementation_status`

**P1 (Architectural debt):**
3. Centralize `ORGANVM_CORPUS_DIR` resolution — extract to a shared `organvm_engine.paths` module (like the MCP server's `data/paths.py` pattern). Remove 4 duplicate inline resolutions.
4. Make `system-dashboard/data/loader.py` import from `organvm_engine` instead of reimplementing registry/governance/metrics loading.
5. Replace hardcoded `omega_met=8` in `contextmd/generator.py` with actual computation.

**P2 (Test gaps):**
6. Add tests for `contextmd/sync.py` — the most operationally critical module (touches 300+ files).
7. Add tests for `git/status.py` and `git/superproject.py` — at least for data transformation logic (not actual git operations).
8. Add tests for MCP tools — at least `query_registry`, `get_context`, `system_health`.
9. Add tests for dashboard routes — at least `test_health`, `test_registry`.

**P3 (Completeness):**
10. Implement `omega_status()` in MCP server — parse omega-evidence-map.md or at minimum read from a structured data file.
11. Remove or mark `alchemia review` as explicitly unimplemented (currently crashes with `sys.exit(1)`).
12. Add `list_repos` to `organvm_engine/registry/__init__.py` exports for cleaner imports.

---

## Phase 3: Risk Analysis

### 3.1 Blind Spots

| Blind Spot | Risk | Mitigation |
|------------|------|------------|
| **Context sync has no rollback.** If `sync_all()` crashes mid-run, some files are updated and others aren't. | Partial state across 300+ files | Add a transaction-like pattern: write to `.tmp` files, then rename atomically, or at minimum add `--verify` mode that checks consistency after sync |
| **MCP server caches are never invalidated during a session.** If registry changes while MCP server is running (e.g., someone runs `organvm registry update`), stale data is served. | Stale tool responses | The `reload()` function exists but is never called. Consider TTL-based cache invalidation or file mtime checking |
| **No validation of seed.yaml against schema.** `organvm-validate` can validate registry, governance, dispatch, soak, and metrics against JSON Schema — but `seed-v1.schema.json` is defined yet `seed validate` only checks 4 required fields. | Malformed seeds pass validation | Wire `schema-definitions/schemas/seed-v1.schema.json` into `organvm seed validate` |
| **`propagator.py` SKIP_MARKERS list is a maintenance burden.** Any new document with historical content needs manual marker additions. | Metrics overwrite historical data | Consider switching to explicit `<!-- METRICS:SKIP -->` markers in documents instead |
| **Personal namespace `4444J99` / `PERSONAL` is partially supported.** MCP context tool handles it specially (`context.py:51-55`) but seed discovery doesn't scan it (not in `ORGAN_ORGS`). | Inconsistent treatment of personal repos | Either fully support or explicitly exclude |

### 3.2 Shatter Points

| Vulnerability | Severity | Impact |
|---------------|----------|--------|
| **`registry-v2.json` is a single point of failure.** Every subproject reads it. If it's corrupted, context sync will propagate errors to 300+ files (though the pre-flight validation in `sync.py:43-45` mitigates this). | High | System-wide breakage |
| **No backup before context sync.** Running `organvm context sync` overwrites files in-place with no undo. | High | Unrecoverable if bugs in generator |
| **`subprocess` calls in `git/superproject.py` and `git/status.py` have no timeout.** A hung git process blocks the CLI indefinitely. | Medium | CLI hangs |
| **Dashboard binds to `0.0.0.0:8000`** (`system-dashboard/src/dashboard/app.py:45`). This exposes the dashboard to all network interfaces, not just localhost. | Medium | Unintended network exposure |
| **`alchemia alchemize --force` deploys files to repos without confirmation or backup.** Combined with batch processing, this could overwrite legitimate content. | Medium | Data loss in target repos |

---

## Phase 4: Growth

### 4.1 Bloom (Emergent Insights)

1. **The context sync + MCP server pattern is the system's killer feature.** It makes the 100-repo system navigable for AI. Investing here has the highest ROI.
2. **The engine could become a standalone governance toolkit** beyond organvm. The registry/governance/seed pattern is generic enough for any multi-repo system.
3. **The aesthetic cascade (taste.yaml → organ-aesthetic.yaml → repo-aesthetic.yaml) is architecturally elegant** but currently only used for prompt injection. It could drive actual CI-enforced style checks (color palettes, typography in generated assets).
4. **`organvm git reproduce-workspace` is an underappreciated onboarding tool.** New contributors (or new machines) get a complete, reproducible workspace.

### 4.2 Evolve — Implementation Plan

The following changes are ordered by impact and dependency. Each item includes the files to modify and verification steps.

---

## Implementation Plan

### Step 1: Fix P0 bugs

**1a. Fix `impact.py` string literal newlines**
- File: `organvm-engine/src/organvm_engine/governance/impact.py`
- Lines 26-27, 33-34, 48-49: Replace the `"...\n..."` pattern in `summary()` with proper multi-line string or `\n` inside a single string literal
- Verify: `python -c "from organvm_engine.governance.impact import ImpactReport; r = ImpactReport('test', ['a','b'], {'test':['a','b']}); print(r.summary())"`

**1b. Fix MCP `query_registry()` semantic mismatch**
- File: `organvm-mcp-server/src/organvm_mcp/tools/registry.py`
- Line 38: `list_repos()` `status=` parameter filters by `implementation_status`, but the MCP tool advertises filtering by `promotion_status`. Two options:
  - Option A: Add a `promotion_status` filter to `organvm_engine.registry.query.list_repos()`
  - Option B: Post-filter in the MCP tool after `list_repos()` returns
- Recommended: Option A — add `promotion_status` kwarg to `list_repos()` in `organvm-engine/src/organvm_engine/registry/query.py`
- Verify: `pytest organvm-engine/tests/test_registry.py -v` + manual MCP tool test

### Step 2: Centralize path resolution (P1)

**2a. Create `organvm_engine/paths.py`**
- New file: `organvm-engine/src/organvm_engine/paths.py`
- Consolidate the `ORGANVM_CORPUS_DIR` / `ORGANVM_WORKSPACE_DIR` resolution from:
  - `registry/loader.py:8-12`
  - `governance/rules.py:7-11`
  - `metrics/timeseries.py:7-11`
  - `seed/discover.py:18-21`
- Pattern: follow `organvm-mcp-server/data/paths.py` (already the best version)
- Update all 4 files to import from `paths.py`
- Verify: `pytest organvm-engine/tests/ -v`

**2b. Make dashboard import from engine**
- File: `system-dashboard/src/dashboard/data/loader.py`
- Replace `_load_json(CORPUS_DIR / "registry-v2.json")` with `from organvm_engine.registry.loader import load_registry`
- Replace `_load_json(CORPUS_DIR / "governance-rules.json")` with `from organvm_engine.governance.rules import load_governance_rules`
- Keep dashboard-specific functions (`load_essays`, `organ_summary`, `load_soak_snapshots`) as-is
- Add `organvm-engine` to `system-dashboard/pyproject.toml` dependencies
- Verify: `pytest system-dashboard/tests/ -v`

### Step 3: Fix hardcoded omega + incomplete features (P3)

**3a. Replace hardcoded omega_met in contextmd/generator.py**
- File: `organvm-engine/src/organvm_engine/contextmd/generator.py:234`
- Read omega criteria count from `system-metrics.json` manual section (where it's already tracked) instead of hardcoding `8`
- Verify: `organvm context sync --dry-run --organ META`

**3b. Fix `alchemia review` command**
- File: `alchemia-ingestvm/src/alchemia/cli.py:232-234`
- Replace `sys.exit(1)` with `print("REVIEW — Not yet implemented (Phase B)")` and `return` (don't crash the process)
- Verify: `alchemia review` exits cleanly

### Step 4: Add critical tests (P2)

**4a. Test contextmd sync logic**
- New file: `organvm-engine/tests/test_contextmd.py`
- Test `_inject_section()` with: new file, existing file with markers, existing file without markers
- Test `generate_repo_section()` returns valid markdown with correct organ/tier
- Test that `sync_all()` refuses to run on invalid registry (the pre-flight check)
- Use the existing `registry-minimal.json` fixture

**4b. Test MCP tools**
- File: `organvm-mcp-server/tests/test_tools.py`
- Test `registry.query_registry()`, `registry.list_organs()`, `context.get_context()`
- Mock the data loaders to avoid filesystem dependency
- Verify: `pytest organvm-mcp-server/tests/ -v`

### Step 5: Security/safety hardening

**5a. Bind dashboard to localhost**
- File: `system-dashboard/src/dashboard/app.py:45`
- Change `host="0.0.0.0"` to `host="127.0.0.1"`
- Verify: `organvm-dashboard` only listens on localhost

**5b. Add subprocess timeout to git operations**
- File: `organvm-engine/src/organvm_engine/git/superproject.py` (wherever `_run_git` is defined)
- Add `timeout=30` to subprocess calls
- Verify: `organvm git status`

---

## Verification

After all changes:

```bash
# Run all test suites
pytest organvm-engine/tests/ -v
pytest organvm-mcp-server/tests/ -v
pytest system-dashboard/tests/ -v
pytest alchemia-ingestvm/tests/ -v
pytest schema-definitions/tests/ -v

# Lint
ruff check alchemia-ingestvm/src/
ruff check organvm-mcp-server/src/

# Functional verification
organvm registry validate
organvm governance audit
organvm governance check-deps
organvm seed validate
organvm metrics calculate
organvm git status
organvm context sync --dry-run

# Dashboard smoke test
organvm-dashboard &
curl -s http://127.0.0.1:8000/health/ | head -5
kill %1
```

---

## Summary

| Phase | Key Finding |
|-------|-------------|
| **Critique** | Strong architecture, comprehensive CLI, but 2 bugs (impact.py newlines, MCP filter mismatch), duplicated path resolution, uneven test coverage |
| **Logic Check** | Core governance logic is correct despite confusing variable names. MCP promotion_status filter is silently wrong. |
| **Logos** | System complexity is justified. MCP cross-repo awareness is the strongest value proposition. |
| **Pathos** | Naming is memorable and motivating. CLI output is functional but austere. |
| **Ethos** | Professional code quality. Test gaps in the most critical modules (contextmd, git, MCP tools) undermine confidence. |
| **Blind Spots** | No sync rollback, stale MCP caches, seed schema validation missing, SKIP_MARKERS maintenance burden |
| **Shatter Points** | registry-v2.json SPOF, no backup before context sync, dashboard binds 0.0.0.0, no subprocess timeout |
| **Growth** | Context sync + MCP = killer feature. Engine could be a standalone multi-repo governance toolkit. |

**Recommended execution order:** Steps 1→2→5→3→4 (fix bugs first, then architectural cleanup, then safety, then features, then tests last since they verify everything).
