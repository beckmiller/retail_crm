from django.contrib import admin
from .models import Product, Acceptance


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'category')
    list_editable = ('category', 'description')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)


@admin.register(Acceptance)
class AcceptanceAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier', 'price_in', 'price_out', 'quantity', 'entry_time', 'stock')
    list_filter = ('supplier', 'stock')
    search_fields = ('product__name', 'supplier__name')
    list_per_page = 20
    ordering = ('-entry_time',)
