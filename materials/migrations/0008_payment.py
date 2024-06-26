# Generated by Django 4.2.2 on 2024-06-24 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("materials", "0007_subscription"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                    "amount",
                    models.PositiveIntegerField(
                        help_text="Укажите сумму оплаты", verbose_name="Сумма оплаты"
                    ),
                ),
                (
                    "session_id",
                    models.CharField(
                        blank=True,
                        help_text="Укажите ID сессии",
                        max_length=255,
                        null=True,
                        verbose_name="id сессии",
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        help_text="Укажите ссылку на оплату",
                        max_length=400,
                        verbose_name="Ссылка на оплату",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="material_payment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата",
                "verbose_name_plural": "Оплаты",
            },
        ),
    ]
