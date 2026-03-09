# Department Orchestrator — Full docs/ Generation

**Purpose:** Meta-prompt for generating a complete `docs/` directory tree for any ORGAN-III product. Give this file to an AI agent along with a repo path, and it will produce all department artifacts appropriate for the product's lifecycle phase.

---

## Prerequisites

- A repo path with `seed.yaml`, `CLAUDE.md`, and either `package.json` or `pyproject.toml`
- Access to `registry-v2.json` (at `~/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`)
- Access to the dept templates (this directory)

---

## Step 1: Read Product Identity

Read the following files from the target repo:

| File | Extract |
|------|---------|
| `seed.yaml` | product name, organ, tier, produces/consumes edges, event subscriptions |
| `CLAUDE.md` | tech stack, CLI commands, architecture notes, key contacts |
| `package.json` or `pyproject.toml` | name, version, description, dependencies, scripts |
| `README.md` | product description, features, getting started |
| `LICENSE` | license type |

From `registry-v2.json`, look up the product entry and extract:
- `revenue_model`, `revenue_status`, `implementation_status`, `promotion_status`

---

## Step 2: Determine Lifecycle Phase

Map `promotion_status` to lifecycle phase:

| promotion_status | Phase | Active Departments |
|-----------------|-------|--------------------|
| LOCAL | genesis | ENG, LEG (genesis only), FIN (genesis only), PRD, CROSS |
| CANDIDATE | foundation | ENG, LEG, FIN, PRD, OPS (foundation), CROSS |
| PUBLIC_PROCESS | hardening | ALL except graduation-only artifacts |
| GRADUATED | graduation | ALL |

---

## Step 3: Scan Existing docs/

Read the `docs/` directory tree. For each file that already exists with substantive content (more than just a README placeholder), mark it as SKIP — do not regenerate.

A file is a **placeholder** (regenerate) if:
- It contains only a title and a description of what SHOULD be there
- It has fewer than 20 lines of content
- It explicitly says "TODO" or "scaffolded"

A file is **substantive** (skip) if:
- It has real content beyond a scaffold
- It contains analysis, data, or decisions

---

## Step 4: Scan Source Code

Read the following for auto-pull data:

| Source | What to Extract |
|--------|----------------|
| `src/` directory tree | Module names, service structure, API routes |
| `.github/workflows/` | CI config, test commands, deploy targets, secrets |
| `Dockerfile` / `docker-compose.yml` | Container setup, ports, services |
| `infra/` or `terraform/` | Cloud resources, providers |
| `tests/` directory tree | Test types, coverage |

---

## Step 5: Ask Questions

Collect ALL questions from active departments. Deduplicate — some questions are shared.

### Master Question Set

Present these questions to the user in a single batch. Mark which are required vs. optional.

**Required (cannot generate without):**
1. What problem does this product solve in one sentence? *(PRD)*
2. Who is your primary user? 1-2 sentences. *(PRD, GRO)*
3. What is your pricing model? flat / tiered / usage-based / freemium / one-time *(FIN)*

**Required if applicable (ask, skip if "N/A"):**
4. What jurisdictions do you operate in? US-only / US+EU / Global *(LEG)*
5. Are you handling PII, financial data, or health data? *(LEG — confirm even if inferred)*
6. What is your target monthly revenue at steady state? *(FIN)*
7. What is your current monthly burn rate? *(FIN)*
8. What are your support channels? email / chat / forum / in-app / GitHub Issues *(CXS)*
9. Are you selling B2B, B2C, or B2B2C? *(B2B)*

**Optional (have sensible defaults):**
10. What is your target uptime SLA? Default: 99.9% *(OPS)*
11. What cloud provider? Default: infer from code *(OPS)*
12. What is your target test coverage? Default: 80% *(ENG)*
13. What is the single most important metric? Default: infer from product type *(PRD)*
14. What is your primary acquisition channel? Default: organic *(GRO)*
15. What is your expected support response time? Default: < 24h *(CXS)*
16. What is your target deal size? Default: infer from pricing *(B2B)*
17. Is there an existing business entity? Default: sole prop *(LEG)*

---

## Step 6: Generate in Dependency Order

Departments have cross-references. Generate in this order to ensure upstream docs exist when downstream docs reference them.

```
1. ENG  (E2 architecture → referenced by OPS, B2B, CROSS)
2. PRD  (P1 PRD, P2 personas → referenced by GRO, CXS, B2B, CROSS)
3. LEG  (L1 guardrails → referenced by B2B)
4. FIN  (F1 unit economics, F2 pricing → referenced by GRO, B2B, CROSS)
5. OPS  (O1 incident response → referenced by CXS, B2B)
6. GRO  (G1 GTM → referenced by B2B, CROSS)
7. CXS  (standalone at this point)
8. B2B  (consumes from all above)
9. CROSS (X1 checklist, X5 pitch → references all departments)
```

Within each department, generate artifacts in the order listed in the template file (e.g., E1 before E2 before E3).

**Phase gating:** Skip any artifact whose declared phase has not been reached. For example, if the product is in `foundation` phase, skip all `graduation`-phase artifacts (F4, O5, O6, G4-G6, C3-C5, B4-B6).

---

## Step 7: Create Directory Structure

Ensure these directories exist before writing:

```
docs/
  adr/
  architecture/
  brainstorm/
  checklists/
  customer-success/
  enterprise/
  finance/
  hiring/         (placeholder README only — no templates yet)
  legal/
  marketing/
  operations/
  pitch/
  planning/
  research/
  thesis/
```

---

## Step 8: Write Files

For each generated artifact:
1. Write to the output path declared in the template
2. Add YAML frontmatter with generation metadata:

```yaml
---
generated: true
generator: dept-orchestrator
date: {today}
product: {product_name}
department: {dept}
artifact_id: {E1, L3, etc.}
governing_sop: {SOP name}
phase: {lifecycle phase}
---
```

3. Write substantive content — not placeholders. Every section should have real, inferred or user-provided content.

---

## Step 9: Generate Index

After all artifacts are written, generate `docs/README.md`:

```markdown
# Documentation — {product_name}

**Generated:** {today}
**Phase:** {lifecycle phase}
**Departments active:** {list}

## Document Index

| # | Path | Department | Artifact | Status |
|---|------|-----------|----------|--------|
| 1 | `adr/adr-001-{slug}.md` | ENG | Architecture Decision Record | Generated |
| 2 | `architecture/overview.md` | ENG | Technical Architecture | Generated |
| ... | ... | ... | ... | ... |

## Coverage

| Department | Total Artifacts | Generated | Skipped (exists) | Deferred (phase) |
|-----------|----------------|-----------|-------------------|-------------------|
| ENG | 5 | {N} | {N} | {N} |
| ... | ... | ... | ... | ... |

## Questions & Answers

{Record all answers from Step 5 for future reference.}

## Next Phase

When the product advances to {next_phase}, run this orchestrator again to generate:
{List deferred artifacts with their IDs and departments.}
```

---

## Step 10: Verify

After generation, check:

- [ ] Every generated file references a governing SOP that exists in `praxis-perpetua/standards/`
- [ ] Every generated file has YAML frontmatter with generation metadata
- [ ] No existing substantive files were overwritten
- [ ] Phase gating was respected — no graduation artifacts in a foundation-phase product
- [ ] Questions were deduplicated — no question was asked twice
- [ ] Cross-references between department docs resolve (e.g., B3 references O1 which exists)
- [ ] `docs/README.md` index is complete and accurate
- [ ] Directory structure matches Step 7

---

*This orchestrator produces 45+ artifacts across 9 departments for a fully graduated product, or a subset for earlier phases.*
