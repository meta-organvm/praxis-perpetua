# E2G Review #3: Deferred Items

## Context

The previous E2G review (round 2) deferred four items as out-of-scope. Now tackling all three distinct tasks:

1. **SP1**: Split `cli.py` (1072-line monolith) into a `cli/` package
2. **SP3/W1**: Deduplicate standalone scripts vs engine modules (~1163 lines of duplication)
3. **B3**: Add type checking (mypy/pyright) to the engine

Current state after E2G round 2: 288 engine tests, 24 MCP tests, ruff configured, all lint passing on modified files (pre-existing issues in cli.py and contextmd/sync.py remain).

---

## Task 1: Split cli.py (SP1)

### Problem
`cli.py` is 1072 lines with 36 handler functions, `build_parser()`, `main()`, and the dispatch table all in one file. Every new feature adds 30-50 lines. The file mixes argument parsing, business logic invocation, and output formatting.

### Current Structure (36 handlers in 12 groups)
- **registry** (4): `cmd_registry_show`, `_list`, `_validate`, `_update` (lines 49-131)
- **governance** (4): `cmd_governance_audit`, `_checkdeps`, `_promote`, `_impact` (lines 136-207)
- **seed** (3): `cmd_seed_discover`, `_validate`, `_graph` (lines 213-257)
- **metrics** (5 + 1 helper): `_resolve_workspace`, `cmd_metrics_calculate`, `_propagate`, `_count_words`, `_refresh` (lines 263-419)
- **dispatch** (1): `cmd_dispatch_validate` (lines 425-438)
- **git** (8): `cmd_git_init_superproject`, `_add_submodule`, `_sync_organ`, `_sync_all`, `_status`, `_reproduce`, `_diff_pinned`, `_install_hooks` (lines 444-620)
- **context** (1): `cmd_context_sync` (lines 626-650)
- **omega** (3): `cmd_omega_status`, `_check`, `_update` (lines 656-693)
- **deadlines** (1): `cmd_deadlines` (lines 699-713)
- **ci** (1): `cmd_ci_triage` (lines 719-726)
- **pitch** (2): `cmd_pitch_generate`, `_sync` (lines 732-785)
- **status** (1): `cmd_status` (lines 791-839)

### Approach
Convert `cli.py` into a `cli/` package. Each command group gets its own module. The `__init__.py` holds `build_parser()`, the dispatch table, and `main()`.

### Files

| File | Contents | ~Lines |
|------|----------|--------|
| `cli/__init__.py` | `build_parser()`, dispatch table, `main()`, `_resolve_workspace()` helper | ~280 |
| `cli/registry.py` | `cmd_registry_show/list/validate/update` | ~90 |
| `cli/governance.py` | `cmd_governance_audit/checkdeps/promote/impact` | ~75 |
| `cli/seed.py` | `cmd_seed_discover/validate/graph` | ~50 |
| `cli/metrics.py` | `cmd_metrics_calculate/propagate/count_words/refresh` | ~160 |
| `cli/dispatch.py` | `cmd_dispatch_validate` | ~20 |
| `cli/git_cmds.py` | All 8 `cmd_git_*` handlers | ~180 |
| `cli/context.py` | `cmd_context_sync` | ~30 |
| `cli/omega.py` | `cmd_omega_status/check/update` | ~45 |
| `cli/deadlines.py` | `cmd_deadlines` | ~20 |
| `cli/ci.py` | `cmd_ci_triage` | ~15 |
| `cli/pitch.py` | `cmd_pitch_generate/sync` | ~60 |
| `cli/status.py` | `cmd_status` | ~55 |

### Key details
- **Entry point stays the same**: `organvm = "organvm_engine.cli:main"` in pyproject.toml
- `cli/__init__.py` imports all handlers from submodules and wires them into the dispatch table
- Each submodule imports only what it needs (lazy imports within handlers stay as-is)
- `_resolve_workspace()` moves to `__init__.py` (shared by metrics, git, pitch, context, status)
- The top-level module-scope imports (`load_registry`, `find_repo`, etc.) stay in `__init__.py` since they're used by build_parser's defaults
- Delete old `cli.py` after creating `cli/` package
- Fix pre-existing ruff issues in the handlers as we move them (the F541 f-strings, W293 whitespace, F401 unused imports, E501 long lines, I001 import ordering)

### Tests
- **No test changes needed** — `test_cli.py` imports from `organvm_engine.cli` which will resolve to `cli/__init__.py`
- Run full `pytest organvm-engine/tests/ -v` to verify
- Run `ruff check organvm-engine/src/organvm_engine/cli/` to verify lint

---

## Task 2: Deduplicate Standalone Scripts (SP3/W1)

### Problem
`calculate-metrics.py` (314 lines) and `propagate-metrics.py` (849 lines) in `organvm-corpvs-testamentvm/scripts/` duplicate functions from the engine's `calculator.py` and `propagator.py`. Active drift exists:
- Standalone `build_patterns()` returns 4-tuples `(name, regex, replacement, desc)`, engine returns 3-tuples
- Standalone `format_word_count()` doesn't round (engine does since E2G-2)
- Standalone has hardcoded fallback values (386K, 404K) that are now stale
- Standalone `compute_vitals()` reads `code_files` from `manual` only; engine now puts them in `computed`

### CI Dependency
`metrics-refresh.yml` runs the standalone scripts directly with only `pip install pyyaml`. This is the blocker — CI has no access to the engine package.

### Approach: Thin Wrapper Pattern
Rewrite standalone scripts as thin wrappers that:
1. Try to import from `organvm_engine` (if installed)
2. Fall back to inline implementations only for CI environments where the engine isn't available

Actually, **simpler**: just install the engine in CI from git. The metrics-refresh workflow already has checkout + python setup. Add one line:

```yaml
- name: Install organvm-engine
  run: pip install git+https://github.com/meta-organvm/organvm-engine.git
```

Then rewrite the scripts to import from the engine.

### calculate-metrics.py → thin wrapper (~80 lines)

**Keep** (unique to standalone):
- `count_sprint_specs()` — counts sprint .md files in corpus `docs/specs/sprints/`
- `fetch_essay_count()` — calls GitHub API for essay count
- `load_existing_essay_count()` — fallback when API is skipped
- `main()` with `--skip-essays`, `--skip-words` flags

**Replace with engine imports**:
- `compute_registry_metrics()` → `from organvm_engine.metrics.calculator import compute_metrics`
- `_strip_frontmatter()` → removed (engine has it)
- `_count_file_words()` → removed (engine has it)
- `count_words_local()` → `from organvm_engine.metrics.calculator import count_words`
- `format_word_count()` → `from organvm_engine.metrics.calculator import format_word_count`
- `load_manual_section()` → simplified (engine's `write_metrics` handles this)
- `ORGAN_DIRS` dict → removed (engine uses `organ_config.py`)

### propagate-metrics.py → thin wrapper (~120 lines)

**Keep** (unique to standalone):
- `Replacement` dataclass (used for verbose output)
- `WHITELIST_GLOBS` constant
- `resolve_whitelist()`, `resolve_globs()` — used by standalone main
- `main()` with `--verbose`, `--file` flags
- Verbose per-line replacement reporting (not in engine)

**Replace with engine imports**:
- `build_patterns()` → `from organvm_engine.metrics.propagator import build_patterns`
- `compute_vitals()` → already imported by engine
- `compute_landing()` → already imported by engine
- `transform_for_portfolio()` → already imported by engine
- `copy_json_targets()` → already imported by engine
- `load_manifest()` → `from organvm_engine.metrics.propagator import load_manifest`
- `expand_path()` → `from organvm_engine.metrics.propagator import expand_path` (or inline, it's 1 line)

### Engine propagator alignment
The engine's `build_patterns()` returns 3-tuples but the standalone returns 4-tuples (with `desc`). The standalone's verbose mode uses `desc`. Options:
- **Option A**: Add `desc` as 4th element to engine's tuples → breaks existing tests
- **Option B**: Engine returns named tuples or dataclass → overkill
- **Option C**: Standalone wraps engine patterns to add descriptions → cleanest

**Choose C**: The standalone wrapper maps engine's 3-tuples to 4-tuples by appending the metric name as description. Verbose mode is a standalone-only feature anyway.

### CI workflow update
**File**: `organvm-corpvs-testamentvm/.github/workflows/metrics-refresh.yml`

```yaml
- name: Install dependencies
  run: |
    pip install pyyaml
    pip install git+https://github.com/meta-organvm/organvm-engine.git
```

### Files to modify

| File | Action |
|------|--------|
| `organvm-corpvs-testamentvm/scripts/calculate-metrics.py` | Rewrite as thin wrapper (~80 lines, down from 314) |
| `organvm-corpvs-testamentvm/scripts/propagate-metrics.py` | Rewrite as thin wrapper (~120 lines, down from 849) |
| `organvm-corpvs-testamentvm/.github/workflows/metrics-refresh.yml` | Add engine install step |

### Verification
```bash
# Standalone scripts still work locally
source .venv/bin/activate
python3 organvm-corpvs-testamentvm/scripts/calculate-metrics.py --skip-essays
python3 organvm-corpvs-testamentvm/scripts/propagate-metrics.py --dry-run
python3 organvm-corpvs-testamentvm/scripts/propagate-metrics.py --cross-repo --dry-run

# Engine tests still pass (no engine changes needed)
pytest organvm-engine/tests/ -v
```

---

## Task 3: Add Type Checking (B3)

### Current State
- 187 functions across 36 source files
- ~194 return type annotations (>100% coverage — some helper methods included)
- Parameter type hints used on most public function signatures
- No `py.typed` marker
- No mypy/pyright config
- Heavy use of `dict` returns (not TypedDict) — biggest gap
- Dependencies: pyyaml (has stubs), jsonschema (has stubs), stdlib (fully typed)

### Approach: pyright in basic mode
Use **pyright** over mypy because:
- Faster execution
- Better inference
- `basic` mode is less noisy than mypy's strict mode
- Already works well with Python 3.11+ union syntax (`X | Y`)

### Implementation

**1. Add pyright config to `organvm-engine/pyproject.toml`:**
```toml
[tool.pyright]
pythonVersion = "3.11"
typeCheckingMode = "basic"
include = ["src"]
```

**2. Add `py.typed` marker:**
Create `organvm-engine/src/organvm_engine/py.typed` (empty file).

**3. Add `pyright` to dev dependencies:**
```toml
dev = ["pytest>=8.0", "jsonschema>=4.20", "ruff>=0.4", "pyright>=1.1"]
```

**4. Run pyright, assess and fix errors:**
- Expected: mostly `dict` return types needing `-> dict[str, Any]` instead of `-> dict`
- Won't try to retrofit `TypedDict` — that's a separate effort
- Fix actual type errors (wrong types passed, missing None checks)
- Add `# type: ignore` sparingly for genuinely unavoidable issues

**5. Add to engine CI:**
Update `organvm-engine/.github/workflows/ci.yml`:
```yaml
- run: pyright src/
```

### Files to modify

| File | Action |
|------|--------|
| `organvm-engine/pyproject.toml` | Add `[tool.pyright]` config, add pyright to dev deps |
| `organvm-engine/src/organvm_engine/py.typed` | Create empty marker file |
| `organvm-engine/.github/workflows/ci.yml` | Add pyright step |
| Various source files | Fix type errors found by pyright |

### Verification
```bash
source .venv/bin/activate
pip install pyright
pyright organvm-engine/src/
# Target: 0 errors in basic mode
pytest organvm-engine/tests/ -v  # ensure no regressions
```

---

## Execution Order

1. **Task 1 (Split cli.py)** — first, because it's self-contained and touches only the engine
2. **Task 3 (Type checking)** — second, because pyright will catch issues in the newly-split CLI modules
3. **Task 2 (Deduplicate scripts)** — last, because it depends on the engine being stable and touches a different submodule (corpus)

## Overall Verification

```bash
source .venv/bin/activate

# All engine tests pass
pytest organvm-engine/tests/ -v

# All MCP tests pass
pytest organvm-mcp-server/tests/ -v

# Ruff passes on engine
ruff check organvm-engine/src/

# Pyright passes
pyright organvm-engine/src/

# CLI still works
organvm --help
organvm status
organvm registry list --organ I
organvm governance impact organvm-engine
organvm metrics calculate

# Standalone scripts still work
python3 organvm-corpvs-testamentvm/scripts/calculate-metrics.py --skip-essays
python3 organvm-corpvs-testamentvm/scripts/propagate-metrics.py --dry-run
```
