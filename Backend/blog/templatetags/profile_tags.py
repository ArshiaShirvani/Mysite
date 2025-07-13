from django import template
from accounts.models import Profile

register = template.Library()

@register.simple_tag
def get_profile(user):
    return Profile.objects.get_or_create(user=user)[0]
