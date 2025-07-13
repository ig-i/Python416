from django.shortcuts import render, get_object_or_404
from .models import Dz2


def dz_two(request):
    dz_two = Dz2.objects.order_by('date')  # получаем данные из базы данных по дате
    return render(request, 'dz_two/dz_two.html', {'dz_two': dz_two})


def detail(request, dz_id):
    dz = get_object_or_404(Dz2, pk=dz_id)
    return render(request, 'dz_two/detailes.html', {'dz_two': dz})