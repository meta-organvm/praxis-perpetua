# Workspace Root Cleanup

## Context

After the workspace restructure (2026-02-16), all 68 organ repos were moved to `~/Workspace/<github-org>/<repo>/` flat 2-level layout. But the root still has 18+ leftover items from the pre-restructure era: broken symlinks, old content directories, tooling installs, a stale `~/world/` hierarchy, and miscellaneous cruft. Total cruft: ~1.1 GB.

The goal is to get `~/Workspace/` to a clean state where every top-level directory is either a GitHub org directory, a special-purpose directory (intake/), or an active non-organ project.

## Inventory (33 top-level items currently)

### Keep (correct structure)
- `4444J99/` — GitHub org (portfolio, .github profile)
- `meta-organvm/` — GitHub org (corpus, alchemia-ingestvm)
- `organvm-i-theoria/` through `organvm-vii-kerygma/` — 7 organ org dirs
- `intake/` — universal catch-all triage directory

### Delete
- `4444JPP/` — 43 **broken symlinks** to old `~/world/realm/`. Nothing recoverable. (0 bytes real)
- `.DS_Store` — macOS metadata (70KB)
- `.github alias` — stale macOS alias file pointing to old `~/world/` hierarchy
- `portfolio` symlink — redundant shortcut to `4444J99/portfolio` (symlink)
- `ivviiviivvi/` — contains only `.DS_Store` and an empty subdir (16KB)
- `labores-profani-crux/` — contains only `.DS_Store` files and empty subdirs (16KB)
- `Projects/` — empty Active/ and Archive/ dirs (12KB)
- `src/` — orphaned code snippets (csrf.ts, oauth.ts, auth.ts) — move to intake/ first (80KB)

### Move to `intake/`
These are pre-organ content dirs that should be triaged later:
- `alchemical-synthesizer/` — git repo under 4444J99 org, 13MB. Move to intake/ (it's misplaced at root; should be `4444J99/alchemical-synthesizer/` or intake/)
- `all-fusion-engine/` — document drafts, no git (10MB)
- `auto-rev-epistemic-engine_spec/` — spec documents, no git (304KB)
- `hokage-chess--believe-it!/` — project docs, no git (464KB)
- `JST_/` — business materials, no git (236KB)
- `metasystem-core/` — Python project (not git), agent_utils, configs (80MB)
- `omni-dromenon-machina.BACKUP-20260207/` — backup dir from restructure (41MB)
- `OS-me/` — large mixed content dir, no git (103MB)
- `self-patent-fulfillment/` — patent texts (28KB)
- `src/` — orphan code snippets (80KB)

### Move to `~/tools/`
- `google-cloud-sdk/` — SDK install, not a project (645MB)

### Keep but fix
- `cloudbase-mcp/` — npm package install, keep in Workspace/ (per user's "keep tooling" for mcp-servers)
- `mcp-servers/` — MCP server configs, keep in Workspace/
- `.dbxignore` — Dropbox ignore file, functional, keep

### Archive `~/world/` docs to intake/
- Move `~/world/_registry/` contents to `intake/world-registry-archive/`
- Then delete `~/world/` entirely (audit logs, staging/duplicates, empty realm dirs)

## Execution Steps

### Step 1: Delete pure cruft
```
rm /Users/4jp/Workspace/.DS_Store
rm "/Users/4jp/Workspace/.github alias"
rm /Users/4jp/Workspace/portfolio  # symlink
rm -rf /Users/4jp/Workspace/4444JPP/
rm -rf /Users/4jp/Workspace/ivviiviivvi/
rm -rf /Users/4jp/Workspace/labores-profani-crux/
rm -rf /Users/4jp/Workspace/Projects/
```

### Step 2: Move content dirs to intake/
```
mv alchemical-synthesizer intake/
mv all-fusion-engine intake/
mv auto-rev-epistemic-engine_spec intake/
mv hokage-chess--believe-it! intake/
mv JST_ intake/
mv metasystem-core intake/
mv omni-dromenon-machina.BACKUP-20260207 intake/
mv OS-me intake/
mv self-patent-fulfillment intake/
mv src intake/src-orphan
```

### Step 3: Archive ~/world/ registry, delete ~/world/
```
mkdir -p intake/world-registry-archive
cp -r ~/world/_registry/* intake/world-registry-archive/
rm -rf ~/world/
```

### Step 4: Move google-cloud-sdk to ~/tools/
```
mkdir -p ~/tools
mv google-cloud-sdk ~/tools/
```
Update any shell profile references to google-cloud-sdk path (check .zshrc, .zprofile).

### Step 5: Clean .DS_Store from intake/
```
find intake/ -name .DS_Store -delete
```

## Result

After cleanup, `~/Workspace/` will contain:

| Directory | Purpose |
|-----------|---------|
| `4444J99/` | GitHub org (portfolio, profile) |
| `meta-organvm/` | GitHub org (corpus) |
| `organvm-i-theoria/` | ORGAN-I repos |
| `organvm-ii-poiesis/` | ORGAN-II repos |
| `organvm-iii-ergon/` | ORGAN-III repos |
| `organvm-iv-taxis/` | ORGAN-IV repos |
| `organvm-v-logos/` | ORGAN-V repos |
| `organvm-vi-koinonia/` | ORGAN-VI repos |
| `organvm-vii-kerygma/` | ORGAN-VII repos |
| `intake/` | Triage staging (now ~248MB with moved content) |
| `cloudbase-mcp/` | MCP tooling |
| `mcp-servers/` | MCP server configs |
| `.dbxignore` | Dropbox config (hidden file) |

13 items (from 33). ~700MB freed (645MB google-cloud-sdk + ~57MB deleted cruft). `~/world/` gone.

## Verification

1. `ls ~/Workspace/` shows only the expected 13 items (10 org dirs + intake + 2 MCP dirs)
2. `ls ~/world/` fails (directory gone)
3. `ls ~/tools/google-cloud-sdk/bin/gcloud` succeeds
4. `gcloud --version` still works (check shell path)
5. All organ repos still accessible: `ls ~/Workspace/organvm-iv-taxis/orchestration-start-here/`
6. No broken symlinks: `find ~/Workspace -maxdepth 2 -type l -exec test ! -e {} \; -print` returns empty
