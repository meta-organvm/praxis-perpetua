# Vacuum Analysis and Fill Plan

**Status:** ACTIVE
**Date:** 2026-03-23
**Source:** Session close-out index propagation audit
**Context:** 6 "N/A" entries in the close-out checklist represent infrastructure vacuums -- gaps where the system should have working propagation paths but does not.

---

## Overview

The session close-out protocol (defined in INST-INDEX-RERUM-FACIENDARUM.md lines 37-51) requires checking 10 external indices when work is completed. During close-out of the SGO formalization research programme session, 6 of these 10 indices returned N/A. Each N/A is not merely "not applicable" -- it signals a structural blind spot where the system lacks infrastructure to record its own growth.

This document analyzes each vacuum, diagnoses the root cause, proposes the fill, estimates effort, and creates corresponding IRF entries.

---

## Vacuum 1: GitHub Issues -- No Issue Trail for Research Programme

### What Was Found

The SGO formalization research programme produced:
- 13 research papers (7 original + 3 synthesis + 3 TRP reviews)
- 3 arXiv-ready publication packages
- 74 implementation tasks (IRF-RES-001 through IRF-RES-071 + cross-cutting concerns)
- 4 governance policy declarations deployed to praxis-perpetua/governance/
- 1 code tool (naming-validator, 67 tests)
- 188 citations mapped in a knowledge graph

Yet ZERO GitHub issues track any of this. The corpvs-testamentvm repo has 268 open issues covering omega criteria and sprint work, but none for the research programme. The organvm-engine repo has 66 open issues but none for the IRF-RES tasks. This means:

1. No external discoverability for the research programme
2. No agent-readable tracking for IRF-RES items
3. No cross-referencing between IRF entries and GitHub's project management
4. The research programme is invisible to anyone browsing GitHub

### Root Cause

The research programme was conducted in a rapid multi-session burst (S8-S22, then the 2026-03-21 formalization sprint). Work was tracked in the IRF and intake/ staging area rather than GitHub issues. The IRF-to-GitHub-issue pipeline does not exist -- issue creation is manual.

### What SHOULD Exist

1. **GitHub issues for P0 IRF-RES items** (IRF-RES-003, 004, 006-014) on `meta-organvm/organvm-engine` -- these are implementation tasks that modify engine code
2. **A tracking issue for the research programme itself** on `meta-organvm/organvm-corpvs-testamentvm` -- milestone-level visibility
3. **GitHub issues for P1 IRF-RES items** (IRF-RES-015 through IRF-RES-043) as a backlog
4. **An automated IRF-to-issue pipeline** (`organvm irf github-sync`) that creates/updates issues from IRF entries

### Fill Plan

| Step | Description | Effort | Priority |
|------|-------------|--------|----------|
| 1a | Create tracking issue for SGO research programme on corpvs-testamentvm | S | P0 |
| 1b | Create issues for open P0 IRF-RES items on organvm-engine (11 items) | M | P1 |
| 1c | Create issues for open P1 IRF-RES items on organvm-engine (29 items) | M | P2 |
| 1d | Build `organvm irf github-sync` CLI command | L | P2 |

**Dependencies:** None for 1a-1c. 1d depends on the IRF parser module (already exists at `organvm_engine/irf/`).

**IRF Entry:** IRF-VAC-001

---

## Vacuum 2: Omega Scorecard -- Research Work Not Advancing Criteria

### What Was Found

The omega scorecard has 19 criteria. The SGO research programme produced governance policies, a code tool, and peer-reviewed publications -- yet the close-out stated "process work does not advance any of the 17 omega criteria." The actual scorecard (19 criteria as of 2026-03-21 amendment) measures:

| Met (6) | Not Met (13) |
|---------|-------------|
| #1 30-day soak | #2 Stranger test |
| #3 Engagement baseline | #4 Runbooks validated |
| #5 Application submitted | #7 External feedback |
| #6 AI-conductor essay | #9 Stranger-ready polish |
| #8 Product live | #10 100 unique visitors |
| #13 Organic inbound | #11 Salons/events |
| #15 Portfolio updated | #12 External contributions |
| | #14 Recognition event |
| | #16 Bus factor |
| | #17 Autonomous ops (soak) |
| | #18 Organic revenue |
| | #19 Network testament |

The research programme DOES advance criteria, but the connection is indirect:

1. **#7 (external feedback)** -- The TRP reviews constitute structured feedback on the research. If the 3 arXiv preprints are submitted and receive reviewer feedback, this advances #7 directly.
2. **#14 (recognition event)** -- arXiv publications ARE a recognition pathway. Acceptance = recognition.
3. **#15 (portfolio updated)** -- The research programme is significant portfolio evidence. 13 papers, a code tool, governance declarations.
4. **#9 (stranger-ready polish)** -- The naming-validator tool, if polished and documented, could count toward the 3 products needed.

Additionally, the existing scorecard has no criterion for **internal knowledge production** or **research output**. This was identified in IRF-CCE-012 (propose omega criterion for memory infrastructure) but not yet for research.

### Root Cause

The omega criteria were designed around external-facing milestones (products, visitors, revenue, community). Internal system maturity (governance quality, research depth, institutional authority) has no representation in the scorecard. The research programme advances the SYSTEM but the scorecard does not measure the system's internal sophistication.

### What SHOULD Exist

1. **Direct connection mapping** between research outputs and existing omega criteria (arXiv submissions advance #7, #14)
2. **A research/institutional criterion** -- e.g. "#20: Research authority demonstrated (>=1 peer-reviewed or externally validated publication)"
3. **Evidence propagation** -- when IRF-RES items are completed, relevant omega criteria should be checked for advancement

### Fill Plan

| Step | Description | Effort | Priority |
|------|-------------|--------|----------|
| 2a | Document which existing omega criteria the research programme advances (#7, #14, #15) | S | P0 |
| 2b | Propose omega criterion #20 for research/institutional authority (complement to IRF-CCE-012 memory criterion) | S | P1 |
| 2c | Wire IRF-RES completion events into omega evidence updates | M | P2 |

**Dependencies:** 2b requires omega amendment process (precedent exists: criteria #9, #10 were amended 2026-03-20, #19 added 2026-03-21). 2c depends on the IRF parser module.

**IRF Entry:** IRF-VAC-002

---

## Vacuum 3: Testament Chain -- "Requires Engine Runtime"

### What Was Found

The testament chain IS operational. Research revealed:

- **Chain file:** `~/.organvm/testament/chain.jsonl` -- 5,522 events, 2.9MB
- **Infrastructure:** Full `ledger/` module (7 submodules: chain.py, emit.py, merkle.py, rotation.py, anchor.py, digest.py, tiers.py)
- **Emission function:** `testament_emit()` in `ledger/emit.py` -- fail-safe, never raises
- **CLI:** `organvm testament status`, `organvm testament render`, `organvm testament play`, `organvm testament record-session`
- **Hash-linking:** SHA-256 chain with Merkle checkpoints, rotation at 100MB
- **Self-referential events:** `ARCHITECTURE_CHANGED`, `SCORECARD_EXPANDED`, `VOCABULARY_EXPANDED` (added via IRF-TST-002, DONE-115)
- **Omega integration:** Criterion #19 evaluates network testament health

The vacuum was MISIDENTIFIED. The chain IS running. The actual gap is that the close-out process did not know how to check it, or the session did not emit events for the research work.

The real vacuums within the testament system are:

1. **No session-end auto-emission** -- when a session completes significant work, no automatic testament event is recorded. The `record-session` command exists but is manual.
2. **No milestones directory** -- `data/testament/milestones/` does not exist, which means omega #19's milestone check always returns 0.
3. **Research programme events not recorded** -- the 13 papers, 3 arXiv packages, 4 governance declarations, and 1 code tool produced in the SGO research programme have no testament entries.

### Root Cause

The testament chain emits events when engine CLI commands run (registry updates, omega evaluations). But research work -- documents written to praxis-perpetua, tools created, governance declarations deployed -- happens outside the engine's event scope. The chain witnesses ENGINE operations but not SYSTEM-WIDE production.

### What SHOULD Exist

1. **Milestone recording** -- significant system events (new research programme completed, new tool deployed, governance declarations published) should create milestone files in `data/testament/milestones/`
2. **Session-end auto-emission** -- `organvm session review` should optionally emit a `session.completed` event to the testament chain
3. **Research event types** -- `RESEARCH_PUBLISHED`, `GOVERNANCE_DECLARED`, `TOOL_DEPLOYED` event types alongside the existing vocabulary
4. **Backfill** -- record the SGO research programme events retroactively

### Fill Plan

| Step | Description | Effort | Priority |
|------|-------------|--------|----------|
| 3a | Create `data/testament/milestones/` directory with first milestone (system launch 2026-02-11) | S | P0 |
| 3b | Record SGO research programme events in testament chain (13 papers, 4 governance docs, 1 tool) | M | P1 |
| 3c | Add research event types to EventType enum (`RESEARCH_PUBLISHED`, `GOVERNANCE_DECLARED`, `TOOL_DEPLOYED`) | S | P1 |
| 3d | Wire session review into testament emission (`organvm session review --emit`) | M | P2 |
| 3e | Create milestone creation command (`organvm testament milestone --title "..."`) | S | P2 |

**Dependencies:** 3a is zero-dependency. 3b-3c depend on engine dev environment. 3d depends on session module.

**IRF Entry:** IRF-VAC-003

---

## Vacuum 4: Registry -- Does It Need to Know?

### What Was Found

The registry (`registry-v2.json`) tracks 118 repos across 8 organs. Each entry records: name, org, status, description, documentation_status, portfolio_relevance, dependencies, promotion_status, tier, last_validated, implementation_status, ci_workflow, platinum_status, functional_class, and optional fields.

Recent work created:
1. `meta-organvm/tools/naming-validator/` -- a superproject-level tool (Python, 67 tests)
2. 4 governance declarations in `praxis-perpetua/governance/` (trilemma, naming spec, research pipeline SOP, syntactic-semantic boundary)
3. A full research corpus at `praxis-perpetua/research/` (57+ documents)

The registry tracks **repos**, not files, tools, or documents within repos. So:

- **naming-validator** -- This is a tool within the meta-organvm superproject, tracked by the superproject's `.gitignore` allowlist. It does NOT need a registry entry because it is not a standalone repo. However, meta-organvm's registry entry could mention it in its description/note field.
- **governance declarations** -- These are files within praxis-perpetua. The registry tracks praxis-perpetua as a repo. Its entry could be updated to reflect the expanded governance capability.
- **research corpus** -- Same as governance: files within praxis-perpetua. The repo's description and last_validated fields should be updated.

### Root Cause

The close-out assumed "no repo state changes" meant no registry update was needed. But TWO repos DID change their capabilities: praxis-perpetua gained governance declarations and research corpus expansion, and meta-organvm gained a new tool. The registry entries for both repos should have `last_validated` bumped and their descriptions/notes updated.

### What SHOULD Exist

1. **Updated praxis-perpetua registry entry** -- description should mention SGO governance infrastructure and 57+ research documents
2. **Updated meta-organvm registry metadata** -- notes should mention naming-validator tool
3. **A "capabilities changed" trigger** -- when significant new artifacts land in a repo, the registry entry should be refreshed

### Fill Plan

| Step | Description | Effort | Priority |
|------|-------------|--------|----------|
| 4a | Update praxis-perpetua entry in registry-v2.json (description, note, last_validated) | S | P1 |
| 4b | Update meta-organvm superproject notation to include naming-validator in tools | S | P1 |
| 4c | Design registry "capabilities delta" detection (compare seed produces/consumes vs. actual) | M | P3 |

**Dependencies:** 4a-4b are zero-dependency targeted edits. 4c is a design task.

**IRF Entry:** IRF-VAC-004

---

## Vacuum 5: Seed Contracts -- Meta-Organvm Capability Changes

### What Was Found

**organvm-corpvs-testamentvm seed.yaml** (last validated 2026-02-11):
- Produces: `meta-documentation` to ORGAN-IV
- Consumes: `orchestration-artifact` from ORGAN-IV
- Subscribes: `governance.updated`, `health-audit.completed`

This seed is STALE. The corpus repo's capabilities have expanded significantly:
- It now contains the IMPLEMENTATION-MANIFEST with 74 research tasks
- It houses the IRF (universal work registry)
- It produces governance documentation that multiple organs consume
- The research programme generates data consumed by praxis-perpetua

**praxis-perpetua seed.yaml** (last validated 2026-03-19):
- Rich seed with 4 consumes, 3 produces, 2 subscriptions
- Correctly declares SGO identity, IRA consumption, publication production
- Missing: new governance declarations (trilemma, naming spec, syntactic-semantic boundary, research pipeline SOP)

**meta-organvm superproject** -- has no seed.yaml (it is a git superproject, not a standalone repo). The tools/ directory including naming-validator is tracked by the superproject allowlist.

### Root Cause

Seed contracts are manually maintained. When capabilities change incrementally (new governance docs, new tool), the seed is not updated unless someone explicitly runs `organvm seed validate` and notices the drift.

### What SHOULD Exist

1. **Updated corpvs-testamentvm seed.yaml** -- add produces for `research-tasks` (to engine, to praxis-perpetua), `work-registry` (to all organs). Bump last_validated.
2. **Updated praxis-perpetua seed.yaml** -- add produces for `governance-declarations` (to META-ORGANVM). Bump last_validated.
3. **Seed drift detection** -- `organvm seed validate` should compare declared produces/consumes against actual file system contents and flag discrepancies.

### Fill Plan

| Step | Description | Effort | Priority |
|------|-------------|--------|----------|
| 5a | Update corpvs-testamentvm seed.yaml: add research-task and work-registry produces edges, bump last_validated to 2026-03-23 | S | P1 |
| 5b | Update praxis-perpetua seed.yaml: add governance-declarations produce edge, bump last_validated to 2026-03-23 | S | P1 |
| 5c | Design seed drift detection heuristic for `organvm seed validate` | M | P2 |

**Dependencies:** 5a-5b are zero-dependency targeted edits. 5c is a design task depending on seed module.

**IRF Entry:** IRF-VAC-005

---

## Vacuum 6: Companion Indices (Index Locorum / Nominum / Rerum) -- Not Yet Built

### What Was Found

The companion indices are the three reference instruments completing the four-part classical index apparatus:

| Index | Purpose | IRF Entry | Status |
|-------|---------|-----------|--------|
| **Rerum Faciendarum** | Things to be done (governance) | THIS EXISTS | ACTIVE, 600+ lines |
| **Locorum** | Where things live (reference) | IRF-IDX-001 | PLANNED, P1 |
| **Nominum** | What things are called (reference) | IRF-IDX-002 | PLANNED, P1 |
| **Rerum** | What things are (reference) | IRF-IDX-003 | PLANNED, P1 |

DONE-130 records "Companion indices unblocked -- construction plan written with full audit for Index Locorum, Nominum, Rerum (in stakeholder-portal/Hermeneus)." A plan exists but no indices have been built.

**What the indices would contain (based on current system state):**

**Index Locorum (places):**
- 118 repos across 8 GitHub organizations
- Key file paths: registry-v2.json, governance-rules.json, system-metrics.json, 72+ seed.yaml files
- Infrastructure endpoints: Cloudflare Pages (object-lessons), Vercel (portfolio, Hermeneus, products), Render (products), GitHub Pages (public-process)
- MCP servers: filesystem, memory, sequential-thinking, organvm
- Data paths: ~/.organvm/ (testament, events, ontologia), intake/, data/ (atoms, fossil, soak-test)
- CI/CD: 105 GitHub Actions workflows

**Index Nominum (names):**
- 8 organs (Theoria, Poiesis, Ergon, Taxis, Logos, Koinonia, Kerygma, Meta)
- 118 repos with double-hyphen naming convention
- CLI tools: organvm (24 command groups), alchemia, ontologia, cce
- Agent personas: Architect, QA Lead, Operator, Auditor
- 22 Vigiles regimes, 8 Watcher Orders
- 18+ SPECs, 67+ SOPs
- 3 dissertations (D-001, D-002, D-003)
- 8 faculties (per faculty-registry.yaml)
- Named protocols: Testament, Descent, Membrane, Styx, Formation
- People: Chris (collaborator), the Provost (SGO authority)
- Research programme: 13 papers with RP-/SYN-/TRP- prefixes
- 188 cited authors from the citation knowledge graph

**Index Rerum (things):**
- Artifact types: YAML spec, Python module, Markdown research, SVG visual, YAML regime, test file, dissertation chapter, governance declaration, LaTeX preprint
- States: implemented, specified, planned, archived
- Relationships: produces/consumes (58 dependency edges), depends-on, references
- Provenance: session IDs (S1-S31+), commit SHAs, sprint names (33 completed sprints)

### Root Cause

The indices are substantial documents (each would be 500+ lines) that require systematic crawling of the workspace. They cannot be written by hand -- they need automation. IRF-IDX-004 plans an `organvm index generate` CLI command but this depends on IRF-IDX-001/002/003 defining the content structure first.

### What SHOULD Exist

1. **Content schemas** for each index -- what fields, what granularity, what inclusion criteria
2. **Manual v1 of each index** -- a human-curated starting point that automation can later maintain
3. **Generator tooling** -- `organvm index generate locorum|nominum|rerum` that reads from registry, seeds, filesystem, and ontologia
4. **Cross-referencing** -- each index entry links to the others (a name in Nominum links to its location in Locorum and its type in Rerum)

### Fill Plan

| Step | Description | Effort | Priority |
|------|-------------|--------|----------|
| 6a | Design content schema for all three indices (what fields, inclusion criteria, format) | M | P1 |
| 6b | Build INST-INDEX-LOCORUM.md v1 -- manual curation of top-level structure, key paths, endpoints | L | P1 |
| 6c | Build INST-INDEX-NOMINUM.md v1 -- manual curation of named entities from registry, seeds, governance docs | L | P1 |
| 6d | Build INST-INDEX-RERUM.md v1 -- manual curation of artifact inventory from filesystem scan | L | P2 |
| 6e | Build `organvm index generate` CLI (IRF-IDX-004) | XL | P2 |

**Dependencies:** 6a must precede 6b-6d. 6e depends on all three v1 indices defining the target output format.

**IRF Entry:** IRF-VAC-006 (umbrella), advances existing IRF-IDX-001/002/003/004

---

## Summary Matrix

| Vacuum | Root Cause | Severity | Effort to Fix | Priority |
|--------|-----------|----------|---------------|----------|
| 1. GitHub Issues | No IRF-to-issue pipeline | HIGH | M (batch) | P0/P1 |
| 2. Omega Scorecard | No research/institutional criterion | MEDIUM | S (mapping) + S (proposal) | P0/P1 |
| 3. Testament Chain | Misidentified; real gap is milestones + research events | MEDIUM | S-M (events) | P0/P1 |
| 4. Registry | Stale entries after capability changes | LOW | S (targeted edits) | P1 |
| 5. Seed Contracts | Manual maintenance, no drift detection | LOW | S (targeted edits) | P1 |
| 6. Companion Indices | Not yet built, blocked on content schema | HIGH | L-XL (full build) | P1/P2 |

### Immediate Actions (P0, can be done now)

1. Create first testament milestone file (`data/testament/milestones/2026-02-11-system-launch.md`)
2. Document research programme's advancement of omega criteria #7, #14, #15
3. Create tracking issue for SGO research programme on corpvs-testamentvm

### Near-Term (P1, next session)

4. Create GitHub issues for open P0 IRF-RES items (11 issues)
5. Record SGO research events in testament chain
6. Update registry entries for praxis-perpetua and meta-organvm
7. Update seed.yaml for corpvs-testamentvm and praxis-perpetua
8. Design content schema for companion indices
9. Propose omega criterion #20 for research/institutional authority

### Medium-Term (P2, within 2 weeks)

10. Build `organvm irf github-sync` CLI command
11. Build v1 companion indices (Locorum, Nominum, Rerum)
12. Wire session review into testament emission
13. Design seed drift detection

---

## New IRF Entries Created

| ID | Priority | Action | Source |
|----|----------|--------|--------|
| IRF-VAC-001 | P0/P1 | GitHub issue trail for research programme (batch create 11+ issues) | This analysis, Vacuum 1 |
| IRF-VAC-002 | P0/P1 | Omega scorecard research connection mapping + criterion #20 proposal | This analysis, Vacuum 2 |
| IRF-VAC-003 | P0/P1 | Testament milestones directory + research event recording | This analysis, Vacuum 3 |
| IRF-VAC-004 | P1 | Registry entry updates for praxis-perpetua and meta-organvm | This analysis, Vacuum 4 |
| IRF-VAC-005 | P1 | Seed contract updates for corpvs-testamentvm and praxis-perpetua | This analysis, Vacuum 5 |
| IRF-VAC-006 | P1/P2 | Companion indices content schema + v1 builds (advances IRF-IDX-001/002/003) | This analysis, Vacuum 6 |

---

*Generated 2026-03-23. Source: close-out index propagation audit, 6 N/A entries identified as structural vacuums.*
