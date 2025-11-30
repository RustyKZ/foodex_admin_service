# 1. Базовый образ Python
FROM python:3.11-slim

# 2. Рабочая директория внутри контейнера
WORKDIR /app

# 3. Копируем зависимости
COPY requirements.txt .

# 4. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь код проекта
COPY . .

# 6. Применяем переменные окружения (опционально)
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=foodex_admin.settings

# 7. Применяем миграции при старте и запускаем dev сервер
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
