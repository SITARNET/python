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

# 4. Django

# SQLite, MySQL, PortageSQL, Oracle...
# WSGI-приложение -> API интерфейс -> Django ORM -> Драйвер ORN -> SQLite....
# ORM (Object-Relation Mapping) - объектно-реляционное отображение
# sudo apt update
# sudo apt-cache search sqlite
# sudo apt install sqlite3
# sudo apt update
# sudo apt install sqlitebrowser

# coolsite -> women -> models.py
# id: integer, primary key
# title: Varchar
# content: Text
# photo: Image
# time_create: DataTime
# Time_update: DataTime
# is_published: Boolean

# djbook.ru/rel3.0/ref/models/fields.html
# Чтобы Django могло сохранять фото, надо настроить две константы: FileFoeld -> MEDIA_ROOT, MEDIA_URL
# coolsite -> settings.py -> MEDIA_ROOT = os.path.join(BASE_DIR, 'media') -> import os
# MEDIA_URL = '/media/'

# Это настраиваеться только в откладочном режиме (не на реальном сервере) -> DEBUG = True
# coolsite -> urls.py
# from django.conf.urls.static import static
# from coolsite import settings
# if settings.DEBUG:
#       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавляем файлы миграций в папку "migration" -> чтобы добавить структуру таблиц
# ../coolsite$ python manage.py makemigrations
# python -m pip install Pillow -> пакет для работы с фото
# women/migrations/0001_initial.py
# python manage.py sqlmigrate women 0001 -> посмотреть SQL-запрос для модели women под номером 0001
# python manage.py migrate -> запускаем миграцию (sql-запрос)


# 5. Django

# CRUD - Create, Read, Update, Delete
# ORM фркймворка Django

# python manage.py shell -> консоль фрймворка
# >>> form women.maodels import Women
# >>> Women(title='Анджелина Джоли', content='Биография Анджелины Джоли')
# >>> w1 = _
# >>> w1.save()
# >>> w1.id -> 1
# >>> w1.title -> Анджелина Джоли
# >>> w1.pk (=w1.id) -> 1
# >>> from django.db import connection
# >>> connection.queries - посмотреть SQL-запросы
# >>> w3 = Women()
# >>> w3.title = 'Джулия Робертс'
# >>> w3.content = 'Биография Джулии Робертс'
# >>> w3.save()
# Или используем другой метод
# >>> Women.objects
# >>> w4 = Women.objects.create(title='Ума Турман', content='Биография Умы Турман') - записываеться сразу в базу
# >>> w4
# >>> w4.title
# >>> w4.pk
# Можно без присвоения переменной
# >>> Women.objects.create(title='Кира Найтли', content='Биография Киры Найтли')
# >>> Women.objacts.all() - все текущие записи
# models.py -> def __str__(self): return self.title в классе Women
# >>> exit() - выходим из оболочки Django (перезапускаем)
# >>> python manage.py shell
# >>> from women.models import Women
# >>> Women.objects.all() -> <QuerySet [<Women: Анджелина Джоли>, <Women: Энн.... -> ограничение на 21 запись!
# >>> w = _ - присваеваем список
# >>> w[0] -> <Women: Анджелина Джоли>
# >>> w[0].title -> 'Анджелина Джоли'
# >>> len(w) -> 5
# >>> for wi in w: print(wi.title) -> Анджелина Джоли, Энн Хэтэуэй, Джулия Робертс, Ума Турман, Кира Найтли

# >>> Women.objects.filter(title='Энн Хэтэуэй') - выбока с помощью фильтра
# >>> Women.objects.filter(pk=2) -> <QuerySet [<Women: Энн Хэтэуэй>]>
# >>> Women.objacts.filter() => <имя_атрибута>__gte - сравнение больше или равно (>=)
# >>> Women.objacts.filter() => <имя_атрибута>__lte - сравнение меньше или равно (<=)
# >>> Women.objects.filter(pk__gte=2) -> <QuerySet [<Women: Энн Хэтэуэй>, <Women: Джулия Робертс>, <Women: Ума Турман>...

# >>> Women.objects.exclude(pk=2) => выбирает все записи, которые НЕ соответствуют критерию

# >>> Women.objects.get(pk=2) => выбериат если точно знаем что запись есть, иначе генерирует исключение

# >>> Women.obgects.filter(pk__lte=4).order_by('title') - сортировка
# >>> Women.objects.order_by('time_update')
# >>> Women.objects.order_by('-time_update') - обратная сортировка

# >>> wu = Women.objects.get(pk=2)
# >>> wu.tutle = 'Марго Робби' - присваеваем новое значение
# >>> wu.content = 'Биография Марго Робби' - присваеваем новое значение
# >>> wu.save() - сохраняем

# >>> wd = Women.objects.filter(pk__gte=4)
# >>> wd -> <QuerySet [<Women: Ума Турман>, <Women: Кира Найтли>]>
# >>> wd.detete() -> (2, {'women.Women': 2}) - удалили две записи

# http://djbook.ru/rel3.0/topics/db/queries.html


# 6. Django

# ~/PycharmProjects/python/django/djsite/coolsite$ python manage.py runserver
# http://127.0.0.1:8000/

# https://djbook.ru/rel3.0/topics/templates.html

# {% extends 'women/base.html' %} # наследование общего шаблона