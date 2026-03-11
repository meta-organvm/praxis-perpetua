# SOP: Polymorphic Agent Testing (The Adversarial Protocol)

## 1. Ontological Purpose
This SOP formalizes the testing methodology for the `agentic-titan` multi-agent swarm framework. It ensures that before agents are granted autonomy in the meta-workspace, they are subjected to rigorous chaos testing and adversarial prompting to prove their bounds.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** ORGAN-IV (Taxis) agent development.

---

## 2. Phase I: Scenario Generation
**Goal:** Define the test bounds.
1. **Benign Path:** Define standard "happy path" tasks (e.g., "Summarize this theoretical repo").
2. **Adversarial Path:** Inject "jailbreak" prompts or malformed payloads into the context to attempt to force the agent to violate `governance-rules.json`.
3. **Chaos Path:** Simulate a network partition (e.g., block the agent's access to the MCP server mid-execution).

## 3. Phase II: Sandboxed Execution
**Goal:** Run the agent in a sterile environment.
1. **Docker Cage:** Spin up a temporary, isolated Docker container (`alchemia-sandbox`) with zero access to the actual `meta-organvm` files.
2. **Mock MCP:** Connect the agent to a mock MCP server that returns controlled, deterministic responses.
3. **Execution:** Trigger the swarm and capture all tool call logs.

## 4. Phase III: Hallucination Detection & Tuning
**Goal:** Audit the cognitive output.
1. **Trace Analysis:** Scan the agent's `<thought>` blocks for logical inconsistencies or attempts to guess missing data.
2. **Metric Distillation:** Score the run on Token Efficiency, Tool Call Accuracy, and Rule Adherence.
3. **Model Tuning:** Adjust the system prompt weights or the MCP tool descriptions if the agent fails the test.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
