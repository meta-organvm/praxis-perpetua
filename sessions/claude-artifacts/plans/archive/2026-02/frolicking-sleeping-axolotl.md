# Plan B: Workspace Directory Restructure

## Context

The workspace currently has three overlapping directory layers for the same repos:

1. **`~/world/realm/<realm>/org/<org>/repo/<repo>/`** — 140 git repos in a 7-level ontological hierarchy (54GB). Real `.git` dirs live here.
2. **`~/Workspace/<repo-name>`** — 39 symlinks pointing into `~/world/` + ~6 actual git repos + ~20 non-git content dirs.
3. **GitHub** — 91 repos across 8 `organvm-*` orgs + personal repos under `4444J99`/`4444JPP`.

The problems:
- The `~/world/` structure uses **old org names** (`liminal`, `i`, `ii`, `iii`) that don't match the current GitHub org names (`organvm-i-theoria`, `organvm-ii-poiesis`, etc.)
- Repos are scattered across mismatched realms (e.g., ORGAN-III repos in `create/org/i/` or `create/org/liminal/`)
- No tool can `cd ~/Workspace/organvm-i-theoria/recursive-engine--generative-entity/` — it doesn't exist
- The 7-level depth adds friction to navigation and breaks the routing convention from Plan A

**Goal:** Restructure to `~/Workspace/<github-org>/<repo>/` — 2 levels, mirrors GitHub exactly.

**Scope:** Organ system only (91 repos in registry). Personal repos (4444J99, 4444JPP forks/tools) stay as-is.

**Data strategy:** Physical `mv` from `~/world/` into `~/Workspace/`. No re-cloning.

---

## Inventory Summary

| Category | Count | Action |
|---|---|---|
| Registry repos with local clone in `~/world/` | 55 | Move to `~/Workspace/<org>/<repo>/` |
| Registry repos with local clone in `~/Workspace/` (actual dir) | 6 | Move into org subdirectory |
| Registry repos with non-git content dir in `~/Workspace/` | 8 | Move content into new repo dir |
| Registry repos remote-only (no local clone) | 14 | Skip (clone later if needed) |
| `.github` infra repos | 8 | Skip (no local working copy needed) |
| Symlinks in `~/Workspace/` pointing to `~/world/` | 39 | Remove after move |
| Non-organ repos in `~/world/` (4444JPP forks, research) | ~79 | Leave in `~/world/` for now |

---

## Step 1: Create org directories

```bash
mkdir -p ~/Workspace/{organvm-i-theoria,organvm-ii-poiesis,organvm-iii-ergon,organvm-iv-taxis,organvm-v-logos,organvm-vi-koinonia,organvm-vii-kerygma,meta-organvm}
```

---

## Step 2: Move repos from `~/world/` to `~/Workspace/<org>/<repo>/`

For each of the 55 registry repos that have local clones in `~/world/`, move them using the **GitHub repo name** (with double-dashes preserved), not the local single-dash name.

Example:
```bash
mv ~/world/realm/create/org/liminal/repo/recursive-engine-generative-entity \
   ~/Workspace/organvm-i-theoria/recursive-engine--generative-entity
```

**Name mapping rule:** Local names use single dashes; GitHub names use double dashes. The destination must match the GitHub name exactly so that `~/Workspace/<org>/<repo>` is a 1:1 mirror of the GitHub URL `github.com/<org>/<repo>`.

### Full move table (55 repos from ~/world/)

**ORGAN-I → organvm-i-theoria** (16 repos):
| Local path (in ~/world/) | Destination |
|---|---|
| `create/org/liminal/repo/recursive-engine-generative-entity` | `organvm-i-theoria/recursive-engine--generative-entity` |
| `create/org/liminal/repo/organon-noumenon-ontogenetic-morphe` | `organvm-i-theoria/organon-noumenon--ontogenetic-morphe` |
| `create/org/liminal/repo/narratological-algorithmic-lenses` | `organvm-i-theoria/narratological-algorithmic-lenses` |
| `create/org/liminal/repo/call-function-ontological` | `organvm-i-theoria/call-function--ontological` |
| `create/org/liminal/repo/sema-metra-alchemica-mundi` | `organvm-i-theoria/sema-metra--alchemica-mundi` |
| `create/org/i/repo/system-governance-framework` | `organvm-i-theoria/system-governance-framework` |
| `create/org/i/repo/cognitive-archaelogy-tribunal` | `organvm-i-theoria/cognitive-archaelogy-tribunal` |
| `create/org/i/repo/radix-recursiva-solve-coagula-redi` | `organvm-i-theoria/radix-recursiva-solve-coagula-redi` |
| `create/org/i/repo/nexus-babel-alexandria` | `organvm-i-theoria/nexus--babel-alexandria-` |
| `create/org/i/repo/reverse-engine-recursive-run` | `organvm-i-theoria/reverse-engine-recursive-run` |
| `create/org/i/repo/4-ivi374-f0rivi4` | `organvm-i-theoria/4-ivi374-F0Rivi4` |
| `create/org/i/repo/cog-init-1-0` | `organvm-i-theoria/cog-init-1-0-` |
| `create/org/i/repo/collective-persona-operations` | `organvm-i-theoria/collective-persona-operations` |
| `create/org/liminal/repo/linguistic-atomization-framework` | `organvm-i-theoria/linguistic-atomization-framework` |
| `operate/org/liminal/repo/my-knowledge-base` | `organvm-i-theoria/my-knowledge-base` |
| `operate/org/liminal/repo/a-i-skills` | `organvm-i-theoria/a-i--skills` |

**ORGAN-II → organvm-ii-poiesis** (12 repos):
| Local path | Destination |
|---|---|
| `create/org/ii/repo/core-engine` | `organvm-ii-poiesis/core-engine` |
| `create/org/ii/repo/performance-sdk` | `organvm-ii-poiesis/performance-sdk` |
| `create/org/ii/repo/example-generative-music` | `organvm-ii-poiesis/example-generative-music` |
| `create/org/ii/repo/metasystem-master` | `organvm-ii-poiesis/metasystem-master` |
| `create/org/ii/repo/example-choreographic-interface` | `organvm-ii-poiesis/example-choreographic-interface` |
| `create/org/ii/repo/example-generative-visual` | `organvm-ii-poiesis/example-generative-visual` |
| `create/org/ii/repo/docs` | `organvm-ii-poiesis/docs` |
| `create/org/i/repo/a-mavs-olevm` | `organvm-ii-poiesis/a-mavs-olevm` |
| `create/org/i/repo/a-i-council-coliseum` | `organvm-ii-poiesis/a-i-council--coliseum` |
| `create/org/ii/repo/artist-toolkit-and-templates` | `organvm-ii-poiesis/artist-toolkit-and-templates` |
| `create/org/ii/repo/client-sdk` | `organvm-ii-poiesis/client-sdk` |
| `create/org/ii/repo/academic-publication` | `organvm-ii-poiesis/academic-publication` |

**Plus** `example-theatre-dialogue` and `audio-synthesis-bridge` from `create/org/ii/repo/`.

**ORGAN-III → organvm-iii-ergon** (15 repos from ~/world/):
- Repos currently in `create/org/i/repo/`: classroom-rpg-aetheria, gamified-coach-interface, trade-perpetual-future, fetch-familiar-friends, sovereign-ecosystem--real-estate-luxury, search-local--happy-hour, virgil-training-overlay
- Repos in `operate/org/iii/repo/`: public-record-data-scrapper
- Repos in `operate/org/liminal/repo/`: multi-camera--livestream--framework, universal-mail--automation, mirror-mirror, the-invisible-ledger, your-fit-tailored
- Repos in `create/org/liminal/repo/`: the-actual-news, my-block-warfare, life-my-midst-in, my-father-mother
- Repo in `archive/org/liminal_alt/repo/`: enterprise-plugin

**ORGAN-IV → organvm-iv-taxis** (5 repos):
- orchestration-start-here, petasum-super-petasum, universal-node-network, agentic-titan, agent--claude-smith

**ORGAN-V → organvm-v-logos** (1 repo): public-process
**ORGAN-VI → organvm-vi-koinonia** (2 repos): salon-archive, reading-group-curriculum
**ORGAN-VII → organvm-vii-kerygma** (3 repos): announcement-templates, social-automation, distribution-strategy
**META → meta-organvm** (1 repo): alchemia-ingestvm (from ~/Workspace/)

---

## Step 3: Move repos already in `~/Workspace/` (actual dirs)

These 6 repos are actual git directories in `~/Workspace/` (not symlinks). Move them into their org subdirectory:

| Current path | Destination |
|---|---|
| `~/Workspace/alchemia-ingestvm` | `~/Workspace/meta-organvm/alchemia-ingestvm` |
| `~/Workspace/chthon-oneiros` | `~/Workspace/organvm-ii-poiesis/chthon-oneiros` |
| `~/Workspace/krypto-velamen` | `~/Workspace/organvm-ii-poiesis/krypto-velamen` |
| `~/Workspace/alchemical-synthesizer` | Keep as-is (not in registry — personal project) |
| `~/Workspace/portfolio` | Keep as-is (not in registry — `4444J99/portfolio`) |
| `~/Workspace/4444J99` | Keep as-is (personal org, out of scope) |

---

## Step 4: Handle non-git content directories

8 registry repos have **non-git content directories** in `~/Workspace/` (research notes, PDFs, design docs). These predate the GitHub repos. Strategy: move content into the matching repo directory as a `_local/` subdirectory, or keep them as sibling dirs within the org folder.

| Content dir | Registry repo | Action |
|---|---|---|
| `~/Workspace/adaptive-personal-syllabus/` | organvm-vi-koinonia/adaptive-personal-syllabus | Move as `_local/` into cloned repo when it exists |
| `~/Workspace/agentic-titan/` (non-git) | organvm-iv-taxis/agentic-titan | Merge: move content, then mv world repo on top |
| `~/Workspace/card-trade-social/` | organvm-iii-ergon/card-trade-social | Move to `~/Workspace/organvm-iii-ergon/card-trade-social/` |
| `~/Workspace/fetch-familiar-friends/` | organvm-iii-ergon/fetch-familiar-friends | Clone from GitHub, move content to `_local/` |
| `~/Workspace/life-betterment-simulation/` | organvm-ii-poiesis/life-betterment-simulation | Move to `~/Workspace/organvm-ii-poiesis/life-betterment-simulation/` |
| `~/Workspace/scalable-lore-expert/` | organvm-i-theoria/scalable-lore-expert | Move to `~/Workspace/organvm-i-theoria/scalable-lore-expert/` |
| `~/Workspace/shared-rememberance-gateway/` | organvm-ii-poiesis/shared-remembrance-gateway | Move (note: spelling difference) |
| `~/Workspace/universal-waveform-explorer/` | organvm-ii-poiesis/universal-waveform-explorer | Move to `~/Workspace/organvm-ii-poiesis/universal-waveform-explorer/` |

**Note:** `agentic-titan` is special — it has BOTH a non-git dir in `~/Workspace/` AND a git repo in `~/world/`. The git repo takes priority; merge local content into a `_local/` subdirectory.

---

## Step 5: Remove stale symlinks

After all moves, remove the 39 symlinks in `~/Workspace/` that pointed to `~/world/`:

```bash
find ~/Workspace -maxdepth 1 -type l -lname '*/world/*' -delete
```

Also remove the stale `4444j99-*` org directories (contain broken symlinks to non-existent `~/world/` paths):
- `~/Workspace/4444j99-community/` (2 broken symlinks)
- `~/Workspace/4444j99-marketing/` (3 broken symlinks)
- `~/Workspace/4444j99-orchestration/` (1 broken symlink)
- `~/Workspace/4444j99-organs/` (1 broken symlink)

---

## Step 6: Update git remotes

Many repos still point to old GitHub orgs (ivviiviivvi, 4444J99, omni-dromenon-machina, labores-profani-crux, 4444j99-community, etc.). Update them to the current `organvm-*` org names:

```bash
# For each moved repo:
git -C ~/Workspace/<org>/<repo> remote set-url origin https://github.com/<org>/<repo>.git
```

Use HTTPS URLs (not SSH) to match the push pattern from MEMORY.md.

---

## Step 7: Handle `organvm-pactvm/ingesting-organ-document-structure`

This corpus is special — it's `meta-organvm/organvm-corpvs-testamentvm` on GitHub. It currently lives at `~/Workspace/organvm-pactvm/ingesting-organ-document-structure/`.

**Action:** Move to `~/Workspace/meta-organvm/organvm-corpvs-testamentvm/`

This means updating:
- The Plan A routing convention in CLAUDE.md (path reference)
- Claude Code project settings (if any reference the old path)
- MEMORY.md references

---

## Step 8: Update CLAUDE.md routing convention

Update the "Artifact Routing" section added in Plan A to reflect the new paths:

```
Q1: Working repo → ~/Workspace/<github-org>/<repo>/
Q2: Governance doc → ~/Workspace/meta-organvm/organvm-corpvs-testamentvm/
Q3: Unsorted → ~/Workspace/intake/
```

---

## Step 9: Clean up `~/world/` (optional, deferred)

After moving the 55 organ-system repos out, `~/world/` still contains:
- **~79 non-organ repos** (4444JPP forks, research tools, personal projects)
- **`_staging/duplicates/`** (2GB of backups)
- **`_registry/`** and **`_inbox/`** (tooling from the initial setup)

**Recommendation:** Leave `~/world/` intact for now. The non-organ repos can be migrated in a future pass. Once all repos are confirmed working from `~/Workspace/<org>/<repo>/`, the empty realm directories can be pruned.

---

## Execution Order

The implementation script should:

1. **Dry run first** — print all planned moves without executing
2. **Create org dirs** (Step 1)
3. **Move repos from ~/world/** (Step 2) — one `mv` per repo
4. **Move repos from ~/Workspace/** (Step 3)
5. **Handle content dirs** (Step 4)
6. **Remove symlinks** (Step 5)
7. **Update remotes** (Step 6)
8. **Move corpus** (Step 7)
9. **Update CLAUDE.md** (Step 8)
10. **Verify** — confirm all 61 local repos are accessible at their new paths

The script should be written as a Python script (consistent with existing `scripts/` in the corpus) that:
- Reads `registry-v2.json` for the canonical repo list
- Reads `.config/organvm.config.json` for org name mapping
- Discovers local clones via the same matching logic used in exploration
- Outputs a move plan, then executes with `--execute` flag

---

## Verification

1. For each of the 8 org dirs, `ls ~/Workspace/<org>/` shows the expected repos
2. `git -C ~/Workspace/<org>/<repo> status` works for every moved repo
3. `git -C ~/Workspace/<org>/<repo> remote -v` shows correct `organvm-*` GitHub URL
4. No broken symlinks remain: `find ~/Workspace -maxdepth 1 -type l ! -exec test -e {} \; -print` returns empty
5. No stale `4444j99-*` directories remain
6. `~/Workspace/organvm-pactvm/` only contains `portfolio-merge-workspace/` (corpus moved out)
7. The routing convention in CLAUDE.md references the new corpus path

---

## Risk Mitigation

- **No deletions until verified.** The `~/world/` source directories are NOT deleted until the moved repos are confirmed working.
- **Git state preservation.** `mv` preserves all local branches, stashes, uncommitted changes, and `.git/` metadata.
- **Rollback:** If something breaks, the script should log every move so it can be reversed with `mv <dest> <source>`.
- **Disk space:** `mv` within the same filesystem is instant (inode rename). Since `~/world/` and `~/Workspace/` are both under `~/`, this should be zero-copy.

---

## Critical Files

| File | Action |
|---|---|
| `registry-v2.json` | Read-only (source of truth for repo list) |
| `.config/organvm.config.json` | Read-only (org name mapping) |
| `CLAUDE.md` | Update routing convention paths |
| `~/.claude/projects/*/memory/MEMORY.md` | Update any path references |
| New: `scripts/restructure-workspace.py` | Migration script with dry-run + execute modes |
