from django.core.management import BaseCommand
from materials.models import Course


class Command(BaseCommand):
    """Команда создания нового пользователя."""

    def handle(self, *args, **options):
        user_course_title = input("Введите название курса: ")
        if Course.objects.filter(title=user_course_title).exists():
            print("Курс с таким названием уже существует.")
        else:
            course_description = input("Введите описание курса: ")
            course = Course.objects.create(title=user_course_title, description=course_description)

            course.save()
            print(f"Курс {user_course_title} успешно создан.")