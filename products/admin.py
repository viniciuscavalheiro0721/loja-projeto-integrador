from django.contrib import admin

from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("description", "sale_price", "markup_sale",
                    "price_cost", "stock", "stock_min", "code_int", "code_ean")
