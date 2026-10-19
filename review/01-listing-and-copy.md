# Nội dung listing để review

Ngày: 2026-10-19. Nội dung tiếng Anh bên dưới để dùng khi điền form. Bản Việt để bạn kiểm tra ý nghĩa. Đây là bản review; các mục ở `07-readiness.md` chưa hoàn tất.

## Thông tin đã xác nhận

| Mục | Giá trị |
| --- | --- |
| Thương hiệu / tên listing | TrolyPage |
| OpenAI developer identity | Business — Trolypage, đã thấy trong hộp upload |
| Công ty theo website | TROLYPAGE COMPANY LIMITED / CÔNG TY TNHH TROLYPAGE |
| Người phụ trách — email | support.mcp@trolypage.com |
| Người phụ trách — họ tên | Alex Nguyen — chủ tài khoản xác nhận |
| Hỗ trợ công khai | support@trolypage.com |
| Quốc gia | Tất cả quốc gia nền tảng cho phép; phương thức thanh toán/vận chuyển tùy khu vực |
| Thanh toán | Có commerce; thanh toán bên ngoài AI host |
| Logo | Logo launcher mobile app, không vẽ lại; bản 1024, 512, 64 px trong assets |
| Phiên bản candidate | 1.0.1; giữ tên trolypage-mcp từ gói nguồn |

## English listing

**Display name:** TrolyPage

**Subtitle:** AI support, CRM & social posts

TrolyPage is AI customer support, CRM, social media scheduling and order management software for small businesses. It brings customer conversations, products, orders, scheduled content and follow-up work into one business workspace.

This integration connects your AI assistant to an existing TrolyPage workspace. Find customers and summarize conversations, update internal CRM notes, check product prices and stock, prepare orders for shop review, and compare sales reports. You can also manage social post drafts, marketing campaigns, approved knowledge, connected channels, agents, assets, workflows and configured integrations when those modules are available to your account.

Sign in with OAuth and select the workspace you administer. Access requires an owner or administrator role and a plan with the requested MCP modules. Some AI and media actions consume additional quota. Channel features, delivery services and payment methods vary by account, provider and region.

TrolyPage supplies the authoritative price, stock, total and payment status. Drafts, pending approvals, completed actions and delivery to an external service are distinct. Authorized writes can change records, send messages, publish posts or request services. Customers complete merchant payments outside the AI assistant; a payment QR or pending request does not prove that money was received.

### Suggested starting prompts

- Summarize a customer conversation and draft a reply for me to review.
- Find a product by SKU and prepare an order for shop review.
- Compare sales for the last 30 days with the previous period.

### Commerce disclosure

TrolyPage supports merchant product lookup, order preparation and management, payment QR generation/status checks, shipping and bookings. Customers complete payment outside the assistant using the merchant's supported payment method. This integration does not directly debit bank accounts or transfer financial assets. A generated QR, unpaid order or pending approval is not a completed payment. Merchant/provider/region restrictions apply.

## Bản mô tả Việt

TrolyPage là phần mềm AI chăm sóc khách hàng, quản lý CRM, lên lịch bài đăng mạng xã hội và xử lý đơn hàng cho doanh nghiệp nhỏ. Hội thoại, sản phẩm, đơn hàng, nội dung và công việc chăm sóc lại khách được quản lý trong một workspace.

Bản tích hợp kết nối trợ lý AI với workspace TrolyPage sẵn có: tìm khách và tóm tắt hội thoại, cập nhật ghi chú CRM nội bộ, kiểm tra giá và tồn kho, tạo đơn chờ shop duyệt, so sánh báo cáo bán hàng. Các module được cấp quyền còn hỗ trợ bài nháp, chiến dịch, tri thức, kênh, AI Agent, tài nguyên, workflow và tích hợp.

Đăng nhập OAuth, chọn workspace bạn quản trị và dùng gói có quyền MCP tương ứng. Một số tác vụ AI/media tiêu hao quota; khả năng kênh, vận chuyển và thanh toán tùy tài khoản, nhà cung cấp và khu vực. Giá, tồn kho, tổng tiền và trạng thái thanh toán do TrolyPage xác nhận. Phân biệt bản nháp, chờ duyệt, đã thực thi và giao ra kênh. Thanh toán diễn ra bên ngoài trợ lý AI; có QR hoặc yêu cầu chờ xử lý chưa có nghĩa đã nhận tiền.

## URLs

| Trường | URL | Kết quả kiểm tra |
| --- | --- | --- |
| Website | https://trolypage.com/mcp | Đã mở qua Edge; mô tả MCP và có thông tin công ty |
| Support | https://trolypage.com/mcp#errors | Trang MCP có bảng lỗi và email hỗ trợ ở footer; nên nâng cấp trang hỗ trợ riêng sau |
| Privacy | https://trolypage.com/privacy-policy | Truy cập công khai được; có phần tên/pháp nhân cũ cần sửa trước khi nộp |
| Terms | https://trolypage.com/terms-of-service | Đã mở được và có TROLYPAGE COMPANY LIMITED; rà soát phần còn lại trước khi xác nhận pháp lý |

Không có URL demo giả trong manifest. Khi video thực đã được quay và mở được bằng tài khoản reviewer, thêm `review.demo_recording_url` rồi build lại archive.
