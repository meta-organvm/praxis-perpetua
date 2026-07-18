---
schema_version: "1.0"
commission_id: INQ-2026-014
state: settled
observed_at: "2026-07-18T12:37:01Z"
aggregate_evaluation_ref: commissions/2026-07-17-perplexity-research-pilot/aggregate-evaluation.json
verdict: fail
variable_spend_usd: 0
---

# Pilot status

- **Observed:** 2026-07-18T12:37:01Z
- **State:** `settled`
- **Verdict:** `fail`
- **Profile:** `pro_research`
- **Variable spend:** USD 0

All four runs have terminal owner reports, typed `BlockedReceipt` artifacts,
and rejected research receipts. The attended browser bridge exposed no
controllable session, so zero prompts were submitted and zero raw exports were
produced. This does not assert that the Perplexity subscription,
authentication, or Research surface is unavailable.

The deterministic aggregate records 0 accepted packets, 4 durable owner
outputs, 0 provider requests, and USD 0 variable spend. The pilot therefore
settled `fail`, and `pro_research` is disabled. Search and synthesis APIs remain
dormant; Computer, connectors, scheduling, sharing, purchasing, billing, and
automatic refill remain prohibited.

The preliminary handoffs remain bound to the exact enabled execution catalog
recorded in `execution-catalog-receipt.json`. The aggregate separately binds
the terminal disabled registry. This preserves execution provenance without
rewriting the earlier handoff receipts.

This commission is terminal. A later attended attempt requires a new value
case and a new run rather than reopening these receipts.
