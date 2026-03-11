# SOP: Autonomous Content Syndication (The Broadcast Protocol)

## 1. Ontological Purpose
This SOP formalizes the pipeline by which an essay from Logos (ORGAN-V) is automatically parsed, chunked, and dispatched via RSS to Ghost, Mastodon, Discord, and Bluesky. It ensures that the theoretical outputs of the system achieve maximal distribution with minimal manual intervention.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** ORGAN-VII (Kerygma) and ORGAN-V (Logos).

---

## 2. Phase I: Parsing & Markdown Chunking
**Goal:** Translate long-form essays into platform-native chunks.
1. **Ingestion:** Polling the `public-process` RSS feed for new entries.
2. **Chunking:** Break down the essay into a thread based on H2 headers.
3. **Template Mapping:** Pass the parsed chunks into the `announcement-templates` registry to apply platform-specific formatting (e.g., `#Tags` for Mastodon, short links for Bluesky).

## 3. Phase II: Dispatch & Rate Limiting
**Goal:** Syndication without triggering API bans.
1. **Queueing:** Push the formatted templates into the Taxis dispatch ledger.
2. **Rate Limiting:** Enforce backoff protocols specific to each platform's API limits (e.g., Bluesky XRPC vs. Mastodon ActivityPub).
3. **Execution:** Trigger the `distribution.dispatched` webhook.

## 4. Phase III: Delivery Auditing
**Goal:** Cryptographic proof of distribution.
1. **Verification:** Confirm the successful HTTP 200 return from all APIs.
2. **Logging:** Append the live URL links into the `provenance-registry.json` to prove the distribution of the original artifact.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
