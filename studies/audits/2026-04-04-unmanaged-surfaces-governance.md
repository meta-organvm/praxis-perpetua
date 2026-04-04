# Governance Audit: Unmanaged CLAUDE.md Surfaces

**Date:** 2026-04-04
**Context:** Post-System Library rollout, scan of `~/Workspace` found many CLAUDE.md files without `## System Library`.

---

## Classification Summary

| Bucket | Count | Description |
|--------|-------|-------------|
| **Managed (has System Library)** | 28 | Already synced via `organvm context sync` |
| **Unmanaged — should be managed** | ~5 | True misses in ORGANS that should enter sync |
| **Unmanaged — intentionally local** | ~8 | Personal configs, non-organ repos |
| **Unmanaged — vendor/external** | ~4 | Vendor clones, external contributions |
| **Unmanaged — nested docs** | ~4 | Documentation artifacts, not repo roots |

### Detailed Bucket Counts

**Should be managed (in ORGANS, missing System Library):**
- `organvm-i-theoria/.github/.ai/CLAUDE.md` — nested in .github, should sync
- `organvm-i-theoria/.github/docs/CLAUDE.md` — nested docs
- `organvm-i-theoria/.github/docs/guides/CLAUDE.md` — nested docs
- `organvm-iv-taxis/research/CLAUDE.md` — research folder, not repo root
- `organvm-iv-taxis/contrib--*` folders — vendor clones, should NOT sync

**Intentionally local (not ORGANS):**
- `~/Workspace/CLAUDE.md` — personal workspace root
- `~/Workspace/4444J99/CLAUDE.md` — personal application pipeline
- `~/Workspace/dwv/*/CLAUDE.md` — dwv (different org) repos
- `~/Workspace/intake/*/CLAUDE.md` — intake staging
- `~/Workspace/k6-contrib/` — external k6 contrib
- `~/Workspace/python-sdk/` — external Python SDK
- `~/Workspace/fastmcp/` — external FastMCP

**Vendor/external (should NOT sync):**
- `organvm-iv-taxis/contrib--temporal-sdk-python/CLAUDE.md`
- `organvm-iv-taxis/contrib--jairus-dagster-sdlc/CLAUDE.md`
- `organvm-iv-taxis/contrib--indeedeng-iwf/CLAUDE.md`
- `organvm-iv-taxis/reverse-engine-recursive-run/CLAUDE.md`

**Nested docs (not repo roots):**
- `organvm-i-theoria/.github/docs/CLAUDE.md`
- `organvm-i-theoria/.github/docs/guides/CLAUDE.md`
- `organvm-i-theoria/.github/.ai/CLAUDE.md`
- `organvm-iv-taxis/.github/CLAUDE.md` (this IS synced, just nested)

---

## Known Unmanaged (Quick Inventory)

### Vendor/External Clones
- `/Users/4jp/Workspace/k6-contrib/CLAUDE.md`
- `/Users/4jp/Workspace/python-sdk/CLAUDE.md`
- `/Users/4jp/Workspace/fastmcp/CLAUDE.md`

### Contrib Folders (organvm-iv-taxis)
- `contrib--temporal-sdk-python/CLAUDE.md`
- `contrib--jairus-dagster-sdlc/CLAUDE.md`
- `contrib--indeedeng-iwf/CLAUDE.md`
- `reverse-engine-recursive-run/CLAUDE.md`

### Nested Documentation
- `.github/docs/CLAUDE.md`
- `.github/docs/guides/CLAUDE.md`
- `.github/.ai/CLAUDE.md`

### Non-ORGANVM Roots
- `/Users/4jp/Workspace/dwv/*/CLAUDE.md`
- `/Users/4jp/Workspace/intake/*/CLAUDE.md`
- `/Users/4jp/Workspace/4444J99/*/CLAUDE.md`

---

## Disposition Rules

1. **ORGANS in `~/Workspace/meta-organvm`**: Should be managed — these are the ~14 submodules already committed.
2. **ORGANS in other superprojects** (e.g., `organvm-iv-taxis`): Should be managed in their respective superproject context.
3. **Vendor clones under `contrib--*`**: Intentional external — should NOT be managed by ORGANVM context sync.
4. **Personal/non-organ workspaces**: Out of scope.
5. **Nested docs** (`.github/docs`, `.github/.ai`): Documentation artifacts, not repo roots.

---

## Next Steps

For any file that should be managed but isn't:
- Identify the correct superproject/home organ
- Add to that organ's context sync registry
- Run `organvm context sync --write`

*Classification complete. This audit prevents treating all unmanaged files as equivalent failures.*