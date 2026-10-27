---
tags: [engineering-practices]
sources: [PHP Laravel - Kinh nghiệm code.md]
created: 2026-10-27
updated: 2026-10-27
---

# Explaining Variables

Khi một biểu thức lồng nhiều lời gọi hàm, tách từng phần ra **biến có tên mô tả nhiệm vụ**, chặn sớm các trường hợp không hợp lệ, rồi mới ghép thành biểu thức cuối. Code đúng nhưng lồng sâu vẫn là code khó đọc.

```php
// Bad — mọi thứ trong một return
return hash_equals(
    hash_hmac('sha256', $message, config('services.shopify.secret')),
    $query['signature'][0] ?? null
);

// Ok — tách biến, chặn sớm, rồi ghép
$secret = config('services.shopify.secret');
$signature = $query['signature'][0] ?? null;

if (! $secret || ! $signature) {
    return false;
}

return hash_equals(hash_hmac('sha256', $message, $secret), $signature);
```

AI agent đặc biệt hay viết kiểu lồng này, xem [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]]. Là một dạng cụ thể của [[self-documenting-code|Self Documenting Code]].

Nguồn: [[php-laravel-kinh-nghiem-code|PHP Laravel - Kinh Nghiệm Code]].
