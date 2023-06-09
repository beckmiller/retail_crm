from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    location = models.CharField(max_length=200, verbose_name="Местоположение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"


class Transaction(models.Model):
    stock = models.ForeignKey('stock.Stock', on_delete=models.CASCADE, verbose_name="Склад")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name="Товар")
    store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Магазин")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    date = models.DateField(auto_now_add=True, verbose_name="Дата транзакции")

    def __str__(self):
        return f"{self.product} - {self.stock} - {self.store}"

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
