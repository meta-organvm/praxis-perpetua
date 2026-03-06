# Centralized Metrics Propagation System

## Context

Metrics across the ORGANVM system go stale within hours. When a repo is added, a sprint completed, or 100K words written in a day, the number "101 repositories" is immediately wrong in 50+ files across 6+ repos. The previous approach (manual find-and-replace of hardcoded values) is fundamentally broken for a system this volatile.

**The user's directive:** "We need meta-organvm wide variables that will update automatically — from my portfolio website, to each and every README, to the application materials, all down the line."

**Key discovery:** Most of the infrastructure already exists but isn't wired together:

| Component | Location | Status |
|-----------|----------|--------|
| `registry-v2.json` (source of truth) | `meta-organvm/organvm-corpvs-testamentvm/` | EXISTS |
| `calculate-metrics.py` (computes from registry) | same repo, `scripts/` | EXISTS |
| `system-metrics.json` (canonical metrics) | same repo, root | EXISTS |
| `organvm_engine.metrics.calculator` (library version) | `meta-organvm/organvm-engine/` | EXISTS |
| `organvm_engine.metrics.propagator` (library version, accepts arbitrary file lists) | same package | EXISTS |
| `propagate-metrics.py` (standalone, corpus-only whitelist) | corpus `scripts/` | EXISTS, INCOMPLETE |
| `organvm context sync` (CLAUDE.md auto-sections) | engine CLI | EXISTS |
| Portfolio `sync-trust-metrics.mjs` | portfolio `scripts/` | EXISTS but syncs quality data, NOT system-metrics |
| Portfolio `system-metrics.json` copy | portfolio `src/data/` | STALE (97 repos, Feb 17) |
| application-pipeline `check_metrics.py` | app-pipeline `scripts/` | HARDCODED, should read from source |

**What's missing:** A cross-repo propagation config and CLI command that chains: calculate → copy JSON → propagate markdown → (optionally) context sync.

---

## Plan

### Step 1: Create metrics-targets.yaml (propagation manifest)

**File:** `meta-organvm/organvm-corpvs-testamentvm/metrics-targets.yaml`

This file declares every downstream consumer of system-metrics.json, organized by propagation type.

```yaml
# Centralized manifest of all system-metrics.json consumers.
# Used by `organvm metrics propagate` (or propagate-metrics.py --cross-repo).
#
# Types:
#   json_copy — copy system-metrics.json to destination (for code that imports JSON at build time)
#   markdown  — regex-propagate metric values into whitelisted markdown files

json_copies:
  - dest: "~/Workspace/4444J99/portfolio/src/data/system-metrics.json"
    note: "Portfolio site imports at build time via Astro"

markdown_targets:
  # Existing: corpus internal docs
  - root: "."  # relative to this repo
    whitelist:
      - "README.md"
      - "CLAUDE.md"
      - "applications/*.md"
      - "applications/shared/*.md"
      - "docs/applications/*.md"
      - "docs/applications/cover-letters/*.md"
      - "docs/essays/09-ai-conductor-methodology.md"
      - "docs/operations/*.md"

  # NEW: application-pipeline
  - root: "~/Workspace/4444J99/application-pipeline"
    whitelist:
      - "blocks/**/*.md"
      - "strategy/*.md"
      - "docs/*.md"
      - "variants/**/*.md"

  # Future: individual repo READMEs can be added here
```

### Step 2: Extend propagate-metrics.py to read targets from manifest

**File:** `meta-organvm/organvm-corpvs-testamentvm/scripts/propagate-metrics.py`

Changes:
- Add `--cross-repo` flag that reads `metrics-targets.yaml` and processes ALL targets
- Add `--targets` flag to specify a custom manifest path
- When `--cross-repo`, also handle `json_copies` (copy system-metrics.json to destination, transforming schema if needed)
- Keep default behavior (corpus-only whitelist) when `--cross-repo` is not set
- The existing `WHITELIST_GLOBS` becomes the fallback for when no manifest is used

Key modification to `main()`:
```python
parser.add_argument("--cross-repo", action="store_true",
                    help="Read metrics-targets.yaml and propagate to all registered consumers")
parser.add_argument("--targets", default=None,
                    help="Path to metrics-targets.yaml (default: repo root)")
```

When `--cross-repo`:
1. Load `metrics-targets.yaml`
2. For each `json_copies` entry: copy `system-metrics.json` to `dest` (expand `~`)
3. For each `markdown_targets` entry: resolve root, expand whitelist globs, run `update_file()` on each

### Step 3: Transform portfolio's system-metrics.json on copy

**Context:** The portfolio's copy (`src/data/system-metrics.json`) has a DIFFERENT schema than the canonical one. The canonical version has `computed` + `manual` sections. The portfolio version has `registry`, `essays`, `sprint_history`, etc.

**Approach:** Add a transform step in the JSON copy logic. When copying to portfolio:
- Read canonical `system-metrics.json`
- Read portfolio's EXISTING `system-metrics.json` (for fields not in canonical, like `sprint_history`, `engagement_baseline`)
- Update the `registry.*` fields from canonical `computed.*`
- Update `essays.total` from canonical `computed.published_essays`
- Write merged result

**File:** Add `transform_for_portfolio()` function in `propagate-metrics.py` (or a separate `scripts/transform-metrics.py`).

Alternatively (simpler): refactor the portfolio to consume the canonical schema directly. This would require updating `portfolio/src/data/` imports and any component that reads from system-metrics.json.

**Recommendation:** Use the transform approach for now (preserves backward compatibility with portfolio), with a TODO to migrate the portfolio to the canonical schema later.

### Step 4: Fix application-pipeline check_metrics.py

**File:** `4444J99/application-pipeline/scripts/check_metrics.py`

Change from hardcoded `SOURCE_METRICS` dict to reading from system-metrics.json:

```python
# Before:
SOURCE_METRICS = {
    "total_repos": 101,
    "active_repos": 92,
    ...
}

# After:
CANONICAL_METRICS = Path.home() / "Workspace/meta-organvm/organvm-corpvs-testamentvm/system-metrics.json"

def load_source_metrics(path: Path = CANONICAL_METRICS) -> dict:
    """Load source of truth metrics from system-metrics.json."""
    with open(path) as f:
        data = json.load(f)
    c = data["computed"]
    m = data.get("manual", {})
    return {
        "total_repos": c["total_repos"],
        "active_repos": c["active_repos"],
        "archived_repos": c["archived_repos"],
        "github_orgs": c["total_organs"],
        "published_essays": c["published_essays"],
        "organ_repo_counts": {
            info["name"]: info["repos"]
            for key, info in c["per_organ"].items()
        },
    }
```

Add `--metrics` CLI arg to override the default path.

### Step 5: Add `organvm metrics propagate` CLI subcommand

**File:** `meta-organvm/organvm-engine/src/organvm_engine/cli.py`

Add a `propagate` subcommand under `metrics`:
```
organvm metrics propagate              # corpus-only (default)
organvm metrics propagate --cross-repo # all targets from manifest
organvm metrics propagate --dry-run    # preview changes
```

This calls `organvm_engine.metrics.propagator.propagate_metrics()` with the appropriate file list. For `--cross-repo`, load `metrics-targets.yaml` and expand all targets.

### Step 6: Add `organvm metrics refresh` convenience command

**File:** `meta-organvm/organvm-engine/src/organvm_engine/cli.py`

One command that chains the full pipeline:
```
organvm metrics refresh [--cross-repo] [--dry-run]
```

Does:
1. `organvm metrics calculate` (registry → system-metrics.json)
2. `organvm metrics propagate [--cross-repo]` (system-metrics.json → all markdown targets + JSON copies)

This is the "one command to rule them all" the user needs.

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `meta-organvm/organvm-corpvs-testamentvm/metrics-targets.yaml` | CREATE |
| `meta-organvm/organvm-corpvs-testamentvm/scripts/propagate-metrics.py` | MODIFY (add --cross-repo, --targets, JSON copy, manifest loading) |
| `meta-organvm/organvm-engine/src/organvm_engine/cli.py` | MODIFY (add `metrics propagate` and `metrics refresh` subcommands) |
| `meta-organvm/organvm-engine/src/organvm_engine/metrics/propagator.py` | MODIFY (add manifest loading, cross-repo file resolution, JSON copy logic) |
| `4444J99/application-pipeline/scripts/check_metrics.py` | MODIFY (read from system-metrics.json instead of hardcoding) |

---

## Verification

1. **Calculate:** `cd ~/Workspace/meta-organvm/organvm-corpvs-testamentvm && python scripts/calculate-metrics.py` — produces fresh system-metrics.json
2. **Propagate corpus-only:** `python scripts/propagate-metrics.py --dry-run` — shows existing behavior unchanged
3. **Propagate cross-repo:** `python scripts/propagate-metrics.py --cross-repo --dry-run` — shows application-pipeline blocks + strategy files getting updated
4. **JSON copy:** After `--cross-repo` (non-dry-run), `portfolio/src/data/system-metrics.json` has current data
5. **check_metrics validation:** `cd ~/Workspace/4444J99/application-pipeline && python scripts/check_metrics.py` — reads from canonical system-metrics.json, passes
6. **Engine CLI:** `organvm metrics refresh --cross-repo --dry-run` — chains calculate + propagate
7. **Regression:** `pytest meta-organvm/organvm-engine/tests/test_metrics.py -v` — existing tests pass

## Future Work (not in this plan)

- **CI integration:** GitHub Actions in corpus repo that runs `organvm metrics refresh --cross-repo` on registry-v2.json changes
- **Portfolio schema migration:** Move portfolio to consume canonical `computed`/`manual` schema directly
- **Per-repo README propagation:** Add individual repo READMEs to `metrics-targets.yaml` as needed
- **Watch mode:** File watcher that triggers refresh on registry-v2.json save
