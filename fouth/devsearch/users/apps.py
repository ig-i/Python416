from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):  # регистрируем импорт перехватывания сигналов пользователей (изменение, удаление в базе и т.д.)
        import users.signals
