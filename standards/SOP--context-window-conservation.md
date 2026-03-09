---
sop: true
name: context-window-conservation
scope: system
phase: any
triggers:
  - context:session-start
  - context:session-planning
complements:
  - continuous-learning-agent
overrides: null
---
# SOP: Context Window Conservation

**Version:** 1.0.0 | **Date:** March 9, 2026 | **Status:** Active
**Scope:** Session size budgeting and proactive split strategy for AI-assisted work sessions to minimize context exhaustion and cold-restart loss.

---

## 1. Ontological Purpose

A context window is a non-renewable resource within a session. When it runs out, the session dies and restarts with a summary preamble that loses nuance, decision rationale, and accumulated state. Six continuations in 24 hours (observed 2026-03-08) means six cold restarts, six summary preambles, and six opportunities for the new session to misunderstand what the previous one was doing.

Context conservation is not about being frugal — it is about completing goals within a single session so that continuity is maintained and no restart tax is paid.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--session-self-critique.md` (context tracking at session close), `SOP--agent-seeding-and-workforce-planning.md` (delegation strategy)
**Precedent:** 6+ context exhaustion events across 9 Claude sessions in 24 hours (2026-03-08).

---

## 2. Trigger

Execute this SOP at the **start of every AI-assisted session** that involves implementation work (code changes, document creation, multi-step research).

Exception: Quick Q&A or single-file review sessions that are unlikely to exhaust context.

---

## 3. Phase I: Scope Declaration

### Process

1. **Declare a single bounded goal** at session start:
   - Good: "Create 6 new SOP files in praxis-perpetua/standards/"
   - Bad: "Work on the ORGANVM system" (unbounded)
   - Bad: "Implement plan X and also review Y and fix Z" (multi-goal)

2. **Estimate session weight:**
   - **Light** (< 30% context): Single file creation, focused code review, targeted bug fix
   - **Medium** (30-60% context): Multi-file implementation, research + creation, test writing
   - **Heavy** (60-90% context): Large refactor, cross-repo changes, plan implementation with many files

3. **If the goal is Heavy, split it before starting:**
   - Decompose into 2-3 Medium sessions
   - Define the handoff artifact between sessions (plan file, issue list, partial implementation)
   - Sequence the sessions: which must come first?

### Deliverables
- Goal statement (1-2 sentences)
- Weight estimate (Light / Medium / Heavy)
- Split plan if Heavy

---

## 4. Phase II: Context Budget Allocation

### Process

1. **Reserve 20% of context for session close:**
   - Final verification
   - Commit message composition
   - Session review (`SOP--session-self-critique.md`)
   - Summary preamble generation (if continuation is needed)

2. **Delegate research to subagents** to preserve main context:
   - File exploration → Explore subagent
   - Multi-file search → Explore subagent
   - Complex research questions → general-purpose subagent
   - The main context should contain decisions and implementations, not raw search results

3. **Avoid context-expensive operations in the main thread:**
   - Reading entire large files (use line ranges)
   - Dumping full test output (run in background, check summary)
   - Exploring directories without a specific target

### Deliverables
- Context budget awareness (no formal artifact — this is a behavioral discipline)

---

## 5. Phase III: Split Signals

### Process

1. **Monitor for split signals** during the session:
   - The session has completed a distinct phase of the work (e.g., "all SOPs created, now updating existing files")
   - The session has accumulated 5+ large file reads or writes
   - The session has been running for 30+ minutes of active interaction
   - You notice responses becoming less detailed or losing earlier context

2. **When a split signal fires:**
   - Complete the current atomic unit of work (don't stop mid-file)
   - Commit all changes
   - Generate a continuation preamble:

   ```markdown
   ## Continuation Context
   **Goal:** [original goal]
   **Completed:** [what was done]
   **Remaining:** [what is left]
   **Key decisions:** [any decisions that must carry forward]
   **Files modified:** [list]
   **Files to modify next:** [list]
   ```

3. **If possible, finish the session** rather than splitting:
   - Reduce scope: defer nice-to-haves
   - Batch remaining changes: less exploration, more direct edits
   - Accept imperfection: a complete 90% solution beats an incomplete 100% attempt

### Deliverables
- Continuation preamble (if split is needed)
- Committed partial work

---

## 6. Phase IV: Proactive Archiving

### Process

1. **Archive completed phases** within the session:
   - Once Phase 1 of a multi-phase implementation is done and committed, stop referring back to its details
   - Summarize Phase 1 results in a single paragraph for reference, then work from the summary

2. **Use plan files as external memory:**
   - Write intermediate state to a plan file rather than holding it in context
   - Reference the plan file when needed rather than reconstructing from memory
   - Location: `.claude/plans/YYYY-MM-DD-{slug}.md`

3. **Collapse tool output:**
   - After reading a file for information, extract the relevant lines and discard the rest
   - After running tests, note pass/fail counts and specific failures, not full output

### Deliverables
- Plan file updated with intermediate state (if applicable)

---

## 7. Output Artifacts

- Session goal statement (at start)
- Continuation preamble (if session splits)
- Plan file with intermediate state (if multi-phase)

---

## 8. Success Criteria

- Session completes its declared goal without context exhaustion
- If continuation is needed, the next session picks up cleanly from the preamble
- Zero "I've lost track of what we were doing" moments in continued sessions
- Heavy goals are split into Medium sessions before starting, not after context death

---

## 9. Anti-Patterns

- **"Let me just also do X while I'm here"** — Scope creep within a session is the #1 cause of context exhaustion. If X wasn't in the goal, it's a new session.
- **Reading files "just to understand"** — Undirected exploration burns context. Know what you're looking for before reading.
- **Keeping full test output in context** — Run tests in background, check summary. Full output is diagnostic, not context-worthy.
- **Refusing to split** — Continuing past the split signal produces worse output than a clean restart with a good preamble.

---

## 10. Cross-References

- `SOP--session-self-critique.md` — session close includes context budget reflection
- `SOP--agent-seeding-and-workforce-planning.md` — delegation reduces main-thread context consumption
- `SOP--cross-agent-handoff.md` — handoff between sessions requires the same structural validation as handoff between agents
- `coordination/claims.py` — multi-agent coordination prevents duplicate work across sessions

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
