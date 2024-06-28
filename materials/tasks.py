from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_notification(email):
    send_mail("Обновление курса!", "Тело письма", settings.EMAIL_HOST_USER, [email])
