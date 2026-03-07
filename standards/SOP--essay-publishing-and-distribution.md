# SOP: Essay Publishing & Distribution

## 1. Ontological Purpose

This SOP governs the pipeline from essay draft to published artifact to distributed social presence. ORGAN-V (Logos) is the public discourse organ — its purpose is to make the system's thinking visible and legible to the outside world. ORGAN-VII (Kerygma) is the distribution organ — its purpose is to syndicate that discourse across platforms using the POSSE (Publish Own Site, Syndicate Everywhere) model.

This procedure connects the two: an essay drafted from research or product development flows through ORGAN-V's publishing pipeline and out through ORGAN-VII's distribution channels. Without this SOP, essays are published but not distributed, or distributed without a canonical source.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--research-to-implementation-pipeline.md` (research outputs may become essay inputs), `SOP--product-deployment-and-revenue-activation.md` (product launches may generate announcement essays), Corpus `key-workflows.md` section 3 (informal predecessor)

---

## 2. Phase I: Draft & Edit

### Process

1. **Identify essay source.** Essays originate from one of several pipelines:
   - Research output (ORGAN-I -> ORGAN-V): theoretical synthesis
   - Product milestone (ORGAN-III -> ORGAN-V): building-in-public narrative
   - System governance insight (META -> ORGAN-V): process transparency
   - External event response: industry commentary, conference reflection

2. **Draft the essay.** Target: 3,000-5,000 words.
   - Apply the **5 Cs framework** (Cite, Compare, Contrast, Critique, Connect) per METADOC--research-standards.md
   - Structure: thesis statement, evidence/argument sections, synthesis, implications
   - Voice: first-person singular, direct, technical but accessible

3. **Self-review against quality criteria:**
   - [ ] Thesis is stated in the first 200 words
   - [ ] Every claim has supporting evidence or reasoning
   - [ ] No orphaned references (every source cited is in the bibliography)
   - [ ] No internal jargon without definition (the stranger test applies to essays too)
   - [ ] Word count within target range

4. **Store draft** in `organvm-corpvs-testamentvm/docs/essays/` for review before deployment.

### Starter Research Questions
- What is the primary audience for this essay? (Developers, researchers, investors, general public)
- What is the one-sentence thesis?
- Which organ(s) does the content draw from?
- Is there existing research or product documentation to synthesize?
- What is the publication urgency? (Timely response vs. evergreen analysis)

---

## 3. Phase II: Jekyll Deployment

### Process

1. **Format as Jekyll post.** Filename convention: `YYYY-MM-DD-slug-title.md`
   ```markdown
   ---
   layout: post
   title: "Your Essay Title"
   date: 2026-03-07
   categories: [meta-system]
   tags: [transparency, governance, organ-model]
   description: "One-sentence meta description for SEO and social cards"
   ---

   Essay content here...
   ```

2. **Deploy to public-process:**
   ```bash
   cd ~/Workspace/organvm-v-logos/public-process
   cp <draft-path> _posts/YYYY-MM-DD-slug-title.md
   git add _posts/YYYY-MM-DD-slug-title.md
   git commit -m "essay: your essay title"
   git push origin main
   ```

3. **Verify deployment:**
   - [ ] Jekyll build succeeds (GitHub Pages deploys without error)
   - [ ] Essay accessible at public URL
   - [ ] Formatting renders correctly (code blocks, links, images)
   - [ ] Categories and tags appear correctly in the index

4. **Trigger essay-monitor** (if not waiting for daily 09:00 UTC run):
   ```bash
   gh workflow run essay-monitor.yml --repo organvm-iv-taxis/orchestration-start-here
   ```

### Starter Research Questions
- Is the Jekyll frontmatter complete? (layout, title, date, categories, tags, description)
- Does the filename follow the YYYY-MM-DD-slug convention?
- Are all internal links relative and working?
- Does the essay need images or diagrams? Are they committed?

---

## 4. Phase III: POSSE Distribution

### Process

1. **Publish on canonical site first** (Phase II must be complete before distribution).

2. **Distribute across platforms** following the POSSE model:

   | Platform | Format | Timing | Notes |
   |----------|--------|--------|-------|
   | **Mastodon** | Thread (3-5 toots) | Publication day | Link to canonical in first toot |
   | **LinkedIn** | Article or long post | Publication day + 1 | Professional framing, link to canonical |
   | **Discord** | Announcement post | Publication day | In relevant server channels |
   | **GitHub Discussions** | Cross-post summary | Publication day | In corpus or relevant repo discussions |

3. **Compose distribution content:**
   - Extract the thesis and 2-3 key insights for social posts
   - Each platform gets platform-native formatting (not copy-paste)
   - Every post links back to the canonical URL on the ORGAN-V site
   - Use appropriate hashtags per platform

4. **Align with distribution cadence:**
   - Wednesday is the default distribution day (per operational-cadence.md)
   - Urgent/timely essays may break cadence with a note in the distribution log
   - Queue essays published on other days for Wednesday distribution

### Starter Research Questions
- Which platforms are active for this organ/topic?
- What is the appropriate tone for each platform?
- Is there an existing audience on each platform to engage?
- Should this essay be threaded (Mastodon) or posted as a single link?
- Are there relevant hashtags or communities to target?

---

## 5. Phase IV: Metrics & Follow-Up

### Process

1. **Track engagement:**
   - Page views (GitHub Pages analytics or external)
   - Social engagement (replies, boosts, shares)
   - Inbound links (if trackable)

2. **Respond to engagement:**
   - Reply to substantive comments within 48 hours
   - Incorporate feedback into future essays or corrections

3. **Update system metrics:**
   ```bash
   cd ~/Workspace/meta-organvm/organvm-corpvs-testamentvm
   python3 scripts/praxis-metrics-dashboard.py --output system-metrics.json
   ```

4. **Log the publication** in the essay tracker or operational cadence records.

### Starter Research Questions
- What engagement metrics matter for this essay?
- Is there a follow-up essay planned?
- Did the essay generate any actionable feedback?
- Should the essay be referenced in any product README or pitch deck?

---

## 6. Output Artifacts

- Published Jekyll post in `organvm-v-logos/public-process/_posts/`
- Social media posts across distribution platforms (Mastodon, LinkedIn, Discord)
- Updated system metrics
- Distribution log entry
- Engagement responses (if applicable)

---

## Appendix A: Frontmatter Template

```yaml
---
layout: post
title: ""
date: YYYY-MM-DD
categories: []
tags: []
description: ""
---
```

### Category Taxonomy
- `meta-system` — about the ORGANVM system itself
- `building-in-public` — transparency about the development process
- `theory` — research synthesis and theoretical analysis
- `product` — product development narratives
- `governance` — institutional and governance insights

## Appendix B: Social Posting Templates

### Mastodon Thread Template
```
1/N: [Thesis statement] — New essay on [topic].

[Key insight 1]

[Key insight 2]

Read the full essay: [canonical URL]

#organvm #[topic-tag]
```

### LinkedIn Template
```
[Hook — provocative question or surprising insight]

[2-3 paragraph summary of the argument]

[Link to canonical essay]

[3-5 relevant hashtags]
```

## Appendix C: Content Pipeline Diagram

```
ORGAN-I (research) ----+
                        |
ORGAN-III (product) ----+--> Draft --> Edit --> Deploy (ORGAN-V)
                        |                          |
META (governance) ------+                          v
                                         Distribute (ORGAN-VII)
                                                   |
                                    +--------------+
                                    |     |        |
                                 Mastodon LinkedIn Discord
```

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
