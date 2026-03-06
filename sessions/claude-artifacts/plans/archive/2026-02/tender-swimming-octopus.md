# Plan: README Audit Corrections — chthon-oneiros & krypto-velamen

## Context

Both repos were initialized, pushed to GitHub, and added to the registry in a prior session. The user then requested a full content audit: "ensure that each and every document in both directories have been ingested 100% and sync/recapitulate alignment." Every source document in both directories was read in full and compared against the deployed READMEs. The READMEs are structurally sound and capture the core identity of each project well. However, the **Document Manifest** tables contain several inaccurate or incomplete descriptions, and a few conceptual elements from the source material are missing from the body text.

---

## CHTHON-ONEIROS README Corrections

**File:** `/Users/4jp/Workspace/chthon-oneiros/README.md`

### M1. `GRINDER-New-chat.md` — Mischaracterized

**Current:** `Additional project development notes`
**Actual:** Analysis of three "Open View" screenplay drafts (2018–2019) — pre-public archival source material establishing GRINDER's multi-year provenance. Contains scene-by-scene breakdown showing the evolution of the hookup-app-horror premise.
**Fix:** Change to `Analysis of three "Open View" screenplay drafts (2018–2019): archival source material and conceptual seed archive for GRINDER`

### M2. `122325-asciiart-README.md` — Date error

**Current:** `ASCII art README draft (December 2023)`
**Actual:** Filename `122325` = 12/23/25 (December 23, 2025), not December 2023.
**Fix:** Change to `ASCII art README draft (December 2025)`

### M3. `ChatGPT-Demons in Paradise Lost.md` — Description too narrow

**Current:** `Extended research on Paradise Lost, demonology, and horror lineage`
**Actual:** 448KB conversation that starts with Paradise Lost demons but evolves into MET4MORFOSES origins, personal creative calling, and early organ system genesis. Demonology is ~10% of the file.
**Fix:** Change to `Extended conversation spanning Paradise Lost demonology, MET4MORFOSES origins, personal creative calling, and early organ system genesis (shared document)`

### M4. `ChatGPT-QUEER Growth Strategy.md` — Misleading description

**Current:** `Growth strategy for companion project (shared document)`
**Actual:** Takes QUEER's growth strategy and applies it specifically to GRINDER's public creation model. Majority of content is about GRINDER.
**Fix:** Change to `QUEER growth strategy applied to GRINDER's public creation model (shared document)`

### M5. `ChatGPT-Monetization Strategy Priorities.md` — Scope understated

**Current:** `Monetization and access-packaging strategy`
**Actual:** Full AJP Media Arts business structure covering monetization across ALL creative projects, not just GRINDER.
**Fix:** Change to `Full AJP Media Arts monetization strategy across all creative projects (shared document)`

### M6. Add body section — Archival Provenance

The README mentions GRINDER as a "hookup-app murder premise" but never mentions its provenance in three screenplay drafts dating to 2018–2019. This establishes multi-year creative development.
**Fix:** Add 3–4 sentences after "Scope Correction: From Story to Field" in a new "Archival Provenance" section noting the Open View drafts and their role as seed material.

### M7. Add body text — Creative universe context

`ChatGPT-GRINDER Project Threads Summary.md` establishes that GRINDER exists within a broader creative universe (ETCETER4, et4L, MET4MORFOSES, AMP LAB MEDIA, LOCREANCE) but these projects are **explicitly independent** — not tied together creatively, and GRINDER/QUEER have NO AI elements.
**Fix:** Add 2–3 sentences to the "Organ System Genesis Context" section noting the broader creative universe and the deliberate independence of each project.

---

## KRYPTO-VELAMEN README Corrections

**File:** `/Users/4jp/Workspace/krypto-velamen/README.md`

### M8. `QUEER-AI-prompts-for-QV33R.md` — Description incomplete

**Current:** `Deep research prompt templates for all three anchor authors + comparative report + next-author recommendations`
**Actual:** Contains TWO major sections: (1) author-specific deep research prompts as described, AND (2) 25 contextual research prompts for QV33R's real/artificial worlds — Stonewall, queer spaces, chosen families, VRChat/digital intimacy, ethics of exposure, queer time theory, etc. README only describes part 1.
**Fix:** Change to `Deep research prompt templates: three anchor authors + comparative report, plus 25 contextual world-research prompts (Stonewall, queer spaces, digital intimacy, ethics of exposure)`

### M9. `ChatGPT-Project Threads Summary.md` — Not actually shared

**Current manifest:** `Project thread summary and development notes`
**Current shared-material section:** "Eleven files are shared"
**Actual:** This file is UNIQUE to krypto-velamen. chthon-oneiros has `ChatGPT-GRINDER Project Threads Summary.md` instead (different file). Actual shared count is 10, not 11.
**Fix:** Update description to `Project thread summary across ETCETER4 creative universe (unique to this repo)`. Update shared material count from "Eleven" → "Ten."

### M10. Add body text — Phased expansion model

Source docs (`ChatGPT-QUEER Growth Strategy.md`, `ChatGPT-Queer Project Growth Strategy.md`) describe a phased media expansion: text → visual/graphic → interviews → podcast/reality TV.
**Fix:** Add 2–3 sentences to a new "Media Trajectory" subsection or append to "Why This Project Exists" noting the planned text-first → multimedia expansion.

### M11. Add body text — Creative universe context

Same as M7. QUEER exists within but is independent from the broader ETCETER4 creative universe.
**Fix:** Add 2–3 sentences noting this context and deliberate independence.

---

## Execution Order

1. Edit `chthon-oneiros/README.md` — Apply M1–M5 (5 manifest description fixes) + M6–M7 (2 body additions)
2. Edit `krypto-velamen/README.md` — Apply M8–M9 (2 manifest fixes + shared count fix) + M10–M11 (2 body additions)
3. Commit in each repo: `fix: Correct document manifest descriptions and add missing provenance context`
4. Push both repos to GitHub
5. No registry changes needed (descriptions, tiers, and counts are all still accurate)

---

## Files Modified

| File | Action |
|------|--------|
| `~/Workspace/chthon-oneiros/README.md` | EDIT — 5 manifest fixes + 2 body additions |
| `~/Workspace/krypto-velamen/README.md` | EDIT — 2 manifest fixes + shared count fix + 2 body additions |

---

## What This Plan Does NOT Do

- Does not restructure the READMEs (the overall architecture is solid)
- Does not change word counts or portfolio tone
- Does not touch source documents (they are ingested material, not authored here)
- Does not update the registry (no fields have changed)

---

## Verification

1. Grep both READMEs for old descriptions to confirm they are gone
2. Confirm word counts are still 2,000+ after edits
3. `git diff` in each repo to review changes before committing
4. Push and verify on GitHub
