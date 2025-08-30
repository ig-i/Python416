from django.contrib.auth.forms import UserCreationForm  # импортируем стандартную форму
from django.shortcuts import render

from mobile.models import Mobile


def signup_user(request):
    return render(request, 'mobile/signupuser.html', {'form': UserCreationForm()})


def index(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/index.html', {'projects': projects})
