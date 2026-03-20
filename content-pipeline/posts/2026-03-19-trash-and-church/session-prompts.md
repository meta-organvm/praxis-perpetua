# Session Prompts — 2026-03-19 "Trash and Church"

Six work threads extracted from this session. Each prompt is self-contained — drop into a fresh chat.

---

## 1. AMP Lab — Deep Dive Audit

**Priority:** HIGH — blocks everything else AMP Lab related
**Workspace:** `~/Workspace/meta-organvm`

```
I have a media channel called AMP Lab that I co-created with a collaborator named Chris. We met at MFA for creative writing. The channel has a series called "Object Lessons" where we examine recurring objects across film history — every time milk appears, every time the telephone appears, assembled from clips across decades of cinema. We haven't published since ~2018-2019.

The channel has some videos building viewership naturally but no SEO strategy, no organic traffic optimization, and needs a full V2 relaunch.

Before I scaffold any repos or write any code, I need a deep audit:

1. Research the channel's current public-facing state — find AMP Lab / Object Lessons on YouTube, assess the catalog, titles, descriptions, tags, thumbnails, engagement signals
2. Competitive landscape analysis — who else is doing film-essay / video-essay content on YouTube? What's working in that space? (Every Frame a Painting, Nerdwriter, Thomas Flight, etc.)
3. Market gap analysis — what's the Object Lessons series doing that no one else is? What's the unique positioning?
4. SEO and discoverability audit — what would need to change for organic growth?
5. Content strategy assessment — what format, cadence, and presentation would a V2 need?
6. Produce a structured audit document

Context: This channel is being onboarded as the first production into ORGANVM, an eight-organ creative-institutional system. The system maps to a studio model — ORGAN-II (Poiesis) handles creative production, ORGAN-VII (Kerygma) handles distribution. The audit should be thorough enough to inform both the creative direction and the distribution strategy.

Write the audit to: ~/Workspace/meta-organvm/praxis-perpetua/content-pipeline/audits/2026-03-19-amp-lab-audit.md
```

---

## 2. AMP Lab — Film Scrubbing Tool — Technical Feasibility

**Priority:** MEDIUM — research phase, no code yet
**Workspace:** `~/Workspace/meta-organvm`

```
I want to build an automated film-scrubbing system for a video essay series called "Object Lessons." The series examines recurring objects across film history — milk, telephones, mirrors, etc. Currently, finding every appearance of an object across hundreds of films is manual work. I want to automate it.

Research the technical feasibility of building a system that:

1. Ingests films (video files or streams)
2. Uses computer vision / object detection to identify specific objects in frames
3. Extracts and catalogs clips where the target object appears
4. Tags clips with metadata (film title, year, timestamp, confidence score, scene context)
5. Organizes clips into searchable, assemblable collections per object

Investigate:
- What CV/ML models work best for object detection in film contexts? (YOLO, CLIP, SAM, etc.)
- How do you handle period films where objects look different across eras? (1920s telephone vs 2020s telephone)
- What's the compute cost? Can this run on a 16GB M3 MacBook or does it need cloud GPU?
- Are there existing tools or pipelines that do parts of this? (FFmpeg for extraction, etc.)
- What's the minimum viable version? (e.g., start with CLIP embeddings for similarity search rather than full object detection)
- Legal considerations for sourcing film clips for video essay / fair use contexts

Produce a technical feasibility document with:
- Architecture overview
- MVP scope vs. full scope
- Compute requirements and cost estimates
- Recommended tech stack
- Known risks and limitations

This tool would live in ORGAN-II (Poiesis) or ORGAN-III (Ergon) of the ORGANVM system depending on whether it generalizes beyond this use case.

Write to: ~/Workspace/meta-organvm/praxis-perpetua/content-pipeline/audits/2026-03-19-film-scrubbing-feasibility.md
```

---

## 3. Content Pipeline — Portfolio Infrastructure

**Priority:** HIGH — needed before LinkedIn post goes live
**Workspace:** `~/Workspace/4444J99/portfolio` (or wherever the portfolio site lives)

```
I need to create a section on my portfolio site for unredacted content from my Conversation-to-Content Pipeline.

Context: I have an SOP at ~/Workspace/meta-organvm/praxis-perpetua/standards/SOP--conversation-to-content-pipeline.md that defines a two-version content strategy:
- REDACTED versions go to LinkedIn (professional channels) with JFK-style black bars over personal details
- UNREDACTED versions live on my portfolio with the full context — repos, architecture, live systems surrounding the text as a "labyrinth" that defends the vulnerability

The first post is at ~/Workspace/meta-organvm/praxis-perpetua/content-pipeline/posts/2026-03-19-trash-and-church/full.md

I need:
1. A new section/page on my portfolio for these conversation artifacts
2. Clean presentation of the Artifex/Mercurius dialogue format
3. Each post should link back to relevant repos and system artifacts mentioned in the conversation
4. The page should make clear this is a human-AI collaboration artifact, not a chatbot screenshot
5. Design should be minimal, text-forward — the words carry the weight

My portfolio is an Astro site at 4444j99.github.io/portfolio/. Check the existing structure before adding anything.
```

---

## 4. ORGANVM — Studio Scaling Architecture Review

**Priority:** MEDIUM — strategic, not urgent
**Workspace:** `~/Workspace/meta-organvm`

```
In a recent session, I realized that ORGANVM's eight-organ architecture maps 1:1 to a multi-media production studio structure:

- ORGAN-I (Theoria) → R&D / Innovation Lab
- ORGAN-II (Poiesis) → Production / Creative
- ORGAN-III (Ergon) → Products / Commercial
- ORGAN-IV (Taxis) → Operations / Studio Management
- ORGAN-V (Logos) → Publishing / Editorial
- ORGAN-VI (Koinonia) → Community / Audience Development
- ORGAN-VII (Kerygma) → Marketing / Distribution
- META → Studio Infrastructure / Governance

The system was built for a solo operator, but the long-term vision is a Pixar/Lucasfilm/Rodriguez-scale studio. The solo-operator model is the embryonic form.

I need an architecture review that evaluates the current system against this scaling trajectory:

1. What patterns in the current architecture already scale to multi-person teams? (coordination/claims.py, agent handles, tool checkout, etc.)
2. What patterns are hardcoded for single-operator and would need to change?
3. Where are the collaboration bottlenecks? (e.g., registry-v2.json as single source of truth — does that work with multiple committers?)
4. How should seed.yaml evolve to support collaborator declarations?
5. What does the onboarding path look like for Chris (first collaborator) — what does he need access to, and what should be shielded?
6. What's the promotion state machine's path from "solo operator" to "studio with organ leads"?

Read the relevant modules:
- organvm-engine/src/organvm_engine/coordination/ (claims, tool_lock)
- organvm-engine/src/organvm_engine/governance/ (state_machine, dependency_graph)
- organvm-engine/src/organvm_engine/seed/ (discover, graph)
- organvm-engine/src/organvm_engine/organ_config.py
- The existing CLAUDE.md files for system context

Produce a document: ~/Workspace/meta-organvm/praxis-perpetua/content-pipeline/audits/2026-03-19-studio-scaling-review.md
```

---

## 5. LinkedIn Post — Final Review & Publish

**Priority:** HIGH — but apply the Morning Test first
**Workspace:** `~/Workspace/meta-organvm`

```
I have a LinkedIn post ready for final review before publishing.

The post is at: ~/Workspace/meta-organvm/praxis-perpetua/content-pipeline/posts/2026-03-19-trash-and-church/linkedin.md

It's a conversation transcript between "Artifex" (me) and "Mercurius" (Claude) about building a 105-repo creative-institutional system, the moment its architecture revealed itself as a studio, and eating lasagna while crying about it.

The post uses a JFK-redaction strategy — black bars (█) over personal details that could create professional liability, while keeping all emotional truth, technical substance, and philosophy visible. The unredacted version lives at: ~/Workspace/meta-organvm/praxis-perpetua/content-pipeline/posts/2026-03-19-trash-and-church/full.md

Please:
1. Read both versions
2. Check that the redacted version is emotionally coherent — the bars shouldn't create confusion, only intrigue
3. Check that nothing professionally liable leaked through the bars
4. Verify the Unicode bold text (𝗔𝗿𝘁𝗶𝗳𝗲𝘅 / 𝗠𝗲𝗿𝗰𝘂𝗿𝗶𝘂𝘀) renders correctly
5. Check LinkedIn character/length constraints — if it's too long for a regular post, advise on whether to use LinkedIn Article format instead
6. Suggest any final adjustments

Don't sanitize the voice. Don't polish it. If something needs to change, it's for structural or strategic reasons, not for "professionalism."
```

---

## 6. Weekly Content Cadence — System Integration

**Priority:** LOW — infrastructure for ongoing production
**Workspace:** `~/Workspace/meta-organvm`

```
I have an SOP for a weekly Conversation-to-Content Pipeline at:
~/Workspace/meta-organvm/praxis-perpetua/standards/SOP--conversation-to-content-pipeline.md

And a content staging directory at:
~/Workspace/meta-organvm/praxis-perpetua/content-pipeline/posts/

I need to integrate this pipeline into the ORGANVM system so it's not just a document but a functioning part of the weekly workflow:

1. Add a CLI command to organvm for content pipeline management:
   - `organvm content list` — list all posts with status (draft/published/archived)
   - `organvm content new <slug>` — scaffold a new post directory with meta.yaml template
   - `organvm content status` — weekly content cadence health check (has a post been produced this week?)

2. Add content pipeline awareness to the session review flow:
   - When `organvm session review --latest` runs, flag moments that could be content (emotional shifts, breakthrough insights, powerful lines)
   - This doesn't auto-extract — it just surfaces candidates for the human to decide

3. Add to the dashboard:
   - A /content/ route showing the content pipeline status, recent posts, publishing cadence

4. ORGAN-VII integration:
   - Each post's meta.yaml should declare distribution channels and track engagement
   - The kerygma pipeline should be aware of content-pipeline posts as a source

Read the SOP, the existing CLI structure (organvm-engine/src/organvm_engine/cli/), and the dashboard (system-dashboard/src/dashboard/) before implementing. Follow existing patterns.
```

---

## Summary

| # | Thread | Priority | Blocks |
|---|--------|----------|--------|
| 1 | AMP Lab Deep Dive Audit | HIGH | #2, AMP Lab repo scaffolding |
| 2 | Film Scrubbing Feasibility | MEDIUM | AMP Lab tooling |
| 3 | Portfolio Content Section | HIGH | LinkedIn post going live |
| 4 | Studio Scaling Review | MEDIUM | Nothing immediate |
| 5 | LinkedIn Post Final Review | HIGH | Posting |
| 6 | Content Pipeline Integration | LOW | Nothing immediate |

**Recommended sequence:** 3 → 5 → post it → 1 → 4 → 2 → 6
