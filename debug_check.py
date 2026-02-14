import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valentines.settings')
django.setup()

from love.models import DrawerItem

print("=" * 50)
print("DATABASE CHECK")
print("=" * 50)

items = DrawerItem.objects.all()
print(f"Total items: {items.count()}\n")

if items.count() > 0:
    for item in items:
        print(f"✓ {item.title}")
        print(f"  Message: {item.message[:60]}...")
        print(f"  Date: {item.created_at}\n")
else:
    print("No items found. Adding sample items...\n")
    samples = [
        {"title": "Love Letter", "message": "I love you so much!"},
        {"title": "Sweet Memory", "message": "Remember that day we spent together?"},
        {"title": "Forever with You", "message": "You make me happier every day."},
    ]
    for sample in samples:
        DrawerItem.objects.create(title=sample["title"], message=sample["message"])
    print(f"✓ Created {len(samples)} sample items!")

print("\n" + "=" * 50)
print("URLS CHECK")
print("=" * 50)
from django.urls import get_resolver
resolver = get_resolver()
print(f"URL patterns: {len(resolver.url_patterns)}")
for pattern in resolver.url_patterns:
    print(f"  - {pattern.pattern}")
