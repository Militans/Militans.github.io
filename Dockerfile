FROM python:3.9-slim

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование файла зависимостей и установка зависимостей
COPY requirements.txt ./
RUN pip install --no-cache-dir --default-timeout=400 -r requirements.txt

# Копирование всего проекта в контейнер
COPY . .

# Запуск сервера Django при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
