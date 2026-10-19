---
name: troly-marketing
description: Operate TrolyPage marketing strategies, campaigns, broadcasts, nurture sequences, follow-up suggestions, submission approvals, and broadcast statistics. Use for campaign planning or lifecycle messaging.
---

# TrolyPage Marketing

Use only the `trolypage` MCP server. Read [tool-catalog.md](references/tool-catalog.md) to select the tools available for this workflow.

## Workflow

1. Reuse an existing strategy or campaign when appropriate; inspect it before creating dependent records.
2. Build strategy, campaign, and draft content in that order when the request spans them.
3. Keep broadcast creation separate from `submit-broadcast`; submission enters owner review and is not proof of delivery.
4. State audience assumptions and require explicit targets rather than inventing segments.
5. Verify state or read statistics after execution.
6. If a nurture or follow-up result links to an Automation Hub workflow, use `$troly-automation` to inspect and edit its graph, check, simulate, publish, and monitor runs. Keep the legacy tools for existing records.

Never claim a bulk message was sent merely because a draft or approval request exists, and never bypass consent or workspace approval policy.
