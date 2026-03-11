# SOP: Multi-Agent Swarm Orchestration (The Polymorphic Swarm)

## 1. Ontological Purpose
This SOP governs the deployment, configuration, and safety of multi-agent swarms using the `agentic-titan` framework. It ensures that autonomous agents operate within systemic bounds, conserve tokens, and maintain alignment with the central `registry-v2.json`.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** All multi-agent operations across the Rhizome.
**Upstream dependencies:** `SOP--formal-methods-applied-protocols.md` (Protocol 4: Probabilistic Guardrail).

---

## 2. Phase I: Topology Selection
**Goal:** Match the swarm structure to the operational task.
### Process
1. **Analyze Task:** Determine the complexity and domain of the request.
2. **Select Topology:**
    - **Hierarchical:** For high-precision code reviews and audits.
    - **Decentralized:** For broad environmental scanning and research.
    - **Sequential:** For step-by-step pipeline traversals.
3. **Define Objective:** Set a cryptographically stable "Mission Hash" that agents cannot deviate from.

### Starter Research Questions
- What is the minimum number of agents required for this objective?
- Does this task require a "Lead Architect" agent to coordinate outputs?
- Are there cross-organ dependencies that require specialized "Bridge" agents?

---

## 3. Phase II: Resource Allocation (Linear Logic)
**Goal:** Prevent runaway loops and token exhaustion.
### Process
1. **Budgeting:** Assign a Token Budget (TE) to the swarm based on the project's importance.
2. **Rate Limiting:** Implement linear logic constraints ($A \otimes B$) to ensure an agent cannot consume resources more than its allocated share.
3. **Termination:** Hardcode a "Kill Switch" that triggers if an agent recursively queries itself or the system root.

---

## 4. Phase III: Safety & Dry-Run (The Probabilistic Guardrail)
**Goal:** Prove the swarm cannot execute malformed or destructive commands.
### Process
1. **Tool Bounding:** Ensure all agent outputs are strict subsets of the `S_{tools}` schema.
2. **Verification Loop:** Every agent-proposed state change must pass through a non-executing "Dry-Run" validator in Taxis.
3. **Human Gate:** For critical operations (e.g., registry modifications, deployment), mandate a human review pulse before the swarm proceeds.

---

## 5. Output Artifacts
1. **Swarm Configuration File** — Defining topology, budget, and mission hash.
2. **Verification Trace** — A record of the dry-run loop and any corrected hallucinations.
3. **Mission Post-Mortem** — Analysis of token efficiency and objective fulfillment.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
