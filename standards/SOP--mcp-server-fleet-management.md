# SOP: MCP Server Fleet Management (The Server Protocol)

## 1. Ontological Purpose
This SOP governs the lifecycle, scaling, and health-checking of the `mcp-servers/` directory and `organvm-mcp-server`. It ensures that the AI agents in Taxis have reliable, uninterrupted access to their requisite tools.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** ORGAN-IV (Taxis) and META infrastructure.

---

## 2. Phase I: Uptime Monitoring
**Goal:** Ensure 99.9% availability of context tools.
1. **Health Checks:** Implement a cron job that pings the `health` endpoint of all running MCP servers every 60 seconds.
2. **Auto-Restart:** If a server fails to respond, autonomously restart the specific Node.js or Python subprocess without disrupting the entire fleet.

## 3. Phase II: Tool Registration Audits
**Goal:** Prevent tool bloat and overlapping schemas.
1. **Schema Validation:** Before an MCP server is deployed, validate its `listTools` output against a central schema registry.
2. **Collision Detection:** Ensure no two servers register a tool with the same name but different argument schemas.

## 4. Phase III: Memory State Persistence
**Goal:** Prevent amnesia in stateful servers.
1. **Volume Mounting:** Ensure the Memory and Filesystem MCP servers are writing to persistent, backed-up volumes governed by `SOP--data-migration-and-backup.md`.
2. **State Recovery:** On reboot, the server must successfully load the previous state before accepting new requests.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
