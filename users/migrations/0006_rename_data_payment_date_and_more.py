# Generated by Django 4.2.2 on 2024-06-25 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_payment_delete_payments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="data",
            new_name="date",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="payment_count",
        ),
    ]
