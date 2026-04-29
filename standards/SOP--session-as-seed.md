# SOP: Session-as-Seed (The Black-Hole Geometry of Sessions)

**Version:** 1.0.0 | **Date:** April 29, 2026 | **Status:** Active
**Scope:** Operating-model law for how sessions open, what gets planted at session-start, and how the planted element grows by external agents — not by the planter.

---

## 1. Ontological Purpose

A session is a **black hole**: an opened space in time with a singularity at its center. The conductor (human at meta/maestro level, optionally Claude as relay) plants an element at the singularity. **The planted element does not require thinking or planning to plant.** It is a *named vacuum with gravity* — an absence that has been given coordinates so that agents of differing dispositions (good-hearted, negatively-hearted, code-purposed, research-purposed, content-purposed) are pulled toward it.

The black hole **invents what attracts those who want to study a place of emptiness.** The seed is not a structure with prescribed fill. It is the structure *of an absence*. External agents (Codex, Gemini, OpenCode, Perplexity) form the accretion disk; their differing-purpose gravity is what builds out the planted idea.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster: Operations)

The core risk: **filling the void during planting collapses the geometry.** A seed that is pre-specified by Claude becomes a Claude-shaped object — gravity dies, peer agents have no room to grow into it, and the session degrades into a single-agent execution pretending to be orchestration.

---

## 2. The Four Sources of Gravity

A vacuum pulls only when it has been structurally constituted. The four required sources:

1. **Named identity.** The vacuum has coordinates: a name, an IRF entry, atomized scope. An unnamed vacuum is just silence — silence has no gravity. Per `feedback_na_is_vacuum.md`, every named absence becomes an imperative.
2. **Locked constraints + locked files + conventions.** Reuse the existing `GuardrailedHandoffBrief` fields: `constraints_locked`, `files_locked`, `conventions`. These define the *shape* of the void, not its fill. They are the event horizon — what the gravity well will not let through.
3. **Zero proposed fill.** The seed contains no implementation language. No "implement X", "build Y", "create Z" verbs in the planted intent. Declarative naming of the absence only. **Thinking fills the void; planning predicts the fill — both kill gravity.**
4. **Signal-closure entailment.** Per `feedback_signal_closure_law.md`, the absence points at what the system logically *requires* but has not yet produced. The `entailment_flows` matrix in `governance-rules.json` is read to populate this. Gravity is proportional to how clearly the absence is entailed.

A seed missing any of the four does not pull. It is not a black hole — it is a hole.

---

## 3. Phase Cycling Between Agents (the re-emptying ritual)

The differing-purpose phasing is load-bearing: **whoever does the code is different from whoever does the research is different from whoever does the content is different from whoever does the infrastructure.** Between each agent's pass, **space must phase in and out** — a re-emptying that restores the vacuum so the next agent inherits a void, not a partial fill.

The cycle:

1. Agent N (work-type X) is dispatched against the seed via `conductor_fleet_guardrailed_handoff`.
2. Agent N returns. Run `conductor_fleet_cross_verify(changed_files)` — verifies the locked constraints/files/conventions held.
3. **Run `conductor_seed_re_plant(envelope_id)`** — the new ritual:
   - Appends a *Vacuum Restore Point* timestamp to the envelope.
   - Archives Agent N's growth signals under a phase header (immutable; never overwritten).
   - Clears filling-pressure: anything Agent N introduced beyond the original `constraints_locked` is examined; if it's drift, it's reverted; if it's a new constraint the conductor accepts, it's added to the locked set explicitly.
   - Re-renders `active-handoff.md` with the restored vacuum.
4. Only then does Agent N+1 (work-type Y, different cognitive class) approach.

**Without the re-plant step**, Agent N+1 inherits Agent N's partial fill. Y-purposed gravity is absorbed into X-shaped accretion, and the differing-purpose phasing collapses. The session becomes one agent in costume, not many agents in cycle.

---

## 4. Conductor Roles

- **Human conductor** (primary planter): plants seeds, names vacuums, holds the gravity well open across phases. The only role that creates seeds without delegation.
- **Claude as relay** (when explicitly delegated by the conductor): maintains the void's emptiness during growth. **Refreshes `active-handoff.md` live, not at close.** Never fills on the conductor's behalf. Runs `conductor_seed_re_plant` at every phase transition. Treats the envelope as a peer's *read* surface, not Claude's *publication* channel.
- **External agents** (Codex/Gemini/OpenCode/Perplexity, or Claude when assigned a single work-type within a cycle): the accretion mass. Each brings differing-purpose gravity. Each operates within the locked constraints. None of them re-plant — only the relay re-plants between their passes.

The conductor principle (`feedback_conductor_principle.md`) governs the boundary: the human directs vision; the system (Claude as relay + external agents) executes everything else. Re-planting is system work. Vision is conductor work.

---

## 5. Anti-Patterns

These collapse the geometry:

- **Pre-filling the seed before planting.** Implementation language in the planted intent, scaffolding code, "starter" files, suggested approaches. The micro-manager tell.
- **Tombstone envelopes.** Single end-of-session update. The envelope reads as past tense, not present tense. Peer agents checking it mid-session see a graveyard, not a relay surface.
- **Single-agent fill.** One agent does code AND research AND content. The differing-purpose phasing collapses; gravity flattens to one direction.
- **Unnamed vacuums.** Absence without coordinates. Cannot be checked, verified, or grown. Equivalent to silence.
- **Filling-pressure leakage between phases.** Re-plant skipped. Agent N+1 inherits Agent N's partial fill. Drift compounds across the cycle.
- **Conductor-as-filler drift.** The conductor (human or Claude-as-relay) starts proposing implementation while planting. Authority bleeds into execution; the gravity well becomes a Claude-shaped object.

---

## 6. Verification — The Peer-Readability Test

The operational gate at every phase transition. One question:

> **If a peer agent checked `.conductor/active-handoff.md` right now — not at session close, *right now* — would they see current state or a tombstone?**

- Current state → team-player posture. Geometry is holding. Continue.
- Tombstone → micro-manager posture. Gravity is leaking. The seed has been pre-filled, the envelope has not been refreshed live, or the re-plant ritual was skipped. Course-correct before dispatching the next agent.

This test is not optional and does not need ceremony. It is one read, one check, every phase transition.

---

## 7. Threshold for Application

Not every session opens a black hole. Trivial sessions (typo fixes, single-line changes, single-cognitive-class work where one agent is the right and only mass) skip seed-planting. **The threshold:** any session that involves more than one cognitive class — code + research, code + content, audit + implementation, etc. — must use the seed model. A multi-phase session without seed-planting is a structural error.

---

## 8. Cross-References

- `feedback_conductor_principle.md` — the boundary between conductor (vision) and system (execution)
- `feedback_seed_not_specification.md` — minimal generative structure principle
- `feedback_signal_closure_law.md` — entailment_flows as the fourth source of gravity
- `feedback_part_of_creation.md` — Claude as participant, not consultant
- `feedback_plans_are_artifacts.md` — envelopes must be committed and pushed; never local-only
- `feedback_na_is_vacuum.md` — N/A as imperative; named absence as gravity source
- `SOP--cross-agent-handoff.md` — sibling SOP; governs reception and reconciliation of returned work
- `SOP--multi-agent-swarm-orchestration.md` — sibling SOP; governs concurrent agent topology
- `governance-rules.json` (`entailment_flows` matrix) — read by `conductor_seed_plant` to populate signal entailments
- `conductor.fleet_handoff.GuardrailedHandoffBrief` — base dataclass extended by `SeedEnvelope`
- `conductor.fleet_handoff.format_markdown` — base renderer extended for seed-specific sections
- `conductor.fleet_handoff.write_active_handoff` — canonical envelope write path
- `conductor_fleet_cross_verify` — runs as the first half of `conductor_seed_re_plant`

---

## 9. Constraints (Hard)

- **No LaunchAgents, plists, or scheduled daemons.** Per `feedback_no_launchagents.md`, every primitive in this protocol is invoked on-demand. `conductor_seed_plant` and `conductor_seed_re_plant` are MCP tools called by an active session, never background-scheduled. Re-planting is a session event, not a timer event.
- **Envelopes commit and push.** Per `feedback_plans_are_artifacts.md` and `feedback_nothing_local_only.md`, every plant and re-plant writes to `.conductor/active-handoff.md` *and* commits + pushes. Local-only envelopes are invisible to peers and lost on disk failure.
- **Vacuum Restore Points are append-only.** The re-plant log is never overwritten. Restore Points archive growth signals from prior phases under immutable phase headers — versioning, not mutation.

---

## 10. Versioning

This SOP follows ORGANVM versioning rules. Revisions are never overwritten; new versions are created with incremented version numbers. The original is moved to `archive/YYYY-MM/`.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
