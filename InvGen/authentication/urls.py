from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]

