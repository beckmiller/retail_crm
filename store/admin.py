from django.contrib import admin

from products.models import Acceptance
from .models import Store, Transaction


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
    raw_id_fields = ('stock',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product':
            # Отображение всех партий товара в выборе
            kwargs['queryset'] = Acceptance.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
