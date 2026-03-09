---
sop: true
name: session-self-critique
scope: system
phase: any
triggers:
  - context:session-end
complements:
  - evaluation-to-growth
overrides: null
---
# SOP: Session Self-Critique

**Version:** 1.0.0 | **Date:** March 6, 2026 | **Status:** Active
**Scope:** Daily review process for every terminal session that produces or modifies files in the ORGANVM system.

---

## 1. Ontological Purpose

Self-critique is the system observing itself — meta-cognition operationalized as governance. It is not optional housekeeping or a nice-to-have retrospective. Every session produces artifacts that may contain structural errors, content gaps, or violated standards. Without systematic review, these accumulate as technical and intellectual debt that compounds silently.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)

The practice is perpetual: every session ends with a review. The review produces a session log. The session log feeds derived principles. The principles improve the next session. The loop does not close — it spirals upward.

---

## 2. Trigger

Execute this SOP at the **end of every terminal session** that:
- Created new files
- Modified existing files
- Produced deliverables against a METADOC or SOP standard
- Received output from an external AI agent (see also: `SOP--cross-agent-handoff.md`)

**Exception:** Sessions that only read files or ran queries without producing artifacts do not require a review.

---

## 3. Phase I: Inventory

**Goal:** Know exactly what was produced before judging its quality.

1. Run `git status` in every repo touched during the session
2. Run `git log --since="<session-start-time>"` to capture all commits
3. List every file created, modified, or deleted
4. Note any files that were produced but are **not tracked by git** (gitignore, untracked)
5. Capture the session's original goals — what was the user trying to accomplish?

**Output:** A file inventory table in the session log.

---

## 4. Phase II: Structural Triage

**Goal:** Verify that all artifacts are structurally sound before evaluating content.

Per `SOP--cross-agent-handoff.md` Section 3, check:

- [ ] **Git tracking:** Are all produced files tracked? Check `.gitignore` allowlists in superprojects.
- [ ] **File placement:** Are files in the correct repo and directory per the workspace map?
- [ ] **Naming conventions:** Do filenames follow project patterns (double-hyphen, date prefixes, etc.)?
- [ ] **Data integrity:** Were any protected files modified? (registry-v2.json, governance-rules.json, seed.yaml)
- [ ] **Cross-references:** Do internal links between files resolve to tracked, accessible paths?
- [ ] **Version integrity:** Were files destructively overwritten? (Check git log for multiple writes)

**Output:** Structural issues list with severity (CRITICAL / MAJOR / MINOR).

---

## 5. Phase III: Content Audit

**Goal:** Verify that deliverables meet their governing standards.

1. For each deliverable, identify the governing METADOC or SOP
2. Check section-by-section compliance against the standard
3. Classify gaps:
   - **CRITICAL:** Entire required framework missing (e.g., no STEEP analysis, no CLA)
   - **MAJOR:** Section exists but is skeletal or generic
   - **MINOR:** Formatting, naming, or cross-reference issues
4. Use the user's **original prompts** as ground truth, not the agent's paraphrases (prompt drift risk)

**Output:** Content audit table with gap classifications.

---

## 6. Phase IV: Lessons Extraction

**Goal:** Extract reusable principles from this session's successes and failures.

For each structural issue or content gap found:
1. **What went well?** — Identify patterns that worked
2. **What was missed?** — Identify the specific gap
3. **Why was it missed?** — Root cause: tool limitation? Standard unclear? Oversight? Context overflow?
4. **What structural or behavioral pattern caused the miss?** — Generalize beyond this session

Cross-reference against `lessons/derived-principles.md`:
- Does this lesson already exist? If so, does this session add nuance?
- Is this a new principle? If so, add it with the session date and context.

**Output:** Lessons list for the session log + updates to derived-principles.md.

---

## 7. Phase V: Reconciliation

**Goal:** Fix everything found and close the loop.

1. Fix structural issues (git tracking, file placement, naming)
2. Expand content gaps to meet standards
3. Commit all fixes with clear provenance (`review: fix [issue] found in session self-critique`)
4. Write the session log to `sessions/YYYY-MM-DD--description.md`
5. Update `lessons/derived-principles.md` with new or refined principles
6. Update `lessons/agent-behavioral-risks.md` if agent-specific risks were observed
7. Update `lessons/structural-patterns.md` if recurring structural patterns were identified

---

## 8. Output Artifacts

Each session review produces:
- A dated session log in `sessions/`
- Updates to `lessons/derived-principles.md` (if new principles emerged)
- Updates to other lessons files as applicable
- Git commits for all fixes

---

## 9. Cadence

| Frequency | Action |
|-----------|--------|
| **Daily** | Session self-critique at session end |
| **Weekly** | Synthesis: review the week's session logs, identify recurring patterns, update structural-patterns.md |
| **Monthly** | Audit: review all standards for completeness, archive superseded versions |

---

## 10. Phase VI: Concrete Output Gate

**Goal:** Verify that the session produced tangible artifacts, not just analysis.

Per `SOP--theory-to-concrete-gate.md`, every session must produce at least one of:
- Files changed and committed
- Plan file created
- Issues filed
- Decision log entry written
- Concrete next actions documented

### Process

1. Check `git status` and `git log --since="<session-start>"` across all touched repos
2. If no changes were committed and no artifacts were created:
   - Create a plan file summarizing insights with concrete next steps
   - OR create GitHub issues for each actionable finding
   - OR document decisions in the session log with explicit "next action" items
3. Rate the session on the concreteness spectrum:
   - **Level 5:** Deployed — running in production
   - **Level 4:** Committed — code/docs committed to git
   - **Level 3:** Planned — plan file with tasks and file paths
   - **Level 2:** Issued — GitHub issues with acceptance criteria
   - **Level 1:** Logged — decision log entry or session notes
   - **Level 0:** Nothing — gate failure, must remediate before session close

**Output:** Concreteness level noted in session log. Level 0 requires remediation.

---

## 11. Phase VII: Context Budget Tracking

**Goal:** Assess context consumption and improve future session planning.

Per `SOP--context-window-conservation.md`:

1. Note whether the session required continuation (context exhaustion)
2. If continuation was needed:
   - Was the scope too broad? Could it have been split at the start?
   - Was research delegated to subagents or done in the main thread?
   - Were large files read in full when line ranges would have sufficed?
3. Rate context efficiency:
   - **Efficient:** Completed goal with context to spare
   - **Tight:** Completed goal but context was nearly exhausted
   - **Exhausted:** Required continuation — document what caused it
4. Log context efficiency rating and any lessons for future sessions

**Output:** Context efficiency note in session log.

---

## 12. Anti-Patterns

- **Skipping the review because "nothing went wrong"** — The review is how you discover what went wrong. You cannot skip what you haven't done.
- **Reviewing your own paraphrases instead of the original prompts** — Prompt drift is real. Go back to the source.
- **Logging lessons without updating derived-principles.md** — A lesson in a session log is a one-time observation. A lesson in derived-principles.md is a system improvement. Both are required.
- **Treating the review as a checklist to rush through** — Read your own output as if a hostile reviewer is trying to find reasons to reject it.
- **Closing a session at Level 0 concreteness without remediation** — Pure analysis sessions must produce at minimum a plan file or issue list.
- **Ignoring context exhaustion as "just how it is"** — Every exhaustion event is a session planning failure. Log it, learn from it, split earlier next time.

---
*Version: 1.1.0 | System-Wide Directive | ORGANVM*
