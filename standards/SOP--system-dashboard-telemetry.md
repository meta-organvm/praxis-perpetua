# SOP: System Dashboard Telemetry (The Panopticon Protocol)

## 1. Ontological Purpose
This SOP formalizes how all 8 organs report real-time metrics, logs, and health status to the `system-dashboard` (FastAPI + HTMX). It ensures the meta-system maintains a unified, low-latency visual representation of its own autopoiesis.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** All repositories emitting telemetry, managed by META.

---

## 2. Phase I: Metric Standardization
**Goal:** Ensure universal readability.
1. **Schema Compliance:** All emitted metrics must conform to the `registry-v2.schema.json` telemetrics structure.
2. **Payload:** Every ping must include `organ_id`, `repo_name`, `timestamp`, `status` (GREEN, YELLOW, RED), and `te_burned` (Tokens Expended).

## 3. Phase II: High-Frequency Ingestion
**Goal:** Real-time visibility without bottlenecking the system.
1. **UDP Transport:** Use lightweight UDP packets or an async Redis queue for non-critical telemetry to avoid slowing down core processes.
2. **Aggregation:** The `system-dashboard` backend aggregates the data in a fast, in-memory cache (e.g., Redis).

## 4. Phase III: Cache Invalidation & UI Hydration
**Goal:** Reflect state changes instantly to the user.
1. **HTMX Polling:** The frontend UI uses HTMX to poll the backend cache every 5 seconds for updates.
2. **Critical Alerts:** If an organ emits a RED status (e.g., a CI build fails or a smart contract audit fails), the backend pushes an immediate Server-Sent Event (SSE) to force a UI re-render, flashing the screen and logging the error in the "Omega Scorecard."

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
