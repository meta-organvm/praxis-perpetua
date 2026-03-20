# AMP Lab Media -- Google Drive Archive

Google Drive export of AMP Lab Media's original production materials (2017--2020), organized from the shared folder at `https://drive.google.com/drive/folders/0BziW38fp8U5DcE5jbFV6NElHS2c`.

Exported and organized 2026-03-19. 152 files total.

## What This Contains

| Category | Files | Description |
|----------|-------|-------------|
| Object Lessons (published) | 7 | Research docs, storyboard, and audio for 4 published YouTube episodes |
| Object Lessons (researched) | 14 | Research docs for 14 objects that were researched but never produced |
| Object Lessons (reference) | 3 | Academic paper, original candidate list, series opening template |
| Essays (completed) | 28 | Scripts, stills, clips, and audio for 4 completed video essays |
| Essays (abandoned) | 56 | Drafts, notes, and reference images for 19 abandoned essay topics |
| Originals | 13 | Deep Probe (talk show) and New Password (short film) materials |
| Comedy | 7 | Anthony & Mary Get High scripts, Trebawkward logo, podcast characters |
| Talk | 1 | Podcast format and ideology document |
| Reference | 7 | Copyright notes, visibility guides, contact lists, video ideas |
| Strategy | 3 | The 3 revival strategy documents (also archived as markdown in V2) |
| Sensitive | 1 | Login credentials -- NEVER READ OR COMMIT |

## Published Object Lessons (V1)

The original numbering diverged from the published episode order:

| Published Ep | Object | Their # | YouTube ID |
|-------------|--------|---------|------------|
| 1 | Cereal | #1 | Sk_xTM7TGoQ |
| 2 | Telephones | #2 | -- |
| 3 | Balloons | #4 | -- |
| 4 | Eggs | #5 | -- |

Objects #3 (Televisions) was researched but never published. The gap between #2 and #4 in the published order reflects this.

## Completed Standalone Essays (V1)

These were produced and uploaded to YouTube as standalone video essays, separate from the Object Lessons series:

1. **Rick & Morty** -- Analysis of the show's storytelling structure
2. **A Child's Eye View** -- Children's perspective in cinema (includes del Toro audio on Spirit of the Beehive)
3. **The Upside Down** -- Visual inversion in cinema (includes camera obscura history)
4. **Black & White & Color** -- Chromatic choices in cinema (references Maggie Nelson's Bluets)

## Empty Google Drive Folders

These directories existed in the Drive export but contained no files (created but never populated):

- `AMP Essay/Object Lessons/Doors/`
- `AMP Essay/Object Lessons/Hats/`
- `AMP Essay/Object Lessons/Musical Artifacts/`
- `AMP Essay/(Not Current)/UnReylatable/Video/`
- `AMP Reads/` (entire sub-channel was never populated)

## Cross-References with V2 Research

The V2 relaunch (`content-pipeline/amp-lab/`) has independent research briefs. The following original V1 research docs overlap with V2 work:

### Direct Overlaps

| V1 Object | V1 File | V2 Document | Notes |
|-----------|---------|-------------|-------|
| **Mirrors** | `object-lessons/researched/mirrors/clips-and-sources.docx` | `research--mirrors-in-cinema.md` (85 films, 43K words) | V1 is the foundation. V2 expanded massively. Compare for any missed films from the original clips list. |
| **Watches** | `object-lessons/researched/watches/watches-clips-and-sources.docx` | `object-candidates.md` Tier 1 #4: Clocks/Watches (4/5) | This IS our V2 Episode 4 candidate. The V1 research is a significant head start -- extract all clip timestamps and source films. |
| **Flowers** | `object-lessons/researched/flowers/flowers.docx` | `object-candidates.md` Tier 3 #11: Flowers (3/5) | V1 research exists. V2 rated it as backlog (score 3/5). V1 clips may raise the score. |

### V1 Research Not in V2 Candidate List

These objects were researched in V1 but did NOT make our V2 ranked list of 20 objects. They should be evaluated for inclusion:

- **Coffee** -- Strong cultural weight. Twin Peaks, Pulp Fiction, Jim Jarmusch's Coffee and Cigarettes. Was researched as V1 #9.
- **Pens** -- V1 #6. Assess cinematic depth.
- **Pencils** -- V1 #11. Related to pens but distinct (John Wick, etc.).
- **Pinball Machines** -- V1 #10. Niche but visually distinctive.
- **Televisions** -- V1 #3 and #12 (two passes). Strong candidate -- screens within screens, Poltergeist, Videodrome.
- **Chewing Gum** -- Unnumbered. Assess.
- **Cones** -- Unnumbered. Traffic cones? Ice cream cones? Assess.
- **Eyeglasses** -- Unnumbered. Distinct from V2's existing candidates.
- **Gloves** -- Unnumbered. Could be strong (noir, horror).
- **Lamps** -- Unnumbered. Lighting as object.
- **Lollipops** -- Unnumbered. Niche.
- **Matches** -- Unnumbered. Fire-starting, noir, westerns.

### Reference Document Comparison

- `object-lessons/reference/potential-object-lessons.docx` -- Their original candidate list. Compare directly with `object-candidates.md` (our ranked V2 list of 20) to identify any strong candidates we missed.

## Sensitive Files

The `SENSITIVE/` directory contains login credentials and MUST NEVER be committed to git. The `.gitignore` excludes it.

## Git Tracking

Binary files (`.docx`, `.xlsx`, `.pdf`, `.png`, `.jpg`, `.mp3`, `.mp4`, `.wav`, `.numbers`) are excluded from git via `.gitignore`. Only `manifest.yaml`, `README.md`, and `.gitignore` are tracked. The manifest serves as the authoritative index of all archive contents.

## Directory Structure

```
gdrive-archive/
  manifest.yaml
  README.md
  .gitignore
  object-lessons/
    published/         4 episodes (renumbered to match YouTube)
    researched/        17 objects (14 with docs + 3 empty from GDrive)
    reference/         Academic paper, candidate list, opening template
  essays/
    completed/         4 essays (Rick & Morty, Child's Eye View, Upside Down, B&W&Color)
    abandoned/         19 essay topics with drafts and reference images
  originals/
    deep-probe/        Talk show (scripts, characters, world-building)
    new-password/      Short film (script, character sheets)
  comedy/
    anthony-and-mary/  Sketch comedy series scripts
    trebawkward/       Logo/title card
    podcast-characters/ Character concepts
  talk/
    podcast-format/    Format and ideology doc
  reference/           Copyright, visibility, contacts, ideas
  strategy/            3 revival strategy documents
  SENSITIVE/           Login credentials -- NEVER COMMIT
```
