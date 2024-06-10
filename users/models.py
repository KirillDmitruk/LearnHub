from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="email", help_text="Введите ваш email"
    )
    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="phone",
        help_text="Введите ваш номер телефона",
    )
    avatar = models.ImageField(
        upload_to="user/", **NULLABLE, verbose_name="avatar", help_text="Загузите фото"
    )
    city = models.CharField(
        max_length=100, **NULLABLE, verbose_name="city", help_text="Укажите ваш город"
    )
    token = models.CharField(max_length=100, **NULLABLE, verbose_name="token")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
