from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):
    """Команда создания оплаты"""

    def handle(self, *args, **options):
        course_id = None
        lesson_id = None

        user_id = input("Введите id пользователя: ")
        if not User.objects.filter(id=user_id).exists():
            print("Пользователь с таким id не найден.")

        payment_count = int(
            input("Введите сумму оплаты одним числом без знаков препинания: ")
        )
        if payment_count < 0:
            print("Сумма оплаты не может быть отрицательной.")

        payment_method = input(
            "Выберите метод оплаты:\n1. Оплата картой\n2. Оплата наличными\n"
        )
        if payment_method not in ["1", "2"]:
            print("Неверный метод оплаты.")
        if payment_method == "1":
            payment_method = "Оплата картой"
        else:
            payment_method = "Оплата наличными"

        is_course_or_lesson = input(
            "Выберите что оплачиваемый объект:\n1. Курс\n2. Урок\n"
        )

        if is_course_or_lesson not in ["1", "2"]:
            print("Неверный объект оплаты.")
        if is_course_or_lesson == "1":
            course_id = int(input("Введите id курса: "))
            if not Course.objects.filter(id=course_id).exists():
                print("Курс с таким id не найден.")
        elif is_course_or_lesson == "2":
            lesson_id = int(input("Введите id урока: "))
            if not Lesson.objects.filter(id=lesson_id).exists():
                print("Урок с таким id не найден.")

        if course_id is not None:
            payment = Payments.objects.create(
                user=User(id=user_id),
                paid_course=Course(id=course_id),
                payment_count=payment_count,
                payment_method=payment_method,
            )
            print("Оплата успешно создана.")
            payment.save()
        elif lesson_id is not None:
            payment = Payments.objects.create(
                user=User(id=user_id),
                paid_lesson=Lesson(id=lesson_id),
                payment_count=payment_count,
                payment_method=payment_method,
            )
            print("Оплата успешно создана.")
            payment.save()
