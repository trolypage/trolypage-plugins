# Current source tool reference

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `search-subscribers` | support | readOnlyHint=true | Tìm kiếm khách hàng (subscribers) theo tên, số điện thoại, email, trạng thái hoặc subscriber_id. Trả về danh sách kết quả phù hợp. |
| `get-subscriber` | support | readOnlyHint=true | Hồ sơ chi tiết một subscriber: thông tin, tags, ghi chú CRM, trạng thái AI, lead stage. |
| `get-conversation` | support | readOnlyHint=true | Lấy lịch sử hội thoại của một subscriber. Hiển thị tin nhắn khách hàng và phản hồi AI theo thứ tự thời gian. |
| `list-conversations` | support | readOnlyHint=true | Hội thoại gần đây: theo subscriber cụ thể hoặc toàn workspace. |
| `send-message` | support | destructiveHint=true, openWorldHint=true | Gửi tin nhắn cho một subscriber qua kênh của họ (Messenger, Zalo, Telegram...). Tuân thủ cửa sổ nhắn tin (messaging window) — bị chặn thì cần force_override. |
| `forward-message` | support | destructiveHint=true, openWorldHint=true | Chuyển tiếp một tin nhắn trong hội thoại tới người nhận khác (chỉ kênh hỗ trợ forward). |
| `close-conversation` | support | destructiveHint=true, idempotentHint=true | Đóng hội thoại của một subscriber (đánh dấu đã xử lý xong). |
| `reopen-conversation` | support | destructiveHint=true | Mở lại hội thoại đã đóng của một subscriber. |
| `archive-conversation` | support | destructiveHint=true | Lưu trữ hội thoại của một subscriber (ẩn khỏi inbox). |
| `add-subscriber-tag` | support | destructiveHint=true, idempotentHint=true | Gắn một/nhiều tag cho subscriber (kích hoạt tag rules tự động nếu có). |
| `remove-subscriber-tag` | support | destructiveHint=true | Gỡ một tag khỏi subscriber. |
| `add-customer-note` | support | destructiveHint=true | Thêm ghi chú CRM (nội bộ, chỉ nhân viên thấy) cho một subscriber. |
| `set-lead-stage` | support | destructiveHint=true, idempotentHint=true | Gán giai đoạn khách hàng tiềm năng (lead stage) cho một subscriber — dùng bảng stage đã cấu hình của workspace. |
| `send-telegram-notification` | support | openWorldHint=true, destructiveHint=true | Gửi thông báo đến nhóm Telegram của đội hỗ trợ. Dùng để báo cáo khách hàng mới, yêu cầu hỗ trợ kỹ thuật, hoặc thông báo hoàn tất flow. |
| `update-subscriber-status` | support | destructiveHint=true, idempotentHint=true | Cập nhật trạng thái (status) và bật/tắt AI cho một subscriber. Status: Active (AI đang hỗ trợ), Pause (chờ kỹ thuật), Done (hoàn tất). |
| `chat-with-ai` | support | openWorldHint=true, destructiveHint=true | Gửi tin nhắn qua AI Agent và nhận phản hồi. Chạy runtime thật, có tính phí AI, ghi hội thoại và có thể thực thi công cụ nghiệp vụ; không phải sandbox, không xác nhận giao tin trên kênh. AI sẽ sử dụng system prompt và knowledge base của agent được chỉ định. |
| `create-customer-report` | support | openWorldHint=true, destructiveHint=true | Tạo báo cáo khách hàng mới và gửi đến Telegram. Dùng khi thu thập đủ thông tin (tên, SĐT, nhu cầu) từ khách hàng. |
| `support-lookups` | support | readOnlyHint=true | Discover workspace tag and lead-stage IDs before tagging customers or changing their stage. Returns full paginated lookup records. |
