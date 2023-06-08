# Generated by Django 4.2.2 on 2023-06-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("supplier", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supplier",
            name="email",
        ),
        migrations.AddField(
            model_name="supplier",
            name="contact_number",
            field=models.CharField(
                max_length=20, null=True, verbose_name="Контактный номер"
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="address",
            field=models.CharField(max_length=200, verbose_name="Адрес"),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
    ]
