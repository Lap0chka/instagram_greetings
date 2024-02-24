from django.urls import path, include
from . import views

app_name = 'greeting'

urlpatterns = [
    path('', views.index, name='index'),
]
