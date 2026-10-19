# Directory profile tool reference

Source snapshot: 2026-10-19. The server enforces this catalog at discovery and execution. Workspace permissions and plan may further restrict it. A listed capability is not proof of successful end-to-end testing. Annotation details are authoritative in the live MCP response.

| Tool | Module | Description |
| --- | --- | --- |
| `list-channels` | workspace | Overview of connected messaging channels (Messenger, Zalo OA, Zalo personal, Telegram, WhatsApp, Email, WebChat, etc.), with counts and states. |
| `channel-status` | workspace | Detailed connection state for one channel type, including active/error status. |
| `list-agents` | agents | List workspace AI Agents: ID, name, provider/model and status. |
| `agent-status` | workspace | Detailed AI Agent status: model configuration, tool count, knowledge-node count and active state. |
| `list-notifications` | workspace | List internal workspace notifications, unread first and newest first. |
| `ack-notification` | workspace | Mark an internal notification as read. |
| `resolve-notification` | workspace | Acknowledge an internal notification that requires action. |
| `list-support-tickets` | workspace | List support tickets the workspace sent to TrolyPage. |
| `create-support-ticket` | workspace | Create a support ticket for the TrolyPage support team. |
| `reply-support-ticket` | workspace | Reply to an open support ticket. |
| `get-support-ticket` | workspace | Read a workspace support ticket and customer-visible replies/attachments. Internal support notes are excluded. Does not mark it read. |
| `list-mcp-actions` | workspace | Returns approval, execution and failure records for MCP actions in permitted workspace modules. Tool completion is distinct from delivery to an external service. |
| `import-asset` | assets | Imports an accessible HTTPS image/video into workspace media storage and returns its managed asset identifier and URL. Private client attachments and local filesystem paths are not accessible to this tool. |
| `search-assets` | assets | Returns paginated managed media matching a search or asset identifier, with URL, file type, size and dimensions. |
| `detect-asset-c2pa` | assets | Reads a managed workspace image and reports embedded C2PA marker matches without modifying it. This heuristic is not signature validation, watermark verification or proof of AI/human origin. |
| `asset-upload-part-urls` | assets | Returns signed upload URLs for up to 10 part numbers under the current upload lease. Actual bytes are transferred by the client; URL creation alone does not upload bytes. |
| `asset-upload-policies` | assets | Check upload availability, limits and allowed MIME types. Client attachments are not automatically accessible to the server. |
| `cancel-asset-upload` | assets | Cancels a resumable upload session and releases its reservation. Cancelled upload URLs are no longer valid. |
| `complete-asset-upload` | assets | Requests completion of a byte transfer using its upload lease. Verification can continue asynchronously; a completion request alone does not establish that the file is ready. |
| `get-asset-upload` | assets | Poll upload session state and retrieve its managed media result, error_code and retryability. A session ID is not a media ID. |
| `lease-asset-upload` | assets | Acquires or renews an upload lease using a client-generated UUID. The same lease token identifies subsequent part and completion requests. |
| `prepare-asset-upload` | assets | Creates a resumable upload session with idempotent retry handling. Byte transfer, lease acquisition, completion and asynchronous verification are separate lifecycle steps. |
| `upload-asset` | assets | Uploads base64-encoded image/video bytes into managed workspace storage. Limit: 6 MiB decoded, or 64 KiB arguments when queued for approval. Local filesystem paths are not read. Retries with the same idempotency key and arguments are deduplicated. |
