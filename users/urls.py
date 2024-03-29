from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.signin, name='login'),
    path('signout/', views.signout, name='logout'),
    # path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    # path('signout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
  
]