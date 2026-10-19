---
name: troly-automation
description: Create and operate TrolyPage Automation Hub workflows through MCP. Use for templates, workflow drafts, validation, simulation, publication, audiences, runs, tasks, or recovery.
---

# TrolyPage Automation

Use the `trolypage` MCP server. Read [tool-catalog.md](references/tool-catalog.md) for the Automation tool sequence and requirements. For external HTTP connections or webhooks, also read the Integration Hub section of the `$troly-workspace` tool catalog.

1. Discover templates and the action catalog. Get the selected template definition and resolve real IDs through `get-automation-options`.
2. Save the workflow as a draft. Use the same `AutomationDefinitionV1` graph that the app editor uses. For edits, read the latest revision first.
3. Check the exact revision and fix reported field/node issues. Simulate with sample data; explain that it sends no messages or real HTTP requests and cannot prove every wait-event branch.
4. Publish the checked revision under the workspace approval policy. A pending MCP approval is not publication. Once published, inspect runs and individual steps to see what actually happened.
5. Before retrying, inspect the failed action and run state. Never retry an unknown external outcome. Use a fresh `idempotency_key` for a new intent and reuse the same key only for the same arguments after a transport failure.

When a connection needs credentials, return the `setup_url` and ask the user to enter or rotate the secret inside TrolyPage. Never request a secret in MCP parameters or reveal one in chat.
