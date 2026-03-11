# PROMPTS: Formal Methods Implementation & Verification

This library provides specialized prompts for AI agents to implement, verify, and audit formal methods within the ORGANVM system.

---

## 1. STRATUM I: Foundational & Data Logic

### `formal-methods:hoare-contract`
**Use Case:** Implementing strict cross-organ data validation.
**Prompt:**
```markdown
You are a Formal Methods Engineer. Your task is to implement a Hoare Logic contract for the data transfer between [Source Organ] and [Destination Organ].

**Goal:** Prove the invariant {P} C {Q}.
1. **Pre-condition (P):** Define a Pydantic/TypeScript schema that perfectly matches `registry-v2.schema.json`.
2. **Command (C):** Implement the routing logic in Taxis that handles the payload.
3. **Post-condition (Q):** Implement a verification step that ensures the payload was successfully persisted in the downstream queue.

Ensure that if P is false, the system raises a `FormalVerificationError` and halts execution. No malformed data must pass the membrane.
```

### `formal-methods:refinement-audit`
**Use Case:** Running AST analysis to ensure architectural compliance.
**Prompt:**
```markdown
You are a Static Analysis Agent. Perform a Refinement Calculus audit on the repository [Repo Path].

**Constraint:** The implementation (I) must satisfy the specification (S) defined in `governance-rules.json`.
**Specific Rule:** Flow must be strictly Theoria -> Poiesis -> Ergon. Kerygma cannot query Theoria.

1. Parse the AST of all source files in the project.
2. Identify all `import` and `request` calls.
3. Cross-reference these against the dependency DAG.
4. List any "Refinement Violations" where code bypasses the hierarchy.
```

---

## 2. STRATUM II: Temporal & Concurrency Logic

### `formal-methods:tla-pluscal-model`
**Use Case:** Modeling concurrent workflows and webhook handoffs to prevent deadlocks.
**Prompt:**
```markdown
You are a TLA+ Architect. Your task is to mathematically model the concurrent interaction between [Actor A] and [Actor B] using PlusCal.

**Goal:** Create a formal specification that proves the system is free of deadlocks and race conditions.
1. Define the global state variables (e.g., message queues, lock states).
2. Write a PlusCal algorithm modeling the non-deterministic behavior of both actors.
3. Define the **TypeOK** invariant to ensure variables stay within bounds.
4. Define the **Safety** invariant (e.g., an event cannot be processed twice).
5. Define the **Liveness** invariant (e.g., `[]<>` - a sent webhook eventually resolves).
6. Ensure the PlusCal translates cleanly into TLA+.
```

### `formal-methods:liveness-check`
**Use Case:** Proving that orchestration flows eventually resolve.
**Prompt:**
```markdown
You are a Model Checker. Analyze the following orchestration sequence defined in `governance-rules.json` for the [Workflow Name] workflow.

**Goal:** Prove the Liveness property: [] (Trigger -> <> Resolve).
1. Identify all potential states in the sequence.
2. Identify all exit conditions (Success, Timeout, Error).
3. Prove that there is no state where the system can enter an infinite loop or deadlock.
4. Propose a mathematically strict `timeout_ms` and `fallback_state` for every asynchronous call.
```

---

## 3. STRATUM III: Security & Boundary Logic

### `formal-methods:taint-analysis`
**Use Case:** Preventing epistemic leaks of sensitive data.
**Prompt:**
```markdown
You are a Security Auditor. Perform a Taint Analysis on the data flow from Ergon to Kerygma.

1. Identify all "Source" nodes (e.g., raw database fields in Ergon).
2. Mark sensitive fields (API keys, internal IDs, private rules) as `Tainted:Private`.
3. Trace how this data moves through the Logos essay generation process.
4. Verify that the Kerygma distribution node has a hardcoded filter that rejects any string containing `Tainted` metadata.
5. Propose a "Synthesis Layer" that transforms private data into public abstractions.
```

---

## 4. STRATUM IV: Epistemic & Consensus Logic

### `formal-methods:epistemic-bounds`
**Use Case:** Bounding LLM knowledge vs. hallucination.
**Prompt:**
```markdown
You are an Epistemic Governor. Your role is to bound the knowledge of the Claude LLM inside the Taxis MCP server.

**Invariant:** K_a P -> P (If Claude knows P, P must be true).
1. Define the "Set of Truths" Claude is allowed to use (e.g., file hashes, registry entries, git logs).
2. Explicitly define "Beliefs" (e.g., tone, sentiment, creative interpretation).
3. Instructions for the MCP Server: "If you are making a decision based on a Belief, you must tag it as `PROBABILISTIC` and request human audit. If you are using a Truth, you must provide the cryptographic hash as evidence."
```

---

## 5. STRATUM V: Topological & Creation Logic

### `formal-methods:mereology-map`
**Use Case:** Defining the relationship between Organs and the Meta-System.
**Prompt:**
```markdown
You are an Ontological Architect. Map the Mereology of the ORGANVM system for the current project [Project Name].

**Goal:** Define x < y (Project is a proper part of the Organ).
1. List the properties of the Project.
2. List the properties of the Parent Organ.
3. Identify the "Emergent Properties" of the Organ that do not exist in the Project alone (e.g., cross-repo synchronization).
4. Prove that the Project satisfies the "Identity Invariants" of the Organ as defined in `organvm-corpvs-testamentvm`.
```

---
*Version: 1.0.0 | Prompt Library | ORGANVM*
