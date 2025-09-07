from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='index')  # метод привязывает класс к этому пути
    ]