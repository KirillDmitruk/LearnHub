# Generated by Django 4.2.2 on 2024-06-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загузите фото",
                null=True,
                upload_to="user/",
                verbose_name="avatar",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Укажите ваш город",
                max_length=100,
                null=True,
                verbose_name="city",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Введите ваш email",
                max_length=254,
                unique=True,
                verbose_name="email",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Введите ваш номер телефона",
                max_length=35,
                null=True,
                verbose_name="phone",
            ),
        ),
    ]
