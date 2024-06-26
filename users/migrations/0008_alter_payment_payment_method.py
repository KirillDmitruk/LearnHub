# Generated by Django 4.2.2 on 2024-06-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_rename_date_payment_payment_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[("CASH", "Наличные"), ("TRANSFER", "Перевод")],
                default="CASH",
                max_length=50,
                verbose_name="Метод оплаты",
            ),
        ),
    ]
