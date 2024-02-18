FROM python:3.10

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# Для запуска введите две команды:
# docker build . --tag fastapi_app
# docker run -p 80:80 fastapi_app

# Или одной командой
# docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app

# КОММЕНТАРИЙ НИЖЕ ТОЛЬКО ДЛЯ DOCKER COMPOSE. РАСКОММЕНТИРУЙТЕ КОД, ЕСЛИ ВЫ ИСПОЛЬЗУЕТЕ ТОЛЬКО DOCKERFILE
# Предоставляет доступ контейнеру для запуска bash скрипта, если это необходимо
# Запускать bash скрипты без доступа к ним на ОС Linux невозможно. На Windows - возможно,
# но так как контейнеры работают на Linux, приходится давать доступ независимо от вашей ОС.
# RUN chmod a+x /booking/docker/*.sh

# КОММЕНТАРИЙ НИЖЕ ТОЛЬКО ДЛЯ DOCKER COMPOSE. РАСКОММЕНТИРУЙТЕ КОД, ЕСЛИ ВЫ ИСПОЛЬЗУЕТЕ ТОЛЬКО DOCKERFILE
# Эта команда выведена в bash скрипт
# RUN alembic upgrade head

# КОММЕНТАРИЙ НИЖЕ ТОЛЬКО ДЛЯ DOCKER COMPOSE. РАСКОММЕНТИРУЙТЕ КОД, ЕСЛИ ВЫ ИСПОЛЬЗУЕТЕ ТОЛЬКО DOCKERFILE
# Эта команда также выведена в bash скрипт