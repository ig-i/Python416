from django.contrib import admin
from .models import Profile, Skill

# регистрируем модели в админ. панели
admin.site.register(Profile)
admin.site.register(Skill)

