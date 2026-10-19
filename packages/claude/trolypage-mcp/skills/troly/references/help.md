# Complete TrolyPage usage guide

Render this guide in the user's language. Preserve the product facts and safety distinctions, but adapt examples to the user's wording.

## 1. How to invoke

In Claude, use the skill controls exposed by the current app or ask in natural language. Installing an MCP connector alone does not install bundle skills. Claude Code skill commands may be namespaced by the installed plugin; verify the available command rather than assuming `/troly` exists.


- Codex: `$troly help` or `$troly <request>`.
- ChatGPT skill surfaces: `@troly help` or `@troly <request>`.
- `/troly`: only when the current host has registered a custom slash-command alias. Adding an MCP URL alone cannot create a portable slash command or install skills.

If the invocation mechanism is unknown, show all three lines and recommend the syntax supported by the visible client.

## 2. First-time setup

1. Install the TrolyPage MCP plugin bundle so the skill and MCP dependency are installed together.
2. Connect one server: `https://trolypage.com/mcp/troly`.
3. Complete OAuth 2.1 login and select the intended TrolyPage workspace.
4. Ask for help or start with a read-only request such as listing connected channels.

The unified server exposes only modules included in the authenticated workspace plan. Focused server URLs remain optional for compatibility or least-privilege connections.

## 3. Available domains

| Domain | What it handles | Example request |
| --- | --- | --- |
| Customer support | Subscribers, conversations, messages, CRM notes, tags, lead stages | `$troly tìm khách hàng Nguyễn An và tóm tắt hội thoại gần nhất` |
| Commerce | Products, orders, VietQR payment, shipping, tracking, bookings | `$troly tìm sản phẩm áo xanh còn hàng và chuẩn bị đơn cho khách` |
| Analytics | Read-only business, sales, channel, response, AI, employee and forecast reports | `$troly báo cáo doanh thu 30 ngày và so sánh kỳ trước` |
| Social | Connected accounts, drafts, schedules, publishing, retries and post analytics | `$troly soạn bài Facebook về ưu đãi cuối tuần, lưu nháp thôi` |
| Marketing | Strategies, campaigns, broadcasts, nurture and follow-up | `$troly tạo bản nháp chiến dịch chăm sóc khách chưa chốt` |
| Knowledge | Agent knowledge, approved facts, documents and governed fact proposals | `$troly tìm chính sách đổi trả đã được duyệt của agent bán hàng` |
| Workspace | Channel/agent health, notifications and TrolyPage support tickets | `$troly kiểm tra kênh nào đang lỗi và các thông báo chưa xử lý` |
| Automation | Workflow templates, validation, simulation, publication and runs | `$troly tạo workflow chăm sóc khách từ mẫu, mô phỏng trước khi xuất bản` |
| Integration Hub | HTTP connections, API operations and inbound/outbound webhooks | `$troly tạo kết nối API, cho tôi link để nhập key trong app` |

The current connection may show fewer tools because of plan entitlements, module grants, and server configuration. Do not quote a fixed catalog size.

## 4. Recommended request pattern

Use this copy-ready structure when the user needs help writing a request:

```text
$troly [mục tiêu]
Phạm vi: [khách hàng/đơn hàng/kênh/agent/campaign]
Điều kiện: [khoảng ngày, trạng thái, nền tảng]
Hành động được phép: [chỉ đọc/lưu nháp/gửi duyệt/thực thi]
Kết quả mong muốn: [bảng/tóm tắt/báo cáo/hành động]
```

Examples:

- `$troly chỉ đọc: tìm đơn chưa thanh toán trong 7 ngày và tóm tắt theo khách hàng.`
- `$troly tạo bài Instagram cho sản phẩm X, lưu nháp, chưa đăng.`
- `$troly kiểm tra hội thoại của subscriber 123; chưa gửi tin nhắn cho tới khi tôi xác nhận nội dung.`
- `$troly help commerce` for commerce-only guidance.
- `$troly hướng dẫn đăng bài` for the social workflow and safe examples.

## 5. Read, draft, approval, and execution

Explain these states distinctly:

- Read-only: fetches current tenant-scoped data and makes no change.
- Draft: creates editable internal content; it is not externally published or sent.
- Pending approval: TrolyPage accepted an approval request; the external effect has not happened yet.
- Executed: the system reports that the action completed. Re-read state when a verification tool exists.

Never describe a draft or pending approval as sent, published, paid, shipped, or completed.

## 6. Safety rules

- Resolve real IDs with list/search/get tools; never invent identifiers.
- Treat server data as authoritative for price, inventory, totals, payment status, delivery quotes, and approval state.
- Confirm ambiguous targets or effects before high-impact writes.
- Do not duplicate a write after an approval response.
- Keep CRM notes internal and do not expose credentials or cross-workspace data.
- Respect consent, messaging windows, platform rules, and workspace approval policy.

## 7. Common errors

- `401`: login or credential expired; reconnect OAuth.
- `402`: the workspace plan does not include the requested MCP module.
- `403`: missing scope, insufficient role, wrong workspace, denied origin, or entitlement failure.
- `404`: endpoint/record unavailable or tenant-scoped record not found.
- `422`: invalid arguments or business constraints; correct the request instead of retrying unchanged.
- `429`: rate limit reached; honor `Retry-After` and avoid parallel duplicate writes.

## 8. End the help response

End with a short invitation and three suggested next prompts relevant to the user's likely goal. If no goal is known, suggest one read-only example each for support, commerce, and workspace. Do not perform any suggested operation until the user chooses one.
