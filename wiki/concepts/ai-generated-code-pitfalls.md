---
tags: [ai-engineering, engineering-practices]
sources: [PHP Laravel - Kinh nghiệm code.md]
created: 2026-10-27
updated: 2026-10-27
---

# AI Generated Code Pitfalls

Những lỗi lặp lại khi để AI agent viết code: code thường **chạy đúng** nhưng khó đọc, khó bảo trì. Dùng làm checklist khi review code do AI sinh ra.

## Checklist (PHP/Laravel)

Theo [[php-laravel-kinh-nghiem-code|PHP Laravel - Kinh Nghiệm Code]]:

- Ép kiểu rải rác ở chỗ dùng → chuyển về config, xem [[config-level-casting|Config Level Casting]].
- Tên biến tắt (`$s`) kèm comment từng dòng → đặt tên tự giải thích, xem [[self-documenting-code|Self Documenting Code]].
- Nhiều điều kiện chặn tách rời nhưng cùng kết quả → gộp lại.
- Một biểu thức lồng nhiều lời gọi hàm → tách biến trung gian, xem [[explaining-variables|Explaining Variables]].

## Công cụ hỗ trợ

- [[claude-skills|Claude Skills]] (`php-pro`) — đưa chuẩn code PHP vào agent.
- [[shopify-app-security-checks|Shopify App Security Checks]] — kiểm tra bảo mật cho Shopify app.
