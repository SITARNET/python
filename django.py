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


# 7. Django

# CSS, JavaScript
# coolsite/static -> общая папка для реального сервера
# coolsite/coolsite/static -> не стандартный путь
# coolsite/women/static -> не стандартный путь

# python manage.py collectstatic -> берутся все файлы из не стандартных путей и перемещаються в coolsite/static

# В пакете кофигураций надо определить (coolsite/settings.py):
# STATIC_URL - префикс URL-адреса для статических файлов
# STATIC_ROOT - путь к общей статической папке, исп. реальным сервером
# STATICFILES_DIRS - список нестандартных путей к статическим файлам, исп. для сбора и для режима откладки

# coolsite/women/static/women -> пространство имён
# coolsite/women/static/women/css
# coolsite/women/static/women/js
# coolsite/women/static/women/images

# {% load static %} - служит для подключения статических файлов
# https://djbook.ru/rel3.0/ref/templates/builtins.html#ref-templates-builtins-filters - фильтры


# 8. Django

# {% имя_тега %}  {{ имя_переменной }}  {{ value|имя_фильтра }}
# <a href="#">...</a>
# {% url'<URL-адрес или имя маршрута>'[параметры ссылки] %}


# 9. Django

# Нормализация данных

# ForeignKey - для связей Many to One (поля отношений)
# ManyToManyField - для связей Many to Many (многие к многим)
# OneToOneField - для связей One to One (один к одному)

# ForeignKey(<ссылка на первичную модель>, on_delete=<ограничения при удалении>)

# models.CASCADE - при удалении записи из первичной модели (таблица Category) происходит удаление всех записей
# из вторичной модели (Women), связанных с удаляемой категорией

# models.PROTECT - запрет удаление записи из первичной модели, если она используется во вторичной (выдаёт исключение)

# models.SET_NULL - при удалении записи первичной модели устанавливает значение foreign key в NULL у соответствующих
# записей вторичной модели

# models.SET_DEFAULT - то же самое, что и SET_NULL, только вместо NULL устанавливает значение по умолчанию, каторое
# должно быть определено через класс ForeignKey

# models.SET() - то же самое, только устанавливает пользовательское значение

# models.DO_NOTHING - удаление записи в первичной модели не вызывает никаких действий у вторичных моделей

# djbook.ru/rel3.0/topics/db/models.html#relationships

# python manage.py makemagration -> python manage.py migrate - создали таблицы
# python manage.py shell
# from women.models import *
# Category.objects.create(name='Актрисы')
# Category.objects.create(name='Певицы')
# w_list = Women.objects.all()
# w_list.update(cat_id=1)


# 10. Django

# setting.py -> LANGUAGE_CODE = 'ru'
# 127.0.0.1:8000/admin/

# создаём администратора
# ...djsite/coolsite -> python mange.py createsuperuser

# Регистрируем наше приложение Women
# ...coolsite/women/admin.py -> from .midels import * -> admin.site.register(Women)

# используем вложенный класс для настройки админ-панели -> class Meta в models.py
# apps.py -> verbose_name = 'Женщины мира' # если settings.py -> INSTALLED_APPS -> women.apps.WomenConfig (а не women)
# Добавляем поля ->admin.py

# list_display = ('',...) - список полей которые мы хотим видеть
# list_display_links = ('',...) - список полей на которые мы можем кликнуть
# search_fields = ('',...) - по каким полям можно производить поиск
# list_editable = ('',) - поле будет редактируемым
# list_filter = ('',...) - поля по которым сможем фильтровать список полей
# admin.site.register(Women, WomenAdmin) # регистрируем класс

# Переводим названия title, time create, photo, is published
# mooels.py -> в class Women -> добавляем к каждому полю verbose_name='...'

# Регистрируем Category

# Вносим в таблицы базы данных мета описания
# Создаём файл миграции
# ../coolsite -> python manage.py makemigrations -> создаётся файл
# python manage.py migrate -> применяем все миграции для базы данных


# 11. Django

# Убираем дублирование с помощью пользовательских тегов в models.py
# simple tags - простые теги
# inclusion tags - включающие теги, формирует свой шаблон и возвращает html

# https://djbook.ru/rel3.0/howto/custom-template-tags.html

# 12. Django

# views.py -> show_post()
# get_object_or_404(Women, pk=post_id) -> если в таблице Women не находит pk, то 404
# women/post.html
# models.py -> slug - добавим поле SlugField -> в class Women и в Category
# удаляем старые миграции, из cat удаляем null=True, удаляем базу db.sqlite3
# python manage.py makemigrations -> создаём миграцию
# python manage.py migrate -> применяем миграцию

# admin.py -> class CategoryAdmin() -> prepopulated_fields = {"slug": ("name",)} -> автоматом заполняем поле slug
# admin.py -> class WomenAdmin() -> prepopulated_fields = {"slug": ("title",)} -> автоматом заполняем поле slug

# urls.py -> path('post/<slug:post_slug>/', show_post, name='post')
# views.py -> def show_post(request, post_slug):
#               post = get_object_or_404(Women, slug=post_slug)
# models.py -> def get_absolute_url(self):
#               return reverse('post', kwargs={'post_slug': self.slug})


# 13. Django

# <form>...</form>
# class AddPostForm(forms.Form):
# djbook.ru/rel3.0/ref/forms/fields.html - классы встроенных полей
# addpage.html -> <form action="{% url 'add_page' %}" method="post">
#     {% csrf_token %} # защита формы от csrf аттак
#     {{ form.as_p }} # отображает поля формы через тег <p>
#     <button type="submit">Добавить</button>
# </form>

# чтобы форма отобразилась второй раз с заполнеными полями
# def addpage(request):
#   if request.method == 'POST':
#       form = AddPostForm(request.POST)
#       if form.is_valid():
#           print(form.cleaned_data)
#   else:
#       form = AddPostForm()

#  return...

# label="Заголовок" - перевод
# widget=forms.Textarea(attrs={'cols': 60, 'rows': 10})
# required=False - не обязательное поле
# empty_label="Категория не выбрана" - вместо -----
# initial=True - будет делать checkbox отмеченым

# for="{{ form.title.id_for_label }}" - атоматический индефикатор поля

#     <p><label class="form-label" for="{{ form.title.id_for_label }}">{{ form.title.label }}: </label>{{ form.title }}</p>
#     <div class="form-error">{{ form.title.errors }}</div>
#     <p><label class="form-label" for="{{ form.slug.id_for_label }}">{{ form.slug.label }}: </label>{{ form.slug }}</p>
#     <div class="form-error">{{ form.slug.errors }}</div>
#     <p><label class="form-label" for="{{ form.content.id_for_label }}">{{ form.content.label }}: </label>{{ form.content }}</p>
#     <div class="form-error">{{ form.content.errors }}</div>
#     <p><label class="form-label" for="{{ form.is_published.id_for_label }}">{{ form.is_published.label }}: </label>{{ form.is_published }}</p>
#     <div class="form-error">{{ form.is_published.errors }}</div>
#     <p><label class="form-label" for="{{ form.cat.id_for_label }}">{{ form.cat.label }}: </label>{{ form.cat }}</p>
#     <div class="form-error">{{ form.cat.errors }}</div>

# чтобы строчки не повторялись, выведем с помощью цикла for

# если хотим применить к каждому полю свой класс стилей
# widget=forms.TextInput(attrs={'class': 'form-input'}) - в файле forms.py

# для сохраниния в базу
# в views.py
# if form.is_valid():
#   try:
#       Women.objects.create(**form.cleaned_data)
#       return redirect('home')
#   except:
#       form.add_error(None, 'Ошибка добавления поста')

# в addpage.py перед циклом
# <div class="form-error">{{ form.non_field_errors }}</div>


# 14. Django

# Связываем форму с мделью, убираем дублирование кода
# class Meta
# рекомендуется перечислять список полей fields = ['', ...]

# прописываем свои стили для title, content
# widgets = {'title': forms.TextInput(attrs={'class': 'form-input'})} - class="form-input"

# категория не выбрана - ------
# для этого напишем конструктор
# def __init__(self, *args, **kwargs):
#   super().__init__(*args, **kwargs)
#   self.fields['cat'].empty_label = "Категория не выбрана"

# form.save() # все данные которые будут переданы от формы, будут автоматически занесены в базу данных
# try и exept удаляем, django сама будет проверять на ошибки

# делаем загрузку фото
# добовляем поле 'photo' -> forms.py
# request.FILES - передаём список файлов -> views.py
# в addpage.html -> <form.... enctype="multipart/form-data">

# валидация - проверка корректности полей
# выполняеться за счёт class Women -> models.py
# в SQLite max_length не выполняеться!!!

# Свой собственный валидатор. Если длина больше 200 символов, то ошибка
# is_valid() | save() -> Стандартные валидаторы -> Пользовательские валидаторы

# forms.py -> def clean_title(self): # clean_+название поля для которого пишем валидатор
# ValidationError импортируем


# 15. Django

# CBV - Class-Based Views
# djbook.ru/rel1.9/ref/class-based-views/index.html

# вместо функци index создадим класс представлений
# ListView - список чего либо
# <имя приложения>/<имя модели>_list.html
# women/women_list.html - стандартный путь к шаблону
# template_name = 'women/index.html' - прописываем свой путь к шаблону
# в urls.py -> path('', WomenHome.as_view(), name='home')
# заголовок -> Главная страница -> extra_content = {'title': 'Главная страница'} - для статических данных
# для динамических -> def get_context_data()

# отображение статей отмеченые для публикации

# Для отображения списка категорий
# allow_empty = False # 404 если нету такой категории

# DateilView - для отображения поста

# CreateView - для добавления


# 16. Django

# Методы сортировки
# djbook.ru/rel3.0/ref/models/querysets.html
# python manage.py shell
# from women.models import *
# Women.objects.all() - все записи
# Women.objects.all()[:5] - первые 5 записей
# from django.db import connction
# connection.queries - показывает sql-запросы
# Women.objects.all()[3:8] - с 3 по 8 (8 не вкл.)
# Women.objects.order_by('pk') - сортировка по полю pk (id)
# Women.objects.order_by('-pk') - в обратном порядке
# Women.objects.all().reverse() - в обратном порядке

# Метод filter() - список записей по атрибуту
# Women.objects.filter(pk__lte=2) - pk <= 2
# Women.objects.get(pk=2) - выбор одной записи

# Обработка связанных таблиц
# w = Women.objects.get(pk=1)
# w.title..., w.is_published - значения полей записи таблицы women;
# w.pk, w.id - идентификаторы записи (первичный ключ);
# w.cat_id - идентификатор рубрики (внешний ключ);
# w.cat - объект класса Category, хранящий данные записи с id = cat_id.

# Запросы с использованием первичной модели (_set)
# w.cat.name -> Актрисы
# c = Category.objects.get(pk=1)
# c -> <Category: Актрисы>
# c.women_set.all() - выводит все записи с категории Актрисы
# есл хотим использовать, например: get_posts, то в models.py -> cat = models.ForeignKey(..., related_name='get_posts')

# Фильтры полей Fields lookups
# <имя атрибута>__gte - сравнение больше или равно (>=);
# <имя атрибута>__lte - сравнение меньше или равно (<=);

# Women.ojects.filter(title__contains='ли') -> ищет в title слог 'ли'
# Women.ojects.filter(title__icontains='ли') -> ищет в title слог 'ли' без учёта регистра с латинскими символами
# Women.objects.filter(pk__in=[2,5,11,12]) -> выбираем записи по перечисленным значениям
# Women.objects.filter(pk__in=[2,5,11,12], is_published=True) -> два условия
# Women.objects.filter(cat__in=[1,2]) -> выведет из Актрис и Певиц

# Класс Q: И ИЛИ НЕ
# & - логическое И (приоритет 2)
# | - логическое ИЛИ (приоритет 3)
# ~ - логическое НЕ (приоритет 1)
# from django.db.models import Q
# Women.objects.filter(Q(pk__lt=5) | Q(cat_id=2)) -> pk>=5 или cat_id=2
# Women.objects.filter(~Q(pk__lt=5) | Q(cat_id=2)) -> pk<=5 или cat_id=2

# Быстрое получение записи из таблиц
# Women.objects.first() -> первая запись
# Women.objects.last() -> последняя запись

# Получение записи по дате
# Women.objects.latest('time_update') -> самая поздняя запись
# Women.objects.earliest('time_update') -> самая последняя запись

# Выбор записи относительно текущей (по дате)
# w = Women.objects.get(pk=7)
# w
# w.get_previous_by_time_update() -> предыдущая запись
# w.get_next_by_time_update() -> следующая запись

# exists() - проверка существования записи
# count() - получение числа записей
# добавим новую категорию -> Category.objects.create(name='Спортсменки', slug='sportsmenky')
# c3 = Category.objects.get(pk=3)
# c3
# c3.women_set.exists() -> False (нету ни одной записи связанной)
# c2.women_set.exists() -> True

# # c2.women_set.exists() -> 7 - колличество записей

# Обращение к полю первичной модели через атрибут
# Women.objects.filter(cat__slug='Актрисы')
# <имя первичной модели>__<название поля первичной модели>
# Women.objects.filter(cat__name='Певицы')
# Women.objects.filter(cat__name__contains='цы')
# Category.objects.filter(women__title__conteins='ли') -> выбираем все категории которые связаны в вторичной модели Women
# Category.objects.filter(women__title__conteins='ли').distinct() -> вычираем все уникальные категории

# Фукции агрегации
# Все функции агригации надо импортировать
# from django.db.models import *
# Women.objects.agreegate(Min('cat_id')) -> {'cat_id__min': 1}
# Women.objects.agreegate(Min('cat_id'), Max('cat_id')) -> {'cat_id__min': 1, 'cat_id__max': 2}
# другие ключи
# Women.objects.agreegate(cat_min=Min('cat_id'), cat_max=Max('cat_id')) -> {'cat_min': 1, 'cat_max': 2}
# стандартные матиматические операции
# Women.objects.aggrigate(res=Sum('cat_id') - Count('cat_id')) -> {'res': 7} - вычитание
# Women.objects.aggrigate(res=Avg('cat_id')) -> {'res': 1.5} - среднее арифметическое
# Women.objects.filter(pk__gt=4).aggregate(res=Avg('cat_id')) -> используем фильтр pk>=4

# Выбор записей из конкретных её полей
# Women.objects.value('title', 'cat_id').get(pk=1) -> {'title': 'Анджелина Джоли', 'cat_id': 1} - этот запрос работает быстрее
# Women.objects.value('title', 'cat__name').get(pk=1) -> {'title': 'Анджелина Джоли', 'cat__name': 'Актрисы'}
# w = Women.objects.value('title', 'cat_name')
# for p in w:
#   print(p['title'], p['cat__name']) -> Ариана Гранде Пивицы, Анастасия Эшли Певицы.....

# Групировка записей (метод annotate)
# Women.objects.value('cat_id').annotate(Count('id')) -> [{'cat_id': 1, 'id_count': 7}, {'cat_id': 2, 'id_count': 7}]
# Women.objects.annotate(Count('cat'))
# c = Women.objects.annotete(Count('women'))
# c -> [<Category: Актрисы>, <Category: Певицы>, <Category: Спортсменки>]
# с[0].women__count -> 7
# c[1].women__count -> 7
# c = Women.objects.annotete(total=Count('women'))
# c[0].total -> 7
# len(c) -> 3
# c = Women.objects.annotete(total=Count('women')).filter(total__gt=0)
# c -> [<Category: Актрисы>, <Category: Певицы>]

# Класс F
# from django.db.models import F
# Women.objects.filter(pk__gt=F('cat_id')) -> pk>cat_id - все записи кроме первой
# Допустим. Для увеличение значения при просмотре таблицы
# Women.objects.filter(slug='bejonce').update(views=F('views')+1)
# Или
# w = Women.objects.get(pk=1)
# w -> Women: Анджелина Джоли
# w.view = F('view')+1
# w.save()

# Вычисления на стороне СУБД
# from django.db.models.functions import Length
# ps = Women.objects.annotite(len=Length('title'))
# ps
# for item in ps:
#   print(item.title, item.len) -> Анджелина Джоли 15 Дженифер Лоуренс 17....

# raw SQL запросы - запросы в чистом виде
# Manager.raw(<SQL-запрос>)
# Women.objects.raw('SELECT * FROM women_women') -> <RawQuerySet: SELECT * FROM women_women>
# w = _
# for p in w:
#  print(p.pk, p.title) -> 1 Анджелина Джоли 2 Дженнифер Лоуренс......

# Передача параметров в запрос
# slug = 'Shakira' - переменная
# Women.objects.raw("SELECT id, title FROM women_women WHERE slug='%s'", [slug]) -> безопасная вставка переменной

