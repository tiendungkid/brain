---
tags: [engineering-practices, laravel]
sources: [PHP Laravel experience.md]
created: 2026-10-27
updated: 2026-10-29
---

# Laravel

PHP framework dùng để xây backend cho Shopify app.

## Kinh nghiệm code

- Ép kiểu config trong file config (`config/services.php`), không ở chỗ dùng — [[config-level-casting|Config Level Casting]].
- Tên rõ nghĩa thay comment — [[self-documenting-code|Self Documenting Code]].
- Tách biểu thức lồng thành biến có tên — [[explaining-variables|Explaining Variables]].
- Checklist khi review code AI viết — [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]].
- Agent chạy Inspect CLI của [[phpstorm|PhpStorm]] và sửa sạch lỗi trước khi báo xong — [[agent-self-inspection|Agent Self Inspection]].

Nguồn: [[php-laravel-experience|PHP Laravel Experience]].
