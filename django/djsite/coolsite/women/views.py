from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")

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