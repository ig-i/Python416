from django.shortcuts import render
from .models import Dz


def index(request):
    projects = Dz.objects.all()
    return render(request, 'dz_one/index.html', {'projects': projects})
