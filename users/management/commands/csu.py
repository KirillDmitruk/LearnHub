import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда создания суперпользователя"""
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email=os.getenv('ADMIN_EMAIL'),
            first_name="Admin",
            last_name="Admin",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password(os.getenv('ADMIN_PASSWORD'))
        user.save()
