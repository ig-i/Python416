from django.urls import path
from .import views


urlpatterns = [
    path('', views.dz_two, name='dz_two'),
    path('<int:dz_id>/', views.detail, name='detail'),

    # (регистрация и авторизация)
    path('signup/', views.signup_user, name='signupuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),

    # (постановка задач)
    path('current/', views.current_todos, name="currenttodos"),
    path('', views.home, name="home"),
]


