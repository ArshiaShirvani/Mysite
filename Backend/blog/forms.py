from django import forms
from .models import CommentModel

class SubmitCommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentModel
        fields = [
            "post",
            "message"
        ]