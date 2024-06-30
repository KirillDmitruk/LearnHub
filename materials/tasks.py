from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription, Course
from users.models import User


@shared_task
def send_mail_notification(course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return 'Курс не найден'

    subscription = Subscription.objects.filter(course=course)

    subject = f"Обновление курса {course.title}!"
    message = f"Курс {course.title} был обновлен."

    for sub in subscription:
        """получить email пользователя"""
        user_email = sub.user.email
        if subscription.filter(user=sub.user.pk).exists():
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])
        else:
            print("Подписка не оформлена.")
