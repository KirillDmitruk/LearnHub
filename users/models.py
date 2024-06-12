from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

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


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment", **NULLABLE)
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="paid_course",
        related_name="paid_course",
        **NULLABLE,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="paid_lesson",
        related_name="paid_lesson",
        **NULLABLE,
    )

    data = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата оплаты", **NULLABLE
    )
    payment_count = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=50, verbose_name="Метод оплаты")

    def __str__(self):
        return f"{self.user} - {self.paid_course if self.paid_course else self.paid_lesson}"

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"
