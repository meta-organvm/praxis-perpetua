# SOP: Stranger Test Protocol

## 1. Ontological Purpose

The Stranger Test measures whether the ORGANVM system's public documentation is sufficient for a competent developer to understand the system's purpose, structure, and key artifacts without guidance from the system's creator. It is the ultimate external validation: if a stranger can navigate it, the system is legible. If not, the documentation has failed.

This is not a usability test in the conventional sense — it is a **legibility audit**. The system's value is zero if nobody outside the creator can understand it. Constitution Article V states: *"A stranger should be able to understand the system by reading public documentation alone."*

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 2: Quality & Integrity)
**Cross-reference:** `SOP--promotion-and-state-transitions.md` (stranger test required for PUBLIC_PROCESS -> GRADUATED), `SOP--structural-integrity-audit.md` (documentation quality gate)

---

**Created:** 2026-02-16
**Author:** @4444j99
**Status:** ACTIVE
**Canonical location:** `praxis-perpetua/standards/SOP--stranger-test-protocol.md`
**Reference:** Constitution Article V

---

## 2. Phase I: Participant Selection

### Process

1. **Identify participant profile:**
   - Professional software developer or technically fluent graduate student
   - Comfortable navigating GitHub (repos, orgs, README files, Actions)
   - Familiar with basic concepts: CI/CD, dependency graphs, JSON, Markdown
   - **No prior exposure** to the ORGANVM system, its creator, or this corpus

2. **Preferred qualifications (not required):**
   - Experience with multi-repo or monorepo architectures
   - Familiarity with creative coding, generative art, or institutional governance
   - Has evaluated or reviewed open-source projects before

3. **Disqualifying criteria:**
   - Has previously read any ORGANVM documentation or essays
   - Personal relationship with the system creator (social bias)
   - Currently collaborating on any repo in the system

### Starter Research Questions
- Where can you recruit qualified participants? (Developer communities, university labs, professional networks)
- What compensation is appropriate? (Coffee, book, etc. — this is a favor, not a job)
- How many participants are needed for statistical significance? (Minimum 3 for pattern detection)
- Can remote testing work, or must it be in-person?

---

## 3. Phase II: Test Environment Setup

### Process

1. **Provide the participant with:**
   - The URL of one starting point: `https://github.com/meta-organvm` (the meta-org)
   - A laptop with browser and terminal (with `gh` CLI, or browser-only)
   - The task sheet (Tasks 1-5, Phase III below)
   - A timer (administered by facilitator)

2. **Do NOT provide:**
   - This protocol document (facilitator-only)
   - Any verbal explanation of the system
   - Access to private repos, CLAUDE.md, MEMORY.md, or this corpus's `docs/` directory
   - Hints or guidance during the test (facilitator observes silently)

### Starter Research Questions
- Is the test environment representative of what a stranger would encounter?
- Are all public repos accessible without authentication?
- Are GitHub Pages sites live and accessible?
- Is the starting URL correct and descriptive?

---

## 4. Phase III: Task Execution

### Process

Administer five tasks with individual time limits. The facilitator observes silently.

**Task 1: Identify the System's Purpose (10 min)**
> "Starting from https://github.com/meta-organvm, figure out what this system is and what it's for. Write 2-3 sentences describing it."

Success: Identifies multi-organ/multi-repo system spanning multiple domains.

**Task 2: Find the Flagship Repo for ORGAN-III (8 min)**
> "ORGAN-III is the 'commerce' organ. Find its flagship repository — the most important repo in that organ."

Success: Navigates to correct org, identifies flagship, describes what it does.

**Task 3: Explain the Dependency Rules (10 min)**
> "The system has rules about which organs can depend on which. Find these rules and explain the key constraint."

Success: Finds governance rules, states the no-back-edge rule (I->II->III only).

**Task 4: Locate a Specific Essay (6 min)**
> "Find the essay that discusses AI transparency or honesty in how the system was built."

Success: Navigates to ORGAN-V, finds _posts/, identifies the essay.

**Task 5: Assess System Health (12 min)**
> "Does this system seem healthy and actively maintained, or abandoned? Give 3 specific pieces of evidence."

Success: 3 concrete, accurate observations based on evidence.

### Starter Research Questions
- Are the tasks calibrated to the right difficulty?
- Do the tasks cover all critical navigation paths?
- Is the time allocation realistic for each task?
- Would a different starting point yield different results?

---

## 5. Phase IV: Scoring

### Process

| Task | Max Points | Criteria |
|------|-----------|----------|
| Task 1 | 3 | 1 per success criterion (excluding time) |
| Task 2 | 3 | 1 per success criterion (excluding time) |
| Task 3 | 3 | 1 per success criterion (excluding time) |
| Task 4 | 3 | 1 per success criterion (excluding time) |
| Task 5 | 3 | 1 per success criterion (excluding time) |
| Time bonus | 5 | 1 point per task completed within time limit |
| **Total** | **20** | |

### Thresholds

| Score | Interpretation |
|-------|---------------|
| 16-20 | **PASS** — System is navigable by strangers |
| 11-15 | **PASS WITH NOTES** — Mostly navigable, specific improvements needed |
| 6-10 | **MARGINAL** — Significant documentation gaps |
| 0-5 | **FAIL** — System is not externally navigable |

---

## 6. Phase V: Post-Test Feedback

### Process

1. **Structured questions (1-5 scale):**
   - Clarity: "How clear was the system's purpose?"
   - Navigation: "How easy was it to find things?"
   - Documentation quality: "How well-written were the docs?"
   - Coherence: "Did it feel coordinated or unrelated?"
   - Credibility: "Does this seem real and maintained?"

2. **Open-ended questions:**
   - "What was the single most confusing thing?"
   - "What would have helped you most in the first 5 minutes?"
   - "If you had to explain this system in one sentence?"
   - "Would you star, fork, or bookmark any repos?"

---

## 7. Phase VI: Analysis & Remediation

### Process

1. **Complete the analysis template** with per-task scores, structured feedback, and key findings.
2. **Identify the biggest friction point** (from Q6).
3. **Identify the first-5-minutes gap** (from Q7).
4. **Generate 3 specific, actionable documentation changes** based on findings.
5. **Create GitHub issues** for each recommended change.

---

## 8. Output Artifacts

- Completed scoring sheet
- Structured + open-ended feedback responses
- Analysis summary with recommended actions
- GitHub issues for documentation improvements
- Updated gap register in `METADOC--sop-ecosystem.md` if new gaps found

---

## 9. Execution Cadence

| Trigger | Action |
|---------|--------|
| Pre-GRADUATED promotion | Full 5-task stranger test |
| Quarterly (if resources available) | 3-task abbreviated test (Tasks 1, 3, 5) |
| Major documentation overhaul | Full test to validate improvements |

---

## Appendix A: Analysis Template

```markdown
## Stranger Test Results — [Participant Pseudonym]

**Date:** YYYY-MM-DD
**Participant profile:** [e.g., "Senior backend engineer, 6 years experience"]
**Total score:** X / 20

### Per-Task Results
| Task | Score | Time | Notes |
|------|-------|------|-------|
| 1. System purpose | /3 | Xm | |
| 2. ORGAN-III flagship | /3 | Xm | |
| 3. Dependency rules | /3 | Xm | |
| 4. Essay location | /3 | Xm | |
| 5. System health | /3 | Xm | |
| Time bonus | /5 | | |

### Key Findings
1. **Biggest friction point:**
2. **First-5-minutes gap:**
3. **One-sentence summary:**

### Recommended Actions
1.
2.
3.
```

## Appendix B: Logistics

- **Recording:** Ask participant's permission to screen-record. If declined, facilitator takes timestamped notes.
- **Think-aloud:** Encourage (but don't require) the participant to think aloud.
- **No help:** Facilitator does not answer questions during the test. Stuck = data.
- **Duration:** ~46 minutes task time + ~15 minutes feedback = ~60 minutes total.
- **Compensation:** Budget for a thank-you gift.

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
