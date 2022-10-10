from django.contrib import admin
from .models import Category, Post

# Register your models here.
# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date', 'created_at')
    list_filter = ('status', 'author' )
    # ordering = ['-created_at']
    search_fields = ['title', 'content']
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
