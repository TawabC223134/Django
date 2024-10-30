# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView

from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView, TemplateView

urlpatterns = [
    
      path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #custom login
      path('logout/', auth_views.LogoutView.as_view(), name='logout'), #logout path
      #path('register/', views.register, name='register'),
      path('register/', RegisterView.as_view(), name='register'),

]