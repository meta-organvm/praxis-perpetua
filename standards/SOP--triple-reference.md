---
sop: true
name: triple-reference
scope: system
phase: governance
irf: IRF-SYS-078
github: meta-organvm/organvm-corpvs-testamentvm#303
---

# SOP: Triple Reference Principle

## Rule

Every referenceable item must exist in exactly three locations simultaneously:

1. **IRF** — entry in `INST-INDEX-RERUM-FACIENDARUM.md` with a unique IRF-XXX-NNN ID
2. **Repo** — tracked reference in the repository where the work lives (seed.yaml, README, CLAUDE.md, SOP, inline code comment, or governance-rules.json)
3. **GitHub Issue** — actionable ticket on the relevant repository

## Why

Identity is composite, not assigned. The IRF ID is not a label stamped onto an item and then propagated. It is the convergence artifact — assembled from the three locations coming together as that thing.

Like a triangulation fix: no single station gives position. The position IS the intersection. The unique ID emerges from the fact of being referenced in three distinct places.

- **1 location** = whisper. Invisible to the system. Dies with its host.
- **2 locations** = echo. One can drift without detection.
- **3 locations** = heartbeat. Each validates the other two.

## When to Apply

- **Creating work items**: When logging new work, ensure all three legs exist before declaring the item "logged."
- **Closing sessions**: The Close Protocol (12-step) includes triple-reference verification at step 7 (index propagation).
- **Auditing**: Any item existing in fewer than three locations is ontologically incomplete — not merely under-documented, but lacking full identity.

## Procedure

### On Creation

1. Write the IRF entry with the next available ID in the appropriate domain section
2. Create a GitHub issue on the target repo, referencing the IRF ID in the title or body
3. Add a repo-level reference (SOP, seed.yaml, CLAUDE.md, or code comment) pointing to both IRF and issue

### On Completion

1. Mark the IRF entry as DONE with completion date and session tag
2. Close the GitHub issue with a reference to the completing commit
3. Update the repo reference to reflect completion (or remove if no longer applicable)

### On Audit

For each IRF item, verify:
- Does the GitHub issue exist and reference the IRF ID?
- Does the repo contain a reference to the IRF ID or the issue?
- If any leg is missing, flag as ontologically incomplete

## Exceptions

- **Decision items** (naming choices, architecture decisions) may omit the GitHub issue if no code action is required. They still need IRF + repo reference (2 of 3).
- **Completed items** in the DONE section need not maintain live GitHub issues — the closed issue satisfies the third leg.

## Related

- Close Protocol: `feedback_close_protocol.md` (step 7)
- IRF-SYS-077: IRF↔GitHub bidirectional sync (automates leg 2↔3)
- Issue #74 (a-organvm): Claude memory local-only parity gap (the memory substrate itself violates 1:1 parity)
