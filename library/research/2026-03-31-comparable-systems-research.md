# Comparable Systems Research — System Library Prior Art

**Date:** 2026-03-31
**Scope:** Prompt chains, SOP lifecycle governance, operational vocabulary formalization
**Sources:** 36 systems analyzed across 3 research domains

---

## Domain 1: Prompt Chain Systems (12 systems)

| System | Recognition | Behavior | Nesting | Format | OSS |
|--------|-----------|----------|---------|--------|-----|
| **Our chains** | Human input patterns | Agent posture | Yes | YAML | Yes |
| IBM PDL | No | Data flow blocks | Yes | YAML | Yes |
| DSPy (Stanford) | No | Module types | Yes | Python | Yes |
| Semantic Kernel (MS) | No | Template functions | Planner | YAML | Yes |
| Promptfoo | Output assertions | Test validation | No | YAML | Yes |
| FlowSpec | No | Step transitions | No | JSON | Yes |
| LMQL (ETH) | Output constraints | Token-level | No | Python | Yes |
| Prompt Decorators | Explicit invocation | Behavioral modifiers | Stacking | Inline | Yes |
| Vanderbilt Catalog | No | Pattern descriptions | No | Prose | Yes |
| APPL (ACL 2025) | No | Function embedding | No | Python | Yes |
| Langfuse | No | Version labels | Composability | JSON | Yes |
| AutoGen (MS) | No | Agent patterns | Topology | Python | Yes |

**Key finding:** No existing system combines recognition criteria (pattern-matching on human input), behavioral directives (agent posture), and chain nesting. Our system is uniquely positioned as a **human-steering grammar** — it formalizes the human's role, not the model's.

**Steal from:**
- **PDL** — YAML block composition model
- **DSPy** — Signature abstraction (declare what, not how)
- **Promptfoo** — Assertion patterns for chain validation
- **Prompt Decorators** — Composability specification
- **Vanderbilt** — Taxonomic classification of prompt patterns

---

## Domain 2: SOP / Process Governance (12 systems)

| System | Lifecycle Stages | Practice-First | Session Protocol | Single-Operator | OSS |
|--------|-----------------|----------------|-----------------|-----------------|-----|
| **Our SOP lifecycle** | 5 (rep→chain) | Yes | Yes | Yes | Yes |
| InnerSource Commons | 3 (initial→validated) | Yes (donut patterns) | No | No | Yes |
| Backstage (Spotify) | No explicit | No | No | No | Yes |
| Cortex.io | 5 (aggregate→optimize) | No | No | No | No |
| OpsLevel | 3 (bronze→gold) | No | No | No | No |
| MS ISE Playbook | No explicit | Partial (experiments) | Partial (retros) | No | Yes |
| GitLab Handbook | No explicit | No (handbook-first) | No | No | Yes |
| TW Tech Radar | 4 (assess→hold) | Partial | No | No | Partial |
| Google SRE | Tuckman stages | No | No | No | Yes |
| Rundeck | 3 (crawl→run) | No | No | No | Partial |
| Toyota Kata | No formal | Yes (kata = practice) | No | No | Yes |
| Stripe Writing | 2 (high-leverage/team) | No | No | No | No |
| CNCF Lifecycle | 4 (sandbox→archived) | No | No | No | Yes |

**Key finding:** Only Toyota Kata and InnerSource Commons share our conviction that procedures emerge from practice. Only our system binds SOPs to session lifecycles. Only our system operates at single-operator scale.

**Steal from:**
- **InnerSource** — "donut patterns" (problem without solution, submitted for community)
- **TW Tech Radar** — 4-ring model with bidirectional movement + WIP limits on Trial
- **Google SRE** — disengagement/demotion mechanism when things regress
- **CNCF** — Archive as honorable explicit state, documentation maturity rubric
- **GitLab** — "handbook-first" enforcement (can't communicate what isn't documented)
- **Toyota Kata** — philosophical validation that practice precedes formalization

---

## Domain 3: Operational Vocabulary Formalization (8+ systems)

| System | Formalization | Trigger→Action | Context-Aware | Parameters | OSS |
|--------|-------------|----------------|--------------|------------|-----|
| **Our vocabulary** | YAML dispatch | Yes (12 categories) | Planned | Planned | Yes |
| DDD Ubiquitous Language | Code-level | Implicit | Bounded Context | N/A | Concept |
| Rasa NLU | YAML intents | Yes (ML classify) | Stories/Rules | Entities | Yes |
| Dialogflow | JSON intents | Yes (NLU) | Input/Output contexts | Parameters | No |
| Amazon Lex | JSON intents | Yes (NLU) | Intent chaining | Slots + elicitation | No |
| Alexa Skills | JSON interaction model | Yes (NLU) | Session state | Slots + synonyms | Partial |
| ChatOps (Hubot) | Regex in code | Yes (pattern match) | No | Capture groups | Yes |
| Slack/Discord Commands | JSON manifest | Yes (exact match) | No | Typed options | Partial |
| Kubectl verbs | Convention | Yes (verb+resource) | No | Resource names | Yes |

**Key finding:** Every system converges on three layers: Namespace → Action → Parameters. The academic consensus: effective personal vocabularies emerge from use, then are formalized (Reynolds & McDonell 2021).

**Steal from:**
- **Rasa** — intent + examples YAML format, stories for multi-turn flows
- **Dialogflow** — context prerequisites (trigger valid only in certain states)
- **Alexa** — slot synonyms, required vs optional parameter elicitation
- **Kubectl** — verb orthogonality (shared verb set across all resource types)
- **Hubot** — self-documenting vocabulary (help auto-generates from patterns)

---

## Synthesis: What We Do That Nobody Does

1. **Human-steering grammar.** Every prompt system formalizes what the MODEL does. We formalize what the HUMAN does and tell the model how to respond to that posture.

2. **Practice-first emergence.** Our vocabulary and chains emerged from 14+ sessions of actual use, then were formalized. Most systems design the vocabulary first.

3. **Session protocol integration.** No comparable system binds operational procedures to session lifecycles (start→work→close→handoff with hard gates).

4. **Chaining as lifecycle stage.** No system treats "wire this SOP to other SOPs in an executable graph" as a formal maturation stage.

5. **Single-operator scale.** All comparable systems assume teams. Ours assumes one person steering automation at enterprise scale.

## Synthesis: What the Field Does That We Should Adopt

1. **Automated compliance measurement** (Cortex, OpsLevel, Backstage) — verify SOPs are actually followed
2. **Demotion protocols** (Google SRE, TW Radar) — what happens when a fortified SOP regresses?
3. **WIP limits on experimentation** (TW Radar) — limit how many SOPs are in absorb simultaneously
4. **Context prerequisites** (Dialogflow, Alexa) — trigger phrases valid only in certain phases
5. **Slot elicitation** (Alexa) — when a trigger is missing parameters, ask for them
6. **Verb orthogonality** (kubectl) — shared verb set across all categories
7. **Self-documenting vocabulary** (Hubot) — the system enumerates its own triggers

---

## Source List (36 systems)

### Prompt Chains
1. IBM PDL — github.com/IBM/prompt-declaration-language (Apache-2.0)
2. DSPy — github.com/stanfordnlp/dspy (MIT, Stanford)
3. Semantic Kernel — learn.microsoft.com/semantic-kernel (MIT, Microsoft)
4. Promptfoo — github.com/promptfoo/promptfoo (MIT)
5. FlowSpec — github.com/woodyhayday/FlowSpec (MIT)
6. LMQL — github.com/eth-sri/lmql (Apache-2.0, ETH Zurich)
7. Prompt Decorators — github.com/synaptiai/prompt-decorators (MIT)
8. Vanderbilt Prompt Pattern Catalog — PLoP 2023
9. APPL — ACL 2025, aclanthology.org/2025.acl-long.63
10. Langfuse — github.com/langfuse/langfuse (MIT)
11. PromptLayer — promptlayer.com (SaaS)
12. AutoGen — github.com/microsoft/autogen (MIT)

### SOP / Process Governance
13. InnerSource Commons — patterns.innersourcecommons.org (Apache-2.0)
14. Backstage — backstage.io (Apache-2.0, CNCF)
15. Cortex.io — cortex.io (Commercial)
16. OpsLevel — opslevel.com (Commercial)
17. MS ISE Engineering Playbook — microsoft.github.io/code-with-engineering-playbook (MIT)
18. GitLab Handbook — handbook.gitlab.com (Public)
19. TW Technology Radar — thoughtworks.com/radar (Public methodology)
20. Google SRE — sre.google (Public books)
21. Rundeck — github.com/rundeck/rundeck (Apache-2.0)
22. Toyota Kata — Mike Rother (Public methodology)
23. Stripe Writing Culture — documented in Pragmatic Engineer
24. CNCF Project Lifecycle — contribute.cncf.io/projects/lifecycle (Public)

### Operational Vocabulary
25. DDD Ubiquitous Language — Eric Evans 2003
26. Rasa NLU — github.com/RasaHQ/rasa (Apache-2.0)
27. Dialogflow — cloud.google.com/dialogflow (Commercial)
28. Amazon Lex — aws.amazon.com/lex (Commercial)
29. Alexa Skills Kit — developer.amazon.com/alexa (Partial OSS)
30. Hubot — github.com/hubotio/hubot (MIT, archived)
31. Errbot — github.com/errbotio/errbot (GPL-3.0)
32. Slack Slash Commands — api.slack.com (API)
33. Discord Application Commands — discord.dev (API)
34. Kubectl — github.com/kubernetes/kubectl (Apache-2.0)
35. Emacs M-x — gnu.org/software/emacs (GPL)
36. Reynolds & McDonell 2021 — "Prompt Programming for Large Language Models"
