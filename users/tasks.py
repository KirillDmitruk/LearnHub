from datetime import timedelta

from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from users.models import User


@shared_task
def block_users():
    """ Блокировка неактивных пользователей """

    now = timezone.now()
    month_ago = now - relativedelta(months=1)
    qs = User.objects.filter(
        is_active=True,
        last_login__lte=month_ago
    )
    qs.update(is_active=False)
    print(f"Пользователь заблокирован.")