# Generated by Django 4.2.2 on 2024-06-12 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_payments"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Payments",
        ),
    ]