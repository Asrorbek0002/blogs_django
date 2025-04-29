from django.contrib import admin

from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'owner__username', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    list_display_links = ('id', 'title', 'owner__username')
    search_fields = ('title', 'description')
    readonly_fields = ('views_count', )


