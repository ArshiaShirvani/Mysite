from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login"),
    path("signup/",views.SignUpView.as_view(),name="register"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
]