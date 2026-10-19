# Directory profile tool reference

Source snapshot: 2026-10-19. The server enforces this catalog at discovery and execution. Workspace permissions and plan may further restrict it. A listed capability is not proof of successful end-to-end testing. Annotation details are authoritative in the live MCP response.

| Tool | Module | Description |
| --- | --- | --- |
| `report-options` | analytics | List available Analytics reports and explain shared filters. |
| `overview-report` | analytics | Overview report: conversations, new customers, revenue and AI effectiveness for a period. |
| `sales-report` | analytics | Sales report: revenue, AI orders, average value, conversion, daily trends and top products. |
| `channel-report` | analytics | Channel health: conversations, new customers and revenue by channel (Messenger, Zalo, Telegram, etc.). |
| `activity-report` | analytics | Conversation activity: message counts and hourly/daily heatmaps. |
| `response-report` | analytics | Response quality: response times and AI/human proportions. |
| `ai-report` | analytics | AI effectiveness: conversations handled, cost and human handovers. |
| `employee-report` | analytics | Staff performance: conversations, response times and orders by employee. |
| `followup-report` | analytics | Follow-up effectiveness: sends, customer response rate and order conversions. |
| `social-report` | analytics | Social post effectiveness: reach, engagement by platform and recent posts. |
| `sources-report` | analytics | Customer sources: new customers and revenue by source (ads, groups, webchat, etc.). |
| `forecast-report` | analytics | Forecast conversations and revenue from recent trends. |
| `export-report` | analytics | Queues a report export using web-report filters and workspace actor timezone. A queued export is not yet a downloadable file. |
| `list-report-exports` | analytics | Returns paginated workspace report exports records. |
| `get-report-export` | analytics | Poll a report export by job ID. Completed exports return a signed download link requiring the current user login. File availability is checked before returning a link. |
