# SOP — Conversation-to-Content Pipeline

**Status:** ACTIVE
**Owner:** Human (creative direction) + AI Agent (extraction, formatting)
**Cadence:** Weekly — minimum 1 post per week
**Organ:** ORGAN-VII (Kerygma) for distribution; ORGAN-V (Logos) for archive
**Created:** 2026-03-19

## Purpose

Transform organic working conversations between the operator and AI agents into public-facing content that projects the operator's authentic voice. The system already generates hundreds of sessions — this SOP extracts the moments where insight, breakthrough, or emotional truth emerges and formats them for distribution.

The operator's voice is the missing output of the system. Code ships. Content doesn't. This pipeline fixes that.

## Guiding Principle

> "Trash and church exist in the same space."

Content is not manufactured. It is excavated from real work. The operator does not write LinkedIn posts — the operator works, and the work produces the posts.

## The JFK Redaction Strategy

Every post exists in two versions:

1. **REDACTED (Professional):** JFK-style black bars (█) over anything that creates professional liability. Distributed on LinkedIn, professional channels, ORGAN-VII surfaces. The redactions themselves create intrigue, protect employment prospects, and signal information-architecture sophistication.

2. **UNREDACTED (Personal):** Full conversation with no bars. Lives on portfolio, personal sites, ORGAN-V surfaces. The surrounding context — repos, architecture, live systems — acts as a labyrinth that defends any vulnerability the text contains. Anyone who reaches the unredacted version has already seen enough evidence to understand the person behind the words.

### What Gets Redacted

- Clinical disclosures (rehab, mental health treatment, substance)
- Specific personal circumstances that could trigger discrimination (living situation, age, family dynamics)
- Financial details that suggest instability
- Anything a risk-averse HR department would flag

### What Never Gets Redacted

- Emotional truth (the feeling, not the clinical detail)
- Technical substance (architecture, repos, system design)
- Philosophy and aesthetic statements
- Humor (lasagna stays)
- The hook line

## Phases

### Phase 1: CAPTURE (During Any Session)

Flag moments where genuine insight emerges from conversation. Markers:

- The operator's voice shifts from directive to reflective
- An architectural or creative connection is made that surprises both parties
- Emotional resonance — the operator responds with feeling, not just instruction
- A line is spoken that has standalone power ("trash and church exist in the same space")

**Do not manufacture content.** If a session has no moment, it has no post. Never force it.

### Phase 2: EXTRACT (End of Session or Next Day)

Pull the 3-5 prompt/response pairs that form the narrative arc. Identify:

- **The Hook** — the single line that stops scrolling. This becomes the opening.
- **The Turn** — where the conversation shifts register (technical → human, or human → technical)
- **The Landing** — the final exchange that grounds everything

Trim surrounding exchanges. A post needs an arc, not a transcript. Three beats is ideal:
1. Setup (the question or discovery)
2. Escalation (the emotional or intellectual peak)
3. Grounding (the return to earth — the lasagna, the kitchen, the real)

### Phase 3: BIFURCATE

Create both versions simultaneously. Start with the unredacted version, then apply bars.

Redaction rules:
- Use Unicode full block character: █ (U+2588)
- Redacted spans should approximate the length of the original text
- A redacted sentence must still be grammatically parseable around the bars
- The emotional arc must survive redaction — if removing a detail kills the feeling, find a way to keep the feeling without the detail

### Phase 4: FORMAT

Structure as conversation transcript:

```
**Me:**
[operator's prompt — cleaned for readability, not sanitized for voice]

**Claude:**
[response — trimmed for length, not for substance]
```

Platform constraints:
- **LinkedIn:** ~3,000 characters before "see more" fold. Hook MUST be in first 2 lines. Total post can run 8,000-10,000 characters for long-form. Conversation format makes long posts scannable.
- **Portfolio/blog:** No length constraint. Include session metadata (date, session type, what was being worked on).

End every LinkedIn post with a link to the unredacted version on portfolio.

### Phase 5: DISTRIBUTE

| Version | Channel | Organ |
|---------|---------|-------|
| Redacted | LinkedIn, professional networks | ORGAN-VII |
| Unredacted | Portfolio, personal site | ORGAN-V |
| Source session | Session archive (never distributed) | META |

Post timing: weekday mornings (Tue-Thu optimal for LinkedIn engagement).

### Phase 6: ARCHIVE

After posting:
- Store both versions in `content-pipeline/posts/YYYY-MM-DD-{slug}/`
  - `linkedin.md` (redacted)
  - `full.md` (unredacted)
  - `meta.yaml` (source session ID, hook line, engagement data post-publish)
- Update content log with date, topic, hook, and any engagement metrics (add weekly)
- Track patterns: which hooks performed, which topics resonated, which redaction density worked

## Integration Points

- **Session transcripts** (session architecture): Source material. `organvm session review --latest` surfaces recent sessions for mining.
- **Kerygma profiles** (ORGAN-VII): Distribution channel config.
- **Portfolio** (4444J99): Unredacted publication surface.
- **Alchemia intake**: Raw conversation material enters through capture pipeline if not already in session logs.

## Quality Gates

Before publishing any post:

1. **The Morning Test:** Read the redacted version the morning after writing it. If any sentence feels like a wound opened for an audience rather than for yourself — cut it. You don't owe LinkedIn your pain. You owe yourself the truth.
2. **The Labyrinth Test:** Does the unredacted version have enough surrounding context (repos, architecture, live systems) that a reader who follows the link can verify the substance? If the portfolio can't defend the vulnerability, don't publish the vulnerability.
3. **The Voice Test:** Read both versions aloud. Do they sound like you talking, or like content? If they sound like content, rewrite.

## Anti-Patterns

- **Content-first sessions:** Working just to produce a post. The work comes first. The content is a byproduct.
- **Over-redaction:** If more than 40% of the text is bars, the post loses coherence. Restructure instead.
- **Under-redaction:** If reading the redacted version would make an HR department hesitate, you haven't redacted enough.
- **Polishing the voice:** The operator's voice uses fragments, dashes, images, and registers that shift mid-sentence. This is not a bug. Never smooth it into "professional" writing.
- **Weekly obligation without material:** If the week had no moment, skip the week. Consistency matters less than authenticity. A forced post violates the first principle.

## Cross-References

- `SOP--essay-publishing-and-distribution.md` — for longer-form editorial content
- `SOP--autonomous-content-syndication.md` — for automated distribution pipelines
- `SOP--session-self-critique.md` — session review process that feeds content discovery
- `transcript-style-guide.md` — formatting standards for session transcripts
