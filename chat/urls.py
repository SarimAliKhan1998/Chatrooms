# chat/urls.py
from django.urls import path

from .views import indexView, roomView

app_name = "chat"

urlpatterns = [
    path('', indexView, name='index'),
    path('<str:room_name>/', roomView, name='room'),
]