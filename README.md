# MusicFinder

کتابخانه پایتون برای جستجوی نامحدود و دقیق در گوگل و استخراج لینک‌های دانلود.

## نصب

```bash
pip install musicfinder
```

## نحوه استفاده
```python
Copy
Edit
from musicfinder import MusicFinder

# ساخت نمونه‌ای از کلاس جستجوگر
finder = MusicFinder()

# جستجو در گوگل
results = finder.search("دانلود آهنگ های جدید")
# چاپ لینک‌ها
print(results)
```

کتابخانه با قابلیت جستجوی بدون محدودیت و استخراج لینک‌های دانلود دقیق به شما کمک می‌کند تا ربات جستجوی شخصی خود را بسازید.
