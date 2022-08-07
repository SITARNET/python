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


# 4. REST

# Сериализатор (Serializer) - для выполнения конвертирования произвольных объектов языка Python в формат JSON
# def encode() -> кодирует в JSON формат (объект в словарь, потом JSON строку)
# def decode() -> c JSON в упорядоченный словарь


# 5. REST

# create(self, validated_data) - для добавления (создания) записи данных
# update(self, instance, validated_data) - для изменения данных
# delete(self, instance) - для удаления данных


# 6. REST

# Класс ModelSerializer - упрощает текст программы при описании сериализатора связанного с моделями Django

# Классы представлений
# CreateAPIView - создание данных по POST-запросу
# ListAPIView - чтение списка данных по GET-запросу
# RetrieveAPIView - чтение конкретных данных (записи) по GET-запросу
# DestroyAPIView - удаление данных (записи) по DELETE-запросу
# UpdateAPIView - изменение записи по PUT- или PATCH-запросу
# ListCreateAPIView - для чтения (по GET-запросу) и создания списка данных (по POST-запросу)
# RetrieveUpdateAPIView - чтение и изменение отдельной записи (GET- и POST-запрос)
# RetrieveDestroyAPIView - чтение (GET-запрос) и удаление (DELETE-запрос) отдельной записи
# RetrieveUpdateDestroyAPIView - чтение, изменение и добавление отдельной записи (GET-, PUT-, PATCH-, DELETE-запросы)


# 7. REST

# Глобальные настройки Django REST Framework
# settings.py
# REST_FRAMEWORK = {
#   'DEFAULT_RENDERER_CLASSES': [
#       'rest_framework.renderers.JSONRenderer',
#       'rest_framework.renderers.BrowsableAPIRenderer' - коментируем - отключаем браузерное API (показывает сырые данные JSON)
#   ]
# }


# 8. REST

# https://www.django-rest-framework.org/api-guide/viewsets/
# ModelViewSet
# Какие методы -> раздел ViewSets Action

# Routers
# https://www.django-rest-framework.org/api-guide/routers/
# SimpleRouter
# DefaultRouter

# from rest_framework import routers
#
# router = routers.SimpleRouter() # оздаёт объект класса SimpleRouter()
# router.register(r'women', WomenViewSet) # регистрируем роутер
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)), # подключаем все маршруты которые связаны с ViewSet (../api/v1/women/)
# ]



# 9. REST

# Как использовать роутеры

# [<URLPattern '^women/$' [name='women-list']>,
# <URLPattern '^women\.(?P<format>[a-z0-9]+)/?$' [name='women-list']>,
# <URLPattern '^women/(?P<pk>[^/.]+)/$' [name='women-detail']>,
# <URLPattern '^women/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='women-detail']>,
# <URLPattern '^$' [name='api-root']>,
# <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>]

# /api/v1/women/            /api/v1/women/pk/         /api/v1/
# basename='men'
# если надо определить свой маршрут
# @action - декоратор

# Список категорий
# <URLPattern '^women/category/$' [name='women-category']>,
# <URLPattern '^women/category\.(?P<format>[a-z0-9]+)/?$' [name='women-category']>

# @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})

# http://127.0.0.1:8000/api/v1/women/category/ - список категорий

# @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

# http://127.0.0.1:8000/api/v1/women/1/category/ - одна категория


# 10. REST

# models.py -> user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
# from django.contrib.auth.models import User
# python manage.py makemigrations
# 1 -> default -> 1
# python manage.py migrate

# AllowAny - полный доступ
# IsAuthenticated - только для авторизованных пользователей
# IsAdminUser - только администраторов
# IsAuthenticatedOrReadOnly - только для авторизованых или всем, но для чтения

# https://www.django-rest-framework.org/api-guide/permissions/

# serializer.py -> class WomenSerialazer() -> user = serializers.HiddenField(default=serializers.CurrentUserDefault())

# Чтобы просматривать мог каждый, а удалять - администратор
# Custom permissions

# class BasePermission(metaclass=BasePermissionMetaclass):
#   def has_permission(self, request, view):
#       return True
#   def has_object_permission(self, request, view, obj):
#       return True

# women/permissions.py -> все классы с permissions

# Чтобы просматривать мог каждый, а изменять только автор статьи

# Можем назначать глобальные ограничения -> settings.py
# 'DEFAULT_PERMISSION_CLASSES': [
#       'rest_framework.permission.IsAuthenticated' - только авторизованым пользователям
#   ]

# 'DEFAULT_PERMISSION_CLASSES': [
#       'rest_framework.permission.AllowAny' - по умолчанию
#   ]


# 11. REST

# Session-based authentication - аунтефикация на основе сессий и cookie
# Token-based authentication - на основе токенов
# JSON Web Token (JWT) authentication - на основе JWT-токенов
# Django REST framework OAuth - через социальные сети

# https://www.django-rest-framework.org/api-guide/authentication/


# 12. REST

# Token-based authentication
# обычная аунтефикация токенами (библтотека Djoser)
# JWT-токены (библиотека Simple JWT)

# https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

# https://djoser.readthedocs.io/en/latest/

# pip install djoser
# settings.py -> INSTALLED_APPS -> rest_framework.authtoken -> djoser

# python manage.py migrate

# urls.py -> urlpatterns
# path('api/v1/auth/', include('djoser.urls')),
# re_path(r'^auth/', include('djoser.urls.authtoken')),

# settings.py -> REST_FRAMEWORK -> DEFAULT_AUTHENTICATION_CLASSES
# 'rest_framework.authentication.TokenAuthentication' - по токенам
# 'rest_framework.authentication.BasicAuthentication' - по сессиям (по умолчанию)
# 'rest_framework.authentication.SessionAuthentication' - по сессиям (по умолчанию)

# https://djoser.readthedocs.io/en/latest/base_endpoints.html

# User create
# POSTMAN -> http://127.0.0.1:8000/api/v1/auth/users/ -> POST -> Body -> form-data
# username -> seconduser, password -> SJKNdhcd1234, email -> seconduser@ukr.net

# Авторизация нового пользователя (seconduser)
# POSTMAN -> http://127.0.0.1:8000/auth/token/login/ -> POST -> Body -> form-data
# username -> seconduser, password -> SJKNdhcd1234

# Для каждого класса можно использовать авторизацию по сессиям или токенам
# authentication_classes = (TokenAuthentication, )


# 13. REST

# JSON Web Token (JWT)
# sdiufhsif84ry9w48fh948h9w uiefhfhf89f98h349hf4398hf98fhewef sdkuh98hd98hehd839d
# header                    payload                      signature
# {"alg":"HS256", "typ":"JWT"} {"userid":1,"exp":1000,"email":"user@ukr.net"} HMAC-SHA256(header.payload,SECRET_KEY)
# header=base64urlEncode(b'...')
# payload=base64urlEncode(b'...')
# signature=HMAC-SHA256(header.payload,SECRET_KEY)
# jwt_token = header.payload.signature

# JWT-authorization/authentication
# access_token = 5 мин.
# refresh_token = от 24 ч.


# 14. REST

# JWT-токены (библиотека Simple JWT)
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html

# pip install djangorestframework-simplejwt
# settings.py -> DEFAULT_AUTHENTICATION_CLASSES -> rest_framework_simplejwt.authentication.JWTAuthentication
# urls.py -> urlpatterns ->
# path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

# settings.py ->
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'UPDATE_LAST_LOGIN': False,
#
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,
#
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
#
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#     'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
#
#     'JTI_CLAIM': 'jti',
#
#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }

# https://jwt.io/