from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE, verbose_name="Поставщик")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Batch(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name="Товар")
    batch_number = models.CharField(max_length=50, verbose_name="Номер партии")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name="Время захода")

    def __str__(self):
        return f"{self.product.name} - Партия {self.batch_number}"

    class Meta:
        verbose_name = "Партия"
        verbose_name_plural = "Партии"
