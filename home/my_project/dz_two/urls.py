from django.urls import path
from .import views


urlpatterns = [
    path('', views.dz_two, name='dz_two'),
    path('<int:dz_id>/', views.detail, name='detail'),
]