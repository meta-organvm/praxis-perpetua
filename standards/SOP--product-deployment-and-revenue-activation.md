---
sop: true
name: product-deployment-and-revenue-activation
scope: system
phase: hardening
triggers:
  - context:deployment
complements:
  - deployment-cicd
overrides: null
---
# SOP: Product Deployment & Revenue Activation

## 1. Ontological Purpose

This SOP governs the deployment of ORGAN-III commercial products and the activation of revenue streams. Deployment is not just "putting code on a server" — it is the transition from a governed development artifact to a living product that handles real traffic, real money, and real users. Every step in this procedure exists because its absence has caused failure in production systems.

Revenue activation is a state machine, not a binary switch. A product moves through defined states (pre-launch -> beta -> live -> sunset), each with its own requirements and verification gates.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--promotion-and-state-transitions.md` (deployment typically accompanies or follows promotion to PUBLIC_PROCESS), `SOP--cicd-resilience-and-recovery.md` (CI must pass before deployment), `SOP--security-and-accessibility-audit.md` (security audit required pre-deployment), Standard `12-habitat-governance-lifecycle.md` (governance artifacts for ORGAN-III)

---

## 2. Phase I: Pre-Deployment Checklist

### Process

1. **Verify development readiness:**
   - [ ] All tests pass (`pytest` / `npm test`)
   - [ ] Linter clean (`ruff check` / `eslint`)
   - [ ] Type checker clean (`pyright` / `tsc --noEmit`)
   - [ ] CI pipeline green on main branch

2. **Verify documentation readiness:**
   - [ ] `DEPLOY.md` or deployment section in README exists
   - [ ] Environment variables documented (every `process.env.*` or `os.environ[]` has a corresponding doc entry)
   - [ ] API documentation current (endpoints, auth, rate limits)

3. **Verify infrastructure readiness:**
   - [ ] Database provisioned and schema migrated
   - [ ] Domain configured (DNS, SSL)
   - [ ] CDN configured (if applicable)
   - [ ] Secrets stored in platform secret manager (never in code or .env committed to git)
   - [ ] **Container preflight completed** (if deploying to a container platform): execute `SOP--container-deployment-preflight.md` in full before proceeding to Phase II

4. **Verify governance readiness:**
   - [ ] `seed.yaml` current with correct `promotion_status`
   - [ ] Registry entry has `implementation_status: ACTIVE`
   - [ ] Security audit completed (see `SOP--security-and-accessibility-audit.md`)
   - [ ] For financial products: 2+ ADRs, 2-reviewer policy documented

### Starter Research Questions
- What environment variables does this application require?
- Is the database schema up to date with the codebase?
- Are there any secrets that need to be rotated before going live?
- Has a security scan been run recently?
- What is the expected traffic volume at launch?

---

## 3. Phase II: Hosting Deployment

### Process

1. **Select hosting platform** based on product requirements:

   | Platform | Best For | Cost Model |
   |----------|----------|------------|
   | **Render** | Full-stack apps, background workers, managed Postgres | Free tier + usage |
   | **Vercel** | Next.js/React frontends, serverless functions | Free tier + usage |
   | **Cloudflare** | Workers, Pages, R2 storage, edge compute | Generous free tier |
   | **GitHub Pages** | Static sites, pitch decks, documentation | Free |

2. **Deploy the application:**
   ```bash
   # Platform-specific deployment
   # Render: push to connected branch or use render.yaml
   # Vercel: vercel deploy --prod
   # Cloudflare: wrangler deploy
   ```

3. **Verify deployment health:**
   - [ ] Application loads at production URL
   - [ ] Health check endpoint responds (`/health` or `/api/health`)
   - [ ] All assets load (no 404s in DevTools Network tab)
   - [ ] Database connectivity confirmed
   - [ ] Environment variables resolved correctly

4. **Configure monitoring:**
   - Uptime monitoring (platform-native or external)
   - Error tracking (Sentry or equivalent)
   - Basic alerting on 5xx error rate

### Starter Research Questions
- Which platform best fits this product's architecture?
- Does the platform support the required runtime (Python, Node, etc.)?
- What is the cost at expected traffic volume?
- Is there a free tier sufficient for beta?
- Does the platform support the required database?

---

## 4. Phase III: Payment Integration

### Process

1. **Set up Stripe account/product:**
   - Create product in Stripe Dashboard
   - Define pricing model (subscription, one-time, usage-based)
   - Configure tax settings if applicable

2. **Implement payment flow:**
   - Stripe Checkout for simple flows
   - Stripe Elements for embedded forms
   - Webhook endpoint for event processing (`checkout.session.completed`, `invoice.paid`, `customer.subscription.deleted`)

3. **Sandbox testing:**
   - [ ] Complete purchase flow with test cards (4242...)
   - [ ] Verify webhook delivery in Stripe Dashboard
   - [ ] Test failure scenarios (declined card, insufficient funds)
   - [ ] Verify subscription lifecycle (create, upgrade, cancel, resume)

4. **Production cutover:**
   - Switch from test to live API keys
   - Update webhook endpoint to production URL
   - Verify first real transaction

### Starter Research Questions
- What is the pricing model? (subscription, one-time, freemium, commission)
- Does the product need metered billing?
- What payment methods are required? (card, ACH, international)
- Are there regulatory requirements for this product's payments?
- What happens when a payment fails — how does the product degrade?

---

## 5. Phase IV: Revenue Status Transition

### Process

1. **Update `revenue_status` in registry-v2.json** according to the state machine:

   ```
   pre-launch --> beta --> live --> sunset
       |                            ^
       +----------------------------+
              (skip beta if appropriate)
   ```

   | State | Criteria | Registry Value |
   |-------|----------|---------------|
   | **pre-launch** | No users, no payments | `"pre-revenue"` or `"pre-launch"` |
   | **beta** | Limited users, payments may be test-mode | `"beta"` |
   | **live** | Production payments, real users | `"live"` |
   | **sunset** | Winding down, no new customers | `"sunset"` |

2. **Update related registry fields:**
   ```bash
   organvm registry update <repo> revenue_status live
   organvm registry update <repo> implementation_status ACTIVE
   ```

3. **Document the revenue model:**
   - Update `revenue_model` field in registry
   - Ensure pricing is documented in README or product docs
   - Update pitch deck if pricing/revenue model changed

### Starter Research Questions
- What state is the product currently in?
- Are the transition criteria met for the next state?
- Is the revenue model accurately documented?
- Does the pitch deck reflect current pricing?

---

## 6. Phase V: Post-Launch Monitoring

### Process

1. **Establish baselines** (first 48 hours):
   - Response time p50, p95, p99
   - Error rate (target: < 0.1%)
   - Uptime (target: 99.9%)

2. **First-user verification:**
   - [ ] A real (non-creator) user has successfully completed the core flow
   - [ ] User feedback mechanism exists (feedback form, GitHub Issues, email)

3. **Post-launch checklist:**
   - [ ] Monitoring alerts configured and tested
   - [ ] Backup schedule verified (database, user data)
   - [ ] Incident response notes documented (even a paragraph in SECURITY.md)
   - [ ] Logs accessible and not expiring too quickly

4. **Weekly review (first month):**
   - Check error logs for new failure patterns
   - Review user feedback
   - Monitor cost vs. budget
   - Verify backup integrity

### Starter Research Questions
- What are acceptable latency thresholds for this product?
- What is the error budget for the first month?
- How will users report issues?
- What is the backup strategy and recovery time objective?
- At what traffic level do costs become a concern?

---

## 7. Output Artifacts

- Deployed and verified production application
- Health check endpoint responding
- Stripe integration (if revenue-generating) with tested webhooks
- Updated `registry-v2.json` with current `revenue_status` and `implementation_status`
- Monitoring and alerting configured
- `DEPLOY.md` or deployment documentation current
- Post-launch baseline metrics documented

---

## Appendix A: Platform Comparison Matrix

| Factor | Render | Vercel | Cloudflare | GitHub Pages |
|--------|--------|--------|------------|-------------|
| Full-stack apps | Yes | Limited (serverless) | Workers (V8) | No |
| Managed DB | Postgres | No | D1 (SQLite), Hyperdrive | No |
| Background jobs | Yes | Cron (limited) | Cron Triggers | No |
| Custom domains | Yes | Yes | Yes | Yes |
| Free tier | Generous | Generous | Very generous | Free |
| Auto-deploy from git | Yes | Yes | Yes | Yes |
| Best for | Python/Node backends | Next.js frontends | Edge-first apps | Static content |

## Appendix B: Environment Variable Checklist

Every deployment must verify these categories:

| Category | Variables | Source |
|----------|-----------|--------|
| Application | `DATABASE_URL`, `SECRET_KEY`, `APP_ENV` | Platform secrets |
| Payment | `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` | Stripe Dashboard |
| External APIs | Service-specific keys | Provider dashboards |
| Monitoring | `SENTRY_DSN` | Sentry project settings |
| Feature flags | `FEATURE_*` | Application config |

## Appendix C: Revenue Status State Machine

```
pre-launch -----> beta -----> live -----> sunset
    |                                       ^
    +---------------------------------------+
         (direct sunset if product abandoned)
```

| Transition | Gate |
|-----------|------|
| pre-launch -> beta | Deployment verified, test payments working |
| beta -> live | Real payments processing, first paying user |
| live -> sunset | Decision to wind down, no new customers accepted |

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
