from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def block_users():
    """Блокировка неактивных пользователей"""
    users = User.objects.exclude(last_login__isnull=True)
    now = timezone.now()
    for user in users:
        if now - user.last_login > timedelta(days=31):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} заблокирован.")
