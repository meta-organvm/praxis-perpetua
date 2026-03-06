# Commit: Fix update-action-pins.py Parsing Bug

## Status
✅ **Implementation complete** - Ready to commit

## Summary
Fixed the `resolve_tag_to_sha()` function in `update-action-pins.py` to handle list responses from the GitHub API when querying tag prefixes that match multiple refs.

## File Modified
- `src/automation/scripts/utils/update-action-pins.py`

## Commit Message
```
fix(scripts): handle list responses in update-action-pins

GitHub API returns a list when querying tag prefixes that match
multiple refs. Add isinstance check to handle both dict and list
responses in resolve_tag_to_sha().
```

## Next Step
Commit the changes.
