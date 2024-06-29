from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_notification(course_id, message, email):
    send_mail(course_id, message, settings.EMAIL_HOST_USER, [email])
