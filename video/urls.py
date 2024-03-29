from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('redirect/<int:video_id>/', views.redirect_to_video, name='redirect_to_video'),
]
