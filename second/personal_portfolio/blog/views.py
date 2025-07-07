from django.shortcuts import render, get_object_or_404  # получить обьект ил ошибка 404
from .models import Blog


def blogs(request):
    blogs = Blog.objects.order_by('-date')  # импортируем Blog из модели и получаем данные по датам (по убыванию)
    return render(request, "blog/blogs.html", {"blogs": blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # из blog возвращ. обьект на страницу по первичному ключу (id) иначе ошибка 404
    return render(request, 'blog/details.html', {'blog': blog})

