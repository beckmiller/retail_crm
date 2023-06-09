from django.contrib import admin
from .models import Stock


# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'get_acceptance_count')
    search_fields = ('name', 'location')
    list_per_page = 20
    ordering = ('name',)

    def get_acceptance_count(self, obj):
        return obj.acceptance.count()

    get_acceptance_count.short_description = 'Количество приемок'
