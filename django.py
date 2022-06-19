# 1. Django

# Виртуальное окружение (venv) -> Python 3..3 + Django 3.1.4

# localhost - 127.0.0.1

# python3 -V -> Python 3.9.13
# pip3 list
# cd PycharmProjects/python/django/djsite/
# sudo apt install python3.8-venv - устанавливаем venv
# python3 -m venv venv - устанавливаем venv окружение под названием venv
# source venv/bin/activate - запуск вертуального окружения
# pip install -U pip - обновление pip
# deactivate - выйти из вертуального окружения
# открываем проэкт в PyCharm -> (venv) sitarnet@sitarnet-Latitude-E7450:~/PycharmProjects/python/django/djsite$ 
# pip install django - устанавливаем движок
# pip list -> ...
# django-admin - все комманды django
# django-admin startproject <имя сайта>
# django-admin startproject coolsite
# cd coolsite
# python3 manage.py runserver - запуск сервера
# http://127.0.0.1:8000
# CTRL+C - остановка сервера
# python3 manage.py runserver 40000 - меняем порт
# http://127.0.0.1:4000
# python3 manage.py runserver 192.168.1.1:4000 - меняем ip


# 1. Django

# MTV - models, templates, views
# Создаём приложение (пакет). Оно должно быть максимально независимым от других приложений
# python manage.py startapp women

# 2. Django

# coolsite -> settings.py -> INSTALLED_APPS -> 'women.apps.WomenConfig' - регистрация пакета
# coolsite -> urls.py -> path('women/', index) -> импортируем маршрут
# coolsite -> Mark Directory as -> Sources root - для корректного импортирования
# women -> urls.py - создаём свои маршруты в пакете (если будем переносить пакет на другой сайт)

# 3. Django

# path('cats/<int:catsid>/', categories)
# str - любая не пустая строка, исключая символ /
# int - любое положительное, целое число включая 0
# slug - слаг, то есть, латиница ASCII таблицы, символы дефиса и подчёркивания
# uuid - цыфры, малые латинские ASCII, дефис
# path - любая не пустая строка, включая символ /
# re_path() - для использования регулярных выражений

# Обработка GET и POST запросов
# http://127.0.0.1:8000/?name=Gagarina&cat=music - GET запрос
# request.GET (POST)

# Обработка искючений при запросах к серверу
# coolsite -> settings.py -> DEBUG = False - режим откладки отключён
# coolsite -> settings.py -> ALLOWED_HOSTS = ['127.0.0.1']

# handler404 = pageNotFound -> coolsite/urls.py
# women/view.py -> pageNotFound(request, exception)

# Обработка исключений при запросах к серыеру
# hundler500 - ошибка сервера
# hundler403 - доступ запрещён
# hundler400 - невозможно обработать запрос

# Создание 301 и 302 редиректов
# 301 - страница перемещена на другой постоянный URL-адрес
# 302 - страница перемещена на другой временный URL-адрес

# import django.shortcuts
# django.shortcuts.redirect
# name='home' - используем имя для редиректа

