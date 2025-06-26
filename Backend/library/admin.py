from django.contrib import admin
from .models import BookModel,BookCategory,BookCommentModel,BookStatusType


@admin.register(BookModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','status','created_date')
    
@admin.register(BookCategory)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_date')
    
@admin.register(BookCommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('book','user','message','created_date')