# 1. REST

# Django REST Framework (DRF)
# API - Application Programming Interface
# Phone -> https://site.com/api/v1/listpages/ -> сайт (сервер, API) -> JSON (сырые данные) -> Java на Phone -> HTML

# создание, чтение, изменение и удаление данных (CRUD)
# проверку корректности передаваемых данных от клиента и защиту от хакерских атак
# авторизацию и регистрацию пользователей
# права доступа к данным через API

# API-запрос->Маршрутизатор->Представление 1->Сериализаторы(Serializers)->БД
#                          ->Представление N

# Маршрутизатор отдаёт в обработку тому представлению которое связано с этим предсталением
# Представление - обработка запроса и отправка результата пользователю.
# Сериализаторы - формируют данные для ответа на API запросы, а также выполняют парсинг входной информации


# 2. REST

# Установка
# pip install django
# django-admin startproject drfsite (drfsite совпадает с доменом)
# cd drfsite
# python manage.py runserver
# python manage.py mirgate - создаються таблицы в базе данных
# settings.py -> LANGUAGE_CODE = 'ru'
# TIME_ZONE = 'Europe/Kiev'

# pyhon manage.py startapp women -> создаём приложение women
# settings.py -> INSTALLED_APPS = [..., 'women.apps.WomenConfig']
# women/admin.py -> from .models import Women
# admin.site.register(Women) - регистрация приложения

# women/models.py -> создаём таблицы бд (модели)
# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser - создаём суперпользователя (root->1234)
# http://127.0.0.1:8000/admin/

# установка REST
# pip install djangorestframework
# settings.py -> 'rest_framework' - регистрируем

# Определяем первое представление -> views.py
# women/serializers.py -> создаём сериализатор
# связываем маршрут с представлением -> urls.py
# http://127.0.0.1:8000/api/v1/womenlist/ -> выводит все записи в виде JSON


# 3. REST

# создание представления -> class WomenAPIView()
# создания сериализатора -> class WomenSerializer()
# маршрутизация -> urlpatterns = [...]

# Создание представления
# https://www.django-rest-framework.org/api-guide/generic-views/

# POSTMAN
# sudo apt update
# sudo apt upgrade
# sudo snap install postman

# def get() -> для get запроса
# def post() -> для post запроса

# POST -> Body -> JSON -> SEND


