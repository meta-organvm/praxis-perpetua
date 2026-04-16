# SOP: Domain Architecture & DNS Governance (The Concentric Circles)

## 0. Metadata (The Contract)

- **objective**: Establish, maintain, and evolve a three-circle domain architecture providing professional identity, system addressability, custom email, and API endpoints — all governed by environment variables and Cloudflare infrastructure
- **input_conditions**: Cloudflare account active; chezmoi.toml populated with `domain_*` fields; 1Password available for API credentials
- **output_artifacts**: 6 registered domains, DNS records, email routing rules, redirect rules, env vars in every shell session
- **command_sequence**: See §3 Phased Execution
- **quality_gates**: All domains resolve; email forwarding functional; redirects return 301; env vars present in `env | grep DOMAIN_`; DNSSEC enabled; SPF/DKIM/DMARC pass
- **evidence_required**: `dig` output for each domain; email delivery test; `curl -I` redirect verification; Cloudflare dashboard screenshots (quarterly)
- **metrics_captured**: Domain count, annual cost, email routing success rate, DNS propagation time
- **revision_triggers**: Domain expiration within 60 days; new organ added to ORGANVM; Cloudflare pricing change > 20%; TLD regulatory change (e.g., .io sovereignty); new service requiring a subdomain
- **owner**: Anthony James Padavano / `4444J99`
- **last_validated**: 2026-04-16

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** All ORGANVM organs, portfolio, career infrastructure, commercial products.

---

## 1. Ontological Purpose

A system without addressable surfaces is invisible. ORGANVM operates across 10 organs and 145+ repositories, but presents zero public DNS surface — all traffic routes through GitHub's subdomain (`4444j99.github.io`) or ephemeral platform URLs. This SOP establishes domain infrastructure as a first-class system primitive, governed by the same env-var/chezmoi pipeline that manages identity, secrets, and shell configuration.

The architecture uses three concentric circles — each with distinct function, audience, and lifecycle:

| Circle | Domain(s) | Function | Audience |
|--------|-----------|----------|----------|
| **Handle** (innermost) | `$DOMAIN_HANDLE` | Compact identity, shortlinks, bio URL | Everyone — verbal, card, bio |
| **Name** (middle) | `$DOMAIN_NAME`, `$DOMAIN_NAME_DEF` | Career anchor, portfolio, email | Recruiters, collaborators, professionals |
| **System** (outermost) | `$DOMAIN_SYSTEM`, `$DOMAIN_SYSTEM_ORG`, `$DOMAIN_SYSTEM_DEF` | Organ subdomains, APIs, community | Users, contributors, subscribers |

---

## 2. Retrospective Analysis (Looking Back)

### What Failed

| Item | Analysis |
|------|----------|
| `met4vers.io` (GoDaddy) | Purchased without integration plan. No DNS records configured. Expired Mar 29, 2026 in grace period. $50/yr burned with zero utility. **Lesson:** Never register a domain without an SOP entry and at minimum one A/CNAME record. |
| GoDaddy as registrar | Upsell-heavy, markup pricing, no CDN/Workers integration. Migration friction. **Lesson:** Registrar = infrastructure vendor, not a shopping cart. |
| GitHub Pages as sole host | URL not career-portable (`4444j99.github.io/portfolio/`), base path `/portfolio` pollutes all links, no custom email, no API hosting. **Lesson:** Platform hosting is a deployment target, not an identity anchor. |
| Netlify mirror (`4444j99-portfolio.netlify.app`) | Exists but undocumented, no DNS pointed at it, no purpose. Shadow deployment. **Lesson:** Every deployment target must be in `seed.yaml` or deleted. |

### What Worked

| Item | Analysis |
|------|----------|
| Cloudflare migration | Already in progress. At-cost pricing, integrated DNS/CDN/Workers/Pages/Email Routing. Single vendor, single dashboard. |
| chezmoi identity pattern | `org_liminal`, `github_primary`, `email` in chezmoi.toml → rendered into `dot_zshenv.tmpl` → available in every shell. Domain vars follow the same pipeline. |
| Organ naming convention | `ORG_I` through `ORG_META` as env vars. Domain subdomains mirror this: `theoria.organvm.dev` for Organ I. No new naming required. |

---

## 3. Phased Execution

### Phase 1: Registration (Day 1)

**Pre-condition:** Cloudflare account active, payment method on file.

1. Navigate to `domains.cloudflare.com`
2. Search and register each domain (verify availability before purchase):

| Domain | Expected Cost | Fallback if taken |
|--------|--------------|-------------------|
| `4jp.dev` | $10.18/yr | `4jpdev.com` ($10.46) |
| `anthonypadavano.com` | $10.46/yr | `apadavano.com` or `anthonyjpadavano.com` |
| `anthonypadavano.dev` | $10.18/yr | Skip if .com acquired |
| `organvm.dev` | $10.18/yr | `organvm.systems` ($27.20) |
| `organvm.org` | $10.13/yr | `organvm.community` |
| `organvm.io` | $50.00/yr | Defer — purely defensive |

3. Enable DNSSEC on all domains
4. Enable auto-renew on all domains
5. Update `chezmoi.toml` `[data]` section with actual registered domains (if fallbacks used)
6. Run `chezmoi apply` to propagate domain vars into shell environment

**Evidence:** Cloudflare dashboard showing all domains active. `env | grep DOMAIN_` output.

### Phase 2: Email Infrastructure (Day 1-2)

1. Configure Cloudflare Email Routing on `$DOMAIN_NAME`:
   - `anthony@` → primary inbox (currently `$email` in chezmoi.toml)
   - `aj@` → alias to same
   - Catch-all → forward to primary
2. Configure Cloudflare Email Routing on `$DOMAIN_HANDLE`:
   - Catch-all → forward to primary
3. Configure Cloudflare Email Routing on `$DOMAIN_SYSTEM`:
   - `system@` → operational inbox
   - `api@` → transactional email (future)
4. Set DNS records on all email-enabled domains:
   - SPF: `v=spf1 include:_spf.mx.cloudflare.net ~all`
   - DKIM: Generated by Cloudflare Email Routing
   - DMARC: `v=DMARC1; p=quarantine; rua=mailto:dmarc@$DOMAIN_NAME`

**Quality gate:** Send test email to `$DOMAIN_EMAIL`. Must arrive within 60 seconds. Check headers for SPF=pass, DKIM=pass, DMARC=pass.

### Phase 3: Redirect Architecture (Day 2)

Configure Cloudflare Redirect Rules (not Page Rules — those are deprecated):

| Source | Target | Type |
|--------|--------|------|
| `$DOMAIN_HANDLE/*` | `https://$DOMAIN_NAME/$1` | 301 Permanent |
| `$DOMAIN_NAME_DEF/*` | `https://$DOMAIN_NAME/$1` | 301 Permanent |
| `$DOMAIN_SYSTEM_DEF/*` | `https://$DOMAIN_SYSTEM/$1` | 301 Permanent |
| `resume.$DOMAIN_NAME` | `https://$DOMAIN_NAME/resume` | 301 Permanent |

**Quality gate:** `curl -I https://$DOMAIN_HANDLE` returns `301` with `Location: https://$DOMAIN_NAME/`.

### Phase 4: Portfolio Migration (Day 2-5)

**This is a high-risk step.** The portfolio's `CLAUDE.md` explicitly marks changing `base` from `/portfolio` to `/` as "total breakage — nothing automated."

1. Create Cloudflare Pages project linked to `4444J99/portfolio` repo
2. Configure custom domain `$DOMAIN_NAME` on the Pages project
3. **Feature branch:** Create `feat/domain-migration` in portfolio
4. Update `astro.config.mjs`: change `base` from `/portfolio` to `/`
5. Update `canonicalBase` in `src/utils/paths.ts`
6. Update all internal links that hardcode `/portfolio/` prefix
7. Run `npm run sync:a11y-routes` (route manifest regeneration)
8. Run full quality suite: `npm run quality:local`
9. Keep GitHub Pages active during migration (zero-downtime cutover)
10. After Cloudflare Pages deploys successfully, update `seed.yaml` `deployment_url`
11. Decommission Netlify mirror

**Quality gate:** `npm run quality:local` passes. Lighthouse scores maintained. All internal links resolve.

### Phase 5: System Subdomains (Day 5-14)

1. Create CNAME/A records for each organ subdomain:

| Subdomain | Organ | Initial Target |
|-----------|-------|----------------|
| `theoria.$DOMAIN_SYSTEM` | I | Parking page or GitHub org redirect |
| `poiesis.$DOMAIN_SYSTEM` | II | Parking page or GitHub org redirect |
| `ergon.$DOMAIN_SYSTEM` | III | Parking page or GitHub org redirect |
| `taxis.$DOMAIN_SYSTEM` | IV | Parking page or GitHub org redirect |
| `logos.$DOMAIN_SYSTEM_ORG` | V | Parking page or GitHub org redirect |
| `koinonia.$DOMAIN_SYSTEM_ORG` | VI | Parking page or GitHub org redirect |
| `kerygma.$DOMAIN_SYSTEM_ORG` | VII | Parking page or GitHub org redirect |
| `meta.$DOMAIN_SYSTEM` | META | System dashboard (when ready) |
| `api.$DOMAIN_SYSTEM` | III/IV | Cloudflare Worker (when ready) |
| `status.$DOMAIN_SYSTEM` | META | Health monitor (when ready) |

2. Set up `go.$DOMAIN_HANDLE` link shortener (Cloudflare Workers KV)
3. Configure wildcard redirect `*.$DOMAIN_SYSTEM_DEF` → `*.$DOMAIN_SYSTEM`

### Phase 6: Domus Integration (Day 14+)

1. Update `AGENTS.md.tmpl` with domain mapping table
2. Update `CLAUDE.md` (domus) with domain architecture section
3. Update all `seed.yaml` files with `deployment_url` pointing to organ subdomains
4. Run `organvm context sync` to propagate domain references to all CLAUDE.md files

---

## 4. Environment Variable Reference

### Identity Layer (chezmoi.toml → dot_zshenv.tmpl)

| Variable | Example Value | Source |
|----------|---------------|--------|
| `DOMAIN_HANDLE` | `4jp.dev` | `chezmoi.toml: domain_handle` |
| `DOMAIN_NAME` | `anthonypadavano.com` | `chezmoi.toml: domain_name` |
| `DOMAIN_NAME_DEF` | `anthonypadavano.dev` | `chezmoi.toml: domain_name_defensive` |
| `DOMAIN_SYSTEM` | `organvm.dev` | `chezmoi.toml: domain_system` |
| `DOMAIN_SYSTEM_ORG` | `organvm.org` | `chezmoi.toml: domain_system_org` |
| `DOMAIN_SYSTEM_DEF` | `organvm.io` | `chezmoi.toml: domain_system_defensive` |
| `DOMAIN_EMAIL` | `anthony@anthonypadavano.com` | `chezmoi.toml: domain_email` |
| `DOMAIN_REGISTRAR` | `cloudflare` | `chezmoi.toml: domain_registrar` |

### Derived Layer (15-env.zsh, computed from identity vars)

| Variable | Computed Value | Purpose |
|----------|----------------|---------|
| `DOMAIN_ORGAN_I` | `theoria.organvm.dev` | Organ I subdomain |
| `DOMAIN_ORGAN_II` | `poiesis.organvm.dev` | Organ II subdomain |
| `DOMAIN_ORGAN_III` | `ergon.organvm.dev` | Organ III subdomain |
| `DOMAIN_ORGAN_IV` | `taxis.organvm.dev` | Organ IV subdomain |
| `DOMAIN_ORGAN_V` | `logos.organvm.org` | Organ V subdomain (.org) |
| `DOMAIN_ORGAN_VI` | `koinonia.organvm.org` | Organ VI subdomain (.org) |
| `DOMAIN_ORGAN_VII` | `kerygma.organvm.org` | Organ VII subdomain (.org) |
| `DOMAIN_ORGAN_META` | `meta.organvm.dev` | META organ subdomain |
| `DOMAIN_API` | `api.organvm.dev` | API gateway |
| `DOMAIN_STATUS` | `status.organvm.dev` | Health monitoring |
| `DOMAIN_SHORTENER` | `go.4jp.dev` | Vanity link shortener |
| `DOMAIN_PORTFOLIO` | `https://anthonypadavano.com` | Portfolio canonical URL |
| `DOMAIN_RESUME` | `https://resume.anthonypadavano.com` | Resume direct link |

---

## 5. Forward Evolution (Looking Ahead)

### Triggers for SOP Revision

| Trigger | Action |
|---------|--------|
| New organ added | Add `DOMAIN_ORGAN_*` env var to `15-env.zsh`, add subdomain to Cloudflare, update this SOP |
| Commercial product launches (Organ III) | Allocate dedicated subdomain under `ergon.$DOMAIN_SYSTEM` or product-specific domain |
| Email send-as needed | Upgrade from Cloudflare Email Routing to Google Workspace ($7.20/mo) or Fastmail ($5/mo) |
| API traffic exceeds free tier | Evaluate Cloudflare Workers Paid ($5/mo) vs. dedicated hosting |
| `.io` TLD regulatory change | Drop `$DOMAIN_SYSTEM_DEF` if .io becomes unstable; redirect traffic to `.dev` |
| Community growth (Organ VI) | Consider dedicated community domain or platform (e.g., community.organvm.org) |
| Content syndication scales | Add POSSE endpoints on `kerygma.$DOMAIN_SYSTEM_ORG` |

### Annual Review Checklist

- [ ] All 6 domains show auto-renew enabled in Cloudflare
- [ ] `dig +dnssec $DOMAIN_NAME` shows valid RRSIG records
- [ ] Email test: send to `$DOMAIN_EMAIL`, verify headers (SPF/DKIM/DMARC pass)
- [ ] All redirects functional: `curl -I` on handle, defensive, and resume subdomains
- [ ] Orphan DNS records audit: no records pointing to decommissioned services
- [ ] Cost audit: compare Cloudflare invoice to expected $101.13/yr
- [ ] env vars present: `env | grep DOMAIN_ | wc -l` returns ≥ 21

---

## 6. Cost Model

| Domain | TLD | Registrar | Annual | Circle |
|--------|-----|-----------|--------|--------|
| `4jp.dev` | .dev | Cloudflare | $10.18 | Handle |
| `anthonypadavano.com` | .com | Cloudflare | $10.46 | Name |
| `anthonypadavano.dev` | .dev | Cloudflare | $10.18 | Name (defensive) |
| `organvm.dev` | .dev | Cloudflare | $10.18 | System |
| `organvm.org` | .org | Cloudflare | $10.13 | System |
| `organvm.io` | .io | Cloudflare | $50.00 | System (defensive) |
| **Total** | | | **$101.13** | |
| **Without .io** | | | **$51.13** | |

> **Pricing note (verified 2026-04-16):** For `.io` specifically, Vercel charges $37.99/yr vs. Cloudflare's $50.00. If cost matters, `organvm.io` could be registered via Vercel (saving $12/yr) while keeping all other domains on Cloudflare. All 9 domains (primary + fallbacks) confirmed available as of 2026-04-16.

### Complementary Services (Future)

| Service | Provider | Cost | When |
|---------|----------|------|------|
| Email send-as | Fastmail or Google Workspace | $5-7.20/mo | When outbound email from custom domain needed |
| Workers Paid | Cloudflare | $5/mo | When API or shortener exceeds free tier (100K req/day) |
| R2 Storage | Cloudflare | $0.015/GB/mo | When hosting static assets beyond Pages limits |

---

## 7. Design Rationale

**Why `.dev` over `.io` as primary system TLD:** `.dev` has HSTS preloaded (mandatory HTTPS — no mixed-content accidents), stable pricing via Google Registry ($10 vs $50), and no geopolitical risk. The British Indian Ocean Territory sovereignty transfer to Mauritius may affect `.io` governance and pricing. `.dev` is a safer long-term bet.

**Why split `.dev`/`.org` for ORGANVM:** Organs I-IV are *making* organs (theory, art, commerce, orchestration). Organs V-VII are *speaking* organs (discourse, community, proclamation). `.dev` signals construction; `.org` signals public commons. This provides separate SSL certs, independent Cloudflare Pages projects, and the ability to delegate community subdomains without exposing technical infrastructure.

**Why Cloudflare for everything:** At-cost registration (no markup), integrated DNS/CDN/Pages/Workers/Email Routing, single dashboard, API-first. The user is already consolidating from GoDaddy. Vendor lock-in risk is low — DNS is portable, domains can transfer to any ICANN registrar.

**Why env vars for domains:** The existing ORGANVM pattern uses shell env vars (`ORG_I` through `ORG_META`) as the structural glue between organs and scripts. Domain vars follow the same pattern: deploy scripts, `seed.yaml` sync, and SOPs all reference `$DOMAIN_ORGAN_III` rather than hardcoding `ergon.organvm.dev`. If a domain changes, one edit to `chezmoi.toml` + `chezmoi apply` propagates everywhere.

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
