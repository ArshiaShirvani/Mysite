from django.db import models
from taggit.managers import TaggableManager


class BookStatusType(models.IntegerChoices):
    active = 1,("active")
    disabled = 2,("Inactive")

class BookCategory(models.Model):
    name = models.CharField(max_length=255)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class BookModel(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(allow_unicode=True,unique=True)
    content = models.TextField()
    file = models.FileField(upload_to='books/files/')
    category = models.ManyToManyField(BookCategory)
    tags = TaggableManager()
    status = models.IntegerField(choices=BookStatusType.choices,default=BookStatusType.disabled.value)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class BookCommentModel(models.Model):
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    message = models.TextField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return " {} - {} ".format(self.post.title,self.user.email)