# OpenAI — nội dung và cách nộp

## Tệp dùng

`archives/openai-trolypage-mcp-1.0.1-DRAFT.zip` là bản để bạn review. Chưa gọi đây là submission-ready. ZIP có một plugin ở root: `plugin.json`, `mcp.json`, `skills/`, `assets/`, README.

Metadata public nằm trong `extensions.com.openai.interface`; 5 positive/3 negative cases nằm ở `extensions.com.openai.review.test_cases`; khai báo commerce=true; countries=[] theo lựa chọn phát hành toàn bộ quốc gia nền tảng cho phép. English ở listing gốc, Vietnamese ở `publication.translations.vi-VN`. Không có `.app.json`, app binding, hook, token hoặc mật khẩu.

## Chỉ thực hiện sau khi đã review

1. Sửa các mục readiness cần thiết, tạo tài khoản demo và chạy bộ test. Quay và kiểm tra video; thêm URL thực vào manifest.
2. Build lại gói, kiểm tra `validation-report.json` và đúng hash ZIP. Vào https://platform.openai.com/plugins dưới tổ chức TroLyPage và chọn `Business — Trolypage`.
3. Upload ZIP để tạo draft. Upload không đồng nghĩa đã gửi duyệt hay đã được chấp thuận.
4. Kiểm tra metadata import, countries/translations, mô tả commerce, test cases và release notes. Hoàn tất domain challenge đúng token portal cấp. Chọn Authentication=OAuth trong portal, dùng DCR từ discovery và scope mcp:use, rồi scan tools. mcp.json dùng transport/URL chuẩn; không đặt override auth nâng cao hay client secret trong gói.
5. Điền tài khoản reviewer ở trường bảo mật của dashboard. Không đưa mật khẩu vào ZIP, Git hoặc listing. Chạy lại test trên đúng bản draft đã lưu.
6. Chủ tài khoản đọc và xác nhận policy attestations, sau đó Submit for review. Publish là bước riêng sau khi được duyệt.

## Điều đã biết

Tổ chức có trạng thái Verified và hộp upload chọn được Business — Trolypage trong phiên kiểm tra ngày 2026-10-19. Xác minh danh tính và xác minh domain MCP là hai việc riêng. Domain challenge và scan của draft chưa thực hiện.

## Nguồn

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission-errors
