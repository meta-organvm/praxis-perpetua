# Operational Handoff Guide

**Purpose:** Everything a second operator needs to maintain and run ORGANVM independently.

**Positions:** Omega #4 (runbooks validated), #16 (bus factor >1)

---

## Prerequisites

- macOS or Linux
- Python 3.11+, Node.js 22+
- Git with SSH access to `meta-organvm` GitHub org
- Familiarity with CLI tools, pytest, npm

## Environment Setup

```bash
# 1. Clone the superproject
git clone --recurse-submodules git@github.com:meta-organvm/meta-organvm--superproject.git ~/Workspace/meta-organvm
cd ~/Workspace/meta-organvm

# 2. Create and activate venv
python3 -m venv .venv
source .venv/bin/activate

# 3. Install all packages in dev mode
pip install -e "organvm-engine/[dev]"
pip install -e "organvm-ontologia/[dev]"
pip install -e "organvm-mcp-server/[dev]"
pip install -e "schema-definitions/"
pip install -e "system-dashboard/[dev]"
pip install -e "alchemia-ingestvm/[dev]"

# 4. Verify
organvm status
pytest organvm-engine/tests/ -v --tb=short
```

## Daily Operations

### Morning Health Check

```bash
# 1. System status
organvm status

# 2. Omega scorecard
organvm omega status

# 3. Nervous system scan
organvm ontologia sense              # sensor signals
organvm ontologia tensions           # structural tensions
organvm ontologia policies --evaluate  # governance policy triggers

# 4. Soak test
organvm ci health                    # CI status across repos

# 5. State snapshot
organvm ontologia snapshot           # creates daily snapshot
organvm ontologia snapshot --compare # drift since last snapshot
```

### Weekly Tasks

1. **Registry validation:** `organvm registry validate`
2. **Seed graph check:** `organvm seed validate`
3. **Governance audit:** `organvm governance audit`
4. **Dependency check:** `organvm governance check-deps`
5. **Revision review:** `organvm ontologia revisions`

### When Things Break

See the operational runbooks at `praxis-perpetua/runbooks/`:

| Runbook | When to Use |
|---------|-------------|
| `rb-repo-promotion.md` | Promoting a repo through the state machine |
| `rb-ci-failure-response.md` | CI workflow fails |
| `rb-registry-update.md` | Updating registry-v2.json safely |
| `rb-soak-incident.md` | Soak test incident or data anomaly |
| `rb-entity-rename.md` | Renaming an entity in ontologia |
| `rb-system-health-check.md` | Full system health investigation |

## Critical System Components

### Registry (source of truth)

**File:** `organvm-corpvs-testamentvm/registry-v2.json`

Never edit directly. Use:
```bash
organvm registry update <repo> <field> <value>
organvm registry show <repo>
```

**Safety guard:** `save_registry()` refuses to write <50 repos.

### Ontologia (entity identity)

**Store:** `~/.organvm/ontologia/` (entities.json, names.jsonl, events.jsonl)

Bootstrap from registry:
```bash
organvm ontologia bootstrap --registry organvm-corpvs-testamentvm/registry-v2.json
```

### Governance Policies

**File:** `~/.organvm/ontologia/policies.json` (6 policies)
**Log:** `~/.organvm/ontologia/revisions.jsonl` (append-only)

Evaluate all policies:
```bash
organvm ontologia policies --evaluate --write
```

### State Snapshots

**Directory:** `~/.organvm/ontologia/snapshots/`
**Retention:** 30-day rolling window (auto-pruned)

### Soak Test

**Directory:** `organvm-corpvs-testamentvm/data/soak/`
**Format:** `daily-YYYY-MM-DD.json`
**Requirement:** 30 consecutive days with ≤3 incidents

## Promotion Workflow

```
LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED
```

Requirements for each transition:
- **→ CANDIDATE:** Repo exists, has seed.yaml, basic documentation
- **→ PUBLIC_PROCESS:** CI workflow set + platinum_status + implementation_status=ACTIVE
- **→ GRADUATED:** All promotion criteria met, sustained operation
- **→ ARCHIVED:** Intentional archival (no auto-archive)

```bash
# Check if transition is valid
organvm governance promote <repo> <target-state>

# Apply it
organvm registry update <repo> promotion_status <target-state>
```

## Git Workflow

Each subdirectory is a separate git repo (submodule). Commits are per-subproject.

```bash
# Work in a subproject
cd organvm-engine
git add <files>
git commit -m "feat: description"
git push origin main

# Update superproject pointers
cd ..
git add organvm-engine
git commit -m "chore: sync submodule pointers"
git push origin main
```

## Emergency Procedures

### Registry Corruption
1. Check git history: `cd organvm-corpvs-testamentvm && git log --oneline -5 registry-v2.json`
2. Restore: `git checkout <good-commit> -- registry-v2.json`
3. Validate: `organvm registry validate`

### Ontologia Store Reset
1. Back up: `cp -r ~/.organvm/ontologia/ ~/.organvm/ontologia.bak/`
2. Re-bootstrap: `organvm ontologia bootstrap --registry organvm-corpvs-testamentvm/registry-v2.json`

### Test Suite Failures
1. Run with verbose: `pytest organvm-engine/tests/ -v --tb=long`
2. Check for environment issues: `which python3 && python3 --version`
3. Check conftest guards: tests should NOT touch production data

### Dashboard Won't Start
1. Check port: `lsof -i :8000`
2. Check install: `pip install -e "system-dashboard/[dev]"`
3. Start manually: `uvicorn dashboard.app:app --reload --port 8000`

## Key Contacts

- **Primary maintainer:** System director (check GitHub org members)
- **Issue tracker:** `meta-organvm/organvm-corpvs-testamentvm` GitHub Issues
- **Community:** GitHub Discussions on corpus and engine repos

## Verification Checklist

After completing handoff, the second operator should be able to:

- [ ] Run `organvm status` and explain the output
- [ ] Run the full test suite (`pytest organvm-engine/tests/ -v`)
- [ ] Promote a repo through the state machine
- [ ] Run the nervous system health check
- [ ] Respond to a CI failure using the runbook
- [ ] Create a state snapshot and check for drift
- [ ] Navigate the registry and find a specific repo
- [ ] Start the dashboard and browse entities
