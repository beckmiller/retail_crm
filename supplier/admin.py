from django.contrib import admin
from .models import Supplier


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'contact_number')
    search_fields = ('name', 'address', 'phone', 'contact_number')
    list_per_page = 20
