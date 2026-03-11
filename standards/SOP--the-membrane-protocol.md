---
sop: true
name: the-membrane-protocol
scope: system
phase: any
triggers:
  - context:repo-creation
  - context:incubation-end
  - context:project-review
complements:
  - genesis-dna
  - promotion-and-state-transitions
overrides: null
---
# SOP: The Membrane Protocol — Graduating from Chaos to Logic

## 1. Ontological Purpose

This SOP governs the "Phase 0" lifecycle of experimental projects and their graduation into the formal ORGANVM system. It protects the Bauhaus spirit of "sanctioned chaos" while ensuring that only structurally sound components enter the active production Organs (I–VII). 

The "Membrane" is a semi-permeable boundary. It allows raw creative nutrients to pass through only after they have been formalized into a structure the system can safely consume. This prevents "vacuous truths" and system-wide failures caused by unverified, chaotic scripts.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 3: Governance & Lifecycle)
**Cross-reference:** `SOP--genesis-dna.md` (initial structure), `SOP--promotion-and-state-transitions.md` (graduation to LOCAL), `governance-rules.json` (DAG constraints).

---

## 2. Phase 0: The Spike (Sanctioned Chaos)

A "Spike" is a dedicated experimental phase where formal engineering rules are suspended to allow for blind discovery and messy experimentation.

### Rules of the Lab (Theoria & Poiesis)
- **Chaos is Allowed:** Messy code, unnamed variables, and missing tests are permitted.
- **Boundaries:** Spike code is **prohibited** from touching `Ergon` (III), `Taxis` (IV), or `Kerygma` (VII). It is strictly for internal discovery.
- **Location:** Spikes live in the `Liminal Incubation Zone` (Personal Profile / @4444J99) or as `LOCAL` repos in `Theoria` (I) or `Poiesis` (II).

---

## 3. The 3-Step Membrane Checklist

Before an experiment can graduate out of the Incubator and into the active pipeline, it must pass these three tests.

### Step 1: The Epistemic Boundary (Schema Definition)
The project's inputs and outputs must be formally defined so the rest of the organism can understand it.
- **Requirement:** Create a strict JSON Schema or YAML configuration defining the shape of the project's output.
- **Invariant:** "This tool will output [Shape X] with [Constraints Y]."

### Step 2: The Directed Graph Placement (DAG Check)
The project must submit to the unidirectional flow of the system (Theory $\rightarrow$ Art $\rightarrow$ Commerce $\rightarrow$ Distribution).
- **Requirement:** Explicitly define upstream parents and downstream children in `seed.yaml` and `registry-v2.json`.
- **Constraint:** No circular loops. A tool cannot consume from an organ it feeds.

### Step 3: The Neurological Handshake (Interface Contract)
The project must be connected to the system's nervous system (Taxis or meta-engine).
- **Requirement:** Establish the Cryptographic Contract or Interface definition.
- **Artifacts:** Define Webhook signatures (with HMAC/Idempotency) or an MCP Tool JSON schema so AI agents know how to operate the component.

---

## 4. The 14-Day TTL (Temporal Degradation)

The Incubator is for hatching, not permanent residence. To prevent "procrastinating iterational masochism" (endless gold-plating), all Incubator projects are subject to a **14-day Time-To-Live (TTL)**.

### TTL Protocol
1. **Clock Start:** The timer begins the moment a repository is created or a Spike is declared.
2. **Day 14 Decision:** At the end of 14 days, the project must:
   - **Graduate:** Pass the 3-step Membrane Checklist and move to an active Organ.
   - **Archive:** Accept it as a completed experiment and move to `archive` status.
3. **No Third Option:** Tweak-locking beyond Day 14 is a violation of system discipline.

---

## 5. Pre-Phase Validation Tests

Use these tests to break through "iteration masochism" before graduation:

- **The Utility Invariant:** If a hardcoded version of the current output is accepted by a downstream organ, **stop iterating.** The payload is valid; formalize it.
- **Ockham's Check:** For every "cool feature" added during the Spike, ask: *"Am I willing to write the formal logic and tests for this?"* If not, **delete the feature.**

---

## 6. Output Artifacts

- **Graduation Issue:** A GitHub issue documenting the Membrane Checklist pass.
- **Formal Schema:** `schema.json` or equivalent in the repo.
- **Updated seed.yaml:** Declaring formal edges and status.
- **Registry Update:** Repository moved from Personal/Incubator to Organ I, II, or III.

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
