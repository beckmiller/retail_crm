# Generated by Django 4.2.2 on 2023-06-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_remove_acceptance_product_remove_acceptance_stock_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="date",
            field=models.DateField(
                auto_now_add=True, null=True, verbose_name="Дата транзакции"
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="quantity",
            field=models.PositiveIntegerField(null=True, verbose_name="Количество"),
        ),
    ]