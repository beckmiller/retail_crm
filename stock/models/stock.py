from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    location = models.CharField(max_length=200, verbose_name="Местоположение")
    batches = models.ManyToManyField('products.Batch', through='StockBatch', verbose_name="Партии")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class StockBatch(models.Model):
    batch = models.ForeignKey('products.Batch', on_delete=models.CASCADE, verbose_name="Партия",
                              related_name='stock_batches')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name="Склад", related_name='stock_batches')
    quantity = models.IntegerField(default=0, verbose_name="Количество")

    def __str__(self):
        return f"{self.batch} - {self.stock}"
