---
tags: [engineering-practices, laravel]
sources: [PHP Laravel - Kinh nghiệm code.md]
created: 2026-10-27
updated: 2026-10-27
---

# Config Level Casting

Ép kiểu giá trị cấu hình **một lần tại file config**, thay vì ép kiểu mỗi lần đọc trong code nghiệp vụ. Kiểu dữ liệu được đảm bảo từ một nguồn duy nhất, code gọi gọn hơn.

```php
// Bad — ép kiểu ở chỗ dùng
$secret = (string) config('services.shopify.secret');

// Good — config/services.php
'shopify' => [
    'secret' => (string) env('SHOPIFY_API_SECRET', ''),
],
```

Trong [[laravel|Laravel]], `env()` chỉ nên gọi trong file config; ép kiểu và giá trị mặc định đặt cạnh nhau ở đó là tự nhiên nhất.

Nguồn: [[php-laravel-kinh-nghiem-code|PHP Laravel - Kinh Nghiệm Code]]. Xem thêm [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]].
