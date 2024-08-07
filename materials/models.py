from django.db import models

from config import settings
from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """ Модель курса """

    title = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="course/",
        **NULLABLE,
        verbose_name="Превью курса",
        help_text="Загрузите изображение",
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса"
    )

    owner = models.ForeignKey(
        "users.User",
        verbose_name="Владеле курса",
        help_text="Укажите владельца",
        **NULLABLE,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """ Модель урока """

    title_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="Введите название курса",
        verbose_name="Название курса",
        related_name="lessons",
    )
    title_lesson = models.CharField(
        max_length=150,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Введите описание урока"
    )
    preview = models.ImageField(
        upload_to="lesson/",
        **NULLABLE,
        verbose_name="Превью урока",
        help_text="Загрузите изображение",
    )
    video_url = models.URLField(
        max_length=200,
        **NULLABLE,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
    )

    owner = models.ForeignKey(
        "users.User",
        verbose_name="Владелец урока",
        help_text="Укажите владельца",
        **NULLABLE,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title_lesson

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    """ Модель подписки """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    course = models.ForeignKey(
        "materials.Course",
        on_delete=models.CASCADE,
        related_name="Курс",
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def get_user_email(self):
        return self.user.email

    def __str__(self):
        return f"{self.user.email} подписан на {self.course.title}."

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        unique_together = ('user', 'course')