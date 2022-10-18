

from django.db import models


class Products(models.Model):
    description = models.CharField(max_length=200, default="", unique=False)
    active = models.IntegerField(max_length=1, default=0)
    sale_price = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    dt_last_sale = models.DateTimeField(auto_now=True)
    markup_sale = models.DecimalField(max_length=5, default=0)
    price_cost = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    stock = models.FloatField(max_length=5, default=0)
    stock_min = models.FloatField(max_length=5, default=0)
    code_int = models.IntegerField(max_length=7, default=0)
    code_ean = models.CharField(max_length=14, unique=True)
