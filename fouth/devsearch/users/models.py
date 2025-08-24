from django.db import models
from django.contrib.auth.models import User


# профиль Пользователя
class Profile(models.Model):  # создаем табл. в базе  и делаем связь один к одному (у 1 пользователя будет 1 профиль)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # если пользователь удалится
    name = models.CharField(max_length=200, null=True, blank=True)  # то его профиль тоже будет удален
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", default="profiles/user-default.png", null=True, blank=True)
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name






