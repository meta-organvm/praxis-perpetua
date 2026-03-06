# Plan: Implement Local/Remote Organizational Protocol

## Context

You have a 3600-line protocol document (`~/Workspace/Organizing-Local-Remote-Structure.md`) that defines a comprehensive system for unifying your local filesystem and GitHub remote structure. It contains: an ontology law, an organ charter, 12 supporting registry documents, 4 Python generators, shell wrappers, and multi-phase audit prompts.

**The problem**: 100 git repos scattered flat across `~/Workspace/` with no governing structure. Three GitHub accounts (4444J99 active, 4444JPP inactive, plus 3 orgs). No env vars. No canonical root.

**The goal**: Stand up `$WORLD_ROOT` at `$HOME/world`, deploy all registry files and tooling, so the phased audit (Phase 1-4) can run. All identity is env-var-driven — no hardcoded org names anywhere.

---

## Decisions Made

- **WORLD_ROOT**: `$HOME/world` (fresh root, as the document proposes)
- **4444JPP repos**: Archive realm by default
- **DEFAULT_ORG_UNIT**: `liminal` (matches LIMINAL_ZONE concept)
- **All org names are env vars**: `$ORG_I` through `$ORG_VII` plus `$ORG_LIMINAL`. Actual GitHub names are mutable values. The system references only the env vars.
- **All orgs created**: IV-VII need GitHub orgs (names TBD by user). I-III already exist on GitHub.
- **Org names are placeholders**: Even existing names (ivviiviivvi, omni-dromenon-machina, labores-profani-crux) can be changed — the env var indirection makes this safe.

---

## Current State (observed)

| Metric | Value |
|---|---|
| Git repos in ~/Workspace | 100 |
| GitHub namespaces | `4444JPP`(47), `ivviiviivvi`(25), `4444J99`(24), `omni-dromenon-machina`(2), `tw93`(1), `labores-profani-crux`(1) |
| Duplicate checkouts | 2 |
| Nesting violations | 0 |
| Non-git top-level dirs | ~27 |
| ORG staging dirs | 4 (ORG-IV through VII, seeded) |
| GitHub orgs | 3 (ivviiviivvi, omni-dromenon-machina, labores-profani-crux) |
| Env vars set | None |
| ~/world exists | No |

---

## Architecture: Env-Var-Driven Identity

All identity flows through environment variables. Nothing in the registry, generators, or tooling hardcodes an org name, account name, or path. This means:

- Rename an org on GitHub → update one env var → re-run generators → everything updates
- All manifests, overrides, and scope fences reference `$ORG_I` etc., which the generators resolve at runtime
- The shell env contract is the single source of truth for *what things are called*
- The registry files are the single source of truth for *how things relate*

### Environment Variable Contract

```bash
# ── Core topology ──
export WORLD_ROOT="$HOME/world"
export AUDIT_ROOT="$WORLD_ROOT/.audit"
export REALMS="create research operate publish archive"
export VCS_HOST="github.com"
export ORG_POLICY="mirror-local-to-remote"
export DEFAULT_ORG_UNIT="liminal"

# ── Unmanaged (excluded from audit) ──
export UNMANAGED_DIRS="$HOME/Library $HOME/.cache $HOME/.config $HOME/.Trash"

# ── Organ → GitHub org mapping (stable references, mutable values) ──
export ORG_I="ivviiviivvi"                     # Organ I:   conceptual/symbolic engine
export ORG_II="omni-dromenon-machina"           # Organ II:  art/enactment/experiential
export ORG_III="labores-profani-crux"           # Organ III: commerce/applied labor
export ORG_IV=""                                # Organ IV:  orchestration (name TBD)
export ORG_V=""                                 # Organ V:   public process (name TBD)
export ORG_VI=""                                # Organ VI:  community (name TBD)
export ORG_VII=""                               # Organ VII: marketing/attention (name TBD)

# ── Personal namespaces ──
export ORG_LIMINAL="4444j99"                    # Liminal zone / primary personal
export ORG_LIMINAL_ALT="4444jpp"                # Secondary (archive/forks)

# ── Account identity ──
export GITHUB_PRIMARY="4444J99"
export GITHUB_SECONDARY="4444JPP"
```

### How generators use env vars

The Python generators call `os.environ.get("ORG_I")` etc. when:
- Building canonical_manifest.json (mapping remote URLs to org_unit_ids)
- Building explicit_overrides.json resolution (matching repos to organs)
- Determining canonical paths: `$WORLD_ROOT/realm/<realm>/org/$ORG_I/repo/<name>/`

The `explicit_overrides.json` uses env-var-resolved references:
```json
{
  "org_unit_overrides": [
    {
      "match": { "org_unit_id_env": "ORG_I" },
      "set": { "default_organ_id": "organ_i", "default_realm_id": "create" }
    }
  ]
}
```

Generators resolve `org_unit_id_env` to the current value of that env var at runtime.

---

## Implementation Sequence

### Step 0: Environment variables
**File**: `~/dotfiles/dot_zshenv` (via chezmoi) — or directly to `~/.zshenv`

Add the full env var block above. ORG_IV through ORG_VII remain empty until you choose names.

### Step 1: Create $WORLD_ROOT scaffolding
```
$HOME/world/
  realm/
    create/org/
    research/org/
    operate/org/
    publish/org/
    archive/org/
  _inbox/
  _staging/
  _registry/
    tools/
    repo_template/
      .github/
  .audit/
```

This is `mkdir -p` only. No repo moves.

### Step 2: Deploy critical registry files (4 files)

| File | Source | Notes |
|---|---|---|
| `_registry/ontology_law_v1.md` | Document lines 654-1038 | As-is |
| `_registry/scope_fence.json` | Adapted | include_roots = `[$HOME/Workspace, $HOME/dotfiles]` |
| `_registry/explicit_overrides.json` | New | Env-var-aware org mappings |
| `_registry/realm_organ_matrix.json` | Document lines 2482-2513 | As-is |

### Step 3: Deploy supporting registry files (8 files)

| File | Source |
|---|---|
| `_registry/organ_charter_v0.md` | Document lines 1187-1403 |
| `_registry/lifecycle_law_v1.md` | Document lines 1868-1930 |
| `_registry/exception_taxonomy_v1.md` | Document lines 1936-1986 |
| `_registry/exception_resolution_playbook.md` | Document lines 1990-2042 |
| `_registry/preflight_policy_v1.md` | Document lines 2060-2118 |
| `_registry/secrets_policy_v1.md` | Document lines 2384-2424 |
| `_registry/audit_cadence_v1.md` | Document lines 2430-2472 |
| `_registry/unit_taxonomy_v1.md` | Document lines 2518-2566 |

### Step 4: Deploy generator toolchain (7 files)

| File | Notes |
|---|---|
| `_registry/tools/lib.py` | **New**: extracted shared utilities (normalize_id, load_json, safe_write_json, sha256_bytes, sanitize_remote_url, parse_githubish_remote, env_expand, now_iso) |
| `_registry/tools/gen_canonical_manifest.py` | Refactored to use lib.py + env-var org resolution |
| `_registry/tools/gen_organ_manifest.py` | Refactored to use lib.py |
| `_registry/tools/gen_topology_manifest.py` | Refactored to use lib.py |
| `_registry/tools/gen_repo_index.py` | Refactored to use lib.py |
| `_registry/tools/gen_manifests.sh` | Updated paths for $WORLD_ROOT |
| `_registry/tools/check_repo_conformance.sh` | From document |

**Key change to generators**: `gen_canonical_manifest.py` gains an `--org-env-map` flag or reads a mapping file that connects env var names to their resolved values. The `explicit_overrides.json` can reference `org_unit_id_env: "ORG_I"` instead of hardcoding `ivviiviivvi`. At generation time, the env var is resolved to the current value.

### Step 5: Deploy templates and index (8+ files)

| File | Notes |
|---|---|
| `_registry/repo_template/README.md` | Skeleton with placeholders |
| `_registry/repo_template/CODEOWNERS` | Minimal |
| `_registry/repo_template/LICENSE` | Placeholder |
| `_registry/repo_template/SECURITY.md` | From document |
| `_registry/repo_template/CONTRIBUTING.md` | From document |
| `_registry/repo_template/.gitignore` | Standard |
| `_registry/repo_template/.github/ISSUE_TEMPLATE.md` | From document |
| `_registry/repo_template/.github/PULL_REQUEST_TEMPLATE.md` | From document |
| `_registry/index.md` | Template |
| `_registry/index_generation_contract.md` | From document |

### Step 6: Run Phase 1 inventory audit
Execute against `~/Workspace/` (the current location of all repos). This scans, inventories, and writes:
- `.audit/run_<ts>/inventory.json`
- `.audit/run_<ts>/git_repos.json`
- `.audit/run_<ts>/inventory_summary.md`

**Does NOT move anything.** Read-only scan of `~/Workspace/` and `~/dotfiles/`.

### Step 7: Run generators
```bash
source ~/.zshenv  # load env vars
"$WORLD_ROOT/_registry/tools/gen_manifests.sh" "$AUDIT_ROOT/run_<ts>"
```

Produces:
- `_registry/canonical_manifest.json`
- `_registry/organ_manifest.json`
- `_registry/topology_manifest.json`
- `_registry/repo_index.csv`

At this point you have a complete picture: what exists, where it should go, and the mapping between them. **Phase 2-4 from the document follow from here.**

---

## Total files to create: ~30

- 1 env var file (zshenv)
- ~15 directories (mkdir -p)
- 12 registry markdown/json files
- 7 tool files (5 Python, 2 shell)
- 8 template files
- 2 index files

---

## What this does NOT do (deferred)

- **No repo moves** — that's Phase 4, which requires explicit `EXECUTE PHASE 4` authorization
- **No GitHub org creation** — ORG IV-VII names are TBD; creating them is a separate step after naming
- **No remote modifications** — no `git remote add`, `gh repo create`, or `git push`
- **No file deletion** — nothing in ~/Workspace is touched

---

## Verification

1. `echo $WORLD_ROOT` → `$HOME/world`
2. `ls $WORLD_ROOT/_registry/` → shows all 12+ registry files
3. `python3 $WORLD_ROOT/_registry/tools/gen_canonical_manifest.py --help` → runs
4. `ls $AUDIT_ROOT/run_*/` → shows inventory.json, git_repos.json
5. `jq '.repos | length' $WORLD_ROOT/_registry/canonical_manifest.json` → ~100
6. `wc -l $WORLD_ROOT/_registry/repo_index.csv` → ~101 (header + repos)
7. `jq '.mappings[] | select(.needs_move==true) | .repo_uid' $WORLD_ROOT/_registry/topology_manifest.json | wc -l` → shows how many repos need relocation

---

## Remaining user decisions needed before Phase 4

1. Names for ORG_IV through ORG_VII (GitHub org names)
2. Whether to rename existing orgs (I-III) or keep current names
3. Per-repo realm assignments for anything the audit can't classify with high confidence
4. Whether 4444JPP account repos should be forked/transferred to 4444J99 or remain separate
