from django.urls import path
from . import views

# создали второй urls (дополнительный путь)
urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),  # отдельная страница проекта по номеру первич. ключа
    path('create-project/', views.create_project, name="create_project"),  # страница для создания пользователем
]                                                                    # своего отдельного проекта через страницу сайта

