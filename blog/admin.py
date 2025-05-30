from django.contrib import admin
from .models import Post, About
from django.utils.html import format_html

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image_tag')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'image', 'image_tag')
        }),
        ('Tarih Bilgisi', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;max-width:150px;border-radius:8px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Görsel Önizleme'
    image_tag.allow_tags = True
    readonly_fields = ('image_tag', 'created_at', 'updated_at')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')