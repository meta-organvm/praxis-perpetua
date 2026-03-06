# Plan: Per-Project Alpha-to-Omega Progress Bar

## Context

The ORGANVM workspace has ~100 repos across 8 organs, but no unified "where does this project stand?" view. The promotion state machine (LOCAL → GRADUATED) is too coarse (5 states). The omega scorecard is system-wide, not per-project. The user needs to look at any project and instantly see its completion status with granular checkpoints.

## Design: 12-Stage Progress Bar (α → Ω)

```
  α    SEED  SCAFFOLD  CI  TESTS  DOCS  PROTO  CAND  DEPLOY  GRAD   Ω
  ●━━━━━●━━━━━━●━━━━━●━━━●━━━━━●━━━━●━━━━━●━━━━━●━━━━━━●━━━━━●━━━━●
  ■     ■      ■      ■   ■     □    □     □     □      □     □
                                 ▲ you are here (6/11)
```

### The 11 Checkpoints (+ α origin)

| # | Gate | Registry Signal | Local Signal | Authority |
|---|------|----------------|--------------|-----------|
| α | EXISTS | Entry in registry-v2.json | Repo dir exists | Registry |
| 1 | SEED | — | `seed.yaml` exists + has required fields | Local |
| 2 | SCAFFOLD | `documentation_status` not empty | README.md + .gitignore + package config exist | Reconciled (both must pass) |
| 3 | CI | `ci_workflow` is not null | `.github/workflows/*.yml` exists | Reconciled |
| 4 | TESTS | — | `tests/` dir with ≥1 test file | Local |
| 5 | DOCS | `documentation_status` in DEPLOYED/FLAGSHIP | README >500 words + CHANGELOG.md exists | Registry primary, local upgrades |
| 6 | PROTO | `implementation_status` ≥ PROTOTYPE | `src/` or main package dir has substantive files | Registry primary |
| 7 | CAND | `promotion_status` ≥ CANDIDATE | — | Registry authoritative |
| 8 | DEPLOY | `deployment_url` populated or Pages enabled | — | Registry authoritative |
| 9 | GRAD | `promotion_status` ≥ GRADUATED | — | Registry authoritative |
| Ω | OMEGA | All above + `platinum_status: true` | All local checks pass | Both must agree |

### Truth Reconciliation

Three source layers, reconciled per checkpoint:
1. **Registry** (`registry-v2.json`): promotion_status, implementation_status, ci_workflow, documentation_status, deployment_url, platinum_status
2. **Local filesystem**: seed.yaml, README.md word count, test files, CI workflow files, package config
3. **Derived**: computed from the above (e.g., OMEGA = all 10 previous gates pass)

Reconciliation rules:
- **Registry-authoritative** gates (CAND, DEPLOY, GRAD): registry alone decides
- **Local-authoritative** gates (SEED, TESTS): filesystem alone decides
- **Reconciled** gates (SCAFFOLD, CI, DOCS, PROTO): most conservative signal wins — if registry says CI exists but local shows no workflow file, gate FAILS with a discrepancy warning
- When local filesystem isn't available (repo not cloned), registry-only evaluation with `~` suffix to indicate partial confidence

## Architecture

### Shared Core Module
**File**: `orchestration-start-here/scripts/lib/progress.py`

```python
# Data structures
@dataclass
class Checkpoint:
    name: str           # e.g., "SEED", "CI", "TESTS"
    passed: bool
    confidence: str     # "full" | "registry-only" | "local-only" | "reconciled"
    discrepancy: str    # "" or explanation of mismatch

@dataclass
class ProjectProgress:
    repo: str
    organ: str
    tier: str
    checkpoints: list[Checkpoint]  # ordered α→Ω
    score: int          # count of passed gates
    total: int          # always 11

    def bar(self) -> str: ...  # ASCII rendering
    def to_dict(self) -> dict: ...

# Core evaluator
def evaluate_project(
    repo_entry: dict,              # from registry-v2.json
    local_path: Path | None,       # repo on disk, or None
) -> ProjectProgress: ...

# Batch evaluator
def evaluate_all(
    registry: dict,                # full registry-v2.json
    workspace: Path | None,        # ~/Workspace/ for local scanning
) -> list[ProjectProgress]: ...
```

### CLI Script
**File**: `orchestration-start-here/scripts/project-progress.py`

Modes:
- `python3 scripts/project-progress.py --registry registry-v2.json` → all repos
- `python3 scripts/project-progress.py --registry registry-v2.json --organ IV` → one organ
- `python3 scripts/project-progress.py --registry registry-v2.json --repo orchestration-start-here` → single repo detail view
- `python3 scripts/project-progress.py --registry registry-v2.json --workspace ~/Workspace/` → with local filesystem truth
- `--json` flag for machine-readable output
- `--sort score|organ|name` for ordering

### CLI Output (single repo detail)
```
orchestration-start-here (ORGAN-IV, flagship)
  α ━━●━━●━━●━━●━━●━━●━━●━━●━━○━━○━━○  8/11
      SEED SCAF CI  TEST DOCS PROT CAND DEPL GRAD  Ω
      ■    ■    ■   ■    ■    ■    ■    ■    □    □  □

  ✓ SEED       seed.yaml valid (schema v1.0)
  ✓ SCAFFOLD   README.md (2,847 words), .gitignore, pyproject.toml
  ✓ CI         ci-python.yml (registry) + .github/workflows/ci.yml (local)
  ✓ TESTS      tests/ (14 files)
  ✓ DOCS       FLAGSHIP README DEPLOYED + CHANGELOG.md
  ✓ PROTOTYPE  implementation_status: ACTIVE
  ✓ CANDIDATE  promotion_status: PUBLIC_PROCESS
  ✓ DEPLOYED   deployment_url: set
  ✗ GRADUATED  promotion_status: PUBLIC_PROCESS (need GRADUATED)
  ✗ OMEGA      9/10 prerequisites met
```

### CLI Output (organ summary)
```
ORGAN-IV: Orchestration (7 repos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  orchestration-start-here  ●●●●●●●●○○○  8/11  flagship  PUBLIC_PROCESS
  agentic-titan             ●●●●●●●●○○○  8/11  flagship  PUBLIC_PROCESS
  agent--claude-smith       ●●●●●●●○○○○  7/11  standard  CANDIDATE
  a-i--skills               ●●●●●○●○○○○  6/11  standard  CANDIDATE
  petasum-super-petasum     ●●●○○●●○○○○  5/11  standard  CANDIDATE
  universal-node-network    ●●○○○○●○○○○  3/11  standard  CANDIDATE
  .github                   ●●●●○○○●○○○  4/11  infra     CANDIDATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Organ average: 5.9/11 (53%)
```

### CLI Output (system heatmap)
```
ORGANVM System Progress — α ━━━━━━━━━━━━━━━━━━━━ Ω

  ORGAN-I   ████████░░░  72%  (20 repos, avg 7.9/11)
  ORGAN-II  ██████░░░░░  55%  (31 repos, avg 6.0/11)
  ORGAN-III ███████░░░░  64%  (28 repos, avg 7.0/11)
  ORGAN-IV  █████░░░░░░  53%  ( 7 repos, avg 5.9/11)
  ORGAN-V   ████░░░░░░░  45%  ( 6 repos, avg 5.0/11)
  ORGAN-VI  ████░░░░░░░  42%  ( 6 repos, avg 4.6/11)
  ORGAN-VII ███░░░░░░░░  36%  ( 6 repos, avg 4.0/11)
  META      ████████░░░  73%  ( 7 repos, avg 8.0/11)

  System: ██████░░░░░  59%  (111 repos)

  Graduated: 4 | Deployed: 12 | Candidate: 72 | Local: 6 | Archived: 9
```

### Dashboard Route
**File**: `meta-organvm/system-dashboard/src/dashboard/routes/progress.py`

Route: `/progress/` — renders all repos as horizontal bars grouped by organ, clickable to see detail view. Reuses the same `evaluate_all()` core logic.

**Template**: `meta-organvm/system-dashboard/templates/progress.html`

Visual: colored bars (green=passed, grey=remaining, yellow=discrepancy), grouped by organ with collapsible sections.

## Files to Create/Modify

### Create
1. `orchestration-start-here/scripts/lib/__init__.py` — empty
2. `orchestration-start-here/scripts/lib/progress.py` — core evaluation + rendering logic
3. `orchestration-start-here/scripts/project-progress.py` — CLI entry point
4. `meta-organvm/system-dashboard/src/dashboard/routes/progress.py` — dashboard route
5. `meta-organvm/system-dashboard/templates/progress.html` — dashboard template

### Modify
6. `meta-organvm/system-dashboard/src/dashboard/app.py` — register `/progress/` route

## Implementation Steps

1. **Create `lib/progress.py`**: Checkpoint definitions, `Checkpoint` and `ProjectProgress` dataclasses, `evaluate_project()` with truth reconciliation, `evaluate_all()` batch evaluator, ASCII bar rendering
2. **Create `project-progress.py`**: CLI with argparse, `--registry`, `--workspace`, `--organ`, `--repo`, `--json`, `--sort` flags. Three display modes (detail, organ summary, system heatmap)
3. **Test CLI against registry-v2.json**: Run it, verify output looks correct for known repos
4. **Create dashboard route + template**: Port the rendering to HTML with the existing FastAPI patterns from `/omega/` route
5. **Register route in app.py**: Add the import and router include

## Verification

1. Run CLI in registry-only mode:
   ```bash
   cd orchestration-start-here
   python3 scripts/project-progress.py \
     --registry ~/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json
   ```
2. Run CLI with local workspace scanning:
   ```bash
   python3 scripts/project-progress.py \
     --registry ~/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json \
     --workspace ~/Workspace/
   ```
3. Run single-repo detail:
   ```bash
   python3 scripts/project-progress.py \
     --registry ~/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json \
     --workspace ~/Workspace/ \
     --repo orchestration-start-here
   ```
4. Verify discrepancy detection: check that repos where registry and local disagree show warnings
5. Start dashboard and visit `/progress/`:
   ```bash
   cd ~/Workspace/meta-organvm/system-dashboard
   uvicorn dashboard.app:app --reload
   # Visit http://localhost:8000/progress/
   ```
