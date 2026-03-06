# Living Organism — Variable Binding System

**Date:** 2026-03-06
**Status:** PLAN

## Context

Metrics across the ORGANVM enterprise drift out of sync. Org profile READMEs say "81 repositories" when the registry has 103. Cover letter templates say "320K words" when it's 404K+. The existing propagator uses fragile regex guessing. The user wants: **never manually fix a number again.**

The solution: a **variable binding system** where files declare references to named variables using HTML comment markers. A single `organvm refresh` command resolves all bindings. A CI check blocks PRs that contain bare metric numbers without markers.

**Scope:** Live documents only. Submitted applications/legacy materials are historical snapshots — left as-is.

## Architecture

### Marker Syntax

```markdown
<!-- v:total_repos -->103<!-- /v -->
```

- `<!-- v:VAR_NAME -->` opens a binding
- `<!-- /v -->` closes it
- Inner content is the rendered value (replaced on refresh)
- Invisible in rendered GitHub markdown — just shows `103`
- Dot notation for scoped vars: `<!-- v:organ_repos.ORGAN-III -->27<!-- /v -->`

### Variable Manifest: `system-vars.json`

Generated alongside `system-metrics.json`. Flat key-value map of every bindable variable:

```json
{
  "total_repos": "103",
  "active_repos": "82",
  "archived_repos": "9",
  "total_organs": "8",
  "operational_organs": "8",
  "total_words_short": "404K+",
  "total_words_formatted": "404,000",
  "total_words_numeric": "404000",
  "ci_workflows": "102",
  "dependency_edges": "156",
  "published_essays": "48",
  "sprints_completed": "33",
  "organ_repos.ORGAN-I": "20",
  "organ_repos.ORGAN-II": "31",
  "organ_repos.ORGAN-III": "27",
  "organ_repos.ORGAN-IV": "7",
  "organ_repos.ORGAN-V": "6",
  "organ_repos.ORGAN-VI": "6",
  "organ_repos.ORGAN-VII": "6",
  "organ_repos.META-ORGANVM": "7",
  "organ_name.ORGAN-I": "Theoria",
  "organ_name.ORGAN-II": "Poiesis",
  "organ_name.ORGAN-III": "Ergon"
}
```

All values are strings (since they're injected into markdown). Computed from registry + `system-metrics.json` computed section.

### File Categories

**Bound (live, get variable markers):**
- 8 org profile READMEs (`*/.github/profile/README.md`)
- Workspace-level `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`
- Organ-level `CLAUDE.md`, `GEMINI.md` (manually-written metric references)
- Corpus: `README.md`, `CLAUDE.md`, `docs/operations/*.md`, `docs/essays/09-*.md`
- Application pipeline: `blocks/**/*.md`, `strategy/*.md`, `docs/*.md` (composable templates)

**Frozen (no markers, leave as-is):**
- `pipeline/submissions/*` (already sent)
- `scripts/legacy-submission/*`
- `materials/resumes/batch-*/*`
- `variants/cover-letters/*-alchemized.md` (generated outputs, already sent)
- `docs/archive/*`
- `docs/planning/*` (historical planning docs with period-specific numbers)

## Implementation Phases

### Phase 1: Variable Resolver Engine

**New file:** `organvm-engine/src/organvm_engine/metrics/vars.py`

Core functions:

```python
VAR_PATTERN = re.compile(r'<!-- v:([a-zA-Z0-9_.]+) -->.*?<!-- /v -->', re.DOTALL)

def build_vars(metrics: dict, registry: dict) -> dict[str, str]:
    """Build flat variable manifest from system-metrics.json computed + registry."""

def write_vars(variables: dict, output: Path) -> None:
    """Write system-vars.json."""

def resolve_file(path: Path, variables: dict, dry_run: bool = False) -> list[Replacement]:
    """Scan a single file for <!-- v:KEY --> markers and replace values."""

def resolve_targets(
    variables: dict,
    targets_path: Path,
    dry_run: bool = False,
) -> ResolutionResult:
    """Walk all files listed in vars-targets.yaml and resolve bindings."""

def scan_unbound(path: Path, variables: dict) -> list[UnboundMetric]:
    """Find bare metric numbers that SHOULD have variable markers but don't."""
    # Used by the CI linter
```

**New file:** `organvm-engine/tests/test_vars.py`

Tests:
- `build_vars` produces correct flat manifest from metrics + registry
- `resolve_file` replaces marker content with variable value
- `resolve_file` preserves unknown keys (warns, doesn't delete)
- `resolve_file` handles multiline markers
- `resolve_file` dry_run returns changes without writing
- `scan_unbound` detects bare numbers matching known metric patterns
- `scan_unbound` ignores numbers inside `<!-- v: -->` markers
- `scan_unbound` ignores frozen file patterns (submissions, legacy)
- Round-trip: write markers → resolve → read back = correct values

### Phase 2: `organvm refresh` CLI Command

**New file:** `organvm-engine/src/organvm_engine/cli/refresh.py`

```
organvm refresh [--dry-run] [--skip-context] [--skip-organism] [--skip-legacy]
```

Steps:
1. `compute_metrics()` → write `system-metrics.json`
2. `build_vars()` → write `system-vars.json`
3. `resolve_targets()` → resolve all `<!-- v:KEY -->` bindings in `vars-targets.yaml`
4. `propagate_metrics()` → legacy regex propagation for corpus markdown (unless `--skip-legacy`)
5. `copy_json_targets()` → portfolio JSON copies
6. `sync_all()` → CLAUDE.md auto-blocks (unless `--skip-context`)
7. `compute_organism()` + snapshot (unless `--skip-organism`)

Prints summary: `N variables resolved in M files, P legacy replacements, Q JSON copies`

**Modify:** `organvm-engine/src/organvm_engine/cli/__init__.py` — register `refresh` command

**New file:** `organvm-engine/tests/test_refresh.py`

### Phase 3: Variable Targets Manifest

**New file:** `organvm-corpvs-testamentvm/vars-targets.yaml`

```yaml
# Files containing <!-- v:KEY --> variable bindings.
# Resolved by `organvm refresh`.

targets:
  # Org profile READMEs
  - root: "~/Workspace/organvm-i-theoria/.github"
    files: ["profile/README.md"]
  - root: "~/Workspace/organvm-ii-poiesis/.github"
    files: ["profile/README.md"]
  - root: "~/Workspace/organvm-iii-ergon/.github"
    files: ["profile/README.md"]
  - root: "~/Workspace/organvm-v-logos/.github"
    files: ["profile/README.md"]
  - root: "~/Workspace/organvm-vi-koinonia/.github"
    files: ["profile/README.md"]
  - root: "~/Workspace/organvm-vii-kerygma/.github"
    files: ["profile/README.md"]
  - root: "~/Workspace/meta-organvm/.github"
    files: ["profile/README.md"]

  # Workspace context files
  - root: "~/Workspace"
    files: ["CLAUDE.md", "GEMINI.md", "AGENTS.md"]

  # Corpus docs
  - root: "."
    files:
      - "README.md"
      - "CLAUDE.md"

  # Application pipeline (composable templates only)
  - root: "~/Workspace/4444J99/application-pipeline"
    globs:
      - "blocks/**/*.md"
      - "strategy/*.md"
      - "docs/*.md"
      - "docs/thesis/*.md"
```

### Phase 4: CI Linter — Unbound Metric Check

**New file:** `organvm-engine/src/organvm_engine/metrics/lint_vars.py`

```python
def lint_file(path: Path, variables: dict) -> list[LintViolation]:
    """Check a markdown file for bare metric numbers that should be bound."""

def lint_workspace(workspace: Path, variables: dict, frozen_patterns: list[str]) -> LintReport:
    """Walk workspace, lint all non-frozen markdown files."""
```

The linter knows the current variable values and scans for:
- Bare occurrences of `total_repos` value (e.g., `103`) near words like "repo", "repository"
- Bare occurrences of word counts near "words"
- Bare occurrences of organ counts
- Numbers inside `<!-- v: -->` markers are IGNORED (they're properly bound)

Frozen patterns (paths excluded from linting):
- `**/pipeline/submissions/**`
- `**/scripts/legacy-submission/**`
- `**/materials/resumes/**`
- `**/variants/cover-letters/*-alchemized.md`
- `**/docs/archive/**`
- `**/docs/planning/**`
- `**/.claude/plans/**`
- `**/node_modules/**`
- `**/intake/**`

**CLI command:** `organvm lint-vars [--fix]`
- Without `--fix`: reports unbound metrics
- With `--fix`: wraps bare numbers in `<!-- v:KEY -->` markers (best-effort, review before committing)

**GitHub Actions workflow** (for repos that have this check):

```yaml
# .github/workflows/lint-vars.yml
name: Lint Variable Bindings
on: [pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install git+https://github.com/meta-organvm/organvm-engine.git
      - run: organvm lint-vars --strict
```

### Phase 5: Sweep + Migration

Run `organvm lint-vars` to identify all unbound metrics in live files. Then for each file:
1. Add `<!-- v:KEY -->VALUE<!-- /v -->` markers around bare numbers
2. Run `organvm refresh` to verify bindings resolve correctly
3. Commit per-organ or per-category

This is the bulk of the work — ~80-120 files to migrate. Can be parallelized across organs.

### Phase 6: Wire into Daily CI

Update `organvm-corpvs-testamentvm/.github/workflows/metrics-refresh.yml`:

```yaml
- name: Refresh system
  run: |
    organvm refresh --skip-context --skip-organism
```

(Skip context + organism in CI since those need local workspace access. The CI runs on ubuntu with only the corpus repo checked out.)

## Files to Create/Modify

| File | Change |
|------|--------|
| `organvm-engine/src/organvm_engine/metrics/vars.py` | **NEW** — variable manifest builder + resolver |
| `organvm-engine/src/organvm_engine/metrics/lint_vars.py` | **NEW** — CI linter for unbound metrics |
| `organvm-engine/src/organvm_engine/cli/refresh.py` | **NEW** — `organvm refresh` command |
| `organvm-engine/src/organvm_engine/cli/__init__.py` | Register `refresh` + `lint-vars` commands |
| `organvm-engine/src/organvm_engine/metrics/__init__.py` | Export vars module |
| `organvm-engine/tests/test_vars.py` | **NEW** — resolver tests |
| `organvm-engine/tests/test_lint_vars.py` | **NEW** — linter tests |
| `organvm-engine/tests/test_refresh.py` | **NEW** — refresh command tests |
| `organvm-corpvs-testamentvm/vars-targets.yaml` | **NEW** — target manifest |
| `organvm-corpvs-testamentvm/.github/workflows/metrics-refresh.yml` | Use `organvm refresh` |
| 8 org profile READMEs | Add `<!-- v:KEY -->` markers |
| Workspace CLAUDE.md, GEMINI.md | Add markers to metric references |
| Corpus README.md, CLAUDE.md | Add markers to metric references |
| Application pipeline blocks/strategy/docs | Add markers |

## Functions to Reuse

| Function | Location | Used For |
|----------|----------|----------|
| `compute_metrics()` | `metrics/calculator.py` | Calculate metrics |
| `write_metrics()` | `metrics/calculator.py` | Write system-metrics.json |
| `propagate_metrics()` | `metrics/propagator.py` | Legacy regex propagation |
| `copy_json_targets()` + `load_manifest()` | `metrics/propagator.py` | Portfolio JSON |
| `sync_all()` | `contextmd/sync.py` | Context file sync |
| `compute_organism()` | `metrics/organism.py` | Organism snapshot |
| `ORGAN_DIRS` / `REGISTRY_KEY_MAP` | `organ_config.py` | Organ key → directory mapping |
| `load_registry()` | `registry/loader.py` | Load registry |
| `count_words()` | `metrics/calculator.py` | Word counts |

## Execution Order

Build in this order (each phase testable independently):

1. `vars.py` + `test_vars.py` — core resolver (can test with fixture files)
2. `vars-targets.yaml` — target manifest
3. `refresh.py` + `test_refresh.py` — CLI command
4. Register in `cli/__init__.py` — wire up parser
5. `lint_vars.py` + `test_lint_vars.py` — linter
6. Migrate org profiles (8 files) — first batch of marker adoption
7. Migrate corpus docs — second batch
8. Migrate workspace context files — third batch
9. Migrate app pipeline templates — fourth batch
10. CI workflow update — daily automation

## Verification

1. `pytest organvm-engine/tests/test_vars.py -v` — resolver tests pass
2. `pytest organvm-engine/tests/test_lint_vars.py -v` — linter tests pass
3. `pytest organvm-engine/tests/test_refresh.py -v` — refresh tests pass
4. `pytest organvm-engine/tests/ -v` — full suite passes (existing 459+ tests unaffected)
5. `organvm refresh --dry-run` — shows all 7 steps, no writes
6. `organvm refresh` — full run, then verify:
   - `system-vars.json` exists with correct values
   - Org profiles show updated counts in `git diff`
   - `organvm lint-vars` reports zero violations in live files
7. `organvm lint-vars` on a file with bare numbers — reports violations
8. Add a marker to a test file, run `organvm refresh`, confirm value resolved
