# Generated by Django 4.2.2 on 2023-06-08 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stock",
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
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "location",
                    models.CharField(max_length=200, verbose_name="Местоположение"),
                ),
            ],
            options={
                "verbose_name": "Склад",
                "verbose_name_plural": "Склады",
            },
        ),
        migrations.CreateModel(
            name="StockBatch",
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
                ("quantity", models.IntegerField(default=0, verbose_name="Количество")),
                (
                    "batch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stock_batches",
                        to="products.batch",
                        verbose_name="Партия",
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stock_batches",
                        to="stock.stock",
                        verbose_name="Склад",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="stock",
            name="batches",
            field=models.ManyToManyField(
                through="stock.StockBatch", to="products.batch", verbose_name="Партии"
            ),
        ),
    ]