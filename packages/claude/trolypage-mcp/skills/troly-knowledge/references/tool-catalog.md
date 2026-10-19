# Current source tool reference

Human-readable source descriptions have been translated into English. Tool identifiers and contracts are unchanged; live server wording may differ.

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `search-knowledge` | knowledge | readOnlyHint=true | Query an AI Agent's knowledge base using hybrid recall, reranking and approved facts. Returns knowledge blocks for customer replies. |
| `list-knowledge-nodes` | knowledge | readOnlyHint=true | List an AI Agent's knowledge nodes with status and usage counts. |
| `list-facts` | knowledge | readOnlyHint=true | List an AI Agent's structured facts and approval states. Unapproved facts must not be used in customer replies. |
| `search-facts` | knowledge | readOnlyHint=true | Search approved agent facts by attribute/keyword, returning only information approved for use. |
| `propose-fact` | knowledge | destructiveHint=true | Propose an agent knowledge fact (attribute = value). It remains pending until shop-owner approval in TrolyPage, before use in customer replies. |
| `search-documents` | knowledge | readOnlyHint=true | Search ready knowledge-base document nodes by keyword. |
| `get-knowledge` | knowledge | readOnlyHint=true | Read full knowledge content and ingestion status for an agent-owned node. Use after text/URL imports; processing does not mean ready. |
| `create-knowledge-text` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `delete-knowledge` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `import-knowledge-url` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `list-knowledge-facts` | knowledge | readOnlyHint=true | Read facts for a specific knowledge node, including approval state, values and source evidence. Pending facts are review material and must not be used as approved customer knowledge. |
| `update-knowledge` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `upload-knowledge-file` | knowledge | destructiveHint=true | Upload client-provided document bytes to an agent: TXT, JSON, CSV, Markdown, PDF, XLSX, DOCX or PPTX. Maximum 6 MiB decoded; approval queue limit 64 KiB arguments. Returns nodes and ingestion status; wait until ready. Reuse idempotency_key on retry. |
