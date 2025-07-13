from django.db import models

# Create your models here.
from django.db import models
from taggit.managers import TaggableManager



class PostStatusType(models.IntegerChoices):
    active = 1,("active")
    disabled = 2,("Inactive")


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    


class PostModel(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(allow_unicode=True,unique=True)
    content = models.TextField()
    author = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/images/",null=True,blank=True)
    category = models.ManyToManyField(PostCategory)
    tags = TaggableManager()
    status = models.IntegerField(choices=PostStatusType.choices,default=PostStatusType.disabled.value)
    
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class CommentModel(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    message = models.TextField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return " {} - {} ".format(self.post.title,self.user.email)