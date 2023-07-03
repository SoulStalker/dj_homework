from django.contrib import admin

from .models import Stock, StockProduct


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price']

