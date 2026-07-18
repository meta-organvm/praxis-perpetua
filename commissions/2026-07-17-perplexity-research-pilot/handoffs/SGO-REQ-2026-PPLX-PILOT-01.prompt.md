# Limen Research commission: SGO-REQ-2026-PPLX-PILOT-01

## Question

Which user-tunable, publicly documented macOS 26 Tahoe memory-pressure, compressor, jetsam, purge, and process resource-class controls can safely reduce chronic memory pressure on a 16 GB host running multiple Electron applications, and which commonly proposed controls are unsupported?

## Request constraints

- Required capabilities: current_web_retrieval, multi_source_research, cited_synthesis, claim_verification, markdown_export
- Freshness: {"as_of":"2026-07-17T00:00:00Z"}
- Domain constraints: {"allow_domains":["developer.apple.com","support.apple.com","opensource.apple.com","news.ycombinator.com","stackoverflow.com"],"languages":["en"],"source_types":["official_documentation","source_code","high_quality_technical_analysis"]}
- Preservation tier: operational_internal
- External transmission: sanitized_only
- Verification strength: primary_source
- Variable spend ceiling: USD 0.00
- Minimum primary-source citation ratio: 80%
- Owner-required sections: answers_by_question, unsupported_or_unknown, concrete_commands, contradictions, source_manifest, novel_actionable_findings

## Standing instructions

1. Prefer primary sources for material claims and use secondary sources only to interpret or triangulate.
2. Cite every material claim with a direct, resolvable source.
3. Separate sourced evidence, inference, and unknowns explicitly.
4. Name contradictions between credible sources without forcing false consensus.
5. Include negative searches and state when a requested fact could not be verified.
6. Preserve source title, URL, author or publisher, publication date, retrieval date, source type, quality tier, and locator.
7. Do not use connected private sources. Submit and retrieve only material allowed by the request's `sanitized_only` declaration.
8. Do not schedule tasks, send messages, make purchases, connect services, or perform an external write.
9. Research mode must select its own models; do not claim or request a specific model.

## Owner-required answer headings

Include every heading below as an exact second-level Markdown heading. A heading may contain `None`,
but it may not be omitted.

- `## Answers By Question` (normalized key: `answers_by_question`)
- `## Unsupported Or Unknown` (normalized key: `unsupported_or_unknown`)
- `## Concrete Commands` (normalized key: `concrete_commands`)
- `## Contradictions` (normalized key: `contradictions`)
- `## Source Manifest` (normalized key: `source_manifest`)
- `## Novel Actionable Findings` (normalized key: `novel_actionable_findings`)

## Required normalization appendix

End with these exact second-level headings, even when content is `None`:

- `## Material Claims` — one bullet per claim:
  `[C1][material][evidence|inference][supported|partially_supported|contradicted|unsupported] ... [S1]`.
- `## Contradictions`
- `## Unknowns`
- `## Negative Searches` — one bullet per search:
  `- Query: ... | Surface: ... | Searched: YYYY-MM-DDTHH:MM:SSZ | Result count: 0 | Disposition: ...`.
- `## Novel Actionable Findings`
- `## Source Manifest` — one source per line:
  `- [S1] [Title](URL) | Publisher: ... | Published: YYYY-MM-DD or Unknown | Retrieved: YYYY-MM-DDTHH:MM:SSZ | Source Type: ... | Primary: provisional | Quality Tier: provisional | Locator: ...`.

The `Primary` and `Quality Tier` labels are provisional until Studium's Source Verifier independently
grades them. Return the completed answer as a Markdown Session export. Do not perform any
recommendation in the world.
