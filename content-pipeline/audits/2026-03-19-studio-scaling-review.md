# Studio Scaling Architecture Review

**Date:** 2026-03-19
**Scope:** Evaluate ORGANVM's eight-organ architecture against the multi-media production studio scaling trajectory
**Reviewed modules:** `coordination/` (claims, tool_lock), `governance/` (state_machine, dependency_graph, audit, rules, excavation), `seed/` (discover, graph, reader), `organ_config.py`, `registry/` (loader, query, update), `session/agents.py`

---

## Executive Summary

ORGANVM's architecture is remarkably well-prepared for its embryonic-to-studio scaling trajectory — but in a lopsided way. The **AI-agent coordination layer** (claims registry, tool checkout lines, handle assignment, resource capacity tracking) is already designed for multi-stream parallel work. The **governance layer** (promotion state machine, dependency graph, audit) is structurally sound and organ-agnostic. However, the **data layer** (registry-v2.json as single flat file, `~/.organvm/` as local-only state) and the **identity layer** (no collaborator model in seed.yaml, no role-based access) are hardcoded for a single operator on a single machine. Scaling to a studio requires changes to data storage, not to architectural patterns.

The organ model itself — Theoria/R&D, Poiesis/Production, Ergon/Commercial, Taxis/Operations, Logos/Editorial, Koinonia/Community, Kerygma/Distribution, Meta/Infrastructure — maps 1:1 to a production studio's departmental structure. This is not accidental: the system was designed as a one-person studio from the start, and the solo-operator phase is the embryonic form of the multi-person one.

---

## 1. Patterns That Already Scale to Multi-Person Teams

### 1.1 Multi-Agent Coordination (coordination/claims.py, tool_lock.py)

**Already team-ready:** The punch-in/punch-out claims system (`claims.py:104-174`) is designed for *any number* of concurrent streams — human or AI. Key scaling features:

- **Agent-type polymorphism:** The handle pool system (`_HANDLE_POOLS`, line 46) already includes a `"human"` pool alongside claude/gemini/codex. The `WorkClaim` dataclass accepts `agent: str` without restriction. A human collaborator gets the same first-class presence as an AI agent.
- **Area-of-influence model:** Claims declare organs, repos, files, and modules as areas of influence. Conflict detection (`check_conflicts`, line 234) finds overlaps at any granularity. This is a primitive but functional **distributed lock** for collaborative work.
- **Resource capacity tracking:** `capacity_status()` budgets work against a machine's physical limits (DEFAULT_CAPACITY=6 units for 16GB M3). In a studio context, each machine could advertise its own capacity.
- **Test obligations:** The `prove_sweep()` pattern (line 582) — where builders declare tests and a separate prover session runs them — is a natural fit for a CI/CD model where one integration runner validates all team output.
- **Append-only JSONL:** The claims file (`~/.organvm/claims.jsonl`) uses an append-only event log, not read-modify-write. This is inherently safer for concurrent access than a single mutable JSON file.

**Scaling gap:** The claims file lives at `~/.organvm/` — a local-only path. Multi-machine scaling requires moving this to a shared location (network FS, database, or a distributed event log like Redis Streams).

### 1.2 Tool Checkout Line (coordination/tool_lock.py)

**Already team-ready:** Command classification (`classify_command`, line 57) routes heavy commands (pytest, build) through a single-occupancy lane and medium commands (ruff, git commit) through a 2-occupancy lane. This is a **concurrency limiter** — the pattern transfers directly to team-scale CI queueing.

**Scaling gap:** The limits (heavy=1, medium=2) are calibrated for one machine. A studio would need per-machine or per-cluster limits, configurable via the tool checkout system rather than hardcoded constants.

### 1.3 Governance State Machine (governance/state_machine.py)

**Already team-ready:** The promotion pipeline (LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED) is:

- **Data-driven:** Transitions load from `governance-rules.json` (line 47-98), with a hardcoded fallback. A studio can evolve the rules without changing code.
- **Event-emitting:** Every transition emits to both the EventSpine and the pulse bus (line 206-218). Downstream systems (dashboard, notifications, Kerygma distribution) react automatically.
- **Actor-tracked:** `execute_transition()` accepts an `actor` parameter (line 186). Today it's `"cli"` — tomorrow it could be `"chris"`, `"review-bot"`, or `"organ-lead-poiesis"`.
- **Back-transition safe:** The table allows CANDIDATE → LOCAL and PUBLIC_PROCESS → CANDIDATE, enabling "send back for rework" without state corruption.

**Scaling gap:** No authorization model. Any caller can execute any valid transition. A studio needs role gates: "only the organ lead can promote to GRADUATED."

### 1.4 Dependency Graph (governance/dependency_graph.py)

**Already team-ready:** The unidirectional flow constraint (I→II→III, no back-edges) is enforced programmatically via `ORGAN_LEVELS` and `RESTRICTED_LEVELS`. This is an architectural invariant that protects the system regardless of how many people are pushing code. The cycle detection (DFS with coloring, line 120-134) catches violations that would be invisible in code review.

**Scaling bonus:** This module is the single most valuable governance asset in a team context. Without it, independent teams working in parallel would inevitably create circular dependencies that violate the organ hierarchy.

### 1.5 Organ Config as Data (organ_config.py)

**Already team-ready:** `organ_config.py` is a pure data module with a data-driven topology loader (line 87-151). Organ definitions can be externalized to `governance-rules.json` or a dedicated `organ-topology.yaml`. Adding a new organ (e.g., splitting Ergon into Products and Services) is a config change, not a code change.

### 1.6 Multi-Agent Session Parsing (session/agents.py)

**Already team-ready:** The session discovery system already handles three distinct agent formats (Claude, Gemini, Codex) with format-specific parsers and a unified `AgentSession` dataclass. The pattern extends naturally: adding a "human" agent type for manual session logs would follow the same format-detection → parse → normalize pipeline.

### 1.7 Governance Audit (governance/audit.py)

**Already team-ready:** `run_audit()` is a comprehensive automated governance check (dependency cycles, back-edges, staleness, CI compliance, dictum violations). It runs against registry data, not workspace state, so it can audit a team's combined output without requiring physical access to every workstation. The severity model (critical/warning/info) with configurable thresholds via `governance-rules.json` gives an organ lead granular control.

---

## 2. Patterns Hardcoded for Single-Operator

### 2.1 registry-v2.json as Flat File (CRITICAL)

**Problem:** The entire system's source of truth is a single 2,200-line JSON file with no concurrency model. `save_registry()` in `loader.py` does a full-file `json.dump()` write (line 65-67). Two humans editing registry fields simultaneously will produce merge conflicts in git, or worse, silent data loss if one overwrites the other.

**The 50-repo guard** (line 11, `_MIN_REPO_COUNT = 50`) protects against test data leaking into production, but does nothing against concurrent-edit corruption.

**Studio impact:** In a studio with organ leads, each lead needs to update their organ's repos (status, CI flags, validation dates). If two leads run `organvm registry update` at the same time, one write wins and the other is lost.

**Migration path:**
1. **Near-term (Chris onboarding):** Use git branching discipline — all registry updates go through PRs. The file still merges cleanly if edits touch different organs.
2. **Medium-term:** Split registry into per-organ files (`registry/organ-i.json`, etc.) that can be independently edited. The engine's `load_registry()` merges them at read time.
3. **Long-term:** Replace flat JSON with a lightweight database (SQLite, or Neon Postgres) with per-field atomic updates. The current `all_repos()` / `find_repo()` API in `query.py` already abstracts the storage layer — callers wouldn't need to change.

### 2.2 ~/.organvm/ as Local-Only State

**Problem:** Claims (`claims.jsonl`), ontologia entities (`entities.json`, `names.jsonl`, `events.jsonl`), and tool checkouts all live under `~/.organvm/` — visible only to the local machine. The coordination layer can't coordinate what it can't see.

**Studio impact:** If Chris is running builds on his machine while Claude-forge is running tests on yours, neither knows about the other. The work_board shows only local streams.

**Migration path:**
1. **Near-term:** Move claims to a shared git-tracked location within the superproject (e.g., `meta-organvm/.coordination/claims.jsonl`). Pull before read, commit after write.
2. **Medium-term:** Replace JSONL with a lightweight shared-state service (Redis, or a coordination MCP server that all agents connect to).

### 2.3 Workspace Path Assumptions

**Problem:** `paths.py` resolves `workspace_root()` from `ORGANVM_WORKSPACE_DIR` (default `~/Workspace`). `discover_seeds()` walks `~/Workspace/<org>/<repo>/seed.yaml`. The entire seed/registry discovery model assumes one canonical workspace on one machine.

**Studio impact:** Chris's workspace will be at `~/Workspace/` too, but it may contain only ORGAN-II repos. The system assumes every workspace has every organ — there's no concept of a "partial workspace" or "organ-scoped checkout."

**Migration path:** Add a `workspace-manifest.yaml` at the workspace root declaring which organs are present. `discover_seeds()` reads this manifest instead of scanning all organ dirs.

### 2.4 No Collaborator Identity in seed.yaml

**Problem:** `seed.yaml` declares `organ`, `repo`, `org`, `metadata`, `agents` (CI triggers), `produces`, `consumes`, and `subscriptions`. There is no `collaborators`, `owners`, or `access` section. The system doesn't know who is responsible for what.

**Studio impact:** When Chris joins, there's no way to express "Chris owns ORGAN-II" or "only Chris can approve Poiesis promotions" in the data model.

### 2.5 No Role/Permission Model in Governance

**Problem:** `execute_transition()` in `state_machine.py` accepts an `actor` string (line 186) but doesn't validate it against any permission table. Any actor can execute any valid transition. `run_audit()` checks system health but not authorization.

**Studio impact:** A junior collaborator could accidentally promote a repo to GRADUATED without organ-lead approval.

### 2.6 Single-Machine Resource Budget

**Problem:** `DEFAULT_CAPACITY = 6` in `claims.py` and the tool checkout limits (heavy=1, medium=2) are calibrated for one 16GB M3. These are module-level constants, not configurable per-machine values.

### 2.7 Hardcoded Agent Paths

**Problem:** Session discovery paths are hardcoded per-agent:
```python
CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"
GEMINI_TMP_DIR = Path.home() / ".gemini" / "tmp"
CODEX_SESSIONS_DIR = Path.home() / ".codex" / "sessions"
```
These are local to the operator's home directory. In a studio, session transcripts from other team members would need to be aggregated for audit.

---

## 3. Collaboration Bottlenecks

### 3.1 registry-v2.json Merge Conflicts (SEVERITY: HIGH)

This is the #1 bottleneck. The registry is a single JSON file where changes to one organ's repos affect line numbers throughout the file. Git's line-based merge strategy produces false conflicts when two people edit different organs.

**Concrete scenario:** Chris updates `ORGAN-II/performance-engine` status to CANDIDATE. You simultaneously update `META-ORGANVM/system-dashboard` CI flag. Both edits are valid and non-overlapping, but git sees adjacent line changes in a 2,200-line file and flags a merge conflict.

**Mitigation sequence:**
1. Per-organ file split (eliminates cross-organ conflicts)
2. Per-repo file split (eliminates within-organ conflicts for large organs)
3. Database backend (eliminates file-based conflicts entirely)

### 3.2 governance-rules.json as Shared Config (SEVERITY: MEDIUM)

The governance rules file controls promotion transitions, audit thresholds, and organ-specific requirements. Changes to governance rules affect every organ. In a studio, governance evolution needs a formal change-proposal process (RFC → review → merge), not ad-hoc edits.

### 3.3 Superproject Submodule Pinning (SEVERITY: MEDIUM)

`organvm git sync-organ` updates submodule pointers in the superproject. If two organ leads sync their organs simultaneously, the superproject commit conflicts. This is a git-native problem but is amplified by the superproject model.

**Mitigation:** Each organ lead syncs only their organ's pointers. A scheduled automation (CI or cron) consolidates all organ syncs into a single daily commit.

### 3.4 Context File Generation (SEVERITY: LOW)

`contextmd/generator.py` auto-generates CLAUDE.md/GEMINI.md/AGENTS.md across all repos. If run by two people simultaneously, it produces identical output (deterministic generation from registry data). The bottleneck is less about conflicts and more about staleness — if Chris generates context files from an outdated local registry, his repos get stale context.

**Mitigation:** Context sync should always read from the canonical (git-tracked) registry, not a local copy.

---

## 4. How seed.yaml Should Evolve

Current seed.yaml format (engine example):

```yaml
schema_version: "1.0"
organ: Meta
repo: organvm-engine
org: meta-organvm
metadata:
  implementation_status: ACTIVE
  tier: flagship
  promotion_status: CANDIDATE
agents:
  - name: ci
    trigger: on_push
    workflow: .github/workflows/ci.yml
produces:
  - type: governance-policy
    consumers: [ORGAN-IV, META-ORGANVM]
consumes:
  - type: registry
    source: META-ORGANVM
subscriptions:
  - event: registry.updated
    source: META-ORGANVM
```

### Proposed additions for v1.1:

```yaml
schema_version: "1.1"

# NEW: Ownership and access
ownership:
  lead: "4jp"                              # Primary responsible human
  collaborators:
    - handle: "chris"
      role: contributor                    # contributor | reviewer | lead
      access: [commit, pr]                 # commit, pr, promote, audit, release
      organs: [ORGAN-II]                   # scope limitation
      since: "2026-04-01"

  # AI agent access — evolves from current "agents" section
  ai_agents:
    - type: claude
      access: [read, edit, pr]             # no promote, no registry-write
      scope: "code and tests"
    - type: gemini
      access: [read, research]
      scope: "documentation and research"

# NEW: Review requirements (gates for promotion)
review:
  promote_to_candidate:
    requires: [ci_pass, lead_approval]
  promote_to_public_process:
    requires: [ci_pass, lead_approval, code_review]
  promote_to_graduated:
    requires: [ci_pass, organ_lead_approval, stranger_test]

# EVOLVED: Agents section becomes more specific
agents:
  - name: ci
    trigger: on_push
    workflow: .github/workflows/ci.yml
  - name: deploy
    trigger: on_promote:PUBLIC_PROCESS
    workflow: .github/workflows/deploy.yml
    requires_approval: true                # NEW: human gate
```

### Key design decisions:

1. **`ownership.lead`** is always a single human. This maps to the "organ lead" role in the studio model.
2. **Collaborator access is declarative**, not imperative. The engine reads these declarations at promotion time and enforces gates.
3. **AI agents get explicit access scopes.** Today all agents have implicit full access. In a studio, you want to constrain which AI can modify which repos.
4. **Review requirements are per-transition**, not global. Different repos within the same organ can have different promotion gates.
5. **Backward compatible:** All new sections are optional. Existing v1.0 seeds work unchanged — the engine treats missing `ownership` as "solo operator, full access."

---

## 5. Onboarding Path for Chris (First Collaborator)

### 5.1 What Chris Needs Access To

**Full access (read + write + commit):**
- ORGAN-II repos (Poiesis — his creative domain)
- His own session transcripts and claims
- seed.yaml files in ORGAN-II repos

**Read access (understand the system, can't modify):**
- registry-v2.json (understands the full system graph)
- governance-rules.json (understands promotion rules)
- ORGAN-I repos (Theoria feeds Poiesis — he needs to understand upstream)
- META repos (engine, dashboard, MCP server — tooling he uses)

**No access / shielded:**
- `intake/` directory (untrusted personal material)
- `organvm-i-theoria/my-knowledge-base/intake/canonical/sources/curated-sources/` (personal data archives)
- `~/.organvm/` on your machine (your local agent state)
- API keys, secrets, Stripe/Vercel credentials
- Revenue model details in registry unless discussed

### 5.2 Minimal Viable Onboarding (Week 1)

```
1. Fork or clone ORGAN-II repos to his machine
2. Install organvm-engine in dev mode (pip install -e ".[dev]")
3. Set ORGANVM_WORKSPACE_DIR to his workspace
4. Run `organvm registry show <repo>` to verify he can read the registry
5. Run `organvm governance audit` to see system health
6. Create his first seed.yaml update via PR
7. Set up his agent handle pool entry (add "chris" to _HANDLE_POOLS["human"])
```

### 5.3 Progressive Onboarding (Weeks 2-4)

```
Week 2: Contribute to ORGAN-II, use PR workflow for all changes
Week 3: Get reviewer access — can approve PRs in ORGAN-II
Week 4: Get promoter access — can run `organvm governance promote` for ORGAN-II repos
```

### 5.4 Technical Prerequisites

1. **GitHub org membership:** Add Chris to `omni-dromenon-machina` (ORGAN-II org) with write access
2. **Branch protection:** Enable on ORGAN-II repos — require PR reviews before merge
3. **Registry update workflow:** Chris proposes registry changes via PR to `organvm-corpvs-testamentvm`. You review and merge. This prevents registry corruption while Chris learns the system.
4. **Separate claims file:** Until shared coordination is built, Chris's `~/.organvm/claims.jsonl` is independent. This is fine — his work is in ORGAN-II, yours is elsewhere, so conflict is unlikely.

### 5.5 What Should Be Shielded (and Why)

| Shielded From Chris | Reason |
|---|---|
| Personal data in intake/ and curated-sources/ | Privacy — personal archives |
| Revenue model details | Business sensitivity until partnership terms are set |
| Deployment credentials (Vercel, Stripe, Neon) | Security — shared secrets require trust escalation |
| System-wide governance rule changes | Architectural authority — only the system architect should modify cross-organ rules during the embryonic phase |
| Promotion beyond ORGAN-II | Scope — Chris's authority is organ-scoped, not system-wide |

---

## 6. Promotion State Machine: Solo Operator to Studio with Organ Leads

### 6.1 Current State Machine (Solo Operator)

```
INCUBATOR → LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED
```

No role gates. The operator (you) controls all transitions across all organs. Governance enforces structural rules (valid transitions, dependency graph, CI checks) but not authorization.

### 6.2 Intermediate State Machine (Solo + First Collaborator)

Add a **soft authorization layer** without changing the state machine itself:

```
Transition            | Gate                          | Enforced By
──────────────────────┼───────────────────────────────┼──────────────
→ CANDIDATE           | CI pass + actor = {lead, arch} | seed.yaml review section
→ PUBLIC_PROCESS      | CI pass + code review (1 human)| GitHub PR protection
→ GRADUATED           | CI pass + organ lead + architect| New: architect approval gate
→ ARCHIVED            | organ lead OR architect         | seed.yaml review section
```

**Implementation:** Add an `authorize_transition(actor, repo, target_state, seed)` function to `governance/` that reads the `review` section from `seed.yaml` and validates the actor's role against the required gates. `execute_transition()` calls this before proceeding.

### 6.3 Target State Machine (Studio with Organ Leads)

```
                              ┌──────────────────────────────────┐
                              │       STUDIO GOVERNANCE          │
                              │                                  │
                              │  System Architect (you)          │
                              │  ├── Sets governance-rules.json  │
                              │  ├── Approves cross-organ edges  │
                              │  └── Promotes to GRADUATED       │
                              │                                  │
                              │  Organ Leads                     │
                              │  ├── Own their organ's repos     │
                              │  ├── Promote within their organ  │
                              │  ├── Approve PRs in their organ  │
                              │  └── Run organ-scoped audits     │
                              │                                  │
                              │  Contributors                    │
                              │  ├── Write code, submit PRs      │
                              │  ├── Run local tests             │
                              │  └── Propose promotions (request)│
                              │                                  │
                              │  AI Agents                       │
                              │  ├── Generate volume (code, docs)│
                              │  ├── Run analysis (audit, metrics│
                              │  └── Cannot promote or merge     │
                              └──────────────────────────────────┘
```

**Roles and their promotion authority:**

| Role | LOCAL→CAND | CAND→PUB | PUB→GRAD | →ARCHIVED |
|------|-----------|----------|----------|-----------|
| Contributor | Request | — | — | — |
| Organ Lead | Approve (own organ) | Approve (own organ) | Request | Approve (own organ) |
| System Architect | Approve (all) | Approve (all) | Approve (all) | Approve (all) |
| AI Agent | — | — | — | — |

### 6.4 Migration Path (Phased)

**Phase 0 — Now (solo operator):** No changes needed. Current system works.

**Phase 1 — First collaborator (Chris):**
- Add `ownership` section to ORGAN-II seed.yaml files
- Enable GitHub branch protection on ORGAN-II repos
- Registry changes go through PRs only
- Add `authorize_transition()` to governance module (advisory mode — logs warnings, doesn't block)

**Phase 2 — Organ leads (3-5 people):**
- Split registry into per-organ files
- Move claims to shared coordination backend
- `authorize_transition()` moves to enforcing mode
- Each organ lead gets a `role: lead` entry in their organ's seed.yaml files
- Dashboard shows per-organ ownership and activity

**Phase 3 — Full studio (10+ people):**
- Database-backed registry with per-field atomic updates
- Centralized coordination service (MCP server or dedicated service)
- Formal onboarding pipeline with role assignment
- Audit trail: every governance action recorded with actor, timestamp, justification
- Cross-organ dependency changes require architectural review (not just organ-lead approval)

---

## 7. Architectural Strengths That Transcend Scale

These patterns work at any team size and should be preserved:

1. **Unidirectional dependency flow (I→II→III).** This is the organ system's structural immune system. It prevents the dependency spaghetti that kills large codebases. Enforce it more, not less, as the team grows.

2. **Event-driven architecture (pulse bus + EventSpine).** Every state change emits events. This decouples the governance core from its consumers (dashboard, notifications, Kerygma distribution). New team tools (Slack bots, CI triggers, review assignment) plug in as event consumers.

3. **Seed.yaml as declarative contract.** Each repo declares what it produces, consumes, and subscribes to. This is a service mesh pattern applied to a creative system. As the studio grows, seeds become the API surface between organs.

4. **Data-driven governance.** Transitions, audit thresholds, organ requirements, and organ topology all load from JSON/YAML config. The code is a state machine interpreter, not a hardcoded rule set. A studio can evolve its rules without deploying new code.

5. **Separation of concerns by organ.** Each organ has its own GitHub org, its own repos, its own directory, its own aesthetic identity. This is natural departmental isolation — it already looks like a studio org chart.

---

## 8. Recommended Priority Actions

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| **P0** | Add `ownership` section to seed.yaml schema (v1.1) | 2-3 hours | Enables all role-based features |
| **P0** | Enable branch protection on ORGAN-II repos | 30 min | Prevents accidental direct pushes |
| **P1** | Add `authorize_transition()` advisory function | 4-6 hours | Logs unauthorized promotion attempts |
| **P1** | Split registry into per-organ files with merge loader | 6-8 hours | Eliminates cross-organ merge conflicts |
| **P2** | Add `workspace-manifest.yaml` for partial workspaces | 2-3 hours | Enables Chris's organ-scoped checkout |
| **P2** | Make resource capacity configurable via env/config | 1-2 hours | Supports multi-machine capacity budgets |
| **P3** | Move claims to shared coordination backend | 8-12 hours | Enables cross-machine work visibility |
| **P3** | Database-backed registry (Neon Postgres or SQLite) | 12-20 hours | Full concurrent-access safety |

---

## Appendix A: Module-by-Module Scaling Assessment

| Module | Scale-Ready? | Key Limitation | Fix Complexity |
|--------|-------------|----------------|----------------|
| `coordination/claims.py` | 80% | Local-only state | Medium (shared backend) |
| `coordination/tool_lock.py` | 70% | Hardcoded limits | Low (config file) |
| `governance/state_machine.py` | 90% | No auth gates | Low (advisory function) |
| `governance/dependency_graph.py` | 95% | None significant | — |
| `governance/audit.py` | 85% | No per-organ scoping | Low |
| `governance/rules.py` | 90% | Single-file governance | Low (already data-driven) |
| `governance/excavation.py` | 85% | Workspace path assumptions | Low |
| `seed/discover.py` | 60% | Full-workspace assumption | Medium (manifest) |
| `seed/graph.py` | 80% | None significant | — |
| `seed/reader.py` | 70% | No ownership fields | Low (schema update) |
| `organ_config.py` | 95% | Already data-driven | — |
| `registry/loader.py` | 40% | Single flat file, no concurrency | High (split or DB) |
| `session/agents.py` | 50% | Local-only session paths | Medium (aggregation) |

## Appendix B: The Studio Organ Map

```
┌──────────────────────────────────────────────────────────────┐
│                    ORGANVM STUDIO                             │
│                                                              │
│  ORGAN-I (Theoria)        →  R&D / Innovation Lab            │
│  Lead: System Architect       Foundational theory, engines   │
│                                                              │
│  ORGAN-II (Poiesis)       →  Production / Creative           │
│  Lead: Chris (first hire)     Generative art, performance    │
│                                                              │
│  ORGAN-III (Ergon)        →  Products / Commercial           │
│  Lead: TBD                    SaaS tools, developer utils    │
│                                                              │
│  ORGAN-IV (Taxis)         →  Operations / Studio Management  │
│  Lead: System Architect       Orchestration, governance, AI  │
│                                                              │
│  ORGAN-V (Logos)          →  Publishing / Editorial          │
│  Lead: System Architect       Essays, discourse, analytics   │
│                                                              │
│  ORGAN-VI (Koinonia)      →  Community / Audience Dev        │
│  Lead: TBD                    Reading groups, salons         │
│                                                              │
│  ORGAN-VII (Kerygma)      →  Marketing / Distribution       │
│  Lead: TBD                    POSSE, social automation       │
│                                                              │
│  META (ORGAN-VIII)        →  Studio Infrastructure           │
│  Lead: System Architect       Engine, schemas, dashboard     │
└──────────────────────────────────────────────────────────────┘
```
