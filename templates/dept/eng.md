# ENG — Engineering Department Templates

**Persona:** styx-engineering
**Linked Skills:** `api-design-patterns`, `backend-implementation-patterns`, `testing-patterns`, `tdd-workflow`, `coding-standards-enforcer`, `deployment-cicd`, `security-implementation-guide`

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier, produces/consumes edges
- From `package.json` / `pyproject.toml`: name, version, description, dependencies, scripts
- From `src/` directory: module structure, API routes, service classes
- From `.github/workflows/`: CI config, test commands, deploy targets
- From `CLAUDE.md`: tech stack, CLI commands, architecture notes
- From `docs/adr/`: existing ADRs (skip regeneration)
- From `docs/architecture/`: existing architecture docs (skip regeneration)

## Questions (ask once, shared across E1-E5)

1. Are there any architecture decisions already made but not documented? (List briefly)
2. What is the target test coverage percentage? (Default: 80%)

---

## E1: Architecture Decision Record Template

**Phase:** foundation+
**Governing SOP:** `SOP--architecture-decision-records.md`
**Output:** `docs/adr/adr-NNN-{slug}.md`

### Generation Instructions

1. Scan `docs/adr/` — determine next ADR number
2. For each undocumented decision from Question 1, generate an ADR following the format in `SOP--architecture-decision-records.md` §3
3. For new repos with no ADRs, generate foundational ADRs:
   - ADR-001: Technology stack selection (infer from `package.json`/`pyproject.toml`)
   - ADR-002: API protocol choice (infer from `src/` — REST routes? GraphQL schema? gRPC protos?)
   - ADR-003: Data storage selection (infer from dependencies — Postgres? SQLite? Redis? Neon?)
4. Update `docs/adr/README.md` with an index table

### Template

```markdown
# ADR-{NNN}: {Title}

**Status:** Accepted
**Date:** {today}
**Decision-makers:** styx-engineering
**Department:** ENG

## Context

{Infer from codebase — why was this technology/approach chosen? What problem does it solve?}

## Decision

{State the decision clearly — "We will use X for Y."}

## Consequences

### Positive
- {Infer from the choice — what does it enable?}

### Negative
- {Infer tradeoffs — what does it limit?}

### Neutral
- {Any side effects that are neither good nor bad}

## Alternatives Considered

| Alternative | Pros | Cons | Why Rejected |
|-------------|------|------|--------------|
| {alt1} | ... | ... | ... |
```

---

## E2: Technical Architecture Overview

**Phase:** genesis
**Governing SOP:** `SOP--repo-onboarding-and-habitat-creation.md`
**Output:** `docs/architecture/overview.md`

### Generation Instructions

1. Read `src/` directory tree — identify modules, services, and layers
2. Read `CLAUDE.md` — extract any architecture sections
3. Read `seed.yaml` — identify produces/consumes edges (external interfaces)
4. Read dependency manifests — identify major frameworks and their roles
5. Generate a layered architecture diagram (text/mermaid) and prose description

### Template

```markdown
# Technical Architecture — {product_name}

**Version:** {version from manifest}
**Stack:** {inferred from dependencies}
**Organ:** {organ from seed.yaml} | **Tier:** {tier}

## System Context

{One paragraph: what this product does, who uses it, where it fits in the ORGANVM system.}

## Component Diagram

{Mermaid diagram showing major modules/services and their relationships.}

```mermaid
graph TD
    A[{module1}] --> B[{module2}]
    B --> C[{external_service}]
```

## Module Inventory

| Module | Purpose | Key Files | Dependencies |
|--------|---------|-----------|--------------|
| {mod1} | ... | `src/{mod1}/` | ... |

## Data Flow

{How data moves through the system — ingress, processing, storage, egress.}

## External Interfaces

### Produces
{From seed.yaml produces edges — what events/data does this emit?}

### Consumes
{From seed.yaml consumes edges — what does this depend on?}

## Infrastructure

{Inferred from .github/workflows, Dockerfile, infra/ — where does this run?}
```

---

## E3: API Design Specification

**Phase:** foundation
**Governing SOP:** T1 skill `api-design-patterns`
**Output:** `docs/architecture/api-spec.md`

### Generation Instructions

1. Scan `src/` for route definitions (FastAPI `@app.get`, Express `router.get`, etc.)
2. Read existing OpenAPI/Swagger spec if present
3. Read `seed.yaml` produces edges — these are the external API contract
4. Group endpoints by resource/domain
5. Generate specification with request/response schemas

### Template

```markdown
# API Specification — {product_name}

**Base URL:** {infer from config or deployment}
**Auth:** {infer from middleware/deps — JWT? API key? OAuth?}
**Format:** {JSON | GraphQL | gRPC}

## Endpoints

### {Resource Group 1}

#### `{METHOD} {path}`

**Description:** {inferred from handler docstring or function name}
**Auth required:** {yes/no}

**Request:**
{Infer from parameter types, body schema}

**Response:**
{Infer from return type annotations}

**Errors:**
| Code | Meaning |
|------|---------|
| 400 | ... |
| 404 | ... |

## Data Models

{Infer from Pydantic models, TypeScript interfaces, or database schemas}

## Rate Limits

{If configured — infer from middleware. Otherwise: "Not yet configured."}

## Versioning Strategy

{Infer from URL patterns — /v1/? Header-based? None yet?}
```

---

## E4: Test Strategy & Coverage Plan

**Phase:** foundation
**Governing SOP:** T1 skill `testing-patterns`
**Output:** `docs/architecture/test-strategy.md`

### Generation Instructions

1. Read `tests/` directory — identify test types (unit, integration, e2e)
2. Read CI workflow — what test commands run?
3. Read `pyproject.toml`/`package.json` — coverage config?
4. Count test files and functions
5. Identify untested modules (compare `src/` modules to `tests/` files)

### Template

```markdown
# Test Strategy — {product_name}

**Framework:** {pytest | vitest | jest | ...}
**Current coverage:** {if measurable from CI config}
**Target coverage:** {from Question 2, default 80%}

## Test Types

| Type | Directory | Count | Runner |
|------|-----------|-------|--------|
| Unit | `tests/unit/` | {count} | {framework} |
| Integration | `tests/integration/` | {count} | {framework} |
| E2E | `tests/e2e/` | {count} | {framework} |

## Coverage Map

| Module | Test File | Tests | Coverage |
|--------|-----------|-------|----------|
| `src/{mod1}/` | `tests/test_{mod1}.py` | {count} | {estimate} |
| `src/{mod2}/` | — | 0 | **GAP** |

## Gaps & Priorities

{List modules with no test coverage, prioritized by risk/complexity.}

## CI Integration

{How tests run in CI — commands, triggers, failure handling.}

## Test Data Strategy

{How test data is managed — fixtures, factories, mocks, tmp_path.}
```

---

## E5: Performance & Load Test Report

**Phase:** hardening
**Governing SOP:** `SOP--completeness-verification.md`
**Output:** `docs/architecture/load-test-report.md`

### Generation Instructions

1. Read API spec (E3) — identify critical endpoints
2. Read infrastructure config — identify resource limits
3. Read any existing benchmark scripts in `tests/` or `scripts/`
4. Design load test scenarios based on expected usage patterns

### Template

```markdown
# Performance & Load Test Report — {product_name}

**Date:** {today}
**Environment:** {staging | production}
**Tool:** {k6 | locust | artillery | ab}

## Baseline Metrics

| Metric | Value | Target |
|--------|-------|--------|
| p50 latency | ... | < 200ms |
| p99 latency | ... | < 1s |
| Throughput | ... | > 100 rps |
| Error rate | ... | < 0.1% |

## Test Scenarios

### Scenario 1: {name}
- **Endpoint:** {path}
- **Concurrent users:** {N}
- **Duration:** {time}
- **Results:** {pass/fail + metrics}

## Bottlenecks Identified

| # | Bottleneck | Location | Severity | Mitigation |
|---|-----------|----------|----------|------------|
| 1 | ... | ... | ... | ... |

## Recommendations

{Prioritized list of performance improvements.}

## Next Steps

{When to re-run, what to add to CI.}
```

---

*Generates 5 artifacts: E1 (ADRs), E2 (architecture overview), E3 (API spec), E4 (test strategy), E5 (load test report)*
