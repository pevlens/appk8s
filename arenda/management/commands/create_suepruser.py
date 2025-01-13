from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command
import sys

class Command(BaseCommand):
    help = 'Автоматическое создание суперпользователя'

    def handle(self, *args, **kwargs):
        # Определите параметры для суперпользователя
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin'

        # Проверяем, существует ли уже суперпользователь с таким именем
        if not User.objects.filter(username=username).exists():
            # Создаем суперпользователя
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Суперпользователь {username} успешно создан!'))
        else:
            self.stdout.write(self.style.WARNING(f'Пользователь с именем {username} уже существует!'))
