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


class Payment(models.Model):

    METHODS = (
        ("CASH", "Наличные"),
        ("TRANSFER", "Перевод")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_payment", **NULLABLE)

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

    payment_date = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name="Дата оплаты")
    payment_method = models.CharField(max_length=50, choices=METHODS, default="CASH", verbose_name="Метод оплаты")
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты", help_text="Укажите сумму оплаты")

    session_id = models.CharField(max_length=255, **NULLABLE, verbose_name="id сессии", help_text="Укажите ID сессии")
    link = models.URLField(max_length=400, verbose_name="Ссылка на оплату", help_text="Укажите ссылку на оплату", **NULLABLE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"
