from django.contrib import admin
from .models import Image, Comment

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'image', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
