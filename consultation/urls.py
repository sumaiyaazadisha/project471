from django.urls import path
from . import views
urlpatterns = [
    path("select/",views.schedule_input,name='schedule_input')
]