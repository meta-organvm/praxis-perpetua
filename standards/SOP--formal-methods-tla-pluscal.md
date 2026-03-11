# SOP: Formal Methods — TLA+ and PlusCal Verification (The Blueprint Verifier)

## 1. Ontological Purpose
This SOP operationalizes **Temporal Logic of Actions (TLA+)** and its algorithmic dialect **PlusCal** within the ORGANVM system. It serves as the ultimate "Blueprint Verifier," shifting the focus from testing *code* to testing *thought* and architecture.

By mathematically modeling the logic of the system before writing implementation code, we prevent deadlocks, race conditions, and catastrophic failures in our highly concurrent, 8-organ distributed architecture (The Rhizome).

**Governed by:** `SOP--formal-methods-master-taxonomy.md` (Stratum II: Temporal & Concurrency Logic).
**Inspiration:** Industrial application of TLA+ by AWS, Microsoft, and Intel.

---

## 2. The Core Utility
TLA+ strips away language syntax, memory management, and library overhead. It forces the system architect to define the pure logic and constraints. The TLA+ Model Checker (TLC) then calculates every single possible state the system could ever enter.

### Why TLA+ for ORGANVM?
1.  **Deadlock Prevention:** Proves the Rhizome doesn't deadlock when concurrent events fire (e.g., `Ergon` triggers a webhook, `Koinonia` shifts state, and `Logos` goes offline simultaneously).
2.  **Bounding AI to Physics:** Mathematically proves that the AI orchestration engine (`Taxis`) cannot violate `governance-rules.json` regardless of LLM hallucination.

### The PlusCal Mitigation
Because raw TLA+ is pure mathematics and has a steep learning curve, we mandate the use of **PlusCal**. PlusCal resembles standard pseudo-code (C/Python) and compiles directly into TLA+. This prevents "iterational masochism" while retaining industrial-grade verification.

---

## 3. Workflow: The PlusCal Specification Pipeline

### Phase I: Isolate the Subsystem
1.  **Identify the boundary:** Select a specific, high-risk concurrent interaction (e.g., the `Ergon -> Taxis` webhook handoff).
2.  **Define Variables:** What is the global state? (e.g., webhook queue, database lock status).
3.  **Define Actors:** Who are the concurrent processes? (e.g., Ergon Sender, Taxis Receiver, Taxis Database).

### Phase II: Draft the PlusCal Algorithm
1.  **Write the Algorithm:** Use PlusCal syntax within a `.tla` file comment block to describe the exact steps each actor takes.
2.  **Define Invariants (Safety):** State conditions that must *never* happen (e.g., "The webhook is dropped and the queue is empty, but the event wasn't logged").
3.  **Define Liveness:** State conditions that must *always eventually* happen (e.g., "If Ergon sends a webhook, Taxis will eventually process it or log a failure").

### Phase III: Model Checking (TLC)
1.  **Translate to TLA+:** Run the PlusCal translator to generate the underlying TLA+ math.
2.  **Execute TLC:** Run the TLA+ Model Checker against the specification.
3.  **Analyze Error Traces:** If the model checker finds a violation, it will output the exact sequence of steps that leads to the failure.
4.  **Refine Thought:** Fix the logic in the PlusCal blueprint, re-translate, and re-check until zero errors are found.

### Phase IV: Implementation Handoff
1.  **Code as Translation:** Only after TLC reports zero errors do engineers write the Python/Go implementation.
2.  **Absolute Confidence:** The code is written knowing the underlying architecture is mathematically flawless.

---

## 4. Execution Example: Ergon to Taxis Webhook

**Scenario:** Ergon fires a `product_launch` webhook to Taxis.

**The Threat:** Network stutters cause Ergon to send the webhook twice. Taxis might process it twice, violating idempotency. Or, Taxis might drop it due to a database lock.

**The PlusCal Model:**
1.  Model Ergon as a process that can non-deterministically send 1 or 2 identical webhooks.
2.  Model Taxis as a process that reads the queue, checks a database table for the `event_id`, writes if missing, and executes.
3.  Model the Database as a shared resource that can fail.

**The Proof:** The TLC checker must verify that `execution_count` is *always* exactly 1 for a given `event_id`, regardless of network drops or duplicate sends.

---

## 5. Output Artifacts
1.  **`.tla` Specification Files** — containing both the PlusCal algorithm and the generated TLA+ math.
2.  **TLC Run Logs** — proof of verification.
3.  **Architectural Decision Records (ADR)** — linking the verified TLA+ model to the final system design.

---

## Appendix: Tooling
*   [TLA+ Toolbox](https://github.com/tlaplus/tlaplus) — IDE for writing and checking models.
*   [VS Code TLA+ Extension](https://marketplace.visualstudio.com/items?itemName=alygin.vscode-tlaplus) — Recommended for local development.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
