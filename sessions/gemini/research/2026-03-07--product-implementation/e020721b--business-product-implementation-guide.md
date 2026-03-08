# ADR-001: Technical Architecture for Organ III Business Products

## Status
Proposed

## Context
A new business product needs to be implemented within `organvm-iii-ergon` (Organ III: Commerce). It must respect the unidirectional flow (I &rarr; II &rarr; III), integrate with ORGAN-IV (Taxis) for orchestration, and follow the established Ergon aesthetic.

## Decision
We will adopt a **Modular Monorepo** architecture using **Turborepo**, following the "Hexagonal Architecture" pattern observed in the `life-my--midst--in` flagship repository.

### Technical Stack
*   **Runtime:** Node.js 25.x
*   **Monorepo Manager:** Turborepo / pnpm Workspaces
*   **Frontend:** Next.js 16 (App Router) with TypeScript (Strict Mode)
*   **Backend API:** Fastify (for high performance) or Express.js (for simple microservices)
*   **Persistence:** PostgreSQL (ACID compliant) with Prisma or Drizzle ORM
*   **Background Jobs:** BullMQ + Redis (for asynchronous task processing)
*   **Schema & Validation:** Zod (Schema-first design)
*   **UI/UX:** ShadCN UI components + Tailwind CSS v4
*   **Testing:** Vitest (Unit/Integration) + Playwright (E2E)

### Architectural Patterns
1.  **Hexagonal Architecture:** Decouple core business logic from framework-specific code (routes, database adapters).
2.  **Schema-First:** Define all data models in a shared `packages/schema` package using Zod before implementing UI or services.
3.  **Repository Pattern:** Abstract database access behind interfaces to ensure testability and modularity.
4.  **Functional Core, Imperative Shell:** Keep the core logic pure and handle side effects at the boundaries (apps).

## Consequences
*   **Pros:** High modularity, strict type safety across the stack, consistent with enterprise flagship models, easy to test.
*   **Cons:** Higher initial setup complexity due to monorepo structure.

---

# seed.yaml Template (Organ III)

```yaml
# seed.yaml — Automation Contract for organvm-iii-ergon/[product-name]
# Schema: seed/v1.0
# Category: standard

schema_version: "1.0"
organ: III
organ_name: Commerce
repo: [product-name]
org: organvm-iii-ergon

metadata:
  implementation_status: DEVELOPMENT
  tier: standard
  promotion_status: LOCAL
  last_validated: "2026-03-07"
  sprint: "ERGO-PHASE-1"

agents:
  - name: ci
    trigger: on_push
    workflow: .github/workflows/ci.yml
    description: "Main CI pipeline for testing and building"
  - name: aesthetic-guard
    trigger: on_pull_request
    action: "Lint components against organ-aesthetic.yaml palette"

subscriptions:
  - event: governance.updated
    source: ORGAN-IV
    action: "Trigger local compliance check"
  - event: system.health-check
    source: ORGAN-IV
    action: "Emit health telemetry to .github/events/"

produces:
  - event: product.operational-state
    destination: ORGAN-IV
    description: "Broadcasts operational readiness and state changes"
  - event: product.telemetry
    destination: ORGAN-V
    description: "Read-only metrics for observation and analytics"
```

---

# Implementation Guide: Cross-Organ Propagation

## 1. Registry Integration (META-ORGANVM)
Once the repository is initialized, it must be added to `meta-organvm/registry-v2.json`.
*   **Action:** Submit a PR to `meta-organvm` updating the registry with the new repo metadata.

## 2. Orchestration Handshake (ORGAN-IV)
The product interacts with Taxis via the event bus.
*   **Action:** Implement a listener in `.github/workflows/` that responds to `governance.updated` events.
*   **Action:** Ensure the `produces` events defined in `seed.yaml` are correctly emitted to the shared event path in `.github/`.

## 3. Observability Link (ORGAN-V)
Logos observes the product without direct coupling.
*   **Action:** Expose a `/metrics` or `/telemetry` endpoint (Prometheus format) that is accessible to ORGAN-V's analytics engine.
*   **Constraint:** Ensure this link is strictly read-only from the perspective of ORGAN-V.

## 4. Promotion Workflow
Follow the Conductor OS lifecycle:
*   **FRAME:** Create the SDD and Architecture docs.
*   **SHAPE:** Finalize the schemas and `seed.yaml`.
*   **BUILD:** Implement core logic and UI.
*   **PROVE:** Run the full test suite and trigger `conductor wip promote`.
