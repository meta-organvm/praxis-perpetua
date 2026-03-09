---
sop: true
name: background-task-resilience
scope: system
phase: any
triggers:
  - context:background-task
  - context:parallel-execution
complements:
  - multi-agent-workforce-planner
overrides: null
---
# SOP: Background Task Resilience

**Version:** 1.0.0 | **Date:** March 9, 2026 | **Status:** Active
**Scope:** Timeout budgeting, fallback planning, and health monitoring for background tasks in AI-assisted sessions, with resource constraints for memory-limited machines.

---

## 1. Ontological Purpose

Background tasks in AI-assisted sessions are fire-and-forget by default — they run until they succeed, fail, or get killed by the system. When a background pytest run times out after 5 minutes and is silently killed, the session loses its verification step. When two heavy builds run concurrently on a 16GB machine, both may OOM. When a task fails with no fallback plan, the session stalls.

This SOP ensures that every background task has a timeout, a fallback, and a resource budget — transforming background execution from "hope it works" to "guaranteed to complete or escalate."

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `coordination/tool_lock.py` (tool checkout line with lane capacity), `SOP--context-window-conservation.md` (background tasks preserve context)
**Precedent:** Multiple `status: killed` and `status: failed` background tasks (2026-03-08): engine test suite timeout, build killed, batch update failed.

---

## 2. Trigger

Execute this SOP whenever launching a background task (test suite, build, deployment, long-running script) during an AI-assisted session.

---

## 3. Phase I: Timeout Budget

### Process

1. **Assign an explicit timeout** to every background task:

   | Task Type | Default Timeout | Maximum Timeout |
   |-----------|----------------|-----------------|
   | Test suite (pytest) | 5 minutes | 10 minutes |
   | Build (npm build, cargo build) | 10 minutes | 15 minutes |
   | Deployment (fly deploy, vercel) | 10 minutes | 15 minutes |
   | Lint/typecheck | 3 minutes | 5 minutes |
   | Data processing | 5 minutes | 10 minutes |

2. **Set the timeout explicitly** in the tool call or command:
   - Claude Code Bash tool: use the `timeout` parameter
   - Shell: `timeout 300 pytest tests/ -v`

3. **Never use the default "no timeout"** — every background task must have an explicit time limit.

### Deliverables
- Timeout assigned before launch

---

## 4. Phase II: Fallback Plan

### Process

1. **Before launching, define what happens if the task fails or is killed:**

   | Outcome | Fallback Action |
   |---------|----------------|
   | **Timeout** | Re-run foreground with reduced scope (single test file, subset of build) |
   | **OOM killed** | Re-run with reduced parallelism or split into smaller batches |
   | **Test failure** | Review failures in foreground, fix, re-run targeted tests |
   | **Build failure** | Review errors in foreground, fix, re-run build |
   | **Unknown failure** | Escalate to user — do not retry blindly |

2. **Define the "good enough" threshold:**
   - If the full test suite times out, is running a targeted subset sufficient for the current task?
   - If the full build fails, can you verify the specific files you changed with a lighter check?

3. **Never retry the same failing command more than once** without changing something (scope, flags, environment).

### Deliverables
- Fallback plan stated before launch (even informally: "if this fails, I'll run the tests in foreground")

---

## 5. Phase III: Resource Budget

### Process

1. **Respect the machine's resource constraints** (16GB RAM, Apple Silicon M3):

   | Lane | Max Concurrent | Examples |
   |------|---------------|----------|
   | **Heavy** | 1 | pytest (full suite), npm build, cargo build |
   | **Medium** | 2 | ruff check, git commit, single-file test |
   | **Light** | Unlimited | git status, file reads, grep |

   These align with `coordination/tool_lock.py` lane definitions.

2. **Never run 2+ heavy tasks concurrently** on a 16GB machine:
   - Don't run pytest while building
   - Don't run two separate test suites simultaneously
   - Don't run a build while deploying

3. **Sequence heavy tasks** rather than parallelizing them:
   - Run tests → if pass → run build → if pass → deploy
   - Not: run tests AND build AND deploy simultaneously

### Deliverables
- Resource lane assigned before launch

---

## 6. Phase IV: Health Check

### Process

1. **Check task status at 50% of timeout:**
   - If the task is still running, that's expected — continue waiting
   - If the task has already failed, execute fallback immediately (don't wait for timeout)

2. **When the task completes, verify the result before proceeding:**
   - Tests: check pass count, not just exit code (0 tests collected = false pass)
   - Build: check output artifact exists and has reasonable size
   - Deploy: check health endpoint responds

3. **Log the result** for session review:
   - Task name, timeout, actual duration, outcome (success/failure/timeout/killed)

### Deliverables
- Task result verified

---

## 7. Output Artifacts

- No formal artifacts — this SOP governs behavioral discipline during sessions
- Session review should note any background task failures and how they were handled

---

## 8. Success Criteria

- Zero silent task kills (every killed task triggers a fallback)
- Zero OOM events from concurrent heavy tasks
- Background tasks complete within their timeout budget
- Failed tasks are diagnosed, not blindly retried

---

## 9. Anti-Patterns

- **"I'll run it in the background and check later"** — without a timeout, "later" may be "never" if the task hangs.
- **Running pytest and npm build simultaneously** — on 16GB, this is an OOM invitation.
- **Retrying a failed task without changing anything** — if it failed once, it will fail again. Diagnose first.
- **Ignoring a killed task** — a killed task means the verification step was skipped. Either re-run it foreground or explicitly accept the risk.

---

## 10. Cross-References

- `coordination/tool_lock.py` — tool checkout line with heavy/medium/light lane capacity
- `coordination/claims.py` — multi-agent claims registry prevents duplicate heavy tasks
- `SOP--context-window-conservation.md` — background tasks preserve main-thread context
- `SOP--session-self-critique.md` — session review includes background task outcome audit

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
