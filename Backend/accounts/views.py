from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm,UserRegisterForm
from django.contrib import messages
from django.views .generic import (
    FormView,
    CreateView,
    UpdateView)
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.contrib.auth import get_user_model
from accounts.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()
from .forms import PasswordResetRequestForm,SetNewPasswordForm

class LoginView(auth_views.LoginView):
    template_name = "accounts/authentication.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f"عزیز، خوش آمدید{user.email} ")
        return super().form_valid(form)
    
    
class SignUpView(FormView):
    template_name = "accounts/authentication.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("website:index")

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data["password1"]
        user.set_password(password)
        user.save()

        authenticated_user = authenticate(
            self.request,
            email=form.cleaned_data["email"],
            password=password
        )

        if authenticated_user:
            login(self.request, authenticated_user)
            messages.success(self.request, "ثبت‌نام و ورود با موفقیت انجام شد.")
        else:
            messages.error(self.request, "ثبت‌نام انجام شد اما ورود به سیستم ممکن نشد.")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "خطا در ثبت‌نام. لطفاً اطلاعات وارد شده را بررسی کنید.")
        return super().form_invalid(form)
    
    
class LogoutView(auth_views.LogoutView):
    pass


def password_reset_confirm(request, token, uidb64):
    try:
        # getting uid of the user and decode of them
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Checking the token
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password != confirm_password:
                messages.error(request, 'The password and confirmation do not match')
            elif len(new_password) < 8:
                messages.error(request, 'Password must be at least 8 characters long')
            else:
                # Saving new password
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been successfully changed')
                return redirect(reverse_lazy("accounts:login"))  

        # send token and uid64 to the template
        return render(request, 'accounts/password_reset_confirm.html', {'validlink': True, 'uid': uidb64, 'token': token})
    else:
        messages.error(request, 'The recovery link is invalid or has expired')
        return render(request, 'accounts/password_reset_confirm.html', {'validlink': False})



reset_tokens = {}

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # getting a uid of the user based on the base64
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # make token for retrieving password
            token = default_token_generator.make_token(user)

            # content of the email
            email_body = f"""
                سلام،

                برای تغییر رمز عبور خود، روی لینک زیر کلیک کنید:
                https://{request.get_host()}/accounts/password-reset-confirm/{uid}/{token}/

                اگر این درخواست از طرف شما نبوده، لطفاً این ایمیل را نادیده بگیرید.
            """

            # sending email
            send_mail(
                'بازیابی رمز عبور',  # title
                email_body,  # content
                'from@example.com', 
                [email],  
                fail_silently=False
            )
            
            return render(request,'website/index.html')
        else:
            messages.error(
                request,"No account associated with this email address exists"
            )
    