from django.contrib import admin
from .models import Post
from .models import Comments



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')