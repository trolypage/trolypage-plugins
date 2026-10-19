# OpenAI MCP findings audit — October 19, 2026

All 29 tool detail panels containing findings were inspected in the live OpenAI portal. They contain **31 findings**:

| Scan finding | Count |
| --- | ---: |
| Description missing, blank or unclear | 11 |
| Operations not individually exposed as model-callable tools | 10 |
| Claimed capabilities do not match behavior | 1 |
| New tool definition requires further review | 9 |

Two tools have two findings, so these category counts are not disjoint tool counts. The complete tool-to-finding mapping is in [the JSON evidence](openai-findings-audit-20261019.json).

## Correction to the earlier summary

The previous summary understated the findings by focusing on generic new-tool review notices. **22 findings concern descriptions or capability exposure**, and only nine are generic new-tool review notices. These were non-blocking for submission; that does not make them harmless or establish that the tools will be approved. The active record still shows In review, Configured, Authorized and Domain verified. Tool availability is Not published while approval/publication is outstanding.

## Priorities

1. Correct `update-agent-metadata`. The scanned description says it changes the metadata extraction schema, while its schema and controller write a subscriber field value using agent_id, subscriber_id, field_key and value. This description/behavior mismatch is supported by source inspection.
2. Review all ten operation-exposure findings. They include chat-with-ai, social-target-action, social-comment-action, list/execute/save-integration-operation, run-agent-conversation, update-agent-tool, list-agent-mcp-clients and discover-agent-mcp-tools. Inspect actual behavior before deciding whether to expose separate fixed tools, narrow the directory profile or explain a false positive. A scan finding is not proof that every named read/list tool executes an external action. In particular, save-integration-operation stores a definition; execution is a separate tool.
3. Replace vague descriptions on the eleven affected tools with exact purpose, inputs, outputs and side effects. Examples include “social capabilities” and “Manage Integration Hub save”. Keep configuration changes distinct from execution.
4. Treat the nine new-tool notices as outstanding platform review, not a runtime failure or approval.

This audit is read-only with respect to the platform submission and production MCP. No review cancellation, resubmission, rescan or runtime/source change was performed. Source/description fixes should be prepared and validated separately before any deliberate update to the active review.
