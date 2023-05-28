from django.contrib import admin
from .models import Post, PlainText, News


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(PlainText)
class PostAdmin(admin.ModelAdmin):
    list_display = ['body']


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'content', 'created', 'picture']
    list_filter = ['title', 'created']
    search_fields = ['title', 'created']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ['created']
