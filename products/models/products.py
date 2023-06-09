from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    category = models.CharField(max_length=100, verbose_name="Категория продукта", null=True)
    description = models.TextField(verbose_name="Описание", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Acceptance(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name="Товар")
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE, verbose_name="Поставщик", null=True)
    price_in = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена захода", null=True)
    price_out = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена продажи", null=True)
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name="Время захода")
    stock = models.ForeignKey('stock.Stock', on_delete=models.CASCADE,
                              null=True,
                              related_name='acceptance', verbose_name='Склад')

    def __str__(self):
        return f"{self.product.name} - Приемка {self.id}"

    class Meta:
        verbose_name = "Приемка"
        verbose_name_plural = "Приемки"
