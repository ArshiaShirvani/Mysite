from django.db import models


class NewsletterModel(models.Model):
    email = models.EmailField()
    seen = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email