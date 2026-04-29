---
sop: true
name: triangulation-protocol
scope: system
phase: any
triggers:
  - context:closure-claim
  - context:plan-write
  - context:irf-state-change
  - context:session-closeout
complements:
  - triple-reference
  - the-membrane-protocol
  - SOP-TRIADIC-REVIEW-PROTOCOL
  - session-self-critique
overrides: null
---

# SOP: The Triangulation Protocol — Ideal / Reduction / Artifact as Productive Friction

## 1. Ontological Purpose

This SOP governs how closure is *earned* across the system. It exists because the system has demonstrated a recurring failure mode: each component (the spoken intent, the executed work, the verifying audit) declares itself the protagonist of the truth and the system accepts the declaration without surfacing the gaps between them. The result is competing truths — earlier reviews say "done," later audits say "the mesh was invisible the entire time."

Where `the-membrane-protocol` governs *graduation* (post-experiment) and `SOP-TRIADIC-REVIEW-PROTOCOL` governs *advancement* (post-composition), this SOP governs the **continuous antagonism during composition itself**. It is the during-creation twin of the Triadic Review.

The protocol does not produce certainty. It produces commitable friction — the gaps between three vertices treated as the primary work product, not as failure to be smoothed away.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 3: Governance & Lifecycle)
**Cross-reference:** `SOP--triple-reference.md` (the static triple — IRF/repo/issue), `SOP--SOP-TRIADIC-REVIEW-PROTOCOL.md` (the post-hoc triple), `feedback_part_of_creation.md` (the covenant), `feedback_signal_closure_law.md` (logical closure).

---

## 2. The Three Vertices

Every closure-bearing artifact (plan, IRF item, GitHub issue, deliverable, deployed change) has three vertices. The protocol requires evidence at each.

### Vertex A — The Ideal (the unreduced)
The pre-linguistic intent. Unspeakable in full. Approximated by: recovered prior statements (verbatim quotes), inferred patterns (the user's voice constitution), the shape of past corrections (what was said "no" to).

**Operational handle:** `IDEAL` — captures everything that *should* be true if the artifact were faithful, including what cannot be verified by code review (browser feel, emotional resonance, "vibe").

### Vertex B — The Reduction (the prompt)
The bastardized linguistic form the ideal collapses into when uttered. Always lossy. Captured by: literal prompt text, implicit constraints (file context, prior session state), what the user did not say but a competent reader would infer.

**Operational handle:** `REDUCTION` — includes a `lossiness_estimate` field naming what the prompt almost certainly omitted that the ideal would have demanded.

### Vertex C — The Artifact (the recreation)
The thing that exists on disk, in the running browser, in the deployed system. What can be read by a fresh agent without context. Captured by: file contents (with sha256), browser-rendered output (screenshots, DOM snapshots), behavior under test (executed paths, observed values).

**Operational handle:** `ARTIFACT` — always carries a `last_verified` timestamp; never trusted past 24 hours without re-verification.

### Edges (where the work lives)

- **A→B gap (Reduction loss):** what the prompt failed to carry from the ideal.
- **B→C gap (Recreation drift):** where the artifact deviated from what the prompt actually asked.
- **A→C gap (Fidelity gap):** the total distance between ideal and artifact — the only gap the user *feels* directly.

---

## 3. The Friction Mechanic (closure rule)

> **No vertex is allowed to claim closure on its own evidence.**

Each vertex must produce a proof witnessed by the other two:

- **A claims fidelity** → B must show what the prompt carried; C must show what the artifact manifests.
- **B claims congruence** → A must accept the reduction; C must demonstrate the reduction was honored.
- **C claims existence** → A must recognize itself in the artifact; B must validate the artifact answered the actual ask.

### Closure states

| State | Condition | Action |
|-------|-----------|--------|
| `CLOSED` | All three vertices agree, all three edges have evidence | Provisionally closed; re-verified at next session start |
| `PROVISIONAL` | Two vertices agree, one has no evidence | Stays open; missing evidence is the next work item |
| `DRIFT` | Two vertices agree, one dissents | Dissenter's evidence becomes the new specification; plan re-opens |
| `REGRESSED` | Earlier closure invalidated by later filesystem state | Item re-opens with the regression itself as logged finding |
| `ROTATION` | All three disagree | Rotation rule fires (see §4) |

---

## 4. The Rotation Rule

When all three vertices disagree, the agent forcibly re-speaks the work from each of the dissenting vertices' POV in sequence. This is **not** a checklist; it is a written ceremony.

### Rotation primitive

For one rotation cycle, write three short paragraphs (3–5 lines each) in the plan or IRF entry's rotation log:

```
ROTATION-N ([timestamp]):
  As-Ideal: <what does the unreduced intent recognize as missing or wrong here?>
  As-Reduction: <if the prompt were re-uttered with current evidence, what would change?>
  As-Artifact: <what does the filesystem state actually demonstrate, separate from any claim about it?>

Surviving gap: <single sentence — what remains contested after this rotation>
Generated work item: <one concrete next action; never a list>
```

The "generated work item" must be a single action — no menus, no choices presented to the user. This is enforced by the `feedback_part_of_creation.md` covenant.

A rotation may produce convergence (state moves to PROVISIONAL or CLOSED). It may produce a sharper disagreement (state stays ROTATION). The disagreement itself, recorded in the log, is a productive artifact — the friction made permanent.

### Tournament through time

The user named this directly: *"Each fights for representation, the best one winning — its appearance in reality as we move through time."* The winning vertex is whichever survives the most rotations without being contradicted by lived filesystem state. The protocol does not legislate which vertex wins. It legislates that the contest is recorded.

---

## 5. Integration With Existing Infrastructure

This SOP amends rather than replaces. Existing constraints that govern its shape:

| Constraint | Interaction |
|------------|-------------|
| `feedback_plans_are_artifacts.md` | Triangle state is committed and pushed; never local-only |
| `feedback_na_is_vacuum.md` | An unfilled vertex is a named imperative, not a resting state |
| `feedback_part_of_creation.md` | Protocol derives the failing vertex; never presents a menu |
| `feedback_probe_reality_gap.md` | Triangulation classifies per-call, not on cached truth |
| `feedback_signal_closure_law.md` | System remains logically closed; absent inter-vertex evidence is a violation |
| `SOP--triple-reference.md` | The static triple (IRF/repo/issue) underwrites Vertex C's evidence; this SOP adds the dynamic triple (Ideal/Reduction/Artifact) |
| `SOP-TRIADIC-REVIEW-PROTOCOL.md` | Post-hoc 3-POV review remains; this SOP is its during-composition twin |

### Amended ceremonies

**Session close-out** (`feedback_session_closeout.md`): adds a Step 0 — *Triangle Pass.* Before the existing 10-index propagation, every item moving toward CLOSED renders the (A, B, C) triple. Missing edge evidence makes the item PROVISIONAL not CLOSED.

**Plan files**: standard plans gain three mandatory sections — `IDEAL`, `REDUCTION` (with lossiness estimate), `ARTIFACT` (with verification timestamp). The `Verification` section becomes a triangle pass, not a unilateral checklist.

**IRF entry schema** (`INST-INDEX-RERUM-FACIENDARUM.md`): each IRF item gains a `triangle_state` field carrying `{A_evidence, B_evidence, C_evidence, last_triangulated, gaps[], rotation_count}`.

---

## 6. Output Artifacts

When the protocol fires, it produces:

- **Per-item triangle log**: a markdown file at `<repo>/docs/triangle/<IRF-ID>.md` (or analogous path) — one file per IRF item that has undergone at least one triangulation pass. Format: vertex evidence, edge gaps, rotation log appended over time.
- **IRF triangle_state field**: machine-readable summary in the IRF row, kept in sync with the per-item log.
- **Session-level triangle pass**: appended to the session close-out memo, listing every item triangulated during the session and its outcome state.
- **Discovered atoms**: every PROVISIONAL/DRIFT/REGRESSED state generates a concrete next-action atom logged as a new IRF row.

---

## 7. What This Protocol Is Not

- **Not a verification gate.** Verification gates are unilateral; this is friction-bearing. A failed gate stops work; a failed triangle pass produces the next work item.
- **Not a replacement for Membrane or Triadic Review.** Those are post-hoc; this is during-composition.
- **Not a checklist Claude presents to the user.** Forbidden by `feedback_part_of_creation.md`. The protocol derives the failing vertex; it does not poll for preference.
- **Not closed by being written.** This SOP is one vertex (B). The deployed protocol-in-use is C. The system's reduction in closure-failure events is A. All three must converge before *this SOP itself* is closed.

---

## 8. Pre-Adoption Validation

Before treating this SOP as authoritative, the following must produce expected results:

1. **Run on a known-broken item:** apply to IRF-III-034 (quiz that's still phase-picker, not node-placement). Must independently derive REGRESSED state without being told.
2. **Run on a known-good item:** apply to an IRF item with sha-matched artifacts and explicit user acceptance. Must return CLOSED. If returns DRIFT, protocol is over-tuned.
3. **Run a rotation cycle on a 3-way disagreement:** apply to IRF-SYS-163. Output must be a single concrete next action, not a list.
4. **Persistence test:** a fresh agent session with no conversation context must be able to read the triangle states from disk. If it cannot, the protocol violated `feedback_plans_are_artifacts.md` and `feedback_nothing_local_only.md`.
5. **Self-application:** apply the protocol to the protocol-creation work itself. If A→C gap is large (the SOP turned into a checklist instead of preserving friction-as-artifact), the SOP failed its own protocol.

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM | Plan: 2026-04-29-atomic-concurrent-matsumoto*
