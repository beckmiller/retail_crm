from django.db import models


class Supplier(models.Model):
    name = models.CharField("Имя поставщика", max_length=20)
    phone = models.CharField("Телефон номер", max_length=15, null=False)
    email = models.EmailField("E-mail", max_length=20)
    address = models.CharField("Адрес", max_length=50)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self) -> str:
        return f"Поставщик {self.name} {self.phone}"
