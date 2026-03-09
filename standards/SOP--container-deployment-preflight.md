---
sop: true
name: container-deployment-preflight
scope: system
phase: hardening
triggers:
  - context:deployment
  - context:container
complements:
  - deployment-cicd
overrides: null
---
# SOP: Container Deployment Preflight

**Version:** 1.0.0 | **Date:** March 9, 2026 | **Status:** Active
**Scope:** Pre-deployment verification checklist for containerized applications targeting cloud platforms (Fly.io, Railway, Render, Cloud Run, etc.).

---

## 1. Ontological Purpose

Container platforms impose architectural constraints that do not exist in local development. A Node.js server binding `localhost:3000` works perfectly on a laptop but is unreachable behind a Fly.io proxy expecting `0.0.0.0`. A default 1MB body limit handles form submissions but blocks batch ingestion payloads. A frontend using relative `/api` paths works with a collocated backend but fails when API and UI deploy to different origins.

These are not bugs — they are environment mismatches that manifest only at deploy time. This SOP eliminates the 3-commit fix→deploy→fix cycle by catching every container-specific failure mode before the first deployment attempt.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--product-deployment-and-revenue-activation.md` (Phase II: Hosting Deployment), `SOP--cicd-resilience-and-recovery.md`
**Precedent:** Knowledge Base → Fly.io triple-fix (2026-03-08): commits `c5f4032`, `e8c3c70`, `0abb402` — bind address, body limit, CORS origin.

---

## 2. Trigger

Execute this SOP before any deployment to a container platform where the application has not been previously deployed, or when migrating between container platforms.

---

## 3. Phase I: Network Binding Verification

### Process

1. **Check server bind address.** The application must bind to `0.0.0.0`, not `127.0.0.1` or `localhost`.
   - Node.js/Express: `app.listen(PORT, '0.0.0.0')`
   - Python/Flask: `app.run(host='0.0.0.0')`
   - Python/Uvicorn: `uvicorn app:app --host 0.0.0.0`
   - Go: `http.ListenAndServe(":PORT", handler)`

2. **Check port configuration.** The application must read its port from an environment variable (`PORT` is the convention for most platforms).
   - [ ] Port is not hardcoded
   - [ ] `PORT` env var is read with a sensible default for local dev

3. **Check health endpoint.** The platform needs a way to verify the container is alive.
   - [ ] `/health` or `/api/health` endpoint exists
   - [ ] Endpoint returns 200 OK with no authentication required
   - [ ] Endpoint responds within 2 seconds

### Deliverables
- Bind address verified or corrected
- Port configuration verified or corrected
- Health endpoint verified or created

---

## 4. Phase II: Payload & Limit Configuration

### Process

1. **Identify maximum expected payload size** for all API endpoints.
   - File uploads: what is the largest expected file?
   - Batch operations: what is the largest batch payload?
   - JSON bodies: what is the largest expected request body?

2. **Configure body parser limits** to accommodate the maximum payload plus 20% headroom.
   - Express: `express.json({ limit: '50mb' })`
   - FastAPI/Starlette: configure via middleware or Uvicorn `--limit-concurrency`
   - Default limits are typically 1MB — almost always insufficient for batch operations

3. **Configure platform-level limits** if the platform enforces its own:
   - Fly.io: `max_request_body_size` in `fly.toml` (services section)
   - Cloud Run: `--max-request-body-size` flag
   - Nginx (if reverse proxy): `client_max_body_size`

4. **Configure timeouts** for long-running requests:
   - [ ] Platform-level request timeout set (default is often 60s)
   - [ ] Application-level timeout matches or exceeds platform timeout
   - [ ] Long operations use background jobs, not synchronous requests

### Deliverables
- Body limit configured at application and platform level
- Timeout budget documented

---

## 5. Phase III: CORS & Origin Configuration

### Process

1. **Enumerate all frontends** that will call this API:
   - Production frontend URL
   - Staging/preview URLs
   - Local development URL (`http://localhost:3000` or similar)

2. **Configure CORS origins** as an explicit allowlist — never use `*` in production:
   ```
   CORS_ORIGINS=https://app.example.com,https://staging.example.com,http://localhost:3000
   ```

3. **Configure frontend API base URL** as an environment variable:
   - [ ] Frontend reads API URL from environment, not hardcoded
   - [ ] URL does not include trailing slash
   - [ ] URL is the full origin (`https://api.example.com`), not a relative path

4. **Verify CORS headers** in response:
   - [ ] `Access-Control-Allow-Origin` matches the request origin
   - [ ] `Access-Control-Allow-Methods` includes all used methods
   - [ ] `Access-Control-Allow-Headers` includes `Content-Type` and `Authorization`
   - [ ] Preflight (OPTIONS) requests return 200

### Deliverables
- CORS origin allowlist configured
- Frontend API base URL externalized to environment variable

---

## 6. Phase IV: Environment & Secrets Verification

### Process

1. **Audit all environment variables** the application reads:
   ```bash
   grep -rn 'process\.env\.' src/ || grep -rn 'os\.environ' src/ || grep -rn 'os\.getenv' src/
   ```

2. **Classify each variable:**
   - **Required:** Application will not start without it
   - **Optional:** Has a default, but behavior changes
   - **Secret:** Must be in platform secret manager (never in Dockerfile or fly.toml) <!-- allow-secret -->

3. **Verify all required variables are set** in the target platform's secret/env configuration.

4. **Verify database connectivity:**
   - [ ] `DATABASE_URL` points to a reachable host from the container network <!-- allow-secret -->
   - [ ] Connection string uses SSL if required by the provider
   - [ ] Connection pooling configured for container lifecycle (containers restart)

### Deliverables
- Environment variable audit table (variable, classification, status)
- All secrets stored in platform secret manager

---

## 7. Phase V: Post-Deploy Smoke Test

### Process

1. **Verify the application starts:**
   - [ ] Platform shows healthy status
   - [ ] Health endpoint returns 200
   - [ ] Logs show no startup errors

2. **Verify end-to-end flow:**
   - [ ] Frontend loads and renders
   - [ ] Frontend successfully calls API (check Network tab — no CORS errors)
   - [ ] A representative write operation succeeds (create, update, or upload)
   - [ ] A representative read operation returns expected data

3. **Verify DNS/proxy reachability:**
   - [ ] Custom domain resolves to the platform
   - [ ] HTTPS certificate is valid and not expired
   - [ ] HTTP→HTTPS redirect works

### Deliverables
- Smoke test results logged
- Any failures documented and fixed before announcing deployment

---

## 8. Output Artifacts

- Completed preflight checklist (this SOP's checkboxes)
- Environment variable audit table
- CORS origin allowlist documented in deployment config
- Post-deploy smoke test log

---

## 9. Success Criteria

- Zero fix→deploy→fix cycles after initial deployment
- All 5 phases completed before first `fly deploy` / `render deploy` / equivalent
- Health endpoint responds within 2 seconds of deploy completion

---

## 10. Cross-References

- `SOP--product-deployment-and-revenue-activation.md` — parent deployment procedure; this SOP is a detailed sub-procedure for Phase II
- `SOP--cicd-resilience-and-recovery.md` — CI must pass before container deployment
- `SOP--security-and-accessibility-audit.md` — security audit covers secrets management

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
