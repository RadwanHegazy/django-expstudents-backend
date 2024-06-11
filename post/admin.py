from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostPanel (admin.ModelAdmin) : 
    list_display = ['user', 'created_at']