from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.validators import validate_iranian_cellphone_number

class ContactStatusType(models.IntegerChoices):
    Seen = 1, _("Seen")
    NotSeen = 2, _("NotSeen")


class ContactModel(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_cellphone_number])
    subject = models.CharField(max_length=255)
    message = models.TextField()
    seen = models.IntegerField(
        choices=ContactStatusType.choices, default=ContactStatusType.Seen.value)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email


class NewsletterModel(models.Model):
    email = models.EmailField()
    seen = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email