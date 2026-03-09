# GRO — Growth & Marketing Department Templates

**Persona:** styx-growth
**Linked Skills:** `content-distribution`, `brand-guidelines`

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier, event subscriptions
- From `registry-v2.json`: revenue_model, revenue_status, promotion_status, description
- From `README.md`: product description, features, target audience
- From `docs/planning/prd.md` (P1): user personas, success metrics
- From `docs/planning/user-personas.md` (P2): primary persona
- From `.github/organ-aesthetic.yaml`: brand palette, typography, tone
- From kerygma profile (if exists): distribution channels, posting cadence

## Questions (ask once, shared across G1-G6)

1. Who is your primary customer persona? (1-2 sentences — or reference P2 if exists)
2. What is your primary acquisition channel? (organic search / social / referral / paid / partnerships)

---

## G1: Go-to-Market (GTM) Strategy

**Phase:** hardening
**Governing SOP:** `SOP--business-organism-design.md`
**Output:** `docs/marketing/gtm-strategy.md`

### Generation Instructions

1. Read product description + user personas
2. Read revenue model from registry
3. Read market gap analysis from `docs/research/` if available
4. Structure GTM around: positioning, channels, launch phases

### Template

```markdown
# Go-to-Market Strategy — {product_name}

**Revenue Model:** {from registry}
**Primary Persona:** {from Question 1 or P2}
**Primary Channel:** {from Question 2}

## 1. Positioning

**One-liner:** {product_name} is the {category} for {persona} who {pain point}.
**Differentiation:** {What makes this different from alternatives?}
**Category:** {Existing category or new category creation?}

## 2. Launch Phases

### Phase 1: Soft Launch (foundation → hardening)
- **Goal:** {N} early users for feedback
- **Channels:** {direct outreach, communities, social}
- **Success metric:** {e.g., 50 signups, 10 active users}

### Phase 2: Public Launch (hardening → graduation)
- **Goal:** Public awareness + first revenue
- **Channels:** {Product Hunt, HN, relevant subreddits, press}
- **Success metric:** {e.g., 500 signups, $500 MRR}

### Phase 3: Growth (graduation+)
- **Goal:** Sustainable acquisition
- **Channels:** {SEO, content, partnerships, paid if ROI positive}
- **Success metric:** {e.g., 20% MoM growth}

## 3. Competitive Landscape

| Competitor | Strength | Weakness | Our Edge |
|-----------|----------|----------|----------|
| {comp1} | ... | ... | ... |

## 4. Key Messages

| Audience | Message | Channel |
|----------|---------|---------|
| {persona 1} | {value prop} | {channel} |
```

---

## G2: Content Calendar

**Phase:** hardening
**Governing SOP:** `SOP--essay-publishing-and-distribution.md`
**Output:** `docs/marketing/content-calendar.md`

### Generation Instructions

1. Read GTM strategy (G1) for channels and messages
2. Read kerygma profile for distribution cadence
3. Read organ-aesthetic.yaml for tone
4. Plan 4-week content schedule across channels

### Template

```markdown
# Content Calendar — {product_name}

**Cadence:** {weekly / biweekly}
**Channels:** {blog, Twitter/X, LinkedIn, newsletter, etc.}
**Tone:** {from organ-aesthetic.yaml or product voice}

## Month: {current month}

| Week | Type | Title/Topic | Channel | Status | Owner |
|------|------|------------|---------|--------|-------|
| 1 | {blog/social/email} | {topic} | {channel} | {planned/drafted/published} | styx-growth |
| 2 | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... | ... |

## Content Pillars

1. **{Pillar 1}** — {e.g., Product updates and releases}
2. **{Pillar 2}** — {e.g., Educational content in the domain}
3. **{Pillar 3}** — {e.g., Community stories and use cases}

## Evergreen Content Ideas

- {topic that can be written anytime}
- ...
```

---

## G3: SEO Strategy & Keyword Plan

**Phase:** hardening
**Governing SOP:** T1 skill `content-distribution`
**Output:** `docs/marketing/seo-strategy.md`

### Generation Instructions

1. Read product description — extract domain keywords
2. Read GTM strategy for positioning and category
3. Identify search intent categories (informational, transactional, navigational)
4. Generate keyword clusters with content mapping

### Template

```markdown
# SEO Strategy — {product_name}

## Target Keywords

### Primary (high intent)
| Keyword | Volume Est. | Difficulty | Content |
|---------|------------|------------|---------|
| {keyword} | {est.} | {low/med/high} | {landing page / blog post} |

### Long-tail (informational)
| Keyword | Content Type |
|---------|-------------|
| {how to X with Y} | Blog post |
| {best Z for W} | Comparison page |

## Technical SEO Checklist

- [ ] Meta titles and descriptions on all pages
- [ ] Sitemap.xml generated and submitted
- [ ] robots.txt configured
- [ ] Open Graph tags for social sharing
- [ ] Page load < 3s (Core Web Vitals)
- [ ] Mobile responsive

## Content Strategy

{Map keywords to content pillars from G2.}

## Measurement

- **Tool:** {Google Search Console / Plausible / etc.}
- **KPIs:** Organic traffic, keyword rankings, click-through rate
- **Review cadence:** Monthly
```

---

## G4: PR & Launch Communications Plan

**Phase:** graduation
**Governing SOP:** `SOP--essay-publishing-and-distribution.md`
**Output:** `docs/marketing/pr-plan.md`

### Template

```markdown
# PR & Launch Plan — {product_name}

## Launch Date: {target}

## Pre-Launch (T-14 days)
- [ ] Press kit prepared (logo, screenshots, one-pager)
- [ ] Embargo outreach to {N} journalists/bloggers
- [ ] Social accounts created and populated
- [ ] Landing page live with waitlist

## Launch Day
- [ ] Product Hunt submission
- [ ] Hacker News "Show HN" post
- [ ] Social media blitz (all channels)
- [ ] Email to waitlist
- [ ] Personal outreach to {N} warm contacts

## Post-Launch (T+7 days)
- [ ] Respond to all comments/feedback
- [ ] Collect and share testimonials
- [ ] Publish retrospective blog post
- [ ] Evaluate metrics against GTM targets

## Media List

| Contact | Outlet | Relevance | Status |
|---------|--------|-----------|--------|
| ... | ... | ... | ... |
```

---

## G5: Referral Program Design

**Phase:** graduation
**Governing SOP:** `SOP--business-organism-design.md`
**Output:** `docs/marketing/referral-program.md`

### Template

```markdown
# Referral Program — {product_name}

## Mechanics

- **Incentive (referrer):** {discount / credit / feature unlock}
- **Incentive (referee):** {discount / extended trial}
- **Tracking:** {referral code / unique link}

## Implementation

1. Generate unique referral links per user
2. Track referral conversions
3. Auto-apply incentives on successful conversion
4. Dashboard for users to see referral stats

## Metrics

| Metric | Target |
|--------|--------|
| Referral rate | {X}% of users share |
| Conversion rate | {X}% of referred users convert |
| Viral coefficient | > 1.0 |
```

---

## G6: Partnership Outreach Playbook

**Phase:** graduation
**Governing SOP:** T1 skill `networking-outreach`
**Output:** `docs/marketing/partnership-outreach.md`

### Template

```markdown
# Partnership Outreach — {product_name}

## Partnership Types

| Type | Value Exchange | Target Partners |
|------|---------------|----------------|
| Integration | Mutual user access | {complementary tools} |
| Content | Co-marketing | {industry blogs, newsletters} |
| Reseller | Revenue share | {agencies, consultants} |

## Outreach Template

Subject: {product_name} + {partner_name} — {value prop}

{3-sentence pitch: who you are, what you propose, why it benefits them.}

## Pipeline

| Partner | Type | Status | Next Step | Owner |
|---------|------|--------|-----------|-------|
| ... | ... | {prospect/contacted/meeting/active} | ... | styx-growth |
```

---

*Generates 6 artifacts: G1 (GTM strategy), G2 (content calendar), G3 (SEO), G4 (PR plan), G5 (referral program), G6 (partnership outreach)*
