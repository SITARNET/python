from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404 # встренный шаблонизатор django

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Дабавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

def index(request):
    posts = Women.objects.all() # получаем все статьи
    # cats = Category.objects.all() # получаем все категории # применили tags
    context = {
        'posts': posts,
        # 'cats': cats, # применили tags
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }

    # return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!</h1>")

def show_post(request, post_slug):
    # return HttpResponse(f"Отображене статьи с id = {post_id}")
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all() # применили tags

    if len(posts) == 0: # если нету постов -> выводим 404
        raise Http404

    context = {
        'posts': posts,
        # 'cats': cats, # применили tags
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html', context=context)

