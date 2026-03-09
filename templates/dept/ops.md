# OPS — Operations & Infrastructure Department Templates

**Persona:** styx-ops
**Linked Skills:** `incident-response-commander`, `deployment-cicd`, `gcp-resource-optimizer`

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier, produces/consumes edges
- From `.github/workflows/`: CI/CD config, test commands, deploy targets, secrets referenced
- From `Dockerfile` / `docker-compose.yml`: container setup, services, ports
- From `infra/` or `terraform/`: cloud resources, providers, regions
- From `package.json` / `pyproject.toml`: start scripts, dependencies (detect monitoring, logging libs)
- From `CLAUDE.md`: deployment instructions, environment variables

## Questions (ask once, shared across O1-O6)

1. What is your target uptime SLA? (99.9% / 99.99% / "best effort")
2. What cloud provider(s) are you using or planning to use? (Vercel / Railway / AWS / GCP / self-hosted)

---

## O1: Incident Response Runbook

**Phase:** hardening
**Governing SOP:** T1 skill `incident-response-commander`
**Output:** `docs/operations/incident-response.md`

### Generation Instructions

1. Read deployment config — identify failure domains (app crash, DB down, DNS, auth provider)
2. Read monitoring setup — what alerts exist?
3. Read `SOP--cicd-resilience-and-recovery.md` for recovery patterns
4. Generate severity classification and response procedures

### Template

```markdown
# Incident Response Runbook — {product_name}

**SLA Target:** {from Question 1}
**On-call:** {solo founder | team | automated}

## Severity Classification

| Severity | Definition | Response Time | Examples |
|----------|-----------|---------------|---------|
| SEV-1 | Service down, revenue impacted | < 15 min | App unreachable, payment failures |
| SEV-2 | Degraded, users affected | < 1 hour | Slow responses, partial feature failure |
| SEV-3 | Minor issue, workaround exists | < 4 hours | UI glitch, non-critical error |
| SEV-4 | Cosmetic or logged for later | Next business day | Typo, minor visual bug |

## Response Procedures

### SEV-1: Service Down
1. **Detect:** {monitoring alert / user report / health check}
2. **Assess:** {check deployment status, error logs, infrastructure status}
3. **Mitigate:** {rollback deployment / restart service / failover}
4. **Communicate:** {status page update / user notification}
5. **Resolve:** {root cause fix / deploy patch}
6. **Postmortem:** {within 24 hours}

### SEV-2: Degraded Performance
{Similar structure, lower urgency.}

## Key Commands

| Action | Command |
|--------|---------|
| Check status | {infer from CI/deployment} |
| View logs | {infer from provider} |
| Rollback | {infer from CI — git revert + deploy?} |
| Restart | {infer from deployment method} |

## Escalation

| Level | Who | When |
|-------|-----|------|
| L1 | Automated alerts | Always |
| L2 | {founder / styx-ops} | SEV-1/2 |
| L3 | Cloud provider support | Infrastructure failure |

## Postmortem Template

| Field | Content |
|-------|---------|
| Date | ... |
| Severity | ... |
| Duration | ... |
| Root cause | ... |
| Impact | ... |
| Action items | ... |
```

---

## O2: Deployment Procedure

**Phase:** foundation
**Governing SOP:** `SOP--product-deployment-and-revenue-activation.md`
**Output:** `docs/operations/deployment-procedure.md`

### Generation Instructions

1. Read `.github/workflows/` — identify deploy workflows, triggers, environments
2. Read `Dockerfile` / deployment config
3. Read `package.json` / `pyproject.toml` — build and start commands
4. Document the full deploy pipeline: build → test → deploy → verify

### Template

```markdown
# Deployment Procedure — {product_name}

**Platform:** {from Question 2}
**Method:** {CI/CD | manual | hybrid}
**Environments:** {production | staging | preview}

## Prerequisites

- [ ] All tests passing (`{test command from CI}`)
- [ ] Linting clean (`{lint command}`)
- [ ] Environment variables configured (see below)

## Environment Variables

| Variable | Required | Description | Source |
|----------|----------|-------------|--------|
| {var} | Yes | {purpose} | {from .github/workflows secrets} |

## Deploy Pipeline

### 1. Build
```
{build command from CI or manifest}
```

### 2. Test
```
{test command}
```

### 3. Deploy
```
{deploy command or CI trigger description}
```

### 4. Verify
- [ ] Health check endpoint responds
- [ ] Core user flow works
- [ ] No error spike in logs

## Rollback Procedure

{How to revert — git revert + redeploy? Provider-specific rollback?}

## Deployment History

| Date | Version | Deployer | Notes |
|------|---------|----------|-------|
| {today} | {version} | styx-ops | Initial documentation |
```

---

## O3: Monitoring & Alerting Setup

**Phase:** hardening
**Governing SOP:** `SOP--cicd-resilience-and-recovery.md`
**Output:** `docs/operations/monitoring-setup.md`

### Generation Instructions

1. Read dependencies for monitoring/logging libraries (Sentry, Datadog, Prometheus, pino, etc.)
2. Read deployment platform — what built-in monitoring exists?
3. Define alert rules based on SLA target (Question 1)

### Template

```markdown
# Monitoring & Alerting — {product_name}

**Monitoring provider:** {inferred from deps or Question 2's platform}
**Logging provider:** {inferred}
**SLA target:** {from Question 1}

## Metrics Tracked

| Metric | Source | Alert Threshold | Severity |
|--------|--------|----------------|----------|
| Uptime | Health check | < {SLA}% over 5 min | SEV-1 |
| Error rate | Application logs | > 1% | SEV-2 |
| p99 latency | APM | > 2s | SEV-2 |
| Disk/memory usage | Infrastructure | > 85% | SEV-3 |

## Alert Channels

| Channel | When | Who |
|---------|------|-----|
| {Email / Slack / PagerDuty} | SEV-1/2 | {founder} |
| {Dashboard} | All | styx-ops |

## Health Check Endpoint

- **URL:** `{base_url}/health`
- **Expected response:** `200 OK`
- **Check interval:** {60s / 300s}

## Log Access

| Environment | How to access |
|-------------|---------------|
| Production | {provider dashboard URL / CLI command} |
| Staging | {same} |
```

---

## O4: Database Backup & Recovery

**Phase:** foundation
**Governing SOP:** `SOP--cicd-resilience-and-recovery.md`
**Output:** `docs/operations/backup-recovery.md`

### Generation Instructions

1. Read dependencies for database (Postgres/Neon, SQLite, MongoDB, etc.)
2. Read infrastructure config for backup settings
3. Design backup strategy based on data criticality

### Template

```markdown
# Database Backup & Recovery — {product_name}

**Database:** {inferred from deps}
**Provider:** {Neon / Supabase / self-hosted / etc.}

## Backup Strategy

| Type | Frequency | Retention | Method |
|------|-----------|-----------|--------|
| Automated snapshot | {daily} | {30 days} | {provider feature} |
| Point-in-time recovery | Continuous | {7 days} | {WAL archiving / provider feature} |
| Manual export | {weekly} | {indefinite} | {pg_dump / mongodump / script} |

## Recovery Procedures

### Scenario 1: Accidental data deletion
1. {Identify the point-in-time before deletion}
2. {Restore from PITR or snapshot}
3. {Verify data integrity}

### Scenario 2: Database corruption
1. {Stop writes}
2. {Restore from latest clean snapshot}
3. {Replay WAL if available}

### Scenario 3: Full disaster recovery
1. {Provision new database instance}
2. {Restore from off-site backup}
3. {Update connection strings}
4. {Verify and resume service}

## Testing Schedule

- Backup restoration test: {monthly}
- Last tested: {never — schedule first test}
```

---

## O5: Cost Management & Scaling Policy

**Phase:** graduation
**Governing SOP:** `SOP--business-organism-design.md`
**Output:** `docs/operations/cost-management.md`

### Generation Instructions

1. Read infrastructure config — identify all paid services
2. Read deployment platform pricing model
3. Read revenue projections from FIN docs if available
4. Define scaling triggers and cost guardrails

### Template

```markdown
# Cost Management & Scaling — {product_name}

## Current Infrastructure Costs

| Service | Provider | Plan | Monthly Cost | Notes |
|---------|----------|------|-------------|-------|
| {Hosting} | {provider} | {plan} | ${amount} | ... |
| {Database} | {provider} | {plan} | ${amount} | ... |
| {AI/API} | {provider} | {plan} | ${amount} | ... |
| **Total** | | | **${total}** | |

## Scaling Triggers

| Metric | Current | Scale-up Trigger | Action |
|--------|---------|-----------------|--------|
| Users | {N} | {threshold} | {upgrade plan / add capacity} |
| API calls | {N}/mo | {threshold} | {rate limit / scale} |
| Storage | {N} GB | {threshold} | {archive / expand} |

## Cost Guardrails

- Monthly spend limit: ${max}
- Alert at: ${alert_threshold} (80% of limit)
- Auto-scale: {enabled / disabled / manual approval}

## Optimization Opportunities

{List identified opportunities — caching, CDN, reserved instances, etc.}
```

---

## O6: On-Call Rotation & Escalation

**Phase:** graduation
**Governing SOP:** references O1 (incident response)
**Output:** `docs/operations/oncall-rotation.md`

### Generation Instructions

1. Read O1 incident response for severity levels
2. Assess team size (solo founder = simplified rotation)
3. Design rotation that prevents burnout

### Template

```markdown
# On-Call Rotation — {product_name}

## Current Setup

**Team size:** {solo founder | N people}
**Rotation:** {24/7 | business hours only | automated-first}

## Schedule

{For solo founders:}
- Automated monitoring handles SEV-3/4
- Phone alerts for SEV-1/2 during {hours}
- Acknowledge within {response time from O1}

{For teams:}
| Week | Primary | Secondary |
|------|---------|-----------|
| 1 | ... | ... |

## Escalation Matrix

{Reference O1 escalation table.}

## Burnout Prevention

- Maximum consecutive on-call days: {N}
- Mandatory handoff at rotation end
- Post-incident cooldown: {hours}
```

---

*Generates 6 artifacts: O1 (incident response), O2 (deployment), O3 (monitoring), O4 (backup/recovery), O5 (cost management), O6 (on-call)*
