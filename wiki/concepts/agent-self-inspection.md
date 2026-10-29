---
tags: [ai-engineering, engineering-practices]
sources: [PHP Laravel experience.md, Senior developer experience.md]
created: 2026-10-29
updated: 2026-10-29
---

# Agent Self Inspection

AI agent tự chạy phân tích tĩnh (inspection) trên code mình vừa viết và sửa sạch lỗi **trước khi** báo hoàn thành, thay vì để người review phát hiện.

## Vì sao cần

Code AI viết thường chạy được nhưng vẫn dính những lỗi IDE bắt được ngay: gọi method không tồn tại, sai type, biến không dùng, điều kiện luôn đúng/sai, code chết ([[php-laravel-experience|PHP Laravel Experience]]). Inspection còn kéo code về một coding convention chung: tên biến tốt hơn, khối code gọn hơn, cú pháp mới hơn ([[senior-developer-experience|Senior Developer Experience]]).

Đây là bước tự động bổ sung cho checklist review tay ở [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]].

## Quy tắc

Theo [[php-laravel-experience|PHP Laravel Experience]], với PHP/[[laravel|Laravel]] dùng Inspect CLI của [[phpstorm|PhpStorm]]:

1. **Phạm vi:** mặc định chỉ quét file có thay đổi. Sửa hết `ERROR`/`WARNING` trong file mình đã đụng tới. `WEAK WARNING` chỉ sửa nếu nằm trong dòng mình vừa đụng tới.
2. **Không mở rộng scope:** lỗi cũ ở file không liên quan để nguyên, tránh diff phình to.
3. **Không né lỗi:** không dùng `@noinspection`, `@phpstan-ignore`, không tắt inspection, không cast bừa. False positive thì để nguyên và giải thích trong báo cáo.
4. **Lặp đến khi sạch:** sửa xong chạy lại, chỉ báo kết quả của lần chạy cuối.
5. **Tool lỗi ≠ pass:** không chạy được tool thì phải báo cho người dùng, không coi là đã qua.

## Liên quan

- [[ai-agent-handoff-documents|AI Agent Handoff Documents]] — các bước agent làm sau khi xong việc; tự inspect là bước trước khi bàn giao.
