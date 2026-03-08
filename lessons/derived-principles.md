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

---

*Last updated: 2026-03-08 | Source: founding session + structural audit + four-branch synthesis + personal-hell session*
