# Current source tool reference

Human-readable source descriptions have been translated into English. Tool identifiers and contracts are unchanged; live server wording may differ.

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `report-options` | analytics | readOnlyHint=true | List available Analytics reports and explain shared filters. |
| `overview-report` | analytics | readOnlyHint=true | Overview report: conversations, new customers, revenue and AI effectiveness for a period. |
| `sales-report` | analytics | readOnlyHint=true | Sales report: revenue, AI orders, average value, conversion, daily trends and top products. |
| `channel-report` | analytics | readOnlyHint=true | Channel health: conversations, new customers and revenue by channel (Messenger, Zalo, Telegram, etc.). |
| `activity-report` | analytics | readOnlyHint=true | Conversation activity: message counts and hourly/daily heatmaps. |
| `response-report` | analytics | readOnlyHint=true | Response quality: response times and AI/human proportions. |
| `ai-report` | analytics | readOnlyHint=true | AI effectiveness: conversations handled, cost and human handovers. |
| `employee-report` | analytics | readOnlyHint=true | Staff performance: conversations, response times and orders by employee. |
| `followup-report` | analytics | readOnlyHint=true | Follow-up effectiveness: sends, customer response rate and order conversions. |
| `social-report` | analytics | readOnlyHint=true | Social post effectiveness: reach, engagement by platform and recent posts. |
| `sources-report` | analytics | readOnlyHint=true | Customer sources: new customers and revenue by source (ads, groups, webchat, etc.). |
| `forecast-report` | analytics | readOnlyHint=true | Forecast conversations and revenue from recent trends. |
| `export-report` | analytics | destructiveHint=true | Queue a report export with web report filters and workspace actor timezone. Poll export status; queued is not a downloadable file. |
| `list-report-exports` | analytics | readOnlyHint=true | list report exports |
| `get-report-export` | analytics | readOnlyHint=true | Poll a report export by job ID. Completed exports return a signed download link requiring the current user login. File availability is checked before returning a link. |
