---
tags: [engineering-practices]
sources: [PHP Laravel experience.md]
created: 2026-10-27
updated: 2026-10-29
---

# Self Documenting Code

Để tên biến và hàm tự biểu đạt nhiệm vụ, thay vì comment từng dòng để giải thích code làm gì. Comment chỉ dành cho điều tên gọi không nói được (lý do, ràng buộc bất thường).

```php
// Bad — tên tắt, điều kiện chặn tách rời
$s = config('services.shopify.secret');
if (! $secret) { return false; }
if (! $signature) { return false; }

// Good — tên rõ nghĩa, gộp điều kiện cùng mục đích
$secret = config('services.shopify.secret');
$signature = $query['signature'][0] ?? null;

if (! $secret || ! $signature) {
    return false;
}
```

Đây là lỗi phổ biến của AI agent, xem [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]]. Liên quan chặt với [[explaining-variables|Explaining Variables]].

Nguồn: [[php-laravel-experience|PHP Laravel Experience]].
