from django.contrib import admin
from . models import Post
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    ordering = ('author',)
    search_fields = ('title',)
    list_filter = ('date_posted', 'title','author')