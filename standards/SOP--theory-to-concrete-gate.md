---
sop: true
name: theory-to-concrete-gate
scope: system
phase: any
triggers:
  - context:session-end
  - context:research-session
complements:
  - evaluation-to-growth
overrides: null
---
# SOP: Theory-to-Concrete Gate

**Version:** 1.0.0 | **Date:** March 9, 2026 | **Status:** Active
**Scope:** Mandatory output verification at the end of every analysis or research session, ensuring that theoretical work produces concrete, actionable artifacts.

---

## 1. Ontological Purpose

Analysis without concrete output is intellectual consumption, not production. A session that produces extensive reasoning but no files, no issues, and no decisions has consumed energy and context window without advancing the system's state. This is not a prohibition on theory — it is a gate that requires theory to crystallize into something the system can act on.

The gate operationalizes principle E1 (Revenue Imperative): every energy expenditure must have a traceable line to concrete output. The output need not be code — a plan file, an issue, a decision log entry, or an SOP draft all qualify. But "we discussed it thoroughly" does not.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--session-self-critique.md` (concrete output checkpoint at session close), `lessons/derived-principles.md` (E1: Revenue Imperative)
**Precedent:** Gemini sessions producing extensive analysis with zero file changes (2026-03-08). User redirects: *"we did a whole lot of theorizing—define concrete repo changes as result"*, *"if energy-expense yields no possible income-generation...i'm simply masturbating"*.

---

## 2. Trigger

Execute this gate at the **end of every session** that involved analysis, research, design, or strategic discussion — regardless of whether the session was planned as "implementation" or "exploration."

---

## 3. The Gate

### Process

At session close, the session must produce at least **one** of the following concrete artifacts:

| Artifact Type | Minimum Viable Form | Example |
|---------------|---------------------|---------|
| **Files changed** | At least one file created or modified and committed | New SOP, updated config, code change |
| **Plan file** | Dated plan in `.claude/plans/` or `.gemini/plans/` | `2026-03-09-container-preflight.md` |
| **Issues created** | At least one actionable issue filed | GitHub issue with clear acceptance criteria |
| **Decision log entry** | Documented decision with rationale | Entry in ADR or session log |
| **Concrete next actions** | Numbered list with assignee and deadline | "1. Deploy portal to Fly.io (human, by Mar 12)" |

### Verification

1. Run `git status` in every repo touched during the session
2. If `git status` shows no changes and no commits were made:
   - Ask: "What concrete artifact did this session produce?"
   - If the answer is "understanding" or "analysis" — the gate fails
   - Create a plan file or issue list before closing

3. **Gate failure response** (choose one):
   - Write a plan file summarizing the analysis with concrete next steps
   - Create GitHub issues for each actionable insight
   - Write a decision log entry documenting the conclusions reached
   - Draft the first concrete artifact that the analysis points toward

### Agent-Specific Instructions

**Gemini:** Always run `git status` at session close. Your tendency is to analyze thoroughly but not produce files. When analysis is complete, immediately translate insights into a numbered action list with file paths.

**Claude:** When you notice a session trending toward pure discussion, proactively ask: "Should I create a plan file or issues from this analysis, or do you want to continue toward implementation?"

**All agents:** A session that closes with zero concrete artifacts must document why in the session log. Acceptable reasons: "user explicitly chose exploration-only" or "blocked by external dependency." Unacceptable: no reason given.

---

## 4. The Spectrum of Concreteness

Not all concrete output is equal. This spectrum helps evaluate session productivity:

| Level | Output | Value |
|-------|--------|-------|
| **5 — Deployed** | Running in production | Highest |
| **4 — Committed** | Code/docs committed to git | High |
| **3 — Planned** | Plan file with tasks and file paths | Medium |
| **2 — Issued** | GitHub issues with acceptance criteria | Medium |
| **1 — Logged** | Decision log entry or session notes | Low |
| **0 — Nothing** | Pure discussion, no artifacts | Gate failure |

Target: every session produces at least Level 2 output. Level 0 is a hard gate failure.

---

## 5. Output Artifacts

- The concrete artifact itself (file, plan, issue, decision log)
- Session log entry noting what was produced (per `SOP--session-self-critique.md`)

---

## 6. Success Criteria

- Zero sessions close with Level 0 output
- Every analysis session produces at minimum a plan file or issue list
- User does not need to redirect agents toward concrete output — agents self-enforce the gate

---

## 7. Anti-Patterns

- **"We need more analysis before we can act"** — If you've been analyzing for 30+ minutes, you have enough to write a plan file. Write it, then continue analyzing if needed.
- **"The insights are in the conversation"** — Insights in a conversation are ephemeral. They die with the context window. Externalize them.
- **"I'll create the artifacts next session"** — Next session starts cold. Create the artifacts now while context is alive.
- **"This was just a brainstorming session"** — Brainstorming that produces no written output is a conversation, not a work session. Write the brainstorm down.

---

## 8. Cross-References

- `SOP--session-self-critique.md` — integrates the concrete output checkpoint
- `lessons/derived-principles.md` — E1 (Revenue Imperative), E2 (Dual-Level Production)
- `SOP--planning-and-roadmapping.md` — plan files are the minimum concrete output
- `SOP--architecture-decision-records.md` — decision log entries qualify as concrete output

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
