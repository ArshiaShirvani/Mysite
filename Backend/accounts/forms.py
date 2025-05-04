from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AuthenticationForm(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AuthenticationForm,self).confirm_login_allowed(user)
        
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password1",
            "password2",
        )
        
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Enter Your Email", max_length=254)
    
    
class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)