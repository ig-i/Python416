from django.db.models.signals import post_save, post_delete  # перехватывание сигналов по сохранению, изм. или удалению
from .models import Profile  # данных пользователя
from django.contrib.auth.models import User


# редактирование Профиля пользователя (Profile)
def profile_update(sender, instance, created, **kwargs):
    if created:  # eсли будет создан новый пользователь то автоматически
        user = instance
        Profile.objects.create(  # метод create создает новый профиль и данные подтягиваются из таблицы User базы
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


# Редактирование Пользователя (User)
def update_user(sender, instance, created, **kwargs):
    profile = instance  # в profile экземпляр класса
    user = profile.user  # в user профиль пользователя

    if created is False:  # если происходит не создание а изменение профиля пользователя то изменяются данные в User:
        user.first_name = profile.name  # в графе first_name
        user.username = profile.username  # в графе username
        user.email = profile.email  # в графе email
        user.save()  # сохраняем эти данные в базе


# Удаление Пользователя
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()  # удал-е пользователя при удалении профиля (в models.py прописано наоборот: on_delete=models.CASCADE)


post_save.connect(profile_update, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
