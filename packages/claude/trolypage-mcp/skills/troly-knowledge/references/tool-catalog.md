# Directory profile tool reference

Source snapshot: 2026-10-19. The server enforces this catalog at discovery and execution. Workspace permissions and plan may further restrict it. A listed capability is not proof of successful end-to-end testing. Annotation details are authoritative in the live MCP response.

| Tool | Module | Description |
| --- | --- | --- |
| `search-knowledge` | knowledge | Query an AI Agent's knowledge base using hybrid recall, reranking and approved facts. Returns knowledge blocks for customer replies. |
| `list-knowledge-nodes` | knowledge | List an AI Agent's knowledge nodes with status and usage counts. |
| `list-facts` | knowledge | Returns structured agent knowledge facts and their approval states; pending facts are not approved customer knowledge. |
| `search-facts` | knowledge | Search approved agent facts by attribute/keyword, returning only information approved for use. |
| `propose-fact` | knowledge | Propose an agent knowledge fact (attribute = value). It remains pending until shop-owner approval in TrolyPage, before use in customer replies. |
| `search-documents` | knowledge | Search ready knowledge-base document nodes by keyword. |
| `get-knowledge` | knowledge | Returns full content and ingestion state of an agent-owned knowledge node. Processing is distinct from ready. |
| `create-knowledge-text` | knowledge | Creates a text knowledge node through the agent ingestion and review pipeline. |
| `delete-knowledge` | knowledge | Deletes an agent-owned knowledge node through the knowledge-management pipeline. |
| `import-knowledge-url` | knowledge | Imports an accessible document URL into an agent knowledge node through the ingestion and review pipeline. Completion depends on ingestion state. |
| `list-knowledge-facts` | knowledge | Returns facts for a knowledge node, including approval state, values and source evidence. Pending facts are review material, not approved customer knowledge. |
| `update-knowledge` | knowledge | Updates an agent-owned knowledge node through the ingestion and review pipeline. |
| `upload-knowledge-file` | knowledge | Uploads document bytes to an agent: TXT, JSON, CSV, Markdown, PDF, XLSX, DOCX or PPTX. Limit: 6 MiB decoded, or 64 KiB arguments when queued for approval. Returns node identifiers and ingestion state. Retries with the same idempotency key and arguments are deduplicated. |
