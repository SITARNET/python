from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect # встренный шаблонизатор django

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all() # получаем все статьи
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def categories(request, catid):
    if (request.GET): # request.POST
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям: {catid}</h1>")

def archive(request, year):
    if int(year) > 2020:
        # raise Http404
        # return redirect('/') # 302
        return redirect('home', permanent=True) # 301
    return HttpResponse(f"<h1>Архив по годам: {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!</h1>")