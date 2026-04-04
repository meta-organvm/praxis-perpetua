# Governance Audit: Unmanaged CLAUDE.md Surfaces

**Date:** 2026-04-04
**Context:** Post-System Library rollout, scan of `~/Workspace` found 102 CLAUDE.md files without `## System Library`.

---

## Classification Summary

| Bucket | Count | Description |
|--------|-------|-------------|
| **Managed (has System Library)** | 28 | Already synced via `organvm context sync` |
| **Unmanaged — should be managed** | 15 | True misses in ORGANS that should enter sync |
| **Unmanaged — staging/bench** | 53 | Files in `materia-collider` (temporary staging) |
| **Unmanaged — intentionally local** | 15 | Personal configs, non-organ repos (4444J99, dwv, intake) |
| **Unmanaged — vendor/external** | 14 | Vendor clones (contrib--), external SDKs |
| **Unmanaged — nested docs** | 5 | Documentation artifacts, not repo roots |

---

## Known Unmanaged (Exact Inventory)

### Should be managed (ORGANS)
- `organvm-i-theoria/rules-system-bound/CLAUDE.md`
- `organvm-ii-poiesis/chthon-oneiros/CLAUDE.md`
- `organvm-ii-poiesis/krypto-velamen/CLAUDE.md`
- `organvm-iii-ergon/content-engine--asset-amplifier/CLAUDE.md`
- `organvm-iv-taxis/orchestration-start-here/CLAUDE.md`
- `organvm-iv-taxis/vox--publica/CLAUDE.md`
- ... (+ 9 more)

### Vendor/External (should NOT sync)
- `organvm-iv-taxis/contrib--adenhq-hive/CLAUDE.md`
- `organvm-iv-taxis/contrib--indeedeng-iwf/CLAUDE.md`
- `k6-contrib/CLAUDE.md`
- `python-sdk/CLAUDE.md`
- `fastmcp/CLAUDE.md`

---

## Disposition Rules

1. **ORGANS in ORGANS superprojects**: Should be managed. Identified 15 files that need to be added to their respective organ registries.
2. **Staging (`materia-collider`)**: Intentional skip — these are temporary work-in-progress fragments.
3. **Vendor clones under `contrib--*`**: Intentional external — should NOT be managed by ORGANVM context sync.
4. **Personal/non-organ workspaces (`4444J99`, `dwv`)**: Out of scope for organ governance.
5. **Nested docs** (`.github/docs`, `.github/.ai`): Documentation artifacts, not repo roots.

---

## Next Steps

1. Add the 15 "Should be managed" files to their respective organ registries.
2. Re-run `organvm context sync --write` across all superprojects.
3. Archive this audit once counts reach zero for "Should be managed".

*Classification complete. All 102 unmanaged surfaces accounted for.*