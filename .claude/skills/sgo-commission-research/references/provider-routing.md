# Provider-profile routing

Read `governance/research-backend-profiles.yaml` on every invocation. Profile
state and provider catalogs can change after this document is written.

## Selection

1. Reject profiles whose state is not executable for the request.
2. Require every requested capability.
3. Apply P/O/C/E preservation, external-transmission, execution-timeout, and
   variable-spend ceilings.
4. Run every profile health requirement.
5. Rank healthy profiles by verification strength, privacy fit, cost, then
   latency.
6. Use `provider_auto` when live metadata cannot safely distinguish reachable
   providers.
7. Return `ManualHandoff` or `BlockedReceipt` when no executable profile
   remains. Never silently substitute.

Use the registry's declared `outcome_type`, `verification_strength`,
`preservation_tiers`, `external_transmission`, and `variable_cost_usd`; do not
reconstruct them from profile names. A `null` cost requires a live projection
and never means free.
Resolve `provider_auto`'s `selected_adapter` sentinel to the selected concrete
profile's typed outcome before emission.

Evaluate `health.machine` directly. Treat `health.attended.checks_deferred` as
unproven until the operator completes the `ManualHandoff`; never turn profile
state into a claim of live authentication or provider reachability.

Perplexity profiles accept only `public_facing` or `operational_internal`
preservation with `public_only` or `sanitized_only` transmission. They never
use private connected sources.

## Initial profiles

- `pro_research`: enabled, on-demand, attended, existing subscription only;
  its profile owns launch metadata and a 3,600-second execution timeout.
- `pro_computer`: disabled until live Computer-credit verification and a new
  value case.
- `api_search`: dormant until API credential, credit, and spend gates pass.
- `api_synthesis`: dormant under the same gates; selection is live or provider
  Auto, never a fixed model.
- `provider_auto`: available as a provider-neutral discovery path.

## Observed-current provider notes

These observations were checked on 2026-07-17 and are not timeless contract
terms:

- Perplexity Research mode automatically selects the models used for a report;
  Pro subscribers receive extended Research access.
- A Session answer can be exported as PDF, Markdown, or DOCX; this workflow
  requires Markdown.
- The Search API returns raw structured results. Cited generated prose is a
  separate Agent API behavior.
- Current Search API pricing is pay-as-you-go and listed as USD 5 per 1,000
  requests. Always re-read pricing before API activation.
- Ask and standard searches do not consume Computer credits; Computer does.
  Credit auto-refill is off by default but must still be verified off before
  any Computer pilot.

Sources:

- https://www.perplexity.ai/help-center/en/articles/10738684-what-is-research-mode
- https://www.perplexity.ai/help-center/en/articles/10354769-what-is-a-thread
- https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity
- https://docs.perplexity.ai/docs/search/quickstart
- https://docs.perplexity.ai/docs/agent-api/quickstart
- https://docs.perplexity.ai/docs/getting-started/pricing
