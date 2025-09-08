from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'is_published')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/easymde@2.18.0/dist/easymde.min.css',)
        }
        js = ('https://cdn.jsdelivr.net/npm/easymde@2.18.0/dist/easymde.min.js',)
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new blog
            obj.author = request.user
        super().save_model(request, obj, form, change)