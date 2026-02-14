from django.urls import path
from . views import home, add_memory, delete_memory, bulk_delete, diana_notes, diana_music

urlpatterns = [
    path('', home, name='home'),
    path('add-memory/', add_memory, name='add_memory'),
    path('delete/<int:item_id>/', delete_memory, name='delete_memory'),
    path('bulk-delete/', bulk_delete, name='bulk_delete'),
    path('diana/', diana_notes, name='diana_notes'),
    path('diana/music/', diana_music, name='diana_music'),
]