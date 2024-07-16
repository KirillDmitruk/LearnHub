# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем poetry
RUN pip install poetry

# Копируем зависимости в контейнер
COPY poetry.lock pyproject.toml /app/

# Копируем код приложения в контейнер
COPY . /app/
