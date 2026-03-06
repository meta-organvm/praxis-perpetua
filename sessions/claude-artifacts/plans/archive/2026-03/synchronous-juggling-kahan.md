# Essay Backfill Plan: 4 Essays (Feb 21 - Mar 2)

## Context

The last essay was published Feb 18. It's now Mar 3 — a 13-day gap. The user wants 1 essay every 3 days backfilled, which means 4 new essays: **Feb 21, Feb 24, Feb 27, Mar 2**.

The existing corpus (42 essays) is heavily skewed toward `meta-system` (21/42). ORGAN-VI and ORGAN-VII have zero essay coverage. The 4 backfill essays diversify both category and organ coverage.

## Approach

Write the essays directly (not via `essay_drafter` CLI, which would need API keys and topic-suggestions). Claude writes each essay matching the existing voice, schema, and style. Then validate, regenerate index data, commit, and push.

## The 4 Essays

### 1. Feb 21 — `2026-02-21-the-distribution-problem.md`
- **Category:** `guide` | **Relevance:** HIGH
- **Title:** "The Distribution Problem: Why Building in Public Means Nothing Without a Megaphone"
- **Tags:** `organ-vii, distribution-strategy, building-in-public, posse, social-automation, guide`
- **Related repos:** `organvm-vii-kerygma/kerygma-pipeline`, `organvm-vii-kerygma/social-automation`, `organvm-vii-kerygma/distribution-strategy`, `organvm-vii-kerygma/announcement-templates`
- **Outline:** POSSE model explained, ORGAN-VII architecture walkthrough, worked example of essay distribution, common pitfalls (building distribution infra vs. actually distributing)
- **~2200 words**

### 2. Feb 24 — `2026-02-24-community-infrastructure-for-one.md`
- **Category:** `case-study` | **Relevance:** HIGH
- **Title:** "Community Infrastructure for One: Building ORGAN-VI Before the Community Arrives"
- **Tags:** `organ-vi, community, infrastructure, salon-archive, reading-group, case-study`
- **Related repos:** `organvm-vi-koinonia/community-hub`, `organvm-vi-koinonia/reading-group-curriculum`, `organvm-vi-koinonia/salon-archive`, `organvm-vi-koinonia/adaptive-personal-syllabus`
- **Outline:** Candid case study of 5 production repos with zero users. Architecture walkthrough, honest metrics (0 participants), tension between preparedness vs. premature infra
- **~2400 words**

### 3. Feb 27 — `2026-02-27-writing-as-system-architecture.md`
- **Category:** `methodology` | **Relevance:** HIGH
- **Title:** "Writing as System Architecture: How ORGAN-V Became the System's Memory"
- **Tags:** `organ-v, writing, documentation, methodology, essay-pipeline, editorial-standards`
- **Related repos:** `organvm-v-logos/public-process`, `organvm-v-logos/essay-pipeline`, `organvm-v-logos/editorial-standards`
- **Outline:** Read-many-write-one pattern, essay-pipeline architecture, schema validation as editorial governance, comparison to ADRs/wikis/READMEs
- **~2500 words**

### 4. Mar 2 — `2026-03-02-two-weeks-and-forty-six-essays.md`
- **Category:** `retrospective` | **Relevance:** HIGH
- **Title:** "Two Weeks and Forty-Six Essays: The ORGAN-V Production Retrospective"
- **Tags:** `retrospective, organ-v, writing, production, metrics, self-assessment, honesty`
- **Related repos:** `organvm-v-logos/public-process`, `organvm-v-logos/essay-pipeline`, `organvm-v-logos/editorial-standards`, `meta-organvm/organvm-corpvs-testamentvm`
- **Outline:** Timeline and numbers, what schema enforcement got right, category imbalance (21/46 meta-system), velocity vs. depth tradeoff, proposed operational changes
- **~2300 words**

## Implementation Steps

1. Write all 4 essays as `.md` files in `public-process/_posts/`
2. Validate: `python -m src.validator --posts-dir ../public-process/_posts/ --schema ../editorial-standards/schemas/frontmatter-schema.yaml`
3. Regenerate indexes: `python -m src.indexer --posts-dir ../public-process/_posts/ --output-dir ../public-process/data/`
4. Commit all 4 essays + updated data artifacts in `public-process`
5. Push to remote

## Verification

- Validator passes with 0 errors on all 46 essays
- Indexer regenerates without errors
- `essays-index.json` shows 46 entries
- Each essay has correct frontmatter (word_count matches body, reading_time computed, tags lowercase-hyphenated)

## Key Files

- Posts: `/Users/4jp/Workspace/organvm-v-logos/public-process/_posts/`
- Schema: `/Users/4jp/Workspace/organvm-v-logos/editorial-standards/schemas/frontmatter-schema.yaml`
- Validator: `/Users/4jp/Workspace/organvm-v-logos/essay-pipeline/src/validator.py`
- Indexer: `/Users/4jp/Workspace/organvm-v-logos/essay-pipeline/src/indexer.py`
- Style ref: `/Users/4jp/Workspace/organvm-v-logos/public-process/_posts/2026-02-18-the-solo-auteur-method.md`
