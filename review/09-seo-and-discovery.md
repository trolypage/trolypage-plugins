# Review SEO, khả năng được tìm thấy và độ dễ hiểu

Ngày 19/10/2026. Người phụ trách: **Alex Nguyen** — support.mcp@trolypage.com.

## Kết luận

**Hồ sơ bản trước chưa giới thiệu đủ rõ cho người chưa biết TrolyPage.** Subtitle quá rộng và câu mở đầu giả định người đọc đã biết workspace của sản phẩm. Đã sửa bản nháp trong repo để nói rõ nhóm công việc: AI chăm sóc khách hàng, CRM, lên lịch nội dung và quản lý đơn hàng. Tên thương hiệu và verified publisher vẫn giữ nguyên.

**Trang Features có nền tảng on-page tốt hơn phần listing cũ.** Đây là trang tổng quan tác vụ có nội dung HTML đọc được. Cần tăng độ rõ ràng và tính nhất quán; hiện chưa có bằng chứng để kết luận thứ hạng hay lượng tìm kiếm tốt. Review này không dùng Search Console, dữ liệu keyword volume hoặc báo cáo Core Web Vitals.

## Ba nơi cần tối ưu khác nhau

| Nơi | Việc cần làm |
| --- | --- |
| Google / Bing | Trang công khai mô tả đúng nhu cầu, có thể crawl, liên kết nội bộ và nội dung hữu ích cho người tìm kiếm |
| Directory của OpenAI / Claude / Muse | Tên, subtitle, mô tả, README và ví dụ giúp người chưa biết thương hiệu hiểu lợi ích và điều kiện dùng |
| AI chọn công cụ sau khi kết nối | Metadata từng tool, input schema, phạm vi dữ liệu và prompt kiểm thử giúp gọi đúng công cụ |

Không có căn cứ để coi việc thêm từ khóa vào ZIP sẽ tự tăng thứ hạng Google hoặc đảm bảo directory đề xuất TrolyPage. OpenAI hướng dẫn kiểm thử metadata bằng cả prompt nêu thương hiệu, prompt chỉ nêu nhu cầu và prompt không nên dùng tool. [Hướng dẫn metadata](https://developers.openai.com/plugins/guides/optimize-metadata).

## Đã chỉnh trong hồ sơ nháp

| Trường | Bản review hiện tại |
| --- | --- |
| Contact person | Alex Nguyen |
| Display name | TrolyPage — giữ tên thương hiệu |
| English subtitle | AI support, CRM & social posts — 30 ký tự |
| Vietnamese subtitle | AI chăm khách, CRM & đăng bài — 29 ký tự |
| Câu đầu | TrolyPage is AI customer support, CRM, social media scheduling and order management software for small businesses. |
| Câu tiếp theo | Giải thích sản phẩm tập hợp công việc kinh doanh và bản tích hợp kết nối vào workspace sẵn có |
| Starter prompts | Tóm tắt hội thoại/soạn câu trả lời để review; tìm SKU/tạo đơn chờ duyệt; so sánh doanh thu |
| README | Thêm link Features để hiểu sản phẩm, giữ link MCP để cài/kết nối; dùng cùng định nghĩa sản phẩm |
| Claude keywords | customer-support, crm, social-media-scheduling, order-management cùng brand; không coi đây là cơ chế xếp hạng đã được công bố |

Các giới hạn quyền, gói, thanh toán ngoài host và các trạng thái duyệt vẫn được giữ. Không mở rộng phạm vi tool hoặc khai thêm kênh chưa được chứng minh. WebsiteURL của plugin vẫn trỏ trang MCP có hướng dẫn kết nối; Features là trang giải thích sản phẩm được liên kết thêm trong README.

## Kiểm tra kỹ thuật trang Features

Nguồn trực tiếp: `evidence/features-seo.json`. Đọc HTTP công khai vào ngày review; điều hướng trình duyệt gặp timeout, nên không chấm điểm visual hoặc tốc độ từ sự cố đó.

| Kiểm tra | Quan sát | Đánh giá |
| --- | --- | --- |
| HTTP / nội dung | /features và /vi/tinh-nang trả 200, có heading và nội dung trong HTML | Nền tảng crawl tốt |
| Title | Title hiện nêu scheduled posting và multichannel inbox trước brand | Cụ thể hơn slogan; chưa cần đổi chỉ để nhét thêm keyword |
| Description | Có mô tả tác vụ và kênh | Đủ rõ để bắt đầu; Google có thể chọn snippet khác |
| H1 | Có một H1 mô tả chuỗi công việc | Tốt hơn chỉ ghi tên thương hiệu |
| Canonical / locale | EN tự canonical; có alternate EN, VI và x-default; VI có metadata riêng | Cấu trúc đa ngôn ngữ đã có; vẫn cần theo dõi URL thực được Google chọn |
| Robots / sitemap | Không thấy noindex ở meta/X-Robots-Tag đã đọc; robots không chặn Features; sitemap-pages có hai URL EN/VI | Không thấy blocker crawl trong phạm vi kiểm tra; không đồng nghĩa Google đã index |
| Sharing | Có OG/Twitter metadata | Hữu ích cho preview liên kết |
| Structured data | Không thấy application/ld+json ở HTML Features đã đọc | Có thể bổ sung WebPage/BreadcrumbList đúng nội dung; ưu tiên sau copy và thông tin phạm vi |
| Image alt | Tất cả img có thuộc tính alt; một số để rỗng | alt rỗng có thể đúng với ảnh trang trí; cần visual review trước khi coi là lỗi |

Google khuyến nghị title rõ, mô tả đúng trang; meta description có thể được dùng làm snippet, không phải đoạn hiển thị được đảm bảo. [Title links](https://developers.google.com/search/docs/appearance/title-link), [snippets](https://developers.google.com/search/docs/appearance/snippet).

## Ưu tiên sửa trên website — mới là đề xuất

### 1. Thêm định nghĩa sản phẩm ngay dưới thông điệp chính

Giải thích rõ đây là phần mềm cho ai và nhóm công việc nào, rồi mới đi sâu vào automation/AI. Draft English:

> TrolyPage is customer support and social media management software for small business teams. Organize customer conversations, keep CRM records, schedule posts and turn conversations into orders—with AI assistance and human review where needed.

Draft Vietnamese:

> TrolyPage là phần mềm chăm sóc khách hàng và quản lý nội dung mạng xã hội cho doanh nghiệp nhỏ. Tập trung hội thoại, lưu thông tin khách, lên lịch bài đăng và tạo đơn ngay từ cuộc trò chuyện, với AI hỗ trợ và nhân viên duyệt khi cần.

Đây là copy mới đề xuất để chủ sản phẩm review, chưa sửa trang live. Không dùng các claim tăng doanh thu, tiết kiệm một tỷ lệ thời gian hay tự động chốt mọi đơn khi chưa có dữ liệu đo.

### 2. Đồng bộ lời hứa với khả năng đang có

Trang Features giới hạn quản lý comment ở YouTube, trong khi heading khái quát có thể khiến người mới hiểu là mọi kênh đều hỗ trợ. Đề xuất heading sát phạm vi hiện tại, có nhãn mở rộng khi hỗ trợ thêm.

Phần follow-up nên mô tả gửi theo lịch/quy tắc đã cấu hình, tránh gợi ý sản phẩm biết lúc khách rảnh. Footer dùng lời hứa tự động hóa rộng hơn nội dung chính; nên viết thống nhất với quyền duyệt và khả năng từng kênh. [Trang đã review](https://trolypage.com/features).

### 3. Làm rõ luồng khách mới so với người đã có tài khoản

- Người tìm giải pháp: xem ví dụ, kênh hỗ trợ, điều kiện gói và bước thử đầu tiên.
- Người muốn plugin: cần biết có phải tạo TrolyPage workspace trước không, role/gói nào dùng được và có thể thử tác vụ gì sau khi kết nối.

CTA nên nói hành động cụ thể như thử inbox hoặc xem demo một quy trình. Không biến toàn bộ trang thành danh sách thuật ngữ MCP, OAuth, entitlements.

### 4. Phát triển nội dung theo nhu cầu cụ thể

Các nhóm từ khóa bên dưới là **giả thuyết intent**, chưa có số volume/độ khó:

| Nhu cầu | Cụm từ/ý tưởng nội dung |
| --- | --- |
| Chăm sóc khách | AI customer support; AI chatbot for Messenger; chatbot chăm sóc khách hàng |
| Inbox / CRM | shared inbox; Messenger and Zalo OA inbox; quản lý tin nhắn đa kênh; CRM khách hàng |
| Nội dung | social media scheduling; lên lịch đăng bài Facebook; quản lý nội dung mạng xã hội |
| Đơn hàng | order management from chat; tạo đơn từ hội thoại; quản lý đơn hàng |
| Tích hợp AI | customer support tools for an AI assistant; CRM MCP connector; TrolyPage MCP |

Dùng các trang use case đã có trong navigation, bổ sung ví dụ và liên kết từ phần tính năng tương ứng. Với bản EN, review các anchor/navigation còn chữ Việt và chỉ tạo trang EN riêng khi có nội dung hữu ích, đúng phạm vi. Không nhân bản hàng loạt trang keyword gần giống nhau. Cũng không dùng tên đối thủ vào title để câu tìm kiếm.

## Việc nên đo sau khi phát hành

1. Trong Search Console: xem truy vấn không chứa brand, impressions/clicks/CTR theo URL EN/VI, quốc gia và thiết bị; kiểm tra index/canonical được chọn. So sánh cùng nhóm điều kiện trước/sau, không suy ra tác động SEO chỉ từ một ngày dữ liệu.
2. Trong directory nếu có analytics: theo dõi lượt xem → cài/kết nối → tác vụ hữu ích đầu tiên. Không xem số cài là bằng chứng dùng thành công.
3. Với AI routing: chạy `discovery-prompts.json` trên host thực sau khi kết nối demo; ghi tool có được chọn đúng và tránh kích hoạt sai. Bộ này bổ sung cho 5+3 ca nghiệp vụ, không thay thế chúng.

Trước mắt nên chốt copy định nghĩa sản phẩm và listing như bản nháp mới, xử lý các claim phạm vi, rồi đo các truy vấn thực. Các chỉnh sửa server/policy và reviewer account còn ở `07-readiness.md`.
