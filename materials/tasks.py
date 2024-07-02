from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription, Course


@shared_task
def send_mail_notification(course_id):
    course = Course.objects.get(id=course_id)
    subscription = Subscription.objects.filter(course=course)

    subject = f"Обновление курса {course.title}!"
    message = f"Курс {course.title} был обновлен."

    email_list = subscription.values_list('user__email', flat=True)
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email_list])
