
from datetime import datetime
from email.policy import default

from django.contrib.auth.models import User
from django.db import models


class Pdv(models.Model):

    id_user_pdv = models.ForeignKey(User, on_delete=models.CASCADE)
    id_pdv = models.AutoField(primary_key=True)
    balance_pdv = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    active_pdv = models.BooleanField(default=1)
    created = models.DateTimeField(auto_now_add=True)


class forma_pgto(models.Model):

    payment_type = models.CharField(max_length=200, null=False, blank=False)


class cupom(models.Model):

    fecha_cupom = models.BooleanField(default=False)
    codigo_cupom = models.AutoField(primary_key=True)
    acrescimo = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False, default=0)
    dt_cupom = models.DateTimeField(auto_now=False, auto_now_add=False)
    preco_custo = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False, default=0)
    preco = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False, default=0)
    cancela_cupom = models.BooleanField(default=False)
    desconto = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False, default=0)
    id_pdv = models.ForeignKey('Pdv', on_delete=models.CASCADE)
    codigo_pgto = models.ForeignKey('forma_pgto', on_delete=models.CASCADE)


class item_cupom(models.Model):
    codigo_item = models.CharField(
        max_length=7, unique=True, primary_key=True)
    preco = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, blank=False)
    limite_cliente = models.IntegerField(null=True)
    qtd_item = models.FloatField(max_length=5, default=0)
    codigo_cupom = models.ForeignKey('cupom', on_delete=models.CASCADE)
    codigo_int = models.ForeignKey(
        'products.products', on_delete=models.CASCADE)
