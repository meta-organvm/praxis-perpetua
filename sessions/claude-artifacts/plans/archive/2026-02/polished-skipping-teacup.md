# CHTHON-ONEIROS: Complete Research Pipeline + Creative Production Tooling

## Context

Infrastructure parity with krypto-velamen is **done** (CLAUDE.md, seed.yaml agents, 3 director reports, drafts scaffold, Neon linkage). But krypto-velamen's research corpus is **959K bytes across 13 files**. Chthon-oneiros has **300K bytes across 3 files**. The gap:

| Asset | krypto-velamen | chthon-oneiros | Gap |
|-------|---------------|----------------|-----|
| Anchor author/director reports | 3 (174K) | 3 (300K) | **Parity** |
| Comparative synthesis report | 1 (98K) | 0 | **Missing** |
| World research reports | 9 (686K) | 0 | **Missing** |
| Drafts WORKSHEET | 1 | 0 | **Missing** |
| Drafts TEMPLATE | 1 | 0 | **Missing** |
| **Total research bytes** | **959K** | **300K** | **659K deficit** |

This plan completes the research pipeline and builds the creative production tooling. Not a named sprint — same rolling-todo constraint applies (no new named sprints until X1-X3 complete).

**What this unlocks:** After this, every future session can produce actual creative output (drafts/) from the first line, grounded in 1M+ bytes of domain research, with a formalized craft schema and production template.

---

## Step 1: Comparative Director Report

**File:** `research/comparative-director-report.md`
**Template:** Mirrors krypto-velamen's `comparative-report.md` (98K, "Concealment as Compositional Engine")
**Title:** "Horror as Craft System: Argento × Lynch × Kon — A Portable Schema"
**Target:** ~80-100K bytes

### Structure:
1. **Shared Schema** — Variables that appear across all 3 directors, tested for universality:
   - `$REALITY_STATUS` — How stable is the diegetic reality? (Argento: mystery-unstable, Lynch: ontologically-unstable, Kon: media-unstable)
   - `$VICTIM_AWARENESS` — Does the victim know what's happening? (Argento: protracted awareness, Lynch: dawning realization, Kon: cannot distinguish real from performed)
   - `$SENSORY_ASSAULT` — Which sense carries the primary dread? (Argento: vision/color, Lynch: sound/hum, Kon: the gaze itself)
   - `$IDENTITY_INTEGRITY` — How intact is the protagonist's self? (Argento: intact but deceived, Lynch: dissolved/doubled, Kon: consumed by performance)
   - `$AUDIENCE_POSITION` — Where does the viewer stand? (Argento: accomplice via POV, Lynch: dreamer who can't wake, Kon: watcher being watched)

2. **Director Interaction Matrix** — How do the three dials combine? Specific blend recipes:
   - High Argento + High Lynch + Low Kon = "Neon Dream" (color-saturated surrealism)
   - Low Argento + High Lynch + High Kon = "Identity Dissolve" (mundane → media → psychotic break)
   - High Argento + Low Lynch + High Kon = "Spectacle of Surveillance" (ritualized violence under mediation)
   - Equal blend = "Full PHANTASMATA" (reality porous on all axes)

3. **Mechanics Cross-Reference** — Map the ~58 techniques from all 3 reports into functional clusters:
   - Perception Distortion techniques (wrong image, dream intrusion, match cut dissolve)
   - Identity Erosion techniques (doubled character, persistent image, identity theft by performance)
   - Spatial Horror techniques (architectural labyrinth, threshold space, impossible room)
   - Temporal Horror techniques (temporal dislocation, acceleration editing, temporal stutter)
   - Sound-as-Weapon techniques (Goblin Pavlov, electrical hum, silence as presence)
   - Audience Implication techniques (killer-POV, observer contamination, media-within-media)

4. **Production Decision Tree** — For any new creative fragment, walk through:
   - What reality status? → sets primary dial
   - Which sense carries dread? → sets craft mechanism cluster
   - What does the audience believe? → sets format (video-log, screen-capture, etc.)

```
git add research/comparative-director-report.md
git commit -m "feat: add comparative director report (Argento × Lynch × Kon portable schema)"
```

---

## Step 2: PHANTASMATA World Research Reports (10 reports)

**Directory:** `research/`
**Template:** Mirrors krypto-velamen's world research format (A/B sections, 60-90K bytes each)
**Title format:** "World Research Brief NN: [Topic]"
**Operator:** PHANTASMATA World Research Operator — 20 research paths consolidated into 10 reports

### The 20 Research Paths (consolidated → 10 reports):

| Report | Paths Consolidated | Title | Target Size |
|--------|-------------------|-------|-------------|
| `world-01-found-footage-form.md` | 1 (Found Footage as Form), 2 (Mockumentary Continuum) | From Blair Witch to Unfriended: Found Media as Epistemic Horror | 60-80K |
| `world-02-digital-paranoia.md` | 3 (Creepypasta/Internet Horror), 4 (Analog Horror) | Digital Paranoia, Analog Dread: Internet-Native Horror Ecosystems | 60-80K |
| `world-03-giallo-ecosystem.md` | 5 (Giallo Beyond Argento), 6 (Italian Horror Broader) | The Giallo Ecosystem: Bava, Fulci, Martino and the Italian Horror Grammar | 60-80K |
| `world-04-dream-cinema.md` | 7 (Surrealist Cinema), 8 (Oneiric Narrative) | Dream Cinema: From Buñuel to Gondry — How Film Renders the Oneiric | 60-80K |
| `world-05-body-transgression.md` | 9 (Body Horror), 10 (New French Extremity) | Body Horror and Transgression: Cronenberg, Barker, and the Flesh as Surface | 60-80K |
| `world-06-asian-horror.md` | 11 (J-Horror Wave), 12 (Korean/Thai/Southeast Asian Horror) | Asian Horror Waves: Ringu to Parasite — Regional Horror Grammars | 60-80K |
| `world-07-horror-sound.md` | 13 (Horror Sound Design), 14 (Music as Dread) | The Auditory Mechanics of Dread: From Psycho's Strings to Hereditary's Click | 60-80K |
| `world-08-philosophy-fear.md` | 15 (Philosophy of Horror), 16 (Psychology of Fear) | Horror as Epistemology: Carroll, Burke, Radcliffe and the Paradox of Horror | 60-80K |
| `world-09-screen-life.md` | 17 (Screen Life Cinema), 18 (Social Media Horror) | Screen Life and Social Horror: Participatory Dread in Digital Interfaces | 60-80K |
| `world-10-args-immersive.md` | 19 (ARGs and Immersive Horror), 20 (Horror as Experience Design) | Marble Hornets to Sleep No More: Horror as Participatory Experience | 60-80K |

### Report Structure (per file):
- **A) Topic Definition and Scope** — What this research covers, why it matters for PHANTASMATA
- **B) Reality vs. Artifice Decomposition** — adapted from krypto-velamen's format: material history, formal analysis, and how the domain maps to PHANTASMATA's craft system
- **C) Techniques Inventory** — Numbered formal techniques extractable for creative use
- **D) PHANTASMATA Application Notes** — How this domain feeds the director dials and output formats

### Execution Strategy:
Dispatch 3 parallel agents at a time (memory constraint: 16GB RAM). 4 rounds:
- Round 1: world-01, world-02, world-03
- Round 2: world-04, world-05, world-06
- Round 3: world-07, world-08, world-09
- Round 4: world-10

```
git add research/world-*.md
git commit -m "feat: add PHANTASMATA world research reports (10 domain briefs)"
```

---

## Step 3: Drafts Creative Production Tooling

### 3a: DIAL-WORKSHEET.md

**File:** `drafts/DIAL-WORKSHEET.md`
**Template:** Mirrors krypto-velamen's `ENCODING-WORKSHEET.md` (7-variable walkthrough)
**Adaptation:** Walks through the 3 director dials and 5 aesthetic axes for a single creative piece.

Structure:
1. **How to Use** — Start with a feeling/image/situation, walk through each dial
2. **Dial 1: $ARGENTO_GEL** — Questions: What color dominates? Is violence ritualized or chaotic? Is there a mystery structure? What scores the scene?
3. **Dial 2: $LYNCH_DRIFT** — Questions: What's the mundane anchor? Where does dream logic enter? Is identity stable? What does the silence sound like?
4. **Dial 3: $KON_SPIRAL** — Questions: Is there a media frame? Does performance outlive the performer? Who is watching? Can memory be trusted?
5. **Axis Check** — Which of the 5 aesthetic axes is primary? ($GRINDHOUSE / $GIALLO / $LYNCH / $FOUND_FOOTAGE / $PSYCHO_SUBCONSCIOUS)
6. **Format Selection** — Based on answers, which output format? (video-log / screen-capture / audio-log / text-fragment / mock-post)

### 3b: TEMPLATE.md

**File:** `drafts/TEMPLATE.md`
**Template:** Mirrors krypto-velamen's fragment template (yaml front matter + sections + self-check)
**Adaptation:** Uses director dials instead of author dials, 5 aesthetic axes, format type, craft mechanisms.

Structure:
```yaml
# --- Fragment Metadata ---
date: YYYY-MM-DD
slug: ""
format: ""  # video-log | screen-capture | audio-log | text-fragment | mock-post
status: draft  # draft | revision | final

# --- Director Dials (0-100) ---
argento_gel: 0      # color saturation, ritual staging, operatic violence
lynch_drift: 0      # dream intrusion, mundane anchor, identity blur
kon_spiral: 0       # mediation collapse, performance haunt, obsession recursion

# --- Aesthetic Axis (primary) ---
primary_axis: ""    # grindhouse | giallo | lynch | found_footage | psycho_subconscious

# --- Craft Mechanisms Used ---
mechanisms:
  - # found_footage_framework
  - # unnatural_color
  - # hybrid_camera
  - # layered_sound
  - # lofi_editing
  - # social_viral_diegetic
```

Plus: Surface Description, Horror Function Notes, The Fragment, Production Self-Check (reality test, format consistency, dial consistency, dread source audit, safety test: "If it looks produced, it doesn't belong in PHANTASMATA yet").

```
git add drafts/DIAL-WORKSHEET.md drafts/TEMPLATE.md
git commit -m "feat: add creative production tooling (dial worksheet + fragment template)"
```

---

## Step 4: Update CATALOG.md + Knowledge Graph + Neon DB

After adding 12 new files (1 comparative + 10 world research + 1 worksheet/template split):
1. Update CATALOG.md: 25 → 37 files, add world research section, update statistics
2. Add 12 new document entities to Knowledge Graph
3. Insert 12 new rows into Neon `documents` table
4. Update `repositories` table totals

```
git add CATALOG.md
git commit -m "docs: update CATALOG.md with world research and production tooling"
```

---

## Step 5: Push

```
git push origin main
```

### Verification Checklist:
- [ ] comparative-director-report.md exists (~80-100K bytes)
- [ ] 10 world research reports exist (world-01 through world-10, ~60-80K each)
- [ ] DIAL-WORKSHEET.md exists in drafts/
- [ ] TEMPLATE.md exists in drafts/
- [ ] CATALOG.md updated (37 files in inventory)
- [ ] Knowledge Graph updated (+12 entities)
- [ ] Neon DB updated (37 document rows)
- [ ] Total research corpus: ~1.3M bytes (parity with krypto-velamen's ~960K)

---

## Dependency Graph

```
Step 1 (comparative report) ──────────┐
Step 2 (world research, 4 rounds) ────┤
Step 3 (drafts tooling) ──────────────┤
                                       │
Step 4 (CATALOG + KG + Neon) ◄────────┘
Step 5 (push) ◄── depends on Step 4
```

Steps 1-3 are parallelizable. Step 4 depends on all. Step 5 is the gate.

---

## What This Unlocks

After this plan completes, chthon-oneiros has:
- **1.3M+ bytes of research** grounding every creative decision
- **A portable craft schema** (comparative report) that makes the 3 dials interoperable
- **10 domain research briefs** covering the full horror/dream/found-footage landscape
- **Production tooling** (worksheet + template) that makes creative output formulaic to start, not from scratch
- **Full parity with krypto-velamen** on every dimension

The next move after THIS is writing the first actual creative fragment — the maiden output of PHANTASMATA Field II.
