from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import DrawerItem

def home(request):
    """Display all drawer items"""
    drawer_items = DrawerItem.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'drawer_items': drawer_items})

def add_memory(request):
    """Handle adding new memories and display memory management page"""
    drawer_items = DrawerItem.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        title = request.POST.get('title', '')
        message = request.POST.get('message', '')
        image = request.FILES.get('image', None)
        
        if title and message:
            DrawerItem.objects.create(
                title=title,
                message=message,
                image=image
            )
            return redirect('add_memory')
    
    return render(request, 'add_memory.html', {'drawer_items': drawer_items})

def delete_memory(request, item_id):
    """Delete a memory item"""
    item = get_object_or_404(DrawerItem, id=item_id)
    
    if request.method == 'POST':
        item.delete()
    
    return redirect('add_memory')

def bulk_delete(request):
    """Delete multiple memory items at once"""
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')
        if selected_items:
            DrawerItem.objects.filter(id__in=selected_items).delete()
    
    return redirect('add_memory')
def diana_notes(request):
    """Display notes about Diana"""
    diana_info = {
        'name': 'Diana Mae Retulla',
        'birthday': 'March 27, 2006',
        'nicknames': ['Meme', 'Yani', 'Yana'],
        'fav_foods': [
            'Takoyaki', 'Fries', 'Chocolate', 'Cake',
            'Graham/mango float', 'Chuckie', 'Neste',
            'Matcha', 'Grapes', 'Sour mango (mangga indian)'
        ],
        'dislikes_food': [
            'Milk tea', 'Spicy food', 'Coffee', 'Atay'
        ],
        'interests': {
            'Fav color': 'Matcha green',
            'Fav pet': 'Cat & Dog (but mostly cat)',
            'Fav perfume': 'Aficionado',
            'Fav Hobby': 'Photography, Drawing, Playing games'
        },
        'likes': [
            'Me ME & MEEE',
            'Teasing me',
            'Yapping session',
            'Her bff/gf (Shy)',
            'Sleeping',
            'Hugs',
            'Tanday sa paa',
            'Eating (we\'re both foodies)',
            'Loves the plushie I bought',
            'Holding hands in private',
            'Playing games with me',
            'Playing "We Kids"',
            'Listening to music',
            'Reading',
            'Watching anime',
            'Reading manwha',
            'When I promise and keep it'
        ],
        'dislikes': [
            'Smell of cigarette',
            'Someone smoking',
            'Constantly asking the same question',
            'Immature people',
            'People who backbite',
            'When I spend too much on her',
            'When using her things without asking',
            'Hypocrite people',
            'When someone interrupts her',
            'When topic ends'
        ],
        'loves_about_her': [
            'Her beautiful smile',
            'Her cutie face',
            'How she cares about me',
            'How she cares for people',
            'Her voice',
            'Her laugh',
            'How perfect she is',
            'Her hands',
            'Her affection',
            'Her attention',
            'How brave she is',
            'Her insecurities',
            'Her jealousy',
            'Her humor',
            'Her love',
            'How forgiving she is',
            'So gorgeous',
            'Taste of music',
            'Her confidence',
            'The way she takes care of herself',
            'Her way of dressing',
            'When she speaks',
            'When she scolds me for doing bad things',
            'Her jokes',
            'How she makes me smile',
            'SO MANY IMMEASURABLE WORDS TO EXPLAIN WHY I LOVE HER, CAUSE WORDS CAN\'T EXPLAIN WHY I LOVE HER'
        ]
    }
    return render(request, 'diana_notes.html', {'diana': diana_info})

def diana_music(request):
    """Display Diana's favorite music playlist"""
    playlist = {
        'title': "Diana's Favorite Music",
        'description': 'A collection of songs for my love',
        'songs': [
            # John Roberts Songs
            {
                'id': 1,
                'title': 'Forevermore',
                'artist': 'John Roberts',
                'duration': '4:08',
                'youtube_id': 'gu-kPQ51ZX8'
            },
            {
                'id': 2,
                'title': 'Midnight in Manila',
                'artist': 'John Roberts',
                'duration': '3:52',
                'youtube_id': 'y2Ujz0SvPMg'
            },
            # Paramore Songs
            {
                'id': 3,
                'title': 'Decode',
                'artist': 'Paramore',
                'duration': '3:38',
                'youtube_id': 'qN8rHHvhXlE'
            },
            {
                'id': 4,
                'title': 'The Only Exception',
                'artist': 'Paramore',
                'duration': '3:35',
                'youtube_id': 'y988NpSXJ8Y'
            },
            {
                'id': 5,
                'title': 'Still Into You',
                'artist': 'Paramore',
                'duration': '3:44',
                'youtube_id': '7qiZfIcKzOE'
            },
            # Parokya Ni Edgar
            {
                'id': 6,
                'title': 'Buloy',
                'artist': 'Parokya Ni Edgar',
                'duration': '3:45',
                'youtube_id': 'HXlxLNlE2Ac'
            },
            {
                'id': 7,
                'title': 'Harana',
                'artist': 'Parokya Ni Edgar',
                'duration': '4:50',
                'youtube_id': 'wTPzXG3MzgE'
            },
            # Ben and Ben
            {
                'id': 8,
                'title': 'Patuloy',
                'artist': 'Ben&Ben',
                'duration': '4:05',
                'youtube_id': 'hEhF5mBCaJU'
            },
            {
                'id': 9,
                'title': 'Naisip Ko Pa Lang',
                'artist': 'Ben&Ben',
                'duration': '3:25',
                'youtube_id': 'DdYTzFVEqHA'
            },
            {
                'id': 10,
                'title': 'Ang Liwanag ng Buwan',
                'artist': 'Ben&Ben',
                'duration': '3:37',
                'youtube_id': 'KlpvQHJsF0Y'
            }
        ]
    }
    return render(request, 'diana_music.html', {'playlist': playlist})

