# Technical and data-processing dossier — review draft

## Integration facts

The package sends tool calls to TrolyPage's first-party MCP service. Production's public status endpoint reports 11 registered MCP routes, 270 tools (117 read and 153 other tools), 14 resources and 12 prompts on 2026-10-19. The catalog is filtered by workspace entitlements and credential permissions. This public report is not an authenticated end-to-end test.

Endpoint: https://trolypage.com/mcp/troly. Transport: Streamable HTTP. OAuth: authorization code with PKCE S256, public client authentication method `none`, DCR at https://trolypage.com/oauth/register, requested scope `mcp:use`. Discovery metadata was opened in the user's Edge browser and saved under evidence. Authorization and token endpoints are https://trolypage.com/oauth/authorize and https://trolypage.com/oauth/token. Directory OAuth and representative authenticated business calls subsequently succeeded; OpenAI MCP is Configured / Authorized and discovered 271 full-endpoint tools. The directory catalog contains 180 tools; historical counts above describe the initial extraction. See current submission evidence.

The MCP HTTP middleware currently requires a workspace owner/admin, including read requests. Tenant identity comes from the authenticated account context. This source review has not exercised adversarial cross-tenant calls or verified all provider permissions.

## Rate limits and failures

Observed production limits are 180 requests/workspace/minute, 90 requests/actor/minute and 60 public requests/minute. These differ from local config defaults, so use the live status endpoint at release time. Honor HTTP 429 and Retry-After. 401 requires reconnecting authentication; 402 is an unavailable plan/module; 403 covers role/scope/workspace/origin; 404 covers missing endpoints or tenant-scoped records; 422 covers argument/business-rule failures. Return actionable errors and never blindly repeat a write after an uncertain result.

Tool inputs, when serialization succeeded, are in tool-contracts.json. Three schemas need authenticated/runtime follow-up: preview-broadcast-audience, update-broadcast and create-agent-memory. Their isolated extraction failed because their schema paths require a database or authenticated context; this does not establish that the deployed tools fail. Outputs may be MCP text, structuredContent and/or errors; only schemas declared by source are recorded. Do not claim every tool has an output JSON schema.

## Processing answers for owner review

| Question | Supported draft / confirmation needed |
| --- | --- |
| Purpose | Fulfil user-requested business operations in the authorized TrolyPage workspace. |
| Data accessed | Depending on called tools: customer identifiers/contact details, conversations and internal notes; products/prices/stock; order/payment/shipment/booking details; report aggregates; social content/account metadata; knowledge, agent configuration, files/assets, workflow and integration execution metadata. Avoid fetching unrelated customer records. |
| Direction | AI host sends requested tool arguments to TrolyPage; TrolyPage sends results to the host. A requested send/publish/shipping/integration operation can share the required payload with the connected provider. |
| AI providers | Tools that generate text/media or execute an AI agent may call the workspace-configured provider and consume quota. Ordinary CRUD/report calls must not be described as requiring AI inference. Confirm actual processors for the selected review catalog and disclose them. |
| Credentials | OAuth tokens and service credentials remain in host/server secure connection settings. Never put reviewer credentials, API keys, bearer headers or client secrets in a public package. |
| Security supported by source | Credential-bound tenant context, workspace-admin middleware, plan/module gates, scoped API-key checks and write policy/operation receipts. The owner subsequently confirmed at-rest encryption, mandatory administrator MFA, monitoring and incident response; these are owner attestations, not an independent infrastructure audit. |
| Retention | Current public policy describes account data during service use plus a 7-day scheduled deletion grace, conversation history by configuration (retained during use by default), tokens until revoked/disconnected/expired, accounting records for at least 5 years and logs up to 12 months. These are published statements, not independently verified controls or newly adopted commitments. Confirm actual configuration and connector-specific records before submitting. |
| Deletion / revocation | Public instructions at https://trolypage.com/data-deletion. Disconnect/revoke should stop further access; distinguish this from erasing prior host chats, sent messages or statutory records. Local backup-retention default is 35 days, not proof of production retention. |
| Secondary use | Muse requires restrictions on unrelated ads/profiling/model training. Owner must confirm processing and processor terms match those restrictions for connector data. Do not infer approval from a generic website statement. |
| Hosting / international transfers | Public policy states Vietnam/Asia-Pacific storage and potential external AI processing. The owner subsequently confirmed BNIX/Vietnam hosting and the AI providers listed in the Muse dossier; optional Chinese-origin models and global provider processing are disclosed. No signed SCC/DPA is claimed. Do not infer a Vietnam-only residency guarantee. |
| Support / security contact | support@trolypage.com is public support. support.mcp@trolypage.com is the confirmed submission contact. A dedicated security/incident escalation contact still needs owner confirmation. |

## Completion and approvals

Workspace Auto/Hybrid/Strict controls server execution; the host's approval layer is separate. Hybrid's source allowlist permits some real writes directly, including send-message and internal notes. create-order can create an order pending shop review. The public guide's blanket "sensitive writes all queue" claim is too broad. The package must report actual returned states and respect the host's per-action approvals. An MCP execution acknowledgement does not prove an external recipient received a message, a workflow finished or a payment cleared.

## Proposed Muse tool classes

Read tools retrieve account state. Write tools change internal drafts/configuration. Sensitive-write candidates include external sends/publication, payments/order commitment, shipping/booking, destructive operations and consequential integration execution. tool-inventory.csv contains an initial classification for manual review, explicitly separate from current MCP annotations and Muse's final classification.
