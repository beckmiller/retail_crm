from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone = models.CharField("Телефон номер", max_length=15, null=False)
    contact_number = models.CharField(max_length=20, null=True, verbose_name="Контактный номер")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
