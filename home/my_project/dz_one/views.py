from django.shortcuts import render
from .models import Dz   # импортируем модель Dz из models


def index(request):               # функция связанная с urls.py (путь)
    projects = Dz.objects.all()  # взяли все данные из модели Dz, сохр. в перем. projects и передали в index.html
    return render(request, 'dz_one/index.html', {'projects': projects})
