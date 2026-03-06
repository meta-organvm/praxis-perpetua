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

*Last updated: 2026-03-06 | Source: founding session + structural audit*
