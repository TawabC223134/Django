# Django
from django.contrib.auth import views as auth_views
from django.urls import path
# rest_framework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, LogoutView



urlpatterns = [
    
      path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #custom login
      path('logout/', auth_views.LogoutView.as_view(), name='logout'), #logout path
      #path('register/', views.register, name='register'),
      path('register/', RegisterView.as_view(), name='register'),
      path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
      path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      path('token/logout/', LogoutView.as_view(), name='token_logout'),

]