from django.contrib import admin
from .models import PostModel,PostCategory,CommentModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','created_date')
    
@admin.register(PostCategory)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_date')
    
@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('post','user','message','created_date')