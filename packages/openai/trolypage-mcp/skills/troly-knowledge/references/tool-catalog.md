# Current source tool reference

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `search-knowledge` | knowledge | readOnlyHint=true | Tra cứu knowledge base của một AI Agent (hybrid recall + rerank + facts đã duyệt). Trả về block tri thức để agent dùng trả lời khách. |
| `list-knowledge-nodes` | knowledge | readOnlyHint=true | Danh sách node tri thức (cây knowledge base) của một AI Agent kèm trạng thái và số lần sử dụng. |
| `list-facts` | knowledge | readOnlyHint=true | Danh sách facts (thông tin có cấu trúc) của một AI Agent kèm trạng thái duyệt. Facts chưa duyệt KHÔNG được dùng để trả lời khách. |
| `search-facts` | knowledge | readOnlyHint=true | Tìm facts ĐÃ DUYỆT của một AI Agent theo thuộc tính/từ khóa — chỉ trả về thông tin an toàn để dùng. |
| `propose-fact` | knowledge | destructiveHint=true | Đề xuất một fact mới cho knowledge base của agent (attribute = value). Fact vào trạng thái chờ duyệt — chủ shop duyệt trong TrolyPage trước khi được dùng trả lời khách. |
| `search-documents` | knowledge | readOnlyHint=true | Tìm tài liệu trong knowledge base của agent theo từ khóa (nội dung node đã sẵn sàng). |
| `get-knowledge` | knowledge | readOnlyHint=true | Read full knowledge content and ingestion status for an agent-owned node. Use after text/URL imports; processing does not mean ready. |
| `create-knowledge-text` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `delete-knowledge` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `import-knowledge-url` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `list-knowledge-facts` | knowledge | readOnlyHint=true | Read facts for a specific knowledge node, including approval state, values and source evidence. Pending facts are review material and must not be used as approved customer knowledge. |
| `update-knowledge` | knowledge | destructiveHint=true | Manage agent knowledge through the ingestion/review pipeline. After imports inspect status before using it in agent setup. |
| `upload-knowledge-file` | knowledge | destructiveHint=true | Upload client-provided document bytes to an agent: TXT, JSON, CSV, Markdown, PDF, XLSX, DOCX or PPTX. Maximum 6 MiB decoded; approval queue limit 64 KiB arguments. Returns nodes and ingestion status; wait until ready. Reuse idempotency_key on retry. |
