# SOP: Network Testament Protocol (The Mirror Protocol)

**Status:** ACTIVE
**Owner:** Human (engagement direction) + AI Agent (scanning, mapping, synthesis)
**Cadence:** Weekly scan, monthly synthesis, per-session awareness
**Organs:** All (input surface) → ORGAN-VII (distribution) + ORGAN-VI (community)
**Created:** 2026-03-20

## 1. Ontological Purpose

This SOP governs the ongoing practice of mapping ORGANVM's work to the open-source
world and building genuine professional relationships through that mapping. It
formalizes the principle:

    context[current-work] > relevant[open-source] > expand[network]

The system does not network. It works, and the work produces the network — the same
way conversation produces content (SOP--conversation-to-content-pipeline) and essays
produce distribution (SOP--autonomous-content-syndication).

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** All repositories in the ORGANVM ecosystem.

## 2. Governing Principle

> Everything is a mirror. Every repo reflects something external. Every external
> project reflects something internal. The network is not built — it is revealed
> by tracing these reflections.

We are not one thing. We do not take the shape of one thing. A technical dependency
is as meaningful as a philosophical kinship. A pull request upstream is as valuable
as joining a conversation about values. The three lenses are equal because the
person behind the work is not reducible to a category.

## 3. Cadence

### Weekly
- Run `organvm network scan` on active repos
- Review suggestions: accept, reject, or defer mirrors
- Log any engagement actions taken during the week
- Time: ~30 minutes, ideally Friday (week-in-review)

### Monthly
- Run `organvm network synthesize --period monthly --write`
- Review the testament narrative in `praxis-perpetua/testament/`
- Identify patterns: deepening vs. broadening, which lenses most active
- Adjust priorities for next month (not obligations — directions)
- Time: ~1 hour, first week of month

### Per-Session
- When working in any repo, its network-map.yaml is visible in the generated CLAUDE.md
- If work produces something relevant to a mirrored project, act:
  - File an issue, leave a comment, submit a PR, share in a discussion
- Log the action: `organvm network log <repo> <project> --action <type> --detail "..."`

## 4. The Three Lenses

### 4.1 Technical Mirror
Dependencies, tools, frameworks in the actual stack. These are the projects whose
code runs inside ORGANVM.

**Discovery:** Automated via `organvm network scan` — parses pyproject.toml,
package.json, import statements, go.mod, Cargo.toml. Maps each dependency to its
source repository.

**Action types:** Bug reports, documentation improvements, upstream PRs, issue
triage, feature requests grounded in real usage.

**Signal of depth:** When you can describe exactly how you use the tool and what
edge cases you've hit — that's a genuine contribution, not a drive-by.

### 4.2 Domain Mirror
Projects solving similar problems in different ways. These are the projects whose
*shape* resembles ORGANVM's shape.

**Discovery:** Semi-automated via ecosystem taxonomy, registry tags, and seed.yaml
domain fields. Cross-referenced against curated lists of projects in each problem
space (multi-repo governance, MCP servers, generative art frameworks, AI
orchestration, session analysis, etc.).

**Action types:** Comparative discussions, shared pattern documentation,
architectural dialogue, RFC responses, collaborative standards.

**Signal of depth:** When you can articulate what your approach shares with theirs
and where it diverges — that's genuine dialogue, not feature comparison.

### 4.3 Kinship Mirror
Communities and projects aligned in values, not necessarily technology. These are
the projects whose *why* resonates with ORGANVM's *why*.

**Discovery:** Human-driven, AI-suggested. Cannot be fully automated because
philosophical alignment requires judgment. The system suggests based on tags,
descriptions, and community patterns. The human confirms.

**Communities include:** IndieWeb/POSSE advocates, tools-for-thought networks,
solo-operator infrastructure, artist-technologist collectives (SFPC, Gray Area,
Eyebeam), creative coding communities, digital humanities networks, modular
synthesis communities (Lines/llllllll), open-source sustainability networks,
philosophy of technology groups.

**Action types:** Joining spaces, participating in discussions, cross-pollinating
ideas, inviting engagement with ORGANVM's public surfaces, attending events,
writing about shared values.

**Signal of depth:** When someone in the community recognizes you as a contributor,
not a lurker — that's genuine presence, not surveillance.

## 5. The Four Engagement Forms

All forms are simultaneous, not sequential. The form follows the nature of the
connection. A kinship mirror might start with invitation. A technical mirror might
start with contribution. There is no ladder.

### Presence
Be in the room. Star repos. Watch discussions. Join Discords and Slacks. Follow
maintainers. Subscribe to newsletters and RSS feeds.

**Purpose:** Awareness. You cannot engage with what you don't see.

### Contribution
Add value. File issues. Submit PRs. Improve documentation. Report bugs. Review
code. Answer questions.

**Purpose:** Reciprocity. The external project benefits from your engagement.

### Dialogue
Be in conversation. Comment on discussions. Respond to RFCs. Write about how you
use a tool. Cross-reference your work in relevant threads. Share architectural
decisions.

**Purpose:** Recognition. You become known through the substance of your input.

### Invitation
Open your work to the communities you've engaged. Make repos public. Write about
your architecture. Present at meetups. Create shared tooling. Host discussions.

**Purpose:** Destination. Your work becomes a place others want to visit.

## 6. The Testament Layers

### 6.1 Ledger (Raw Evidence)
Append-only JSONL at `~/.organvm/network/ledger.jsonl`.

Every engagement action logged with:
- Timestamp (ISO 8601)
- ORGANVM repo (which project this relates to)
- External project (the mirror target)
- Lens (technical | parallel | kinship)
- Action type (presence | contribution | dialogue | invitation)
- Detail (human-readable description of what was done)
- URL (link to the action — PR, issue, post, profile)
- Outcome (response received, merged, acknowledged, none yet)
- Tags (freeform, for pattern discovery)

**Never purge.** The ledger is the raw material of the testament.

### 6.2 Map (Living Graph)
`network-map.yaml` per repo, validated against `network-map.schema.json`.

Updated by:
- Automated scan (`organvm network scan`)
- Human curation (add kinship mirrors, confirm suggestions)
- Engagement feedback (actions deepen known connections, reveal new ones)

Queryable: "Which ORGANVM repos mirror this external project?" reveals convergence
points — high-value targets where multiple organs connect to the same community.

### 6.3 Narrative (Periodic Synthesis)
Dated testament entries in `praxis-perpetua/testament/`:
- `YYYY-MM-DD-network-synthesis.md` — monthly narrative
- `maps/YYYY-MM-DD-full-network-graph.json` — point-in-time snapshot
- `milestones/YYYY-MM-DD-description.md` — significant moments

The narrative synthesizes:
- What connections were made this period
- Which lenses were most active
- Which organs had the most external engagement
- What patterns are emerging (clustering, deepening, broadening)
- What surprised — the unexpected mirror that revealed something

## 7. Quality Gates

Before any engagement action:

1. **The Mirror Test:** Is this engagement genuine? Would you do it if no one
   tracked it? If it feels performative, don't.

2. **The Relevance Test:** Does your current work actually connect to this project,
   or are you forcing a connection for the ledger?

3. **The Reciprocity Test:** Are you adding value to the external project, or only
   extracting visibility? A star without engagement is a bookmark, not a mirror.

4. **The Voice Test:** Does your contribution sound like you — the person who builds
   ORGANVM, not a networking persona? If the register shifts, rewrite.

## 8. Anti-Patterns

- **Spray-and-pray:** Mass-starring repos without engagement. Presence without
  attention is noise.

- **Trophy hunting:** Targeting high-profile projects for clout rather than genuine
  alignment. Contributor graphs are not scorecards.

- **Content-first networking:** Creating engagement to produce content about it.
  The engagement comes first. If it produces content, that's a byproduct.

- **Neglecting kinship:** Over-indexing on technical mirrors because they're
  automatable. The philosophical connections produce the deepest relationships
  and the most surprising cross-pollination.

- **Ledger anxiety:** Logging for the sake of logging. If a week produces no
  genuine engagement, the ledger stays quiet. Silence is not failure — forced
  entries are.

- **Monoculture engagement:** Only engaging in one form (e.g., only PRs, only
  lurking). The four forms exist because different connections need different
  expressions.

## 9. Integration Points

### Feeds into:
- **SOP--conversation-to-content-pipeline** — engagement stories become content
- **ecosystem.yaml** community arm — discovered communities are registered
- **Kerygma profiles** — distribution targets emerge from network mapping
- **Omega scorecard** — network criterion candidate (#18)
- **Living Data Organism** — network_density, engagement_velocity metrics

### Consumes from:
- **registry-v2.json** — repo metadata, organ membership, status
- **seed.yaml graph** — domain edges, produces/consumes relationships
- **ecosystem taxonomy** — product categories for domain mirror matching
- **Session transcripts** — engagement actions during work sessions

## 10. Cross-References

- `SOP--conversation-to-content-pipeline.md` — content extraction from work
- `SOP--autonomous-content-syndication.md` — distribution automation
- `SOP--open-source-licensing-and-ip.md` — license governance per organ
- `SOP--community-event-facilitation.md` — community hosting and events
- `SOP--essay-publishing-and-distribution.md` — long-form editorial
- `SOP--cross-channel-publishing-metrics.md` — engagement measurement

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
