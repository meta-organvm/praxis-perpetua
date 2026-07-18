# BlockedReceipt

```yaml
schema_version: "1.0"
outcome_type: BlockedReceipt
request_id:
blocked_at:
blocker_code:
attempted_profiles: []
owner_surface:
failed_predicate:
next_action:
reversible_work_completed: []
```

## Healthy alternatives attempted

Record each attempted profile in `attempted_profiles`; do not list a profile
that was skipped because a guardrail made it ineligible.

## Reversible work completed

Copy each completed item into `reversible_work_completed`.

## Sensitive-data statement

The receipt contains no credentials, private prompt body, or sensitive raw
material.
