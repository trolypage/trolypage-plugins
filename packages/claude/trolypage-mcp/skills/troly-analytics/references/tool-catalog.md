# Current source tool reference

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `report-options` | analytics | readOnlyHint=true | Danh sách các báo cáo khả dụng trên server Analytics và cách dùng bộ lọc chung. |
| `overview-report` | analytics | readOnlyHint=true | Báo cáo tổng quan: hội thoại, khách mới, doanh thu, hiệu quả AI trong một kỳ. |
| `sales-report` | analytics | readOnlyHint=true | Báo cáo doanh thu: tổng, đơn AI, giá trị trung bình, tỷ lệ chuyển đổi, trend theo ngày, top sản phẩm. |
| `channel-report` | analytics | readOnlyHint=true | Sức khỏe từng kênh: hội thoại, khách mới, doanh thu theo kênh (Messenger, Zalo, Telegram...). |
| `activity-report` | analytics | readOnlyHint=true | Hoạt động hội thoại: số tin nhắn, heatmap theo giờ/ngày. |
| `response-report` | analytics | readOnlyHint=true | Chất lượng phản hồi: thời gian phản hồi, tỷ lệ AI/human. |
| `ai-report` | analytics | readOnlyHint=true | Hiệu quả AI: số hội thoại AI xử lý, chi phí, chuyển giao human. |
| `employee-report` | analytics | readOnlyHint=true | Hiệu suất nhân viên: số hội thoại, thời gian phản hồi, đơn hàng theo nhân viên. |
| `followup-report` | analytics | readOnlyHint=true | Hiệu quả follow-up: số follow-up gửi, tỷ lệ khách phản hồi, chuyển đổi thành đơn. |
| `social-report` | analytics | readOnlyHint=true | Hiệu quả bài đăng MXH: lượt tiếp cận, tương tác theo nền tảng, bài đăng gần đây. |
| `sources-report` | analytics | readOnlyHint=true | Nguồn khách hàng: khách mới và doanh thu theo nguồn (ads, group, webchat...). |
| `forecast-report` | analytics | readOnlyHint=true | Dự báo: hội thoại và doanh thu dự kiến dựa trên xu hướng kỳ gần nhất. |
| `export-report` | analytics | destructiveHint=true | Queue a report export with web report filters and workspace actor timezone. Poll export status; queued is not a downloadable file. |
| `list-report-exports` | analytics | readOnlyHint=true | list report exports |
| `get-report-export` | analytics | readOnlyHint=true | Poll a report export by job ID. Completed exports return a signed download link requiring the current user login. File availability is checked before returning a link. |
