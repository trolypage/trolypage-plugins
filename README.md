# TrolyPage — bộ hồ sơ review OpenAI, Claude và Muse

TrolyPage provides AI customer support, CRM, social media scheduling and order management for small businesses. This repository contains plugin source and review candidates for connecting an AI assistant to an authorized TrolyPage workspace.

**Repository:** [trolypage/trolypage-plugins](https://github.com/trolypage/trolypage-plugins) · **Status:** review candidates, not yet submitted or approved by the directories.

[OpenAI package](packages/openai/trolypage-mcp) · [Claude package](packages/claude/trolypage-mcp) · [Muse form](review/04-muse.md) · [Readiness](review/07-readiness.md) · [SEO review](review/09-seo-and-discovery.md)

**Bản chuẩn bị ngày 19/10/2026. Trạng thái: REVIEW DRAFT.**

Mở `review.html` để xem toàn bộ nội dung. Bộ này phục vụ chủ tài khoản review trước khi upload. Repository đã public trên GitHub; chưa gửi hồ sơ, tạo draft submission hay chấp nhận điều khoản của các directory.

## Đã chuẩn bị

- Gói OpenAI portable `trolypage-mcp` 1.0.1, OAuth DCR, 9 skills cập nhật catalog, metadata EN/VI, 5 positive/3 negative cases, commerce disclosure, countries và logo mobile.
- Gói Claude skills + MCP connection, hồ sơ riêng cho MCP connector và bundle GitHub. Repository đã public; còn chờ license do bạn chọn và catalog phù hợp chính sách Claude.
- Nội dung form Muse, technical/data-processing dossier, inventory 270 tools, proposed classifications, test ledgers và hướng dẫn reviewer/demo.
- Bằng chứng public status/OAuth/policy được đọc từ trình duyệt Edge của bạn, cùng catalog schemas từ mã nguồn cô lập (không nạp .env, không gọi nghiệp vụ).

Người phụ trách: **Alex Nguyen**, email **support.mcp@trolypage.com**. Bản review bổ sung phần SEO/khả năng được tìm thấy ở `review/09-seo-and-discovery.md`.

## Review theo thứ tự

1. `review/01-listing-and-copy.md`: mô tả sản phẩm, tên, email, commerce, quốc gia.
2. `review/07-readiness.md`: các mục phải xử lý trước khi nộp; đây là phần quan trọng nhất để chốt.
3. `review/02-openai.md`, `03-claude.md`, `04-muse.md`: hồ sơ từng nền tảng.
4. `review/06-tests-demo-and-access.md`: kết quả kiểm tra tài khoản reviewer, fixtures và kịch bản quay.
5. `review/08-policy-copy-to-review.md`: lỗi thông tin cũ và draft chỉnh trang public.

## Tệp để dùng

| Tệp / thư mục | Mục đích |
| --- | --- |
| archives/openai-trolypage-mcp-1.0.1-DRAFT.zip | Review gói sẽ upload OpenAI sau khi hoàn thiện |
| archives/claude-trolypage-mcp-1.0.1-DRAFT.zip | Review bundle; Claude Directory lấy source qua GitHub |
| packages/ | Source sạch cho các gói; không có backend TrolyPage |
| review/ | Nội dung form, checklist, kỹ thuật, test và gap report |
| assets/ | Logo mobile gốc 1024, bản 512, composer 64 và preview |
| evidence/ | Snapshot công khai và source schemas; chưa phải kết quả test nghiệp vụ |
| validation-report.json | Kết quả kiểm tra cấu trúc local và giới hạn của việc kiểm tra |
| archives/SHA256SUMS.txt | Hash archive để đối chiếu đúng bản |

## Chờ hoàn tất

Tài khoản reviewer đã vào được workspace riêng; còn thiếu fixtures, OAuth/tool tests và video thật. Còn chờ license Claude; sửa identity/copy trên trang policy; annotation completeness; giới hạn generate-social-image và integration execution cho Claude; xác nhận data processing/Muse payment classification. Chi tiết và mức độ nằm ở readiness report. Không gọi các ZIP DRAFT là sẵn sàng submit.

## Build lại

Sửa source trong `packages/` và tài liệu trong `review/`. Sau khi thêm URL demo hoặc đổi metadata, chạy `python -X utf8 package.py` để đóng gói và kiểm tra lại mà không ghi đè các chỉnh sửa. Không sửa trực tiếp ZIP.

`build-review-pack.py` chỉ dùng để dựng lại snapshot ban đầu từ `D:/facebook-support-agent`: chạy lại sẽ ghi đè các draft, package source và test ledger. Lưu các chỉnh sửa và kết quả kiểm thử thực trước khi chủ ý tạo lại snapshot. Phần kiểm tra Agent Plugins schema dùng thư viện jsonschema ở thư mục tạm của máy; các kiểm tra local còn lại không thay thế portal scan.

Repo local: D:/trolypage-plugins. GitHub public: https://github.com/trolypage/trolypage-plugins. Chưa chọn giấy phép phát hành cho Claude bundle; việc public repository không tự đặt giấy phép cho nội dung.
