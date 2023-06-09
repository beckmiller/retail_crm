# Generated by Django 4.2.2 on 2023-06-09 18:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_product_remove_transaction_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="acceptance",
            name="product",
        ),
        migrations.RemoveField(
            model_name="acceptance",
            name="stock",
        ),
        migrations.RemoveField(
            model_name="acceptance",
            name="supplier",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
        migrations.DeleteModel(
            name="Acceptance",
        ),
    ]
