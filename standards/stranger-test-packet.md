# Stranger Test Packet

**Purpose:** Everything an external evaluator needs to assess the ORGANVM system without prior context.

**Target:** Omega criterion #2 — Stranger test score ≥80%

---

## What Is ORGANVM?

ORGANVM is a **one-person creative-institutional system** spanning 113 repositories across 8 functional organs. It enables a single director to operate at enterprise scale by steering AI automation toward meaningful creation rather than hollow output.

The system exists to prove: one person, with the right architecture, can build and maintain a portfolio that would normally require a team of 20+.

## The Eight Organs

| Organ | Name | Domain | Repos |
|-------|------|--------|-------|
| I | Theoria | Foundational theory, recursive engines, symbolic computing | 20 |
| II | Poiesis | Generative art, performance systems, creative coding | 30 |
| III | Ergon | Commercial products, SaaS tools, developer utilities | 28 |
| IV | Taxis | Orchestration, governance, AI agents, skills | 7 |
| V | Logos | Public discourse, essays, editorial | 2 |
| VI | Koinonia | Community, salons, reading groups | 6 |
| VII | Kerygma | Distribution, social automation | 4 |
| META | Meta | Cross-organ engine, schemas, dashboard, governance | 8+ |

## How to Navigate

### Entry Points

1. **Registry** — `organvm-corpvs-testamentvm/registry-v2.json` is the single source of truth for all 113 repos. Every repo has: name, organ, promotion_status, tier, description, CI, dependencies.

2. **Engine CLI** — `organvm` command with 23 subcommands. Start with:
   ```bash
   organvm status              # system overview
   organvm omega status        # 17-criterion maturity scorecard
   organvm registry list       # all repos
   organvm ontologia health    # nervous system health view
   ```

3. **Dashboard** — `organvm-dashboard` starts a web UI at localhost:8000 with registry browser, dependency graph, soak monitoring, and omega scorecard.

4. **Stakeholder Portal** — Public-facing intelligence portal with natural language queries over all repos.

### Key Repos to Examine

| Repo | Why |
|------|-----|
| `meta-organvm/organvm-engine` | Core automation: 21 modules, 2000+ tests, unified CLI |
| `meta-organvm/organvm-ontologia` | Identity backbone: 353 tests, 10-layer nervous system |
| `meta-organvm/organvm-corpvs-testamentvm` | Governance corpus: registry, rules, metrics, omega |
| `organvm-iii-ergon/public-record-data-scrapper` | Most mature ORGAN-III product: full-stack, deployed |
| `organvm-iv-taxis/tool-interaction-design` | Orchestration flagship: conductor, agents, workflows |
| `organvm-i-theoria/recursive-engine--generative-entity` | Theory flagship: symbolic computing engine |

## What to Evaluate

### Architecture (weight: 30%)
- [ ] Can you understand the organ model from the registry?
- [ ] Does the dependency flow make sense (I→II→III, IV orchestrates)?
- [ ] Are the schemas well-defined? (check `schema-definitions/schemas/`)
- [ ] Is the governance model (promotion state machine) coherent?

### Operational Maturity (weight: 25%)
- [ ] Can you run `organvm status` and understand the output?
- [ ] Do the tests pass? (`pytest organvm-engine/tests/ -v`)
- [ ] Are CI workflows present and passing?
- [ ] Do the runbooks make sense? (check `praxis-perpetua/runbooks/`)

### Code Quality (weight: 20%)
- [ ] Is the code well-structured? (check engine's `src/` layout)
- [ ] Are there meaningful tests? (not just stubs)
- [ ] Is there lint/type-check configuration?
- [ ] Are error messages helpful?

### Documentation (weight: 15%)
- [ ] Does each repo have a clear README?
- [ ] Are CLAUDE.md files useful for AI navigation?
- [ ] Is the governance corpus readable?
- [ ] Do SOPs exist and are they followed?

### External Viability (weight: 10%)
- [ ] Are any products deployed and accessible?
- [ ] Is there evidence of real usage or engagement?
- [ ] Could a contributor understand how to help?
- [ ] Is the vision compelling and coherent?

## Scoring Rubric

| Score | Meaning |
|-------|---------|
| 90-100 | Exceptional — system is self-evidently well-built |
| 80-89 | Strong — minor gaps but clearly professional |
| 70-79 | Adequate — functional but needs polish |
| 60-69 | Needs work — significant gaps in critical areas |
| <60 | Not ready — fundamental issues |

## System Statistics (2026-03-13)

- **113 repositories** across 8 organs
- **12 flagship** repos, 54 GRADUATED, 4 PUBLIC_PROCESS
- **2,700+ automated tests** across 6 test suites
- **10-layer nervous system** (entity→structure→variables→metrics→events→sensing→inference→governance→state→registry)
- **121 entities** with permanent ULID-based UIDs
- **6 operational runbooks** auto-generated from governance policies
- **6 governance policies** with automated evaluation
- **23 CLI command groups** in the unified `organvm` command
- **94 MCP tools** exposing the full system graph to AI assistants
- **17-criterion omega scorecard** tracking system maturity (4/17 MET, 3 IN_PROGRESS)

## Quick Start for Evaluators

```bash
# Clone the superproject
git clone --recurse-submodules git@github.com:meta-organvm/meta-organvm--superproject.git
cd meta-organvm

# Set up
python3 -m venv .venv && source .venv/bin/activate
pip install -e "organvm-engine/[dev]"

# Orient
organvm status
organvm omega status
organvm registry list --organ META
organvm ontologia health

# Verify
pytest organvm-engine/tests/ -v --tb=short
ruff check organvm-engine/src/

# Explore
organvm-dashboard  # opens localhost:8000
```

## Contact

For questions during evaluation, open an issue on `meta-organvm/organvm-corpvs-testamentvm` or reach out via the org's community channels.
