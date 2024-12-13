# Используем официальный образ Python
FROM python:3.10.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . /app/

# Указываем переменные окружения для Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=project.settings

# Открываем порт для сервера разработки
EXPOSE 8000

# Команда по умолчанию для запуска контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
