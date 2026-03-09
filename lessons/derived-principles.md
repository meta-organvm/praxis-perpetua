# Derived Principles

Living document. Updated as new patterns emerge from session reviews. Each principle includes its source session for traceability.

---

## Structural Principles

### S1. Superproject allowlist `.gitignore` silently hides files
**Source:** 2026-03-06 Gemini Styx session

Always run `git status` after external agent output in a superproject. The allowlist pattern (`*` then `!file`) means new files are invisible unless explicitly added. The agent cannot know about this pattern. Verify tracking before evaluating content.

### S2. SOPs and governance docs belong in governed submodules, not superproject roots
**Source:** 2026-03-06 Gemini Styx session

Superproject roots use allowlist gitignore patterns. Every new file requires a gitignore edit. This creates a maintenance burden and a silent-failure risk. Move governance documents into a dedicated submodule where git tracks all files by default.

### S3. Module-scope evaluation freezes runtime behavior
**Source:** 2026-03-06 structural audit (F6)

`CONSTANT = expensive_function()` runs once at import. If the function depends on environment variables or filesystem state, the value is frozen at import time, not at use time. Call at use-time instead.

### S4. Incomplete lookup tables are silent bombs
**Source:** 2026-03-06 structural audit (F3)

A map with 4 of 8 entries returns the zero value for unmapped keys without raising an error. Every lookup table must either cover all cases or explicitly raise on uncovered ones.

### S5. Sentinel values are invisible to comparison operators
**Source:** 2026-03-06 structural audit (F7)

`-1 > 90` is `False`. `None > 0` raises `TypeError` in Python 3 but may silently return `False` in some contexts. Every sentinel must be handled before it reaches a comparison.

---

## Code Quality Principles

### C1. `dict.get(key, default)` does not protect against `None`
**Source:** 2026-03-06 structural audit (F2)

When the key exists with value `None`, the default is not used. Fix pattern: `dict.get(key) or default`. Know the difference between "key absent" and "value null."

### C2. Dead conditionals are not harmless
**Source:** 2026-03-06 structural audit (F4)

If both branches of an if/else do identical work, the code lies about its intent. The next reader will assume the branches differ and "fix" one, introducing a real bug. Remove them or make them real.

### C3. Data migration creates orphaned readers
**Source:** 2026-03-06 structural audit (F1)

When you move a field from location A to location B, audit every reader of A. The writer knows about the move; the readers don't. `grep` is mandatory, not optional.

### C4. Test coverage does not equal correctness
**Source:** 2026-03-06 structural audit

722 tests passed while 3 CRITICAL bugs silently corrupted data in production paths. Tests verify what you thought to check; audits verify what you didn't think to check.

---

## Agent Interaction Principles

### A1. Verify against `git status`, never against the agent's self-report
**Source:** 2026-03-06 Gemini Styx session

External agents claim completion of operations they have not performed (commits, pushes, tracking). Always verify system state independently.

### A2. Audit against original prompts, not agent paraphrases
**Source:** 2026-03-06 Gemini Styx session

Agents reinterpret requests subtly (prompt drift). The difference between "METADOC-compliant research documents" and "research summaries" is the gap between what was requested and what was delivered.

### A3. Later deliverables in long sessions are most likely to have gaps
**Source:** 2026-03-06 Gemini Styx session

As context windows fill, agents silently drop frameworks that were correctly applied earlier. The last files produced require the most scrutiny.

### A4. Destructive rewrites lose intermediate versions
**Source:** 2026-03-06 Gemini Styx session (Gemini-specific)

Some agents use `open(path, "w")` for every edit, losing all previous content. If version history matters, commit after each agent write cycle, not at session end.

---

## Systemic Principles

### Y1. Structural integrity through semantic flexibility
**Source:** 2026-03-07 four-branch product implementation synthesis (P1)

The acyclic dependency graph (I->II->III) must be maintained in code, but bidirectional reality is maintained through discourse. When Commerce discovers a flaw in upstream Theory, feedback routes through Logos essays and Koinonia discussions — never through code dependencies. The system is structurally unidirectional but semantically bidirectional. See: Logos Bypass protocol.

### Y2. Governance is soil, not bureaucracy
**Source:** 2026-03-07 four-branch synthesis (P2), 2026-03-06 materia-collider founding document

Governance artifacts are growth conditions, not compliance checklists. A seedling (LOCAL) doesn't need a SECURITY.md. A tree bearing fruit that strangers pay for (GRADUATED) does. The promotion ladder encodes organic maturity. Premature governance kills seedlings.

### Y3. Pre-codification is a first-class phase
**Source:** 2026-03-07 four-branch synthesis (P3), 2026-03-06 materia-collider founding document

Ideas need a liminal space (materia-collider) before entering the governed organ system. The pipeline is: Fuel (intake/) -> Collision (materia-collider/) -> Specialization (agentic-titan/) -> Habitat (8 organs). Nothing is canonical until it graduates to an organ. Contradictions are allowed in pre-codified space.

### Y4. The director perceives; specialists execute
**Source:** 2026-03-07 four-branch synthesis (P4), 2026-03-06 materia-collider founding document

The one-person enterprise works because the director holds vision and timing while AI specialists hold domain expertise. Each specialist is a "historically complete corpus contextual expert" of exactly one thing. The director doesn't know how to do their jobs — the director knows that, when, and why they need to be done. The infrastructure (ORGANVM) mediates between them.

### Y5. Human friction is a feature, not a bug
**Source:** 2026-03-07 four-branch synthesis (P5), session 9affb815 (Styx "Cyborg Architecture")

Blocked handoffs, governance gates, and promotion requirements are deliberate speed bumps that prevent premature scaling of half-formed products. Human intervention should be treated as an asynchronous first-class primitive — the system pauses gracefully and resumes when the human actor completes their part.

### Y6: The system is ontologically stratified; decisions must respect their stratum
**Source:** 2026-03-08 ontological topology analysis

Four strata: implementation detail, architectural pattern, governance rule, philosophical commitment. Each has its own logic, timescale, and reversibility. Applying a lower stratum's logic to a higher-stratum decision causes recklessness (treating philosophical commitments as config flags). Applying a higher stratum's logic to a lower-stratum decision causes paralysis (treating linter choice as a moral commitment). Before any decision, ask: which stratum does this belong to?

### Y7: Every organizational system that describes the architecture can be instantiated as a living agent within it
**Source:** 2026-03-08 ontological topology analysis + Study Suite founding specification

The academic system becomes a Reviewer agent. The scientific system becomes an Experimenter agent. The governance system becomes an Auditor agent. The map becomes the territory when the map has agency. Constraint: instantiated organizational systems must be observers, not actors — they produce knowledge; the human conductor acts on it. See: [The Ontological Topology of ORGANVM](../research/2026-03-08-ontological-topology-of-organvm.md), Section IV.

### Y8: Active complexity reduction is structural necessity, not optional optimization
**Source:** 2026-03-08 universal hierarchy synthesis (Convergence 1)

The system's scale exceeds its operator's capacity by every measure — information theory (channel capacity), neuroscience (7±2 chunks), ecology (carrying capacity), economics (scarcity of attention), infrastructure (single points of failure). Active complexity reduction — dimming, suppressing, decomposing inactive units so the conductor's attention is directed to the 7±2 that matter now — is not optional optimization but structural necessity. 5/5 domains confirm: fewer active repos, deeper investment in the ones that remain. See: [Universal Hierarchy Synthesis](../research/2026-03-08-universal-hierarchy-synthesis.md), §I Convergence 1.

### Y9: Monitoring without automatic response is theater
**Source:** 2026-03-08 universal hierarchy synthesis (Convergence 2)

Observation without corrective action is a thermometer without a thermostat. Confirmed by organismal biology, infrastructure, thermodynamics, and governance — 4/4 domains. Vital signs need automatic responses: when test coverage drops, a corrective task auto-generates; when a repo goes stale past STALE_CRIT, it dims in context files; when the omega scorecard stalls, operational cadence shifts. The organism (metrics/organism.py) already observes — it must also act. See: [Universal Hierarchy Synthesis](../research/2026-03-08-universal-hierarchy-synthesis.md), §I Convergence 2.

### Y10: Forgetting is a feature, not a failure
**Source:** 2026-03-08 universal hierarchy synthesis (Convergence 3)

5/5 domains confirm: neuroscience (retrieval-induced forgetting), ecology (decomposers), academia (emeritus), cellular biology (apoptosis), chemistry (decomposition reactions). ARCHIVED status without active nutrient extraction is not forgetting — it is hoarding. Archival must extract reusable patterns, absorb documentation into the corpus, and then truly go cold: no edges, no context, no cognitive load. See: [Universal Hierarchy Synthesis](../research/2026-03-08-universal-hierarchy-synthesis.md), §I Convergence 3.

### Y11: Not all units deserve equal governance
**Source:** 2026-03-08 universal hierarchy synthesis (Convergence 4)

Keystones (registry, engine, schemas) need strictest gates and highest test coverage. Infrastructure repos mature but don't "graduate." Creative/experimental repos need looser governance. Stubs either bond or get composted. The existing gate profiles (gates.py PROFILES) partially implement this — governance-rules.json and promotion criteria should follow. 5/5 domains confirm: ecology, infrastructure, academia, chemistry, mathematics. See: [Universal Hierarchy Synthesis](../research/2026-03-08-universal-hierarchy-synthesis.md), §I Convergence 4. See also: SP6 in [Structural Patterns](structural-patterns.md).

### Y12: Dynamic lens assembly replaces permanent organizational theory
**Source:** 2026-03-08 universal hierarchy synthesis (§III)

Summon 2-3 organizational lenses per decision, interrogate through them, resolve conflicts, release. Never carry lens-specific vocabulary into unrelated work. One assembly per task — perpetual FRAME is the anti-pattern. The 28-lens research program demonstrated the method; the catalog formalizes it. See: [SOP--dynamic-lens-assembly.md](../standards/SOP--dynamic-lens-assembly.md), [lens-catalog.md](lens-catalog.md), [Universal Hierarchy Synthesis](../research/2026-03-08-universal-hierarchy-synthesis.md), §III.

---

## Economic Principles

### E1. The Revenue Imperative (Hard Gate)
**Source:** 2026-03-08 personal-hell session + Essay 36 (construction addiction)

Every energy expenditure must have a traceable line to income generation. This is not advisory — it is a gate. If energy-expense has no traceable line to income-generation, it requires explicit justification. The constraint does not dilute creative work; it challenges the creator to make work that is both true and economically viable. Lucas, Cameron, Eno — they understood that industrial participation unlocks industrial superpowers.

Six valid revenue pathways:
- `direct-product` — revenue from selling the thing itself
- `consulting-service` — revenue from teaching or executing the methodology
- `content-ip` — revenue from essays, courses, books, talks
- `grant-award` — revenue from institutional funding
- `employment` — revenue from hired positions
- `infrastructure` — enabling work with a stated payoff horizon (e.g., "enables Styx deployment in 2 weeks")

Items without a declared pathway are flagged and blocked. Infrastructure pathway requires a concrete payoff horizon — "it'll be useful someday" is not a horizon.

### E2. Dual-Level Production
**Source:** 2026-03-08 personal-hell session

Every action produces two outputs: the direct result AND the reproducible methodology. SOP execution produces a consulting deliverable. Deployment produces a case study. An essay is both art and sales collateral. The clone is not an afterthought — it is designed into the action from the start.

Level 1: Do the thing (deploy, audit, write).
Level 2: Clone it for reproduction, study, and sale.

### E3. The Janus Principle — internal and external serve different strata
**Source:** 2026-03-08 universal hierarchy synthesis (Conflict 3 resolution)

Internal documentation (Layer 0: architectural coherence) and external products (Layer +1: emergent value) are not competing — they serve different strata (Y6). Cap internal documentation at current level; redirect incremental sessions to external-facing outputs. Infrastructure WIP limit: hard-cap infrastructure tasks in the pipeline. The technium's "want" for more tools, aligned with the conductor's cognitive preferences, is the system's most dangerous positive feedback loop. The noosphere demands transmission; the autopoietic cycle demands production. Both are satisfied by shipping products, not by writing more governance documents. See: [Universal Hierarchy Synthesis](../research/2026-03-08-universal-hierarchy-synthesis.md), §II Conflict 3, §IV Finding 4-5.

---

*Last updated: 2026-03-08 | Source: founding session + structural audit + four-branch synthesis + personal-hell session + universal hierarchy synthesis*
