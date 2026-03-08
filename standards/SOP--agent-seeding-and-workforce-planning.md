---
sop: true
name: agent-seeding-and-workforce-planning
scope: system
phase: foundation
triggers:
  - context:large-feature-set
  - context:multi-repo-initiative
complements:
  - planning-and-roadmapping
  - cross-agent-handoff
overrides: null
---
# SOP: Agent Seeding & Workforce Planning

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Decomposing large feature sets into parallel agent workstreams for concurrent execution across Claude Code, Gemini, Codex, and other AI agents.

---

## 1. Ontological Purpose

A single agent working sequentially through a 50-task feature set is a bottleneck disguised as productivity. Agent seeding is the practice of analyzing task dependencies, identifying parallelizable workstreams, and assigning specialized agent instances to maximize throughput without sacrificing coherence.

This is not "throw agents at the problem." It is workforce architecture: understanding which tasks can run independently, which require sequential handoff, and which agent type is best suited to each workstream.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--planning-and-roadmapping.md` (plans feed workstream decomposition), `SOP--cross-agent-handoff.md` (handoff protocol between agents)

---

## 2. Trigger

Execute this SOP when:
- A plan contains >10 tasks with identifiable parallel paths
- Multiple repos need concurrent work (cross-organ initiatives)
- A deadline requires throughput that exceeds single-agent capacity
- A feature set spans distinct domains (frontend + backend + docs + tests)

**Exception:** Single-stream work that fits in one session does not require workforce planning.

---

## 3. Phase I: Dependency Analysis

**Goal:** Map task dependencies to find parallelizable streams.

### Process

1. **Start from the atomized plan** (output of `SOP--planning-and-roadmapping.md` Phase III)
2. **Build a dependency graph:**
   - Which tasks must complete before others can start?
   - Which tasks are independent (no shared file mutations)?
   - Which tasks share a common dependency but are otherwise independent?
3. **Identify workstream candidates:**
   - Group independent tasks into streams
   - Name each stream by its domain: `stream-api`, `stream-frontend`, `stream-docs`, `stream-tests`
4. **Identify synchronization points:**
   - Where do streams need to merge? (e.g., API + frontend integration test)
   - What is the handoff protocol at each sync point?

### Output
A workstream decomposition table: `Stream | Tasks | Dependencies | Sync Points`

---

## 4. Phase II: Agent Assignment

**Goal:** Match agent types to workstream requirements.

### Process

1. **Assess each stream's requirements:**
   - Code generation → Claude Code (worktree isolation), Codex
   - Research / analysis → Claude (main context), Gemini
   - Documentation → Claude (main context)
   - Testing → Claude Code (background agent)
   - File-heavy operations → Agents with filesystem access
2. **Assign agents to streams:**
   - One agent per stream (avoid shared-context collisions)
   - Use worktree isolation for code-generation streams
   - Use background agents for independent verification tasks
3. **Define handoff artifacts** per stream:
   - What file(s) does this stream produce?
   - What format enables the next stream to consume the output?
   - Where are outputs written? (branch, directory, JSONL)

### Output
An assignment table: `Stream | Agent Type | Isolation | Output Artifacts`

---

## 5. Phase III: Execution

**Goal:** Launch and monitor parallel workstreams.

### Process

1. **Launch streams in dependency order:**
   - Start independent streams concurrently
   - Queue dependent streams to auto-start when prerequisites complete
2. **Monitor progress:**
   - Check agent outputs at sync points
   - Verify no file conflicts (two agents writing the same file)
   - Run `git status` across worktrees to detect drift
3. **Handle failures:**
   - If a stream fails, assess blast radius on dependent streams
   - Retry failed stream with adjusted context before escalating
   - Log failures for `SOP--session-self-critique.md` review

### Output
Completed workstreams with artifacts at designated output locations.

---

## 6. Phase IV: Convergence

**Goal:** Merge parallel work into a coherent whole.

### Process

1. **Merge worktree branches** into the main branch in dependency order
2. **Run integration tests** that span multiple streams
3. **Resolve conflicts** — if two streams modified adjacent code, reconcile manually
4. **Run `organvm atoms reconcile`** to update task completion status
5. **Archive the workforce plan** in `.claude/plans/` with a `-workforce` suffix

### Output
Merged codebase with all streams integrated and tested.

---

## 7. Starter Research Questions

- What is the critical path through the dependency graph?
- Which streams have zero dependencies and can start immediately?
- Are there resource constraints (API rate limits, memory) that limit concurrency?
- What is the cost of a stream failure? Can failed streams be retried independently?

---

## 8. Output Artifacts

- Workstream decomposition table
- Agent assignment table
- Completed stream outputs (code, docs, tests)
- Workforce plan file (`YYYY-MM-DD-{slug}-workforce.md`)

---

## 9. Verification

- [ ] Dependency graph identifies all task-to-task dependencies
- [ ] No two streams mutate the same file without a sync point
- [ ] Each stream has a clear agent assignment and isolation strategy
- [ ] Handoff artifacts are defined for every sync point
- [ ] Post-convergence integration tests pass

---

## 10. Prompt Examples

Representative prompts from clipboard history that trigger this pattern:

### Example 1

> plan extensive/exhaustive multi-agent parallel workforce streams to conquer the full
> feature set existing theoretically/specd;

### Example 2

> Think of it this way: same actor, many masks, and each mask plays differently depending
> on which stage and which moment of the life-run it appears on.

### Example 3

> I will give you a reusable schema you can drop into any future Claude Code agent or
> Gemini Deep Research session to seed the context correctly.
