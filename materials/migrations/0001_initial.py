# Generated by Django 4.2.2 on 2024-06-10 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название курса",
                        max_length=150,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="course/",
                        verbose_name="Превью курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание курса",
                        verbose_name="Описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title_lesson",
                    models.CharField(
                        help_text="Введите название урока",
                        max_length=150,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание урока",
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="lesson/",
                        verbose_name="Превью урока",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        blank=True,
                        help_text="Укажите ссылку на видео",
                        null=True,
                        verbose_name="Ссылка на видео",
                    ),
                ),
                (
                    "title_course",
                    models.ForeignKey(
                        help_text="Введите название курса",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]