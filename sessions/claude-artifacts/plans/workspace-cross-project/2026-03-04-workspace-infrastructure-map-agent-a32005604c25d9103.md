# Workspace Infrastructure Map
**Date**: 2026-03-04  
**Status**: Complete — Exploration Phase  
**Agent ID**: a32005604c25d9103

---

## Executive Summary

The `/Users/4jp/Workspace/` contains a fully operational **eight-organ creative-institutional system** with ~80 documented repositories across 8 GitHub organizations. Three distinct control mechanisms already exist that a unified "command center" would integrate:

1. **system-dashboard** (meta-organvm) — Live web UI for system monitoring
2. **orchestration-start-here** (organvm-iv-taxis) — Governance hub with registry & workflows  
3. **organvm-engine** (meta-organvm) — Programmatic orchestration CLI

---

## System Architecture Overview

### Eight-Organ Structure
- **ORGAN-I (Theoria)** — Theory & foundational knowledge (18 repos)
- **ORGAN-II (Poiesis)** — Creative systems & generative patterns (22 repos)
- **ORGAN-III (Ergon)** — Practical work & execution (21 repos)
- **ORGAN-IV (Taxis)** — Orchestration & governance (9 repos) ← **Key coordination point**
- **ORGAN-V (Logos)** — Essays & narrative (2 repos)
- **ORGAN-VI (Koinonia)** — Community & collaboration (3 repos)
- **ORGAN-VII (Kerygma)** — Amplification & distribution (4 repos)
- **META-ORGANVM (Meta)** — System governance & tooling (7 repos)

**Total**: 79 repos on GitHub + 1 locally planned = 80 entries in registry-v2.json

### Governance Model
- **Single Source of Truth**: `organvm-corpvs-testamentvm/registry-v2.json` (80 entries)
- **Unidirectional Dependencies**: I→II→III only (ORGAN-IV orchestrates all)
- **Promotion State Machine**: LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED
- **Constitutional Framework**: 6 articles + 4 amendments + 4 quality gates (governance-rules.json)

---

## Existing Control Mechanisms (Primary Entry Points)

### 1. **system-dashboard** (FastAPI Web UI)
**Location**: `/Users/4jp/Workspace/meta-organvm/system-dashboard/`  
**Type**: Live web application  
**Stack**: FastAPI, Jinja2 templating, HTMX for interactivity  
**Aesthetic**: Brutalist CMYK design  

**Six Pages:**
- `/health/` — System health overview
- `/registry/` — Repository browser (searchable, filterable)
- `/graph/` — Dependency graph visualization
- `/soak/` — Stress test monitoring
- `/essays/` — Meta-system essay feed (5 essays, ~40K words)
- `/omega/` — Scorecard & metrics dashboard

**API Endpoints:**
- `GET /health/api` — System health metrics
- `GET /graph/api` — Dependency graph (JSON)
- `GET /registry/api/{repo_name}` — Individual repo details

**How to Run:**
```bash
cd /Users/4jp/Workspace/meta-organvm/system-dashboard
pip install -e ".[dev]"
organvm-dashboard  # Starts on http://localhost:8000
```

**Key Feature**: This is the **primary unified monitoring surface** currently deployed.

---

### 2. **orchestration-start-here** (Governance Hub)
**Location**: `/Users/4jp/Workspace/organvm-iv-taxis/orchestration-start-here/`  
**Type**: Repository + workflows + validation scripts  
**Role**: Central enforcement point for all cross-organ governance  

**Key Files:**
- `registry.json` — 80 repo entries with status, tier, dependencies, promotion state
- `governance-rules.json` — Constitutional framework (6 articles + 4 amendments + 4 gates)
- `audit-report.md` — Monthly system health snapshot
- `src/agents/` — Governance agents (if any)
- `src/dreamcatcher/` — Monitoring/catch agents (if any)

**Five GitHub Actions Workflows:**
1. `validate-dependencies.yml` — Enforces unidirectional dependency flow (I→II→III only)
2. `monthly-organ-audit.yml` — System-wide health check + issue creation
3. `promote-repo.yml` — Automated registry promotion with validation
4. `publish-process.yml` — README extraction + essay scaffolding
5. `distribute-content.yml` — POSSE distribution (Mastodon, Discord)

**Three Validation Scripts:**
```bash
cd /Users/4jp/Workspace/organvm-iv-taxis/orchestration-start-here

python3 scripts/validate-deps.py         # Check dependency graph
python3 scripts/organ-audit.py           # System-wide audit
python3 scripts/calculate-metrics.py     # Registry metrics
```

**Key Feature**: This is the **enforcement and automation layer** — single point of truth for all governance.

---

### 3. **organvm-engine** (Programmatic Orchestration)
**Location**: `/Users/4jp/Workspace/meta-organvm/organvm-engine/`  
**Type**: Python package with unified CLI  
**Role**: Consolidates ~30 standalone scripts into proper installable package  

**CLI Groups (7 command namespaces):**
```bash
organvm registry <show|list|validate|update>        # Query/update repos
organvm governance <audit|check-deps|promote>       # Governance operations
organvm seed <discover|validate|graph>              # Seed.yaml discovery
organvm metrics <calculate|propagate|refresh>       # Metrics computation
organvm dispatch <validate>                         # Event dispatch
organvm git <init|add-submodule|sync|status>       # Git superproject ops
organvm context <sync>                              # CLAUDE.md sync
```

**Key Modules:**
- `registry/` — Load/save registry-v2.json, query repos, validation
- `governance/` — State machine, dependency graph, audit, impact analysis
- `seed/` — Discover seed.yaml files, build produces/consumes graph
- `metrics/` — Calculate from registry, propagate into markdown/JSON
- `dispatch/` — Event routing and cascade
- `git/` — Superproject management (init, add-submodule, sync, status)
- `contextmd/` — Auto-generate CLAUDE.md/GEMINI.md/AGENTS.md across repos

**How to Use:**
```bash
cd /Users/4jp/Workspace/meta-organvm/organvm-engine
pip install -e ".[dev]"
organvm registry list --organ IV --status GRADUATED
organvm governance check-deps
organvm context sync --organ IV
```

**Key Feature**: This is the **programmatic orchestration engine** — all automation runs through this.

---

### 4. **organvm-mcp-server** (MCP Interface)
**Location**: `/Users/4jp/Workspace/meta-organvm/organvm-mcp-server/`  
**Type**: MCP (Model Context Protocol) server  
**Role**: Exposes entire system graph to Claude sessions  

**16 Tools Across 5 Groups:**

**Registry Group** (3 tools)
- `organvm_query_registry` — Search repos by name, organ, status, tier
- `organvm_get_repo` — Get detailed repo info
- `organvm_list_organs` — List all 8 organs with counts

**Seeds Group** (4 tools)
- `organvm_get_seed` — Get seed.yaml for a repo
- `organvm_find_edges` — Find produces/consumes relationships
- `organvm_get_event_contract` — Query event subscriptions
- `organvm_list_events` — List all system events

**Graph Group** (3 tools)
- `organvm_trace_dependencies` — Full dependency path analysis
- `organvm_check_dependency` — Validate a specific dependency
- `organvm_get_dependency_graph` — Export full graph (JSON)

**Health Group** (5 tools)
- `organvm_system_health` — Overall system metrics
- `organvm_omega_status` — Scorecard data
- `organvm_ci_health` — Workflow status
- `organvm_upcoming_deadlines` — Promotion deadlines
- `organvm_pitch_status` — Essay/pitch status

**Context Group** (1 tool)
- `organvm_get_context` — Primary cross-repo awareness tool

**How to Configure:**
```json
{
  "mcpServers": {
    "organvm": {
      "command": "organvm-mcp"
    }
  }
}
```

**Key Feature**: This is the **Claude-aware interface** to the system graph.

---

## Supporting Infrastructure

### 5. **Local MCP Servers**
**Location**: `/Users/4jp/Workspace/mcp-servers/`  
**Status**: Node.js-based infrastructure  

**Available Servers:**
- `run-fs.js` — Filesystem access MCP
- `run-memory.js` — Memory/knowledge graph MCP
- `run-sequential.js` — Sequential thinking MCP

**Start All:**
```bash
cd /Users/4jp/Workspace/mcp-servers
npm run serve:all     # or ./start-all.sh
```

**Key Feature**: Local computation layer for filesystem and reasoning tasks.

---

### 6. **Skills System**
**Location**: `/Users/4jp/Workspace/organvm-iv-taxis/a-i--skills/skills/`  
**Status**: 101+ skills across 13 categories  
**Structure**: Each skill has SKILL.md with YAML frontmatter + scripts + references + assets  

**13 Categories:**
- **Creative** (15): algorithmic-art, audio-engineering-patterns, canvas-design, creative-writing-craft, generative-art-algorithms, generative-music-composer, interactive-theatre-designer, modular-synthesis-philosophy, movement-notation-systems, narratological-algorithms, reality-tv-narrative-analyzer, theme-factory, three-js-interactive-builder
- **Data** (8): data-pipeline-architect, data-storytelling-analyst, ml-experiment-tracker, sql-query-optimizer, systemic-product-analyst, time-series-analyst, etc.
- **Development** (28): accessibility-patterns, api-design-patterns, artifacts-builder, backend-implementation-patterns, code-refactoring-patterns, etc.
- **Documentation** (6): doc-coauthoring, github-profile-architect, github-repo-curator, github-repository-standards
- **Education** (6): enc1101-curriculum-designer, evaluation-to-growth, feedback-pedagogy, socratic-tutor
- **Integrations** (11): mcp-integration-patterns, oauth-flow-architect, specstory-*, webhook-integration-patterns
- **Knowledge** (8): claude-project-manifest, knowledge-architecture, knowledge-graph-builder, recursive-systems-architect, research-synthesis-workflow, second-brain-librarian
- **Professional** (13): brand-guidelines, content-distribution, cv-resume-builder, freelance-client-ops, grant-proposal-writer, internal-comms, interview-preparation, networking-outreach, portfolio-presentation, slack-gif-creator, workshop-presentation-design
- **Project Management** (5): github-roadmap-strategist, product-requirements-designer, project-alchemy-orchestrator, project-orchestration
- **Security** (8): contract-risk-analyzer, gdpr-compliance-check, incident-response-commander, security-essentials-pack, security-implementation-guide, security-threat-modeler
- **Specialized** (8): blockchain-integration-builder, defi-trading-systems, game-mechanics-designer, interfaith-sacred-geometry, local-llm-fine-tuning, location-ar-experience
- **Tools** (9): agent-swarm-orchestrator, multi-agent-workforce-planner, ontological-renamer, skill-chain-prompts, skill-creator, speckit

**Key Feature**: This is the **capability extension layer** — available for composition into the command center.

---

## Data Flow and Integration Points

```
┌─────────────────────────────────────────────────────────────┐
│                      EXTERNAL USERS                         │
├─────────────────────────────────────────────────────────────┤
│  Web UI: system-dashboard/                                  │
│  (FastAPI on :8000)                                         │
│  ├── /health/       (overview + API)                        │
│  ├── /registry/     (browseable)                            │
│  ├── /graph/        (dependency viz)                        │
│  └── /essays/       (narrative feed)                        │
└────────┬────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│          ORGANVM-ENGINE (Programmatic Layer)                │
├─────────────────────────────────────────────────────────────┤
│  registry/         governance/        seed/                 │
│  metrics/          dispatch/          git/                  │
│  contextmd/        (7 command groups)                       │
└────────┬──────────────────────────┬──────────────────────────┘
         │                          │
         ▼                          ▼
┌──────────────────┐     ┌──────────────────────────────┐
│ REGISTRY-V2.JSON │     │ ORCHESTRATION-START-HERE     │
│                  │     │                              │
│ 80 repo entries  │     │ registry.json (copy)         │
│ (source of truth)│     │ governance-rules.json        │
│                  │     │ 5 GitHub Actions workflows   │
│                  │     │ 3 validation scripts         │
└──────────────────┘     └──────────────────────────────┘
         ▲                          │
         │                          ▼
         │              ┌──────────────────────┐
         │              │  GitHub Actions CI   │
         │              │                      │
         │              │ ✓ validate-deps      │
         │              │ ✓ organ-audit        │
         │              │ ✓ promote-repo       │
         │              │ ✓ publish-process    │
         │              │ ✓ distribute-content │
         │              └──────────────────────┘
         │
         ▼
   ┌─────────────────────────────────────────┐
   │   CLAUDE/MCP SESSIONS                   │
   │                                         │
   │   organvm-mcp-server (16 tools)         │
   │   ├── registry queries                  │
   │   ├── seed discovery                    │
   │   ├── dependency analysis               │
   │   ├── health metrics                    │
   │   └── context awareness                 │
   └─────────────────────────────────────────┘
```

---

## Current Launch Status

- ✅ **System OPERATIONAL** (launched 2026-02-11)
- ✅ **9/9 Launch Criteria Met**
- ✅ **All 8 Organs Locked**
- ✅ **GOLD SPRINT COMPLETE** (~230K words across 72 documented repos)
- ✅ **PLATINUM SPRINT COMPLETE** (65 repos, 228/228 validation checks, 10 meta-system essays)
- ✅ **POSSE Distribution** (Mastodon + Discord verified)
- ✅ **GitHub Pages** (Jekyll live at organvm-v-logos.github.io)
- ✅ **Branch Protection** (4 flagships + rulesets on free plan repos)

---

## Command Center Design Implications

A unified command center would integrate:

1. **Input Layer**: Unify dashboard pages + CLI + MCP queries into single interface
2. **Decision Layer**: Orchestration-start-here workflows as automation rules
3. **Execution Layer**: organvm-engine as the underlying engine
4. **Awareness Layer**: Real-time system state from organvm-mcp-server
5. **Extension Layer**: Skills system for composition and custom workflows

**Key Architectural Decision**: The command center should NOT replace existing systems but rather **unify the interfaces** to them, maintaining their independent integrity.

---

## Next Steps (When Exiting READ-ONLY Mode)

1. Review this infrastructure map for command center design requirements
2. Decide on command center hosting (Node/FastAPI/hybrid?)
3. Plan integration strategy (dashboard aggregation, CLI wrapper, MCP layer)
4. Design unified UX for monitoring + governance + promotion
5. Prototype control mechanisms for common workflows

---

**Prepared by**: Claude Code (Haiku 4.5)  
**Mode**: READ-ONLY — Exploration Complete  
**Awaiting**: User direction on command center design approach
