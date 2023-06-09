from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Store, Transaction
from django.db import models


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    list_per_page = 20


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'stock', 'store', 'quantity', 'date')
    list_filter = ('stock', 'store')
    search_fields = ('product__name', 'stock__name', 'store__name')
    list_per_page = 20
    ordering = ('-date',)

    def save_model(self, request, obj, form, change):
        # Проверка доступного количества товара на складе
        if obj.stock:
            available_quantity = obj.stock.acceptance.filter(product=obj.product).aggregate(models.Sum('quantity'))[
                                     'quantity__sum'] or 0
            if obj.quantity > available_quantity:
                messages.error(request, 'Недостаточное количество товара на складе. Транзакция не сохранена.')
                return

        # Сохранение модели транзакции
        super().save_model(request, obj, form, change)

        # Обновление количества товара на складе
        if obj.stock:
            obj.stock.acceptance.filter(product=obj.product).update(quantity=models.F('quantity') - obj.quantity)

        # Обновление количества товара в магазине
        if obj.store:
            obj.store.transaction_set.filter(product=obj.product).update(quantity=models.F('quantity') + obj.quantity)
