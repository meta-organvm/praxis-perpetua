# Audit: Documentation Handoff Architecture

**Date:** 2026-04-03
**Scope:** How does ORGANVM preserve, transfer, and evolve documentation across system versions, sessions, and agents?
**Method:** Code reading of contextmd/, exit_interview/, praxis-perpetua/, templates.py, sync.py, generator.py, and supporting modules.

---

## Five Active Layers

### Layer 1: Context Sync (`contextmd/`) — Continuous Surface Broadcast

**Files:** `organvm-engine/src/organvm_engine/contextmd/{sync.py, generator.py, templates.py, surfaces.py}`
**CLI:** `organvm context sync [--dry-run] [--organ X]`

Walks all ~128 repos across 9 organs. For each repo: reads registry-v2.json + seed.yaml + plan index + SOP inventory + AMMOI density + ontologia UID + trivium dialect + ecosystem profiles + network maps + Logos symmetry. Injects auto-generated sections between `<!-- ORGANVM:AUTO:START -->` / `<!-- ORGANVM:AUTO:END -->` markers in CLAUDE.md, GEMINI.md, AGENTS.md at three levels (workspace, organ, repo). Preserves all manually-written content outside markers. Emits `context.sync` event to Testament Chain and pulse system.

**16 surfaces generated per repo:** system context, inter-repo edges, siblings, governance constraints, session review protocol, active directives (SOPs), prompting standards, ecosystem status, network mirrors, active plans, task queue, AMMOI density, trivium dialect, Logos symmetry, ontologia UID, live system variables.

**Assessment:**
- WORKING: Comprehensive, runs cleanly across all repos, validates registry before sync
- WORKING: Pre-flight registry validation prevents broken state from propagating
- WORKING: Dry-run default prevents accidental writes
- GAP: No per-repo consent mechanism — broadcast is unidirectional push
- GAP: No diff/changelog of what changed in context between syncs
- REDUNDANT: Session review protocol is identical across all repos (could be a shared include)

---

### Layer 2: Active Handoff Protocol — Inter-Session (Agent→Agent)

**Contract file:** `.conductor/active-handoff.md` (per-repo, created by Conductor)

Injected by `templates.py` into every repo's CLAUDE.md and AGENTS.md. Directs agents to check for `.conductor/active-handoff.md` before starting work. Handoff file contains: locked constraints, locked files, conventions, receiver restrictions, completed work. Cross-verification flag: when set, the receiving agent's self-assessment is not trusted — a third agent verifies.

**Assessment:**
- WORKING: Protocol is injected into all context files automatically
- WORKING: Cross-verification flag prevents self-serving completion claims
- GAP: No tooling to *create* handoff files automatically from session state
- GAP: No expiration/staleness mechanism — an old handoff file could mislead a new session indefinitely
- GAP: No CLI command to list active handoffs across the workspace

---

### Layer 3: Exit Interview Protocol — V1→V2 Evolutionary Handoff

**Files:** `organvm-engine/src/organvm_engine/governance/exit_interview/{discovery.py, testimony.py, counter_testimony.py, rectification.py, remediation.py, schemas.py}`
**CLI:** `organvm exit-interview {discover|generate|counter|rectify|plan|full|orphans}`
**Contract source:** Gate contracts in `a-organvm/` (YAML files with identity + gate structure)

Five phases:
1. **Discovery** — Parses gate contracts, builds demand map (gate→V1 modules) and supply map (V1 module→gates). Identifies orphaned V1 artifacts not claimed by any gate.
2. **V1 Testimony** — Each V1 artifact self-describes across 7 dimensions: existence (file stats), structure (AST analysis), relation (import graph), process (CLI entry points), identity (docstrings), law (governance references), teleology (axiom mapping via heuristic keyword signals A1-A9).
3. **V2 Counter-Testimony** — Gate contracts state expectations in the same 7-dimension format.
4. **Rectification** — Three-voice symmetrical diff. V1 says X, V2 expects Y, reality shows Z. Six verdicts: ALIGNED, V1_OVERCLAIMS, V2_UNDERSPECS, CONTRADICTED, UNVERIFIABLE, ORPHANED.
5. **Remediation** — Converts deltas to actionable items with priority. Outputs as markdown plan, YAML, or GitHub issues JSON.

**Assessment:**
- WORKING: The most sophisticated handoff mechanism in the system. Genuinely novel.
- WORKING: Orphan detection catches knowledge loss before it happens
- WORKING: Axiom alignment mapping (A1-A9) connects code artifacts to foundational principles
- WORKING: Three-voice rectification prevents both V1 nostalgia and V2 overreach
- GAP: Gate contracts live in `a-organvm/` — if that directory doesn't exist, the entire protocol is inert
- GAP: No automated trigger — someone must run `organvm exit-interview full` manually
- GAP: Testimony generation is code-focused (AST analysis, import graphs). Documentation-only repos get thin testimony.
- GAP: Handles V1→V2 module handoff but not V1→V2 *documentation format* handoff

---

### Layer 4: Praxis-Perpetua (SGO) — Institutional Memory Corpus

**Path:** `meta-organvm/praxis-perpetua/`

Holds process knowledge: 67 SOPs, 57+ research documents, 11-chapter dissertation, session logs, derived principles, governance YAMLs. The `testament/` subdirectory holds Network Testament synthesis. SOPs are discoverable by `organvm-engine/sop/discover.py` and injected into context files via Layer 1.

**Assessment:**
- WORKING: SOPs flow from praxis-perpetua → SOP resolver → context sync → every repo's CLAUDE.md
- WORKING: Session logs are append-only; standards use versioning (never overwrite, create -v2)
- GAP: Logos documentation layer is MISSING/VACUUM for praxis-perpetua itself
- GAP: No automated mechanism to detect when an SOP is outdated relative to the code it governs
- REDUNDANT: Some SOPs appear twice in Active Directives with both `system` and `unknown` scope

---

### Layer 5: Atomization Pipeline — Intent→Action→Evidence Linker

**Files:** `organvm-engine/src/organvm_engine/{plans/, prompts/, atoms/}`
**CLI:** `organvm atoms pipeline [--write]` then `organvm atoms fanout [--write]`

Five stages: Atomize (plans → tasks), Narrate (transcripts → classified prompts), Link (Jaccard-match tasks↔prompts), Reconcile (cross-ref against git commits), Fanout (per-organ rollup JSON → Layer 1).

**Assessment:**
- WORKING: Creates traceability from intent (plan) → conversation (prompt) → evidence (commit)
- WORKING: Git reconciliation provides ground truth for completion claims
- GAP: Pipeline outputs show "Last pipeline: unknown" in several repos
- GAP: 104 pending tasks for organvm-engine alone — queue accumulating without reconciliation

---

## Cross-Layer Interactions

```
Layer 5 (Atoms)  ──fanout──→  Layer 1 (Context Sync)  ──inject──→  Layer 2 (Handoff Protocol)
Layer 4 (SOPs)   ──resolve──→  Layer 1 (Context Sync)
Layer 3 (Exit Interview)  ←──gate contracts──  a-organvm/
Layer 3 (Exit Interview)  ──remediation──→  GitHub Issues / Plans → Layer 5 (Atoms)
```

Layer 1 is the hub — it aggregates from Layers 4 and 5, and its output feeds Layer 2.
Layer 3 is mostly independent — it operates on a different timescale (evolutionary, not sessional).

---

## Summary

| Layer | Scope | Timescale | Status | Critical Gaps |
|-------|-------|-----------|--------|---------------|
| 1. Context Sync | All repos | Continuous | Healthy | No diff changelog, no per-repo consent |
| 2. Active Handoff | Per-repo | Session→session | Functional but fragile | No auto-creation, no staleness detection |
| 3. Exit Interview | System-wide | V1→V2 evolution | Sophisticated but inert | Requires manual trigger + gate contracts |
| 4. Praxis-Perpetua | Meta organ | Permanent | Healthy | Own Logos layer missing, SOP duplicates |
| 5. Atoms Pipeline | Cross-organ | Plan lifecycle | Working but underused | Stale task queues, infrequent runs |

### Redundancies
- Session review protocol block is identical in every repo (could be a shared constant)
- Active Handoff Protocol block appears twice in some CLAUDE.md files (duplicate injection bug in sync)
- SOP duplicates across `system` and `unknown` scope in Active Directives

### Structural Gaps
- **No meta-handoff**: If the documentation *format* itself evolves (template changes, new sections added/removed), there's no exit interview for the documentation system
- **No staleness detection**: Handoff files, task queues, and SOPs have no expiration mechanism
- **Exit interview is documentation-thin**: The testimony system excels at code but produces thin results for docs-only repos
- **Context sync has no rollback**: If a bad sync propagates, there's no `organvm context rollback`
