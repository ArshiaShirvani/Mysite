from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm,UserRegisterForm
from django.contrib import messages
from django.views .generic import (
    FormView,
    CreateView,
    UpdateView)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,get_object_or_404,render
from django.contrib.auth import get_user_model
from accounts.models import Profile,User
from django.http import HttpResponseRedirect

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