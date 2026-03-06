# Consolidation Sprint: Close 8 Open Gaps

## Context

The eight-organ system is launched and ~94% complete (108/115 core tasks done). Three workstreams remain from the original plans:

1. **Implementation sprints** — 5 repos need working code (0/5 done)
2. **Close out partials** — Repo standards, GitHub Actions, local migration, newsletter, commerce-meta
3. **Subsidiary essays** — 6 per-organ ORGAN-V deep-dives (0/6 written)

This plan covers all three. Execution order prioritizes quick wins first, then high-effort items.

---

## Workstream A: Close Out Partials (Gaps 4-8)

### A1: Repository standards sweep (Gap 5)
Run a GitHub API audit across all 78 repos checking for: LICENSE, .gitignore, GitHub topics.
Deploy missing files and topics programmatically.

**Steps:**
1. Script: query `gh api` for all repos across 8 orgs, check for LICENSE + .gitignore existence
2. Generate report: which repos are missing what
3. Deploy LICENSE (MIT) to repos missing it via `gh api` / `create_or_update_file`
4. Deploy .gitignore (Python or Node template) to repos missing it
5. Set GitHub topics on all repos (organ tag + domain tags) via `gh api repos/{owner}/{repo}/topics`
6. Configure pinned repos for each org (6 max per org)

**Files:** Script output only — changes go to GitHub repos directly
**Effort:** Medium (scripted, ~1 session)

### A2: Local repo migration (Gap 7)
Read the `local_repos_migration` section of registry-v2.json. For each of the 9 local repos:
- Determine if it should be pushed to GitHub or marked as intentionally local
- Push those that should be public, update registry

**Steps:**
1. Read registry-v2.json `local_repos_migration` entries
2. Present list to user for go/no-go per repo
3. For approved repos: `git remote add` + `git push` + update registry
4. For intentionally-local repos: update registry status to `LOCAL_ONLY`

**Effort:** Low (~30 min with user decisions)

### A3: commerce--meta private repo (Gap 8)
Create the private governance repo in organvm-iii-ergon.

**Steps:**
1. `gh repo create organvm-iii-ergon/commerce--meta --private`
2. Add README with governance template (contracts, IP, customer agreements structure)
3. Update registry-v2.json

**Effort:** Low (~15 min)

### A4: Newsletter + social POSSE (Gap 6)
Set up newsletter and additional POSSE channels.

**Steps:**
1. Ask user: Substack vs. Ghost vs. Buttondown for newsletter
2. Create newsletter account + import first 5 essays as archive
3. Add LinkedIn POSSE endpoint to distribute-content.yml
4. Create publication-calendar.json and engagement-metrics.json stubs
5. Update public-process-map docs to reflect actual state

**Effort:** Medium (~1 session, requires user account decisions)

### A5: GitHub Actions sophistication (Gap 4)
Close the gap between spec and reality for the 3 partially-implemented workflows.

**Steps:**
1. Audit what promote-repo.yml and publish-process.yml actually do now
2. Decide with user: upgrade to spec or document current simplified state as intentional
3. If upgrading: implement per-repo `.meta/dependencies.json` deployment
4. Expand branch protection to additional repos beyond the 4-5 flagships
5. If not upgrading: update github-actions-spec.md to reflect actual implementation

**Effort:** High if upgrading, Low if documenting current state
**User decision needed:** Upgrade vs. document-as-is

---

## Workstream B: Implementation Sprints (Gap 1)

5 repos to prototype, per `docs/implementation/implementation-sprint-specs.md`.

### B1: call-function--ontological (ORGAN-I) — SKELETON → PROTOTYPE
- **Repo:** `organvm-i-theoria/call-function--ontological`
- **What:** Build 12-concept ontological function-calling framework in Python
- **Deliverables:** core/ (ontology, grounding, four_causes, dasein, semiotics), tools/cli.py, 20+ tests
- **Key:** Pure Python, no ML deps, deterministic grounding, OpenAI schema input format
- **Success:** `python -m tools.cli analyze examples/openai_schema.json` produces report, CI green

### B2: example-ai-collaboration (ORGAN-II) — SKELETON → PROTOTYPE
- **Repo:** `organvm-ii-poiesis/example-ai-collaboration`
- **What:** Build AI-conductor collaboration tracking system
- **Deliverables:** src/ (session, attribution, conductor, export, metrics), workflows/, 15+ tests
- **Key:** Pure Python, mock LLM responses, JSON-serializable sessions, markdown export
- **Success:** `python examples/demo_text_session.py` produces collaboration log, CI green

### B3: example-interactive-installation (ORGAN-II) — SKELETON → PROTOTYPE
- **Repo:** `organvm-ii-poiesis/example-interactive-installation`
- **What:** Build sensor-driven interactive installation reference implementation
- **Deliverables:** src/ (sensor_sim, mapping, output, engine), renderers/, presets/, 15+ tests
- **Key:** No hardware deps, YAML presets, OSC output, terminal renderer
- **Success:** `python examples/run_simulation.py` runs with terminal viz, CI green

### B4: tab-bookmark-manager (ORGAN-III) — PRODUCTION → DEPLOYED
- **Repo:** `organvm-iii-ergon/tab-bookmark-manager`
- **What:** Validate and document existing codebase
- **Deliverables:** Docker Compose working, .env.example, deployment docs
- **Key:** Code exists — this is validation + documentation, not new code
- **Success:** `docker-compose up` → all services healthy, deployment docs accurate

### B5: the-actual-news (ORGAN-III) — PRODUCTION → DEPLOYED
- **Repo:** `organvm-iii-ergon/the-actual-news`
- **What:** Validate and document existing codebase
- **Deliverables:** `pnpm dev` working, demo mode, architecture docs
- **Key:** Code exists — validation + documentation. The README describes a Makefile with `make dev` etc.
- **Success:** `make dev` starts gateway, frontend renders, conformance tests pass

**Implementation order:** B4 → B5 (quick wins, code exists) → B1 (highest priority) → B2 → B3

---

## Workstream C: Subsidiary Essays (Gap 3)

6 per-organ deep-dives for ORGAN-V public-process, per `docs/implementation/public-process-map-v2.md`.

### C1: "Recursive Engines at Scale" (from ORGAN-I)
- **Content:** How RE:GE's 21-organ architecture scales, what recursive self-modeling means in practice
- **Source:** recursive-engine README + test suite metrics
- **Length:** ~4,000 words

### C2: "Epistemic Tuning Explained" (from ORGAN-I)
- **Content:** The knowledge atomization methodology, how multi-modal search works
- **Source:** my-knowledge-base README + architecture docs
- **Length:** ~3,500 words

### C3: "Generative Music Case Study" (from ORGAN-II)
- **Content:** Translating symbolic narrative events into live generative music
- **Source:** generative-music repo README + metasystem-master
- **Length:** ~4,000 words

### C4: "Choreographic Interface" (from ORGAN-II)
- **Content:** Performance platform methodology, audience-participatory design
- **Source:** metasystem-master README + example-interactive-installation
- **Length:** ~3,500 words

### C5: "Aetheria RPG Post-Mortem" (from ORGAN-III)
- **Content:** Full I→II→III pipeline retrospective, honest failure analysis
- **Source:** classroom-rpg-aetheria README + existing portfolio page content
- **Length:** ~4,500 words

### C6: "Coaching Platform Metrics" (from ORGAN-III)
- **Content:** Commerce retrospective with actual metrics
- **Source:** ORGAN-III commerce repo READMEs
- **Length:** ~3,500 words

**Essay deployment:** Each essay → `public-process/essays/` directory → Jekyll build → GitHub Pages

---

## Execution Order

| Phase | Tasks | Effort | Session(s) |
|-------|-------|--------|------------|
| **1. Quick wins** | A3 (commerce-meta), A2 (local repos decision) | Low | 1 |
| **2. Repo sweep** | A1 (standards audit + deploy) | Medium | 1 |
| **3. Validate existing code** | B4 (tab-bookmark-manager), B5 (the-actual-news) | Medium | 1-2 |
| **4. Build prototypes** | B1 (call-function-ontological) | High | 1-2 |
| **5. Build prototypes** | B2 (example-ai-collaboration) | High | 1 |
| **6. Build prototypes** | B3 (example-interactive-installation) | High | 1 |
| **7. Essays** | C1-C6 (6 subsidiary essays) | Medium | 2-3 |
| **8. Infrastructure** | A4 (newsletter), A5 (GitHub Actions decision) | Medium | 1 |

**Total estimated sessions:** 8-12

---

## Verification

After all workstreams complete:
- `registry-v2.json` updated: 0 SKELETON repos among the 5 priority targets
- All 78 repos have LICENSE + .gitignore + GitHub topics
- 5 priority repos pass their CI workflows
- 16 total ORGAN-V essays published (10 existing + 6 new)
- Newsletter infrastructure live with back-catalog
- Application tracker updated with any status changes
- Run all 5 validation scripts (V1-V5) to confirm system integrity
