import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valentines.settings')
django.setup()

from love.models import DrawerItem

# Clear existing items
DrawerItem.objects.all().delete()

# Add sample Valentine's items
items = [
    {
        'title': 'First Date Memory',
        'message': 'I still remember that first day when we met. Your smile melted my heart instantly. Every moment with you feels like a dream come true. You are my greatest blessing.'
    },
    {
        'title': 'Forever & Always',
        'message': 'I love the way you laugh, the way you care, and the way you make my world complete. With you by my side, I feel invincible. You are my love, my life, my everything.'
    },
    {
        'title': 'A Sweet Promise',
        'message': 'Through every season, through every challenge, my love for you will never fade. You are my soulmate, my partner, my best friend. Lets grow old together and create a thousand more beautiful memories.'
    },
    {
        'title': 'Missing You',
        'message': 'When you are not around, everything feels incomplete. Your presence makes every ordinary moment extraordinary. I cannot wait to hold you in my arms again. You mean the world to me.'
    },
    {
        'title': 'You Complete Me',
        'message': 'Before you, I did not know what true love felt like. Now I cannot imagine my life without you. Thank you for being my greatest adventure and my safe haven. I love you more each day.'
    },
]

for item in items:
    DrawerItem.objects.create(
        title=item['title'],
        message=item['message']
    )

print('✅ Created 5 sample Valentines items!')
print('Your drawer is now full of love messages!')
