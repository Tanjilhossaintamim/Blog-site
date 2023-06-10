from django.contrib import admin
from .models import Blog, Comment, Like

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    '''Admin View for Blog'''

    list_display = ['id', 'blog_title', 'blog_content', 
                    'blog_image', 'publish_at', 'update_at', 'author']
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ['id', 'user', 'blog', 'comment', 'comment_date']
    list_per_page = 10


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    '''Admin View for Like'''

    list_display = ['user', 'blog']
    list_per_page = 10
