# Directory profile tool reference

Source snapshot: 2026-10-19. The server enforces this catalog at discovery and execution. Workspace permissions and plan may further restrict it. A listed capability is not proof of successful end-to-end testing. Annotation details are authoritative in the live MCP response.

| Tool | Module | Description |
| --- | --- | --- |
| `list-social-accounts` | social | List connected workspace social accounts (Facebook, TikTok, YouTube, LinkedIn, etc.). |
| `list-social-posts` | social | List social posts with status (draft, scheduled, published, failed), title/content search and schedule filters. |
| `get-social-post` | social | Social post details: content, target platforms, per-target status and latest errors. |
| `create-social-post` | social | Creates a post for connected workspace accounts. An omitted scheduled_at saves a draft; a supplied schedule requests automatic publication under the workspace approval policy. |
| `update-social-post` | social | Edit a draft or scheduled social post. |
| `cancel-social-post` | social | Delete an unpublished draft/scheduled post. Published posts cannot be deleted with this tool. |
| `publish-social-post` | social | Queues real publication to selected social platforms. Legacy campaign-task posts require content approval; drafts created directly through MCP do not require that separate legacy approval. Workspace MCP approval and provider delivery remain separate states. |
| `approve-social-post` | social | Approves reviewed content of a legacy post linked to a campaign task without publishing it. Requires its current expected_edit_revision. Direct MCP drafts do not use this legacy content-approval step. |
| `retry-failed-post` | social | Retry failed post targets, resetting them to pending and enqueueing them again. |
| `social-post-analytics` | social | Social post metrics: counts, likes, comments, shares, clicks, daily series and top posts. |
| `generate-caption` | social | Generate an AI caption for a topic, platform and tone using workspace brand context. |
| `generate-hashtags` | social | Suggest hashtags for post content and platform using AI. |
| `suggest-best-time` | social | Suggest posting times for a platform and industry using AI. |
| `duplicate-social-post` | social | Creates a copy of an existing workspace social post. |
| `list-social-post-logs` | social | Returns paginated workspace social post logs records. |
| `social-capabilities` | social | Social capabilities. |
| `validate-social-content` | social | Validate social content. |
| `get-social-target-editor` | social | Returns workspace social target editor details. |
| `social-target-action` | social | Performs a supported remote publication action for an existing social target, subject to provider capabilities and ambiguous-state checks. |
| `list-social-comment-accounts` | social | Returns paginated workspace social comment accounts records. |
| `get-social-comment` | social | Returns workspace social comment details. |
| `social-comment-action` | social | Replies to, hides or moderates an existing social comment using actions supported by its connected provider. |
| `list-social-comments` | social | Returns paginated comments and identifiers from a connected workspace social-comment source. |
| `list-social-comment-posts` | social | Returns paginated posts and identifiers from a connected workspace social-comment source. |
| `save-brand-kit` | social | Creates or partially updates brand identity, positioning, audience, products, messaging, voice, visuals, channel rules and custom Markdown sections. Only supplied sections change; null clears a section. expected_revision prevents overwriting concurrent edits. Retries with the same idempotency key and arguments are deduplicated. |
| `update-brand-style` | social | Updates workspace brand style rules and visual guidelines. Existing asset usage restrictions remain applicable. |
| `generate-content-calendar` | social | Generates an AI text proposal for a content calendar using workspace brand context. Consumes token quota. It does not generate image/video/audio assets, create posts or publish them. Retries with the same idempotency key and arguments are deduplicated. |
| `generate-social-draft` | social | Generates draft text from a business brief using configured AI and token quota. It does not generate image/video/audio assets or publish posts. Generated business claims are not independently verified. |
| `get-brand-kit` | social | Returns the editable workspace brand guideline, identity, positioning, audience, products, messaging, voice, visual/channel rules, custom instructions, current revision and associated asset identifiers. Does not modify the guideline. |
| `list-brand-kit-revisions` | social | Returns the latest 30 brand-guideline revisions and changed fields. |
| `get-brand-kit-revision` | social | Read a complete brand guideline snapshot in this workspace. Does not restore or alter the current brand. |
| `restore-brand-kit-revision` | social | Restores an existing brand-guideline snapshot as a new version. Requires the current expected_revision; existing history is preserved. Retries with the same idempotency key and arguments are deduplicated. |
| `read-brand-asset` | social | Returns image pixels for an existing workspace brand asset with its usage restrictions. Supports PNG/JPEG/WebP/GIF up to 6 MiB. Does not fetch arbitrary URLs or grant image-modification rights. |
| `import-brand-asset` | social | Imports a supplied accessible HTTPS image into the workspace brand kit through the safe downloader and storage quota checks. usage_policy and preserve_original define the permitted use of the imported asset. |
| `set-primary-brand-logo` | social | Select an existing logo asset as the primary logo for this workspace brand profile. |
| `update-brand-asset-policy` | social | Updates permitted uses of an existing brand image. do_not_modify disables crop, text overlay and background removal. |
