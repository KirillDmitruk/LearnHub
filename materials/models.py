from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="course/",
        **NULLABLE,
        verbose_name="Превью курса",
        help_text="Загрузите изображение"
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Введите описание курса"
    )

    owner = models.ForeignKey("users.User", verbose_name="Владеле курса", help_text="Укажите владельца", **NULLABLE,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="Введите название курса",
        verbose_name="Название курса",
        related_name="lessons"
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
        help_text="Загрузите изображение"
    )
    video_url = models.URLField(
        max_length=200,
        **NULLABLE,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео"
    )

    owner = models.ForeignKey("users.User", verbose_name="Владелец урока", help_text="Укажите владельца", **NULLABLE,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return self.title_lesson

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
