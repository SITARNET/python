# 1. Flask

# Flask - микрофреймворк для создания сайтов
# WSGI - интерпретатор Python для запуска приложения на Flask
# Apache -> WSGI -> Flask -> Представление (Представление N)
# WSGI (Web Server Gateway Interface) - стандарт взаимодействия между Python-программой на стороне
# сервера и самим веб-сервером.

# pip install Flask
# from flask import Flask

# app = Flask(__name__) - экземпляр класса Flask

# if __name__ == "__main__": - для запуска локального вервера
#   app.run(debug=True) - режим откладки

# 2. Flask

# render_template
# base.html - общий шаблон
# используем шаблонизатор
# Шаблонизатор Jinja2

# 3. Flask

# Что такое контекст приложения и контекст запроса, переменные g, current_app, request и session.
# Запрос -> Контекст приложения (g, current_app) необ. -> Контекст запроса (request, session) обязательно
# g - текущее соединения с базой данных (например), current_app - какое приложение
# request - содержит данные связанные с текущим запросом (включая текущий url)
# session - сохраняет славайрь данных в пределах сессии

