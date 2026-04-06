# Container Census: meta-organvm

**Date:** 2026-04-05
**Scope:** Every authored container in `meta-organvm/` at depth 0-3, with selective depth 4+ coverage
**Method:** Empirical observation of contents. Function proven by what's inside, not assumed from name.
**Purpose:** Constitutional document for next-generation structural decisions. This report observes. It does not prescribe.

---

## 1. Constitutional Framework

This census is grounded in two theoretical specifications:

### SPEC-SVSE-001: Adaptive System Variable & Structural Evolution Framework
Location: `./ChatGPT-Name and Structure Changes.md`

Core axioms:
- **Identity is immutable.** Every entity has a UID that persists through all changes.
- **Expression is mutable.** Names, locations, classifications may change indefinitely.
- **Relationships are versioned.** Hierarchy defines placement, not essence. Structural changes produce versioned records.
- **Supported mutations:** Rename, Relocate, Reclassify, Merge, Split, Deprecate.
- **All changes emit events.** Historical reconstruction is always possible.
- **Metrics are temporal observations,** not overwritten scalars. Rollups follow aggregation paths anchored to stable entity IDs.

### AMMOI: Adaptive Macro-Micro Ontological Index
Location: `./ChatGPT-Hierarchical Index Structures.md`

Architecture layers and their mapping to this report:
| AMMOI Layer | This Report Section |
|-------------|-------------------|
| Perception | Section 3 (Container Inventory) — raw observation of what exists |
| Normalization | Section 2 (Census) — counts, types, distributions |
| Ontology | Section 3 proven-function entries — what each container empirically does |
| State | Section 4 (Structural Patterns) — signatures, repetitions, anomalies |
| Inference | Section 5 (Tension Map) — orphans, overlap, drift, inconsistency |
| Governance | Not covered — this report provides inputs for governance decisions |
| Revision | Not covered — this report provides inputs for revision proposals |

### What This Report Is Not

This report does not recommend. It does not say "move X to Y" or "merge A with B." The theoretical framework (SPEC-SVSE-001, AMMOI) provides the vocabulary for mutations. This census provides the observations. The next generation combines them to arrive at whatever ideal it arrives at.

### Prior Work

**Directory Dissection (2026-04-04)** established:
- Three-layer model: GOVERNED / LIMINAL / META-INFRA
- 6 structural anomalies
- Flat verb map: 238 functional units, ~116K lines
- Plans: `.claude/plans/2026-04-04-directory-dissection-post-mortem.md`, `2026-04-04-flat-verb-map.md`

This census goes deeper — into every container at every level — and frames findings through the AMMOI lens.

---

## 2. System Census

### Totals

| Metric | Value |
|--------|-------|
| Total authored directories (excl .git/.venv/node_modules/cache) | 4,931 |
| Top-level containers | 21 |
| GOVERNED (git + seed.yaml) | 13 |
| LIMINAL (no git or no seed) | 5 |
| META-INFRA (superproject tooling) | 3 |
| Maximum authored nesting depth | 15 levels |
| Deepest authored hotspot | `materia-collider/bench/organ-reset-2026-03-11/` (9 GB snapshot) |

### File Type Distribution (depth 0-4, authored only)

| Extension | Count |
|-----------|-------|
| md | 1,667 |
| py | 463 |
| json | 313 |
| yaml | 143 |
| yml | 111 |
| ts | 100 |
| html | 45 |
| tsx | 15 |
| toml | 8 |
| js | 8 |
| css | 2 |

The system is overwhelmingly markdown (60%) and Python (17%). TypeScript exists in stakeholder-portal and organvm-corpvs-testamentvm/portfolio-site.

### Layer Breakdown

**GOVERNED** (13 containers — git root + seed.yaml):
aerarium--res-publica, alchemia-ingestvm, cvrsvs-honorvm, materia-collider, organvm-corpvs-testamentvm, organvm-engine, organvm-mcp-server, organvm-ontologia, praxis-perpetua, schema-definitions, stakeholder-portal, system-dashboard, vigiles-aeternae--agon-cosmogonicum

**LIMINAL** (5 containers — on disk, missing governance markers):
| Container | Has .git | Has seed.yaml | Has README | Has CLAUDE.md |
|-----------|----------|---------------|------------|---------------|
| organvm-iii-ergon | no | no | no | no |
| organvm-theoria-knowledge-engine | no | no | no | no |
| post-flood | no | no | no | yes |
| topological-mythos | no | no | no | no |
| intake | no | no | yes | no |

**META-INFRA** (3 containers — superproject tooling):
data, docs, tools

### Identity Marker Coverage

| Marker | Present In | Missing From |
|--------|-----------|-------------|
| git root | 13 governed repos | 5 liminal + 3 meta-infra |
| seed.yaml | 13 governed repos | all liminal + meta-infra |
| README.md | 12 governed + intake | organvm-ontologia, all other liminal/meta |
| CLAUDE.md | 13 governed + post-flood | all liminal except post-flood, all meta-infra |
| pyproject.toml | 8 Python packages | 5 non-code governed repos, all liminal/meta |
| package.json | 1 (stakeholder-portal) | everywhere else |

---

## 3. Container-by-Container Inventory

Format: `path | files:N dirs:N | layer | proven function`

Depth 4+ is summarized per-parent unless notable.

### Root Level (depth 0)

`./` | files:20 dirs:32

Root contains 20 files. Proven function of root-level files:
- `.gitmodules` (426B) — submodule pointer declarations
- `.gitignore` (426B) — allowlist pattern (everything ignored except explicitly tracked)
- `.env.example` (865B) — environment variable template
- `CLAUDE.md` (15K), `GEMINI.md` (5K), `AGENTS.md` (4K) — AI agent context files
- `README-superproject.md` (3K) — superproject documentation
- `VISION.md` (25K) — foundational identity document (**gitignored** per dissection anomaly #1)
- `ORGAN-REPORT.md` (32K) — system-wide organ report
- `TRIPTYCH.md` (5K) — Body/Mind/Seed triptych state document
- `ChatGPT-Hierarchical Index Structures.md` (14K) — AMMOI spec
- `ChatGPT-Name and Structure Changes.md` (23K) — SPEC-SVSE-001
- `filename.txt` (0B) — **empty detritus**
- `.DS_Store` (14K) — macOS detritus
- `storm-record_meta-org_031026.md` (4K) — incident/event record
- 3 session export files (172K + 380K + 3K) — **conversation dumps at root**
- 2 session files (287K + 434K) — **large conversation transcripts at root**

**Observation:** 5 files totaling ~1.3 MB are conversation/session dumps sitting at root. These are the "ChatGPT exports" and "session transcripts" noted in the dissection as detritus.

---

### aerarium--res-publica (GOVERNED)

`aerarium--res-publica/` | files:4 dirs:9

**Proven function:** Grant applications, fiscal sponsorship, entity formation (LLC, GitHub Sponsors, Candid). Financial/legal infrastructure for the system.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| applications/ | 0 | 6 | Parent for grant application packages |
| applications/aspiration-tech-fiscal-sponsor/ | — | — | Aspiration Tech fiscal sponsor application |
| applications/creative-capital-2027/ | — | — | Creative Capital 2027 grant (has scratch/) |
| applications/nlnet-ngi0-commons-2026/ | — | — | NLnet NGI0 Commons grant |
| applications/sloan-foundation-loi/ | — | — | Sloan Foundation letter of intent |
| applications/sovereign-tech-fellowship-2026/ | — | — | Sovereign Tech Fellowship |
| applications/zkm-rauschenberg-2026/ | — | — | ZKM/Rauschenberg art-tech grant |
| docs/ | 0 | 0 | **Empty** |
| entity-formation/ | 1 | 3 | Legal entity setup docs |
| entity-formation/candid/ | — | — | Candid (GuideStar) registration |
| entity-formation/github-sponsors/ | — | — | GitHub Sponsors setup |
| entity-formation/llc/ | — | — | LLC formation docs |
| research/ | 11 | 0 | 11 research files on funding strategy |
| sops/ | 1 | 0 | 1 SOP file |
| strategy/ | 3 | 0 | 3 strategy documents |

**Tension:** `docs/` is empty while `research/` has 11 files and `strategy/` has 3. The distinction between docs, research, and strategy is unclear from contents alone.

---

### alchemia-ingestvm (GOVERNED)

`alchemia-ingestvm/` | files:11 dirs:14

**Proven function:** Python package (`alchemia`). Material ingestion pipeline (INTAKE→ABSORB→ALCHEMIZE) + aesthetic nervous system (taste.yaml cascades).

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| agents/ | 1 | 0 | 1 agent config file |
| data/ | 5 | 3 | Pipeline data: creative-briefs/, notes/, organ-aesthetics/ |
| data/creative-briefs/ | — | — | Creative brief documents |
| data/notes/ | — | — | **Empty** |
| data/organ-aesthetics/ | — | — | Aesthetic config files per organ |
| docs/ | 0 | 1 | Parent for docs/pitch/ |
| docs/pitch/ | — | — | Pitch deck materials |
| ecosystem/ | 0 | 3 | **Template scaffold** (see Pattern #1 below) |
| inspirations/ | 0 | 0 | **Empty** |
| intake/ | 0 | 1 | Pipeline intake directory |
| intake/ai-transcripts/ | — | — | AI conversation transcripts for ingestion |
| scripts/ | 2 | 0 | 2 Python scripts |
| src/alchemia/ | — | — | Package source: intake/, absorb/, alchemize/, channels/, common/ |
| tests/ | 19 | 1 | 19 test files |

---

### cvrsvs-honorvm (GOVERNED)

`cvrsvs-honorvm/` | files:5 dirs:1

**Proven function:** Achievement/honors tracking system. Minimal content — 5 files + 1 subdirectory. Early-stage (LOCAL promotion state).

---

### materia-collider (GOVERNED)

`materia-collider/` | files:10 dirs:15

**Proven function:** Experimental lab. Collision testing, benchmarks, genesis experiments. The "particle accelerator" for system components.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| bench/ | 2 | 1 | **9 GB** dated snapshot of organs I-III from 2026-03-11 |
| bench/organ-reset-2026-03-11/ | — | 3 | Full clones of organ-i/, organ-ii/, organ-iii/ with .venvs and build artifacts. **Deepest nesting in entire system (15 levels).** |
| ecosystem/ | 0 | 3 | **Template scaffold** (all empty) |
| experiments/ | 2 | 0 | 2 experiment files |
| genesis/ | 3 | 1 | Genesis/origin experiment records |
| observations/ | 1 | 0 | 1 observation file |
| organ-iii/ | 0 | 0 | **Empty** — orphaned directory |
| protocols/ | 1 | 0 | 1 protocol file |
| scripts/ | 1 | 1 | Build/utility scripts |
| src/materia_collider/ | — | — | Python package source |
| tests/ | 7 | 0 | 7 test files |

**Tension:** `bench/organ-reset-2026-03-11/` is 9 GB of frozen state. It is not a container in the AMMOI sense — it is a **temporal snapshot** that happens to consume 90%+ of this repo's disk footprint. `organ-iii/` is empty — either unfinished or orphaned.

---

### organvm-corpvs-testamentvm (GOVERNED)

`organvm-corpvs-testamentvm/` | files:41 dirs:24

**Proven function:** Planning and governance corpus. 404K+ words. Contains `registry-v2.json` (source of truth for all 128 repos), governance-rules, specs, essays, site-data, portfolio-site, scripts, templates.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| _posts/ | 2 | 0 | Blog/essay posts |
| applications/ | 12 | 1 | Grant application tracking (12 files) |
| data/ | 0 | 9 | 9 subdirectories of structured data |
| docs/ | 2 | 18 | **18 subdirectories** — the deepest docs tree in the system |
| docs/adr/ | 16 | 0 | 16 Architecture Decision Records |
| docs/agents/ | 2 | 0 | Agent documentation |
| docs/applications/ | 28 | 5 | Grant application docs (28 files + 5 subdirs) |
| docs/archive/ | 10 | 1 | Archived documents |
| docs/essays/ | 13 | 0 | 13 essay documents |
| docs/evaluation/ | 15 | 0 | 15 evaluation documents |
| docs/genesis/ | 15 | 0 | 15 genesis/origin documents |
| docs/governance/ | 1 | 0 | 1 governance doc |
| docs/implementation/ | 9 | 0 | 9 implementation guides |
| docs/legal/ | 1 | 0 | 1 legal document |
| docs/memory/ | 1 | 0 | 1 memory/context doc |
| docs/operations/ | 16 | 1 | 16 operational docs |
| docs/pitch/ | 1 | 0 | 1 pitch document |
| docs/planning/ | 6 | 0 | 6 planning documents |
| docs/specs/ | 1 | 2 | Spec documents with subdirectories |
| docs/standards/ | 5 | 0 | 5 standard documents |
| docs/strategy/ | 9 | 0 | 9 strategy documents |
| docs/validation-runs/ | 0 | 4 | 4 empty validation run directories |
| ecosystem/ | 0 | 3 | **Template scaffold** (mostly empty) |
| essays/ | 1 | 1 | Essay content (separate from docs/essays/) |
| portfolio-site/ | 6 | 5 | Astro-based portfolio website |
| registry/ | 9 | 0 | **registry-v2.json and related registry files** — system source of truth |
| scripts/ | 44 | 1 | **44 Python scripts** — validation, generation, analysis |
| site-data/ | 6 | 0 | Static site data files |
| sops/ | 1 | 0 | 1 SOP file |
| specs/ | 33 | 0 | **33 specification documents** |
| templates/ | 1 | 4 | Template files and directories |
| testament/ | 0 | 1 | Testament rendering directory |

**Tension:** `docs/essays/` (13 files) and `essays/` (1 file + 1 dir) exist as separate containers at different depths. `docs/applications/` (28 files) and `applications/` (12 files) also overlap. `scripts/` has 44 files — the densest script collection in the system.

---

### organvm-engine (GOVERNED)

`organvm-engine/` | files:13 dirs:13

**Proven function:** Core Python package (`organvm-engine`). 39 domain modules, 220 test files. The computational heart of the system.

**Domain modules** (`src/organvm_engine/`):

| Module | .py Files | Proven Function |
|--------|-----------|----------------|
| atoms/ | 7 | Cross-system linking pipeline, Jaccard matching |
| audit/ | 10 | System auditing |
| ci/ | 6 | CI health triage |
| cli/ | 40 | 23-module CLI interface |
| content/ | 5 | Content management |
| contextmd/ | 5 | Auto-generate CLAUDE.md/GEMINI.md/AGENTS.md |
| coordination/ | 4 | Multi-agent claims registry |
| deadlines/ | 2 | Deadline parsing from rolling-todo.md |
| debt/ | 2 | Technical debt tracking |
| dispatch/ | 5 | Event payload validation and routing |
| distill/ | 5 | Operational pattern taxonomy |
| distillatio/ | 2 | Distillation (separate from distill/) |
| ecosystem/ | 11 | Product business profiles, competitive matrix |
| events/ | 2 | Event system |
| fabrica/ | 4 | Factory/scaffold generation |
| fossil/ | 10 | Fossil record / archaeology |
| git/ | 4 | Superproject git management |
| governance/ | 28 | Promotion state machine, dependency validation |
| indexer/ | 6 | Indexing |
| irf/ | 3 | Index Rerum Faciendarum management |
| ledger/ | 8 | Financial/effort ledger |
| metrics/ | 14 | System metrics, propagation, timeseries |
| network/ | 9 | Network/mirror protocol |
| omega/ | 3 | 17-criterion maturity scorecard |
| ontologia/ | 6 | Ontologia bridge |
| ontology/ | 4 | Ontology (separate from ontologia/) |
| pitchdeck/ | 8 | HTML pitch deck generation |
| plans/ | 7 | Plan file management |
| prompting/ | 3 | Agent prompting guidelines |
| prompts/ | 9 | Prompt extraction and classification |
| pulse/ | 24 | System pulse/heartbeat monitoring |
| registry/ | 6 | Registry load/save/query |
| schemas/ | 0 | **Empty** |
| seed/ | 8 | seed.yaml discovery and graph |
| session/ | 6 | Multi-agent session parsing |
| sop/ | 4 | SOP discovery and resolver |
| testament/ | 7 | Testament rendering |
| trivium/ | 10 | Trivium dialectica |
| verification/ | 5 | Verification checks |

**Tension:** `distill/` (5 files) and `distillatio/` (2 files) are sibling modules with potentially overlapping function. `ontologia/` (6 files) and `ontology/` (4 files) are sibling modules with semantically identical names. `schemas/` is empty.

Other subdirectories:
| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| docs/ | 0 | 2 | Empty parent (has subdirs) |
| ecosystem/ | 0 | 3 | **Template scaffold** (mostly empty) |
| notebooks/ | 1 | 0 | 1 Jupyter notebook |
| tests/ | 220 | 2 | **220 test files** — largest test suite |

---

### organvm-mcp-server (GOVERNED)

`organvm-mcp-server/` | files:9 dirs:9

**Proven function:** MCP server exposing the system graph to Claude Code via stdio. 16 tools in 5 groups.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| ecosystem/ | 0 | 3 | **Template scaffold** (all empty) |
| src/organvm_mcp/ | — | — | Server source code |
| tests/ | 21 | 1 | 21 test files |

---

### organvm-ontologia (GOVERNED)

`organvm-ontologia/` | files:7 dirs:6

**Proven function:** UID-based entity identity system. Adaptive structural registry — the closest existing code to SPEC-SVSE-001.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| src/organvm_ontologia/ | — | — | Package source |
| tests/ | 24 | 1 | 24 test files |

**Note:** No README.md. Only governed repo without one.

---

### praxis-perpetua (GOVERNED)

`praxis-perpetua/` | files:7 dirs:23

**Proven function:** Process governance corpus. SOPs, session critiques, derived principles, templates. The "practice of perpetual practice." **23 subdirectories** — the widest container in the system.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| archive/ | 0 | 1 | Archived content (1 subdir: studium-generale/) |
| commissions/ | 1 | 0 | 1 YAML — commission tracking |
| content-pipeline/ | 2 | 5 | Content processing pipeline experiments |
| content-pipeline/siglip-spike/ | — | — | SigLIP ML experiment (**has .venv with torch — large**) |
| defenses/ | 0 | 2 | Defense records: transcripts/, records/ (both have 1 file each) |
| ecosystem/ | 0 | 3 | **Template scaffold** (all empty) |
| governance/ | 9 | 0 | 9 governance documents (md + yaml) |
| lessons/ | 4 | 0 | 4 lesson/learning documents |
| library/ | 2 | 4 | Library index + 4 subdirs (plans/by-domain/ is empty) |
| prompt-corpus/ | 27 | 5 | **27 files + 5 subdirs** — prompt extraction and analysis corpus |
| publications/ | 0 | 3 | 3 empty subdirs (placeholder structure) |
| research/ | 49 | 9 | **49 files + 9 subdirectories** — the densest research collection |
| research/radical-authenticity/ | 2 | 0 | Research on radical authenticity |
| research/solo-auteur-to-studio/ | 1 | 0 | Research on solo→studio transition |
| research/trash-and-church/ | 1 | 0 | Research on trash/sacred aesthetics |
| research/infrastructure-as-art/ | 1 | 0 | Research on infrastructure as art form |
| research/alchemical-system-lifecycle/ | 1 | 0 | Research on alchemical lifecycle |
| research/system-as-genre/ | 1 | 0 | Research on system-as-genre concept |
| research/sgo-2026-formalization-of-knowledge/ | — | — | SGO knowledge formalization (has phase-4/) |
| runbooks/ | 7 | 0 | 7 operational runbooks |
| scripts/ | 3 | 0 | 3 Python utility scripts |
| sessions/ | 11 | 3 | 11 session records + 3 subdirs |
| specifications/ | 7 | 1 | 7 specs (md + tla) + plans/ subdir |
| standards/ | 69 | 0 | **69 standard documents** — largest single-purpose collection |
| strategy/ | 1 | 2 | 1 YAML + 2 subdirs |
| studies/ | 3 | 3 | 3 studies + 3 subdirs (hypotheses/, findings/ both empty) |
| templates/ | 8 | 1 | 8 template files |
| testament/ | 1 | 2 | Testament docs (maps/, milestones/ both empty) |

**Tension:** `standards/` has 69 files with no subdirectories — flat collection. `research/` has 49 files + 9 topic subdirectories, each being a micro-container with 1-2 files. `publications/` has 3 empty subdirectories — placeholder with no content.

---

### schema-definitions (GOVERNED)

`schema-definitions/` | files:10 dirs:12

**Proven function:** Canonical JSON Schemas for all system data contracts. 28 schema files, 23 example files, validation scripts.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| docs/pitch/ | 1 | 0 | 1 pitch document |
| ecosystem/ | 0 | 3 | **Template scaffold** (all empty) |
| examples/ | 23 | 0 | 23 schema example files |
| schemas/ | 28 | 0 | 28 JSON Schema definitions |
| scripts/ | 2 | 0 | 2 validation scripts |
| tests/ | 1 | 0 | 1 test file |

---

### stakeholder-portal (GOVERNED)

`stakeholder-portal/` | files:26 dirs:14

**Proven function:** Next.js stakeholder intelligence portal. Deployed to Vercel (stakeholder-portal-ten.vercel.app). Repo browser + AI chat interface.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| ecosystem/ | 0 | 3 | **Template scaffold** (all empty) |
| public/ | — | — | Static assets |
| scripts/ | 8 | 0 | 8 build/utility scripts |
| src/app/ | — | — | Next.js app routes (ask/, planning/, about/, dashboard/, testament/) |
| tests/ | 40 | 0 | 40 test files |

---

### system-dashboard (GOVERNED)

`system-dashboard/` | files:10 dirs:10

**Proven function:** FastAPI + Jinja2 + HTMX dashboard. Health, registry browser, dependency graph, soak monitoring, essays, omega scorecard.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| docs/pitch/ | 1 | 0 | 1 pitch document |
| ecosystem/ | 0 | 3 | **Template scaffold** (all empty) |
| infra/ | 6 | 0 | 6 infrastructure config files |
| src/dashboard/ | — | — | FastAPI application source |
| tests/ | 9 | 0 | 9 test files |

---

### vigiles-aeternae--agon-cosmogonicum (GOVERNED)

`vigiles-aeternae--agon-cosmogonicum/` | files:11 dirs:12

**Proven function:** Cross-organ mythological multiverse. Chronicles, colosseum, constitutional framework, integration, orders, regimes.

| Path | Files | Dirs | Proven Function |
|------|-------|------|----------------|
| chronicles/ | — | — | Narrative chronicle records |
| colosseum/ | — | — | Contest/arena system |
| constitutional/ | — | — | Constitutional documents (candidates/, enacted/ — both empty) |
| integration/ | — | — | Cross-organ integration |
| orders/ | — | — | Order/faction definitions |
| regimes/ | — | — | Governance regime records |
| src/ | — | — | Python source |
| tests/ | — | — | Test files |

---

### intake (LIMINAL)

`intake/` | files:85 dirs:21

**Proven function:** Unsorted inbound material. 85 files at root level + 21 subdirectories. The primordial soup.

| Path | Files | Dirs | Character |
|------|-------|------|-----------|
| adaptive-personal-syllabus-old-local/ | 2 | 3 | Old syllabus project (aiChatsThread/, narrative-workbook/, syllabusEVOLUTION/) |
| alchemical-synthesizer/ | 10 | 8 | **Full git repo** with .git, .github, .claude, .gemini, docs, tools, brahma/ (pd/, sc/, web/) — predecessor to alchemia-ingestvm |
| all-fusion-engine/ | 4 | 0 | 4 specification files |
| auto-rev-epistemic-engine_spec/ | 7 | 5 | Spec with **doubled nesting** (auto-rev-epistemic-engine_spec/auto-rev-epistemic-engine_spec/) |
| Creator_OS/ | 2 | 0 | 2 files — also exists inside inSORT/ |
| data-2026-02-16-00-20-00-batch-0000/ | 4 | 0 | Dated data batch |
| hokage-chess--believe-it!/ | 6 | 0 | Game concept files |
| inSORT/ | 76 | 2 | 76 files + contains copies of Creator_OS/ and MET4_Fuse-Transform-Symbiote/ |
| JST_/ | 6 | 2 | JST Elevate business content (Personas, System, SOPs, Logic, Substack, Content) |
| MET4_Fuse-Transform-Symbiote/ | 13 | 1 | Meta-fusion spec — also exists inside inSORT/ |
| meta_tmp/ | 10 | 1 | Temporary meta files |
| metasystem-core/ | 61 | 11 | **Largest intake child** — 61 files, 11 dirs (config, benchmarks, integrations) |
| omni-dromenon-machina.BACKUP-20260207/ | 6 | 2 | Backup of organ-II project |
| OS-me/ | 15 | 5 | Personal OS concept docs |
| processCONTAINER/ | 37 | 1 | Process container concept — 37 files |
| projects-local/ | 0 | 14 | **14 local project directories** (many empty) |
| self-patent-fulfillment/ | 2 | 0 | Self-patent concept docs |
| src-orphan/ | 1 | 3 | Orphaned source fragments |
| UNIVERSE_plus_docs_revenue/ | 1 | 1 | Revenue doc concept v1 |
| UNIVERSE_plus_docs_revenue2/ | 1 | 1 | Revenue doc concept v2 |
| world-registry-archive/ | 21 | 2 | 21 world registry files |

**Tension:** `Creator_OS/` exists both at `intake/Creator_OS/` AND inside `intake/inSORT/Creator_OS/`. `MET4_Fuse-Transform-Symbiote/` exists both at root and inside `inSORT/`. `alchemical-synthesizer/` is a full git repo that appears to be the predecessor to the governed `alchemia-ingestvm/`. `auto-rev-epistemic-engine_spec/` has its contents doubled inside a same-named subdirectory.

---

### organvm-theoria-knowledge-engine (LIMINAL)

`organvm-theoria-knowledge-engine/` | files:1 dirs:13

**Proven function:** Knowledge engine scaffold. 13 subdirectories, **15+ are completely empty**. Only file at root is 1 file. Subdirectories define an ambitious architecture (atlas, engine, experiments, governance, ingestion, knowledge_graph, manifest, organvm_bridge, research, scripts, tests) but contain no content.

This is a **blueprint with no body** — directory structure as intention, not implementation.

Empty subdirectories: atlas/, docs/, experiments/, governance/, knowledge_graph/, manifest/, organvm_bridge/, scripts/, tests/, plus 7 empty children under research/ and 3 empty under ingestion/ and 5 empty under engine/.

---

### post-flood (LIMINAL)

`post-flood/` | files:8 dirs:8

**Proven function:** Recovery/reconstruction documents from a system event. Contains specs (12 files + 34 subdirs), archive of original state, commit assessment summaries, hierarchical index structures, name/structure changes, top-down refinement pipeline docs, virtual system architecture docs.

`post-flood/specs/` has **34 subdirectories** at depth 3 — each SPEC-NNN/ contains a main spec file and a sources/ directory. This is the deepest non-bench authored nesting in the system.

---

### topological-mythos (LIMINAL)

`topological-mythos/` | files:29 dirs:0

**Proven function:** Collection of 29 ChatGPT export JSON files. Topics: mythology (Tolkien, Final Fantasy, JoJo, Kingdom Hearts, Ganondorf), biology-as-code, fusion engines, media theory. No subdirectories. Flat archive of AI conversation exports on mythological/theoretical topics.

---

### organvm-iii-ergon (LIMINAL)

`organvm-iii-ergon/` | files:0 dirs:1

**Proven function:** Contains only `styx-behavioral-commerce/` (2 files, 3 dirs). Appears to be an abandoned or relocated organ-III project fragment. The governed organ-III repos live in `~/Workspace/organvm-iii-ergon/`.

---

### data (META-INFRA)

`data/` | files:3 dirs:0

**Proven function:** 3 JSON files — `absorb-mapping.json`, `intake-inventory.json`, `provenance-registry.json`. Pipeline output from alchemia-ingestvm processing.

---

### docs (META-INFRA)

`docs/` | files:2 dirs:2

**Proven function:** Superproject-level documentation. Contains `operations/` (2 files) and `superpowers/` (which has `plans/` and `specs/` with 2 files each). Low content density.

---

### tools (META-INFRA)

`tools/` | files:10 dirs:3

**Proven function:** Superproject-level tooling. Contains `naming-validator/` (Python, 67 tests — enforces double-hyphen naming convention) and `verification-fixtures/` (test fixtures).

---

### .claude, .codex, .gemini (META-INFRA)

- `.claude/` | files:2 dirs:3 — Claude Code plans (83 files in plans/), specs (1 file), worktrees (empty)
- `.codex/` | files:0 dirs:1 — Codex plans (10 files)
- `.gemini/` | files:0 dirs:1 — Gemini plans (4 files in plans/, 1 in archive)

---

### .atoms (META-INFRA)

`.atoms/` | files:1 dirs:0

**Proven function:** 1 JSON file — `organ-rollup.json`. Cross-system linking pipeline output.

---

### .sops (META-INFRA)

`.sops/` | files:3 dirs:0

**Proven function:** 3 SOPs — commit-and-release-workflow.md, session-state-management.md, submodule-sync-protocol.md.

---

### .github (submodule, GOVERNED)

`.github/` | files:12 dirs:4

**Proven function:** Org-level community health files. Contains `.github/ISSUE_TEMPLATE/` and `.github/workflows/`, `actions/system-check/scripts/`, `profile/`. This is itself a git repo (the GitHub `.github` special repo).

---

## 4. Structural Patterns

### Pattern 1: ecosystem/ Template Scaffold

The `ecosystem/` directory appears in **9 of 13 governed repos** with an **identical internal structure**:

```
ecosystem/
  intelligence/
    content/     (empty)
    delivery/    (empty)
    [community/] (empty, only in 3 repos)
  pillar-dna/    (2 files)
  snapshots/
    content/     (empty)
    delivery/    (empty)
    [community/] (empty, only in 3 repos)
```

Across all 9 repos, `intelligence/content/`, `intelligence/delivery/`, `snapshots/content/`, and `snapshots/delivery/` are **universally empty**. Only `pillar-dna/` contains files (2 per repo). This is a scaffolded template that was deployed but never populated.

**Empty directory count from this pattern alone:** 36-42 directories.

### Pattern 2: Repeated Directory Names

Top 10 most repeated directory names (depth 0-3):

| Name | Occurrences | Notes |
|------|------------|-------|
| plans/ | 19 | Spread across .claude, .codex, .gemini, archive subdirs, praxis-perpetua, etc. |
| .github/ | 15 | Expected — one per governed repo |
| workflows/ | 12 | Inside .github/ — expected |
| tests/ | 12 | Expected — one per code package |
| ISSUE_TEMPLATE/ | 12 | Inside .github/ — expected |
| src/ | 10 | Expected — Python src layout |
| snapshots/ | 10 | From ecosystem/ template |
| intelligence/ | 9 | From ecosystem/ template |
| pillar-dna/ | 9 | From ecosystem/ template |
| ecosystem/ | 9 | The template itself |
| docs/ | 9 | In 7 governed repos + corpus docs/ subdirs |
| .claude/ | 9 | Per-repo Claude config |
| scripts/ | 7 | alchemia, materia-collider, corpus, theoria-engine, praxis, schema-defs, stakeholder-portal |

Of these, `ecosystem/`, `intelligence/`, `snapshots/`, `pillar-dna/` are template-generated (Pattern 1). `docs/`, `scripts/`, `.claude/` are organic but inconsistently structured across repos.

### Pattern 3: Empty Containers

**91+ completely empty directories** found at depth ≤4. Sources:
- ecosystem/ template scaffold: ~36-42 empty directories
- organvm-theoria-knowledge-engine: 15+ empty directories (blueprint with no body)
- praxis-perpetua placeholder directories: hypotheses/, findings/, maps/, milestones/, publications/ children
- Various others: constitutional/candidates/, constitutional/enacted/, etc.

### Pattern 4: Micro-Containers

Directories with 1-2 files and no children (unnecessary nesting layer). Notable clusters:
- praxis-perpetua/research/ topic directories: 6 directories each containing 1 file
- praxis-perpetua/defenses/: 2 children each with 1 file
- stakeholder-portal/src/app/: 5 route directories each with 1 file (Next.js convention — expected)
- docs/pitch/ pattern: appears in 3 repos, each with 1 file

### Pattern 5: Root-Level Detritus

The superproject root contains files that don't belong to the superproject's governance function:
- 5 conversation/session dump files (1.3 MB total)
- 1 empty file (`filename.txt`, 0 bytes)
- `.DS_Store` (14K)
- 2 ChatGPT spec exports (the AMMOI and SPEC-SVSE-001 documents — these have constitutional value but are raw exports)

### Pattern 6: Deep Nesting Hotspots (authored content only)

| Depth | Location | Character |
|-------|----------|-----------|
| 15 | materia-collider/bench/organ-reset-2026-03-11/... | Frozen organ snapshots with full .venvs and build artifacts (9 GB) |
| 6-8 | post-flood/specs/SPEC-NNN/sources/ | Spec documents with per-spec source directories |
| 5-6 | intake/auto-rev-epistemic-engine_spec/auto-rev-epistemic-engine_spec/ | Doubled nesting — same name nested inside itself |
| 5-6 | intake/JST_/JST_Elevate/01_Personas through 06_Content | Business content with numbered subdirectories |

---

## 5. Tension Map

Following AMMOI Section 18 (Tension Detection): "Complex systems accumulate unresolved structural strain."

### T1: Orphaned Nodes

Containers with no parent governance (no .git, no seed.yaml, not tracked as submodule):

| Container | Files | Character |
|-----------|-------|-----------|
| organvm-theoria-knowledge-engine/ | 1 | Blueprint scaffold, 15+ empty dirs, no git |
| organvm-iii-ergon/ | 0 | 1 child (styx-behavioral-commerce/), organ-III fragment |
| topological-mythos/ | 29 | Flat archive of ChatGPT JSON exports |
| post-flood/ | 8+ | Recovery/reconstruction documents, has CLAUDE.md but no git |
| intake/ | 85+ | Primordial soup — unsorted material from multiple eras |

`alchemical-synthesizer/` inside intake/ has its own .git — it is a **governed entity trapped inside an ungoverned container**.

### T2: Semantic Overlap Among Siblings

Containers at the same depth serving potentially overlapping functions:

| Location | Overlap |
|----------|---------|
| organvm-engine: `distill/` (5 py) vs `distillatio/` (2 py) | Both names derive from "distillation" |
| organvm-engine: `ontologia/` (6 py) vs `ontology/` (4 py) | Latin vs English for the same concept |
| organvm-corpvs-testamentvm: `docs/essays/` (13) vs `essays/` (1+1) | Same content type at different depths |
| organvm-corpvs-testamentvm: `docs/applications/` (28+5) vs `applications/` (12+1) | Same content type at different depths |
| aerarium--res-publica: `docs/` (empty) vs `research/` (11) vs `strategy/` (3) | Unclear boundary between docs, research, strategy |
| praxis-perpetua: `research/` (49+9) vs `studies/` (3+3) vs `lessons/` (4) | Three containers for investigative/reflective content |
| praxis-perpetua: `governance/` (9) vs `standards/` (69) vs `runbooks/` (7) | Three containers for operational authority |

### T3: Identity Gaps

Containers missing markers that their siblings possess:

| Container | Missing |
|-----------|---------|
| organvm-ontologia | README.md (only governed repo without one) |
| post-flood | .git, seed.yaml (has CLAUDE.md — partial governance) |
| data/, .atoms/ | All markers (pipeline output with no documentation) |
| docs/ | All markers (superproject docs with no self-description) |

### T4: Template Without Content (Structural Inflation)

The ecosystem/ scaffold deployed to 9 repos created 36-42 empty directories. The template defines a structure (intelligence/content, intelligence/delivery, snapshots/content, snapshots/delivery) that has never been populated in any repo. Only `pillar-dna/` (2 files per repo) contains content.

This is structural inflation — directory count increased by ~40 without corresponding content.

### T5: Duplication Inside intake/

| Item | Locations |
|------|-----------|
| Creator_OS/ | `intake/Creator_OS/`, `intake/inSORT/Creator_OS/` |
| MET4_Fuse-Transform-Symbiote/ | `intake/MET4_Fuse-Transform-Symbiote/`, `intake/inSORT/MET4_Fuse-Transform-Symbiote/` |
| auto-rev-epistemic-engine_spec/ | Root level AND nested inside itself at same name |
| alchemical-synthesizer/ | Full git repo in intake/ — appears to be predecessor to governed alchemia-ingestvm/ |

### T6: Frozen Temporal State (materia-collider/bench/)

`materia-collider/bench/organ-reset-2026-03-11/` is a 9 GB snapshot of organs I-III including full .venv directories, build artifacts, and compiled outputs. In AMMOI terms, this is a **StateSnapshot** that was stored as a **literal filesystem copy** rather than as a versioned record. It dominates the repo's disk footprint and contributes the system's deepest nesting.

### T7: Conversation Artifacts at Root

5 session/conversation files (1.3 MB) sit at the superproject root alongside governance files. These are temporal artifacts (session records) mixed with persistent infrastructure (CLAUDE.md, .gitmodules, VISION.md).

---

## 6. Raw Data Appendix

### A. Identity Markers (all top-level containers)

```
aerarium--res-publica      | git:yes seed:yes readme:yes claude:yes pyproject:no  package:no
alchemia-ingestvm          | git:yes seed:yes readme:yes claude:yes pyproject:yes package:no
cvrsvs-honorvm             | git:yes seed:yes readme:yes claude:yes pyproject:no  package:no
data                       | git:no  seed:no  readme:no  claude:no  pyproject:no  package:no
docs                       | git:no  seed:no  readme:no  claude:no  pyproject:no  package:no
intake                     | git:no  seed:no  readme:yes claude:no  pyproject:no  package:no
materia-collider           | git:yes seed:yes readme:yes claude:yes pyproject:yes package:no
organvm-corpvs-testamentvm | git:yes seed:yes readme:yes claude:yes pyproject:no  package:no
organvm-engine             | git:yes seed:yes readme:yes claude:yes pyproject:yes package:no
organvm-iii-ergon          | git:no  seed:no  readme:no  claude:no  pyproject:no  package:no
organvm-mcp-server         | git:yes seed:yes readme:yes claude:yes pyproject:yes package:no
organvm-ontologia          | git:yes seed:yes readme:no  claude:yes pyproject:yes package:no
organvm-theoria-knowledge-engine | git:no seed:no readme:no claude:no pyproject:no package:no
post-flood                 | git:no  seed:no  readme:no  claude:yes pyproject:no  package:no
praxis-perpetua            | git:yes seed:yes readme:yes claude:yes pyproject:no  package:no
schema-definitions         | git:yes seed:yes readme:yes claude:yes pyproject:yes package:no
stakeholder-portal         | git:yes seed:yes readme:yes claude:yes pyproject:no  package:yes
system-dashboard           | git:yes seed:yes readme:yes claude:yes pyproject:yes package:no
tools                      | git:no  seed:no  readme:no  claude:no  pyproject:no  package:no
topological-mythos         | git:no  seed:no  readme:no  claude:no  pyproject:no  package:no
vigiles-aeternae--agon-cosmogonicum | git:yes seed:yes readme:yes claude:yes pyproject:yes package:no
```

### B. File Type Distribution

```
md:   1,667 (60%)
py:     463 (17%)
json:   313 (11%)
yaml:   143 (5%)
yml:    111 (4%)
ts:     100 (4%)
html:    45
tsx:     15
toml:     8
js:       8
css:      2
```

### C. Engine Module Density

```
cli/         40 py   (CLI interface — largest module)
governance/  28 py   (State machine, dependency validation)
pulse/       24 py   (System heartbeat monitoring)
metrics/     14 py   (Metrics, propagation, timeseries)
ecosystem/   11 py   (Product profiles, competitive matrix)
audit/       10 py   (System auditing)
fossil/      10 py   (Fossil record / archaeology)
trivium/     10 py   (Trivium dialectica)
prompts/      9 py   (Prompt extraction, classification)
network/      9 py   (Network/mirror protocol)
```

---

*Census conducted 2026-04-05 by Claude Opus 4.6 at the request of Anthony James Padavano.*
*Constitutional references: SPEC-SVSE-001, AMMOI (both March 12, 2026).*
*Prior work: Directory Dissection Post-Mortem (April 4, 2026).*
