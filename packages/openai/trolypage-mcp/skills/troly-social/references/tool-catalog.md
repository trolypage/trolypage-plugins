# Current source tool reference

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `list-social-accounts` | social | readOnlyHint=true | Danh sách tài khoản MXH đã kết nối của workspace (Facebook, TikTok, YouTube, LinkedIn...). |
| `list-social-posts` | social | readOnlyHint=true | Danh sách bài đăng MXH: lọc theo trạng thái (draft, scheduled, published, failed), tìm theo tiêu đề/nội dung, lịch đăng. |
| `get-social-post` | social | readOnlyHint=true | Chi tiết một bài đăng MXH: nội dung, nền tảng đích, trạng thái từng target, log lỗi gần nhất. |
| `create-social-post` | social | destructiveHint=true, openWorldHint=true | Soạn bài đăng MXH cho tài khoản đã kết nối. Bỏ scheduled_at để lưu nháp; có scheduled_at là yêu cầu xuất bản tự động và cần duyệt ở chế độ Hybrid/Strict. Đăng ngay dùng publish-social-post. |
| `update-social-post` | social | destructiveHint=true | Sửa bài đăng MXH đang ở trạng thái nháp hoặc đã lên lịch. |
| `cancel-social-post` | social | destructiveHint=true | Xóa bài đăng MXH chưa đăng (nháp/lịch). Bài đã publish không xóa được. |
| `publish-social-post` | social | destructiveHint=true, openWorldHint=true | Đăng thật bài đăng lên các nền tảng đã chọn (chạy bất đồng bộ qua queue). Bài cũ liên kết CampaignTask cần duyệt nội dung qua approve-social-post trước; bài nháp tạo trực tiếp qua MCP không cần bước này. |
| `approve-social-post` | social | destructiveHint=true | Approve reviewed content of a legacy post linked to a campaign task, without publishing it. Read get-social-post first and pass its edit_revision as expected_edit_revision. Use only after the user approves the content in chat. Drafts created directly through MCP do not need this step. |
| `retry-failed-post` | social | destructiveHint=true | Đăng lại các target bị lỗi của một bài đăng (reset về pending rồi đưa vào queue). |
| `social-post-analytics` | social | readOnlyHint=true | Tổng hợp hiệu quả bài đăng MXH: số bài, lượt like/comment/share/click, series theo ngày, top bài. |
| `generate-caption` | social | readOnlyHint=true | AI viết caption cho bài đăng MXH theo chủ đề, nền tảng và giọng điệu (dùng brand context của workspace). |
| `generate-hashtags` | social | readOnlyHint=true | AI đề xuất hashtags cho nội dung bài đăng theo nền tảng. |
| `suggest-best-time` | social | readOnlyHint=true | AI gợi ý khung giờ đăng bài tốt nhất cho một nền tảng theo ngành nghề. |
| `duplicate-social-post` | social | destructiveHint=true | duplicate social post |
| `list-social-post-logs` | social | readOnlyHint=true | list social post logs |
| `social-capabilities` | social | readOnlyHint=true | social capabilities |
| `validate-social-content` | social | readOnlyHint=true | validate social content |
| `get-social-target-editor` | social | readOnlyHint=true | get social target editor |
| `social-target-action` | social | destructiveHint=true | Perform a remote publication action advertised by get-social-target-editor. Respect provider capabilities and ambiguous-state checks. |
| `list-social-comment-accounts` | social | readOnlyHint=true | list social comment accounts |
| `get-social-comment` | social | readOnlyHint=true | get social comment |
| `social-comment-action` | social | destructiveHint=true | Reply, hide or moderate a comment using provider-supported actions. Read comment/account capabilities before mutation. |
| `list-social-comments` | social | readOnlyHint=true | Discover paginated comment/post IDs from a source returned by list-social-comment-accounts. |
| `list-social-comment-posts` | social | readOnlyHint=true | Discover paginated comment/post IDs from a source returned by list-social-comment-accounts. |
| `save-brand-kit` | social | destructiveHint=true | Create or partially update a complete brand guideline, language, identity, voice and visual settings. guidelines supports identity, audience, products, messaging, voice, visual, channels and custom Markdown sections. Only supplied sections change; null clears a section. Read get-brand-kit first and send its revision as expected_revision to avoid overwriting newer edits. Use verified business facts and reuse idempotency_key on retry. |
| `update-brand-style` | social | destructiveHint=true | Update brand style rules used by media generation. Inspect existing brand assets and their usage restrictions first; do not invent trademark or image permissions. |
| `generate-content-calendar` | social | destructiveHint=true | Generate a content calendar proposal with AI. Consumes token quota; does not create or publish posts. Review the calendar, upload/generate media, create drafts and inspect each before scheduling. Reuse idempotency_key on retries. |
| `generate-social-image` | social | destructiveHint=true | Queue generation of an image for a social post using configured media providers. Requires an active subscription and quota. Returns task_id; poll get-media-generation-job until completed and use the resulting managed image ID. Queued is not generated. |
| `generate-social-draft` | social | destructiveHint=true | Generate draft copy from a business brief with configured AI. Consumes token quota; inspect the generated text for business accuracy before creating or publishing a post. |
| `get-brand-kit` | social | readOnlyHint=true | Read the editable brand guideline: identity, positioning, audience, products, messaging, language, voice, visuals, channel rules, custom instructions, current revision and assets. Read this before writing branded content. Use read-brand-asset to see images, and search-products/get-product for current catalog facts. This is a pure read. |
| `list-brand-kit-revisions` | social | readOnlyHint=true | Read the latest 30 brand guideline versions and changed fields. Use get-brand-kit-revision to inspect a version before restoring it. |
| `get-brand-kit-revision` | social | readOnlyHint=true | Read a complete brand guideline snapshot in this workspace. Does not restore or alter the current brand. |
| `restore-brand-kit-revision` | social | destructiveHint=true | Restore an inspected brand guideline snapshot as a new version. Read the current revision from get-brand-kit and pass expected_revision. History is preserved. Reuse idempotency_key on retry. |
| `read-brand-asset` | social | readOnlyHint=true | Return actual image pixels for an existing workspace logo, product photo or design reference, plus usage restrictions. Get the asset_id from get-brand-kit. Viewing a reference does not grant permission to modify it. Supports PNG/JPEG/WebP/GIF up to 6 MiB; never fetches arbitrary URLs. |
| `get-media-generation-job` | social | readOnlyHint=true | Read durable, workspace-scoped AI media job status and result. Use a completed image ID/URL for create-social-post; pending/processing does not mean ready. Does not use unscoped cache fallbacks. |
| `import-brand-asset` | social | destructiveHint=true | Import a supplied image URL into the brand kit through the safe downloader and storage quota checks. For local attachments, upload-asset first, then use its URL. Set usage_policy from the intended use and preserve_original for assets that must not be altered. |
| `set-primary-brand-logo` | social | destructiveHint=true | Select an existing logo asset as the primary logo for this workspace brand profile. |
| `update-brand-asset-policy` | social | destructiveHint=true | Set how a brand image may be used or modified. do_not_modify disables crop, text overlay and background removal. Preserve restrictions specified by the user. |
