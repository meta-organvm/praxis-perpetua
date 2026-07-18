# Limen Research commission: SGO-REQ-2026-PPLX-PILOT-04

## Question

Which public-facing claims in the proposed SGO Perplexity research workflow about Pro access, Research model selection, export formats, API separation, pricing, Computer credits, and automatic refill are supported, contradicted, or not established by current first-party sources?

## Request constraints

- Required capabilities: current_web_retrieval, multi_source_research, cited_synthesis, claim_verification, markdown_export
- Freshness: {"as_of":"2026-07-17T00:00:00Z"}
- Domain constraints: {"allow_domains":["perplexity.ai","docs.perplexity.ai"],"languages":["en"],"source_types":["official_documentation","official_help_center","official_pricing"]}
- Preservation tier: public_facing
- External transmission: public_only
- Verification strength: primary_source
- Variable spend ceiling: USD 0.00
- Minimum primary-source citation ratio: 80%
- Owner-required sections: claims_under_review, supported_claims, contradicted_claims, unknown_or_time_sensitive_claims, source_manifest, novel_actionable_findings

## Standing instructions

1. Prefer primary sources for material claims and use secondary sources only to interpret or triangulate.
2. Cite every material claim with a direct, resolvable source.
3. Separate sourced evidence, inference, and unknowns explicitly.
4. Name contradictions between credible sources without forcing false consensus.
5. Include negative searches and state when a requested fact could not be verified.
6. Preserve source title, URL, author or publisher, publication date, retrieval date, source type, quality tier, and locator.
7. Do not use connected private sources. Submit and retrieve only material allowed by the request's `public_only` declaration.
8. Do not schedule tasks, send messages, make purchases, connect services, or perform an external write.
9. Research mode must select its own models; do not claim or request a specific model.

## Owner-required answer headings

Include every heading below as an exact second-level Markdown heading. A heading may contain `None`,
but it may not be omitted.

- `## Claims Under Review` (normalized key: `claims_under_review`)
- `## Supported Claims` (normalized key: `supported_claims`)
- `## Contradicted Claims` (normalized key: `contradicted_claims`)
- `## Unknown Or Time Sensitive Claims` (normalized key: `unknown_or_time_sensitive_claims`)
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
