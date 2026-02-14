from django.contrib import admin
from .models import DrawerItem

@admin.register(DrawerItem)
class DrawerItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
