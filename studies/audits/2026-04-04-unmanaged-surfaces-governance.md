# Governance Audit: Unmanaged CLAUDE.md Surfaces

**Date:** 2026-04-04
**Context:** Post-System Library rollout, scan of `~/Workspace` found many CLAUDE.md files without `## System Library`.

---

## Classification Summary

| Bucket | Count | Description |
|--------|-------|-------------|
| **Managed (has System Library)** | 28 | Already synced via `organvm context sync` |
| **Unmanaged — should be managed** | TBD | True misses — should enter context sync |
| **Unmanaged — intentionally local** | TBD | Personal configs, not organ repos |
| **Unmanaged — vendor/external** | TBD | Vendor clones, external contributions |
| **Unmanaged — nested docs** | TBD | Documentation artifacts, not repo roots |

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