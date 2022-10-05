import random
import string
from email.policy import default
from unittest.util import _MAX_LENGTH

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, reverse_lazy
from tinymce.models import HTMLField

# def generateId():
#     length = 12

# while True:
#     artifact_id = ''.join(random.choices(string.ascii_uppercase, k=length))
#     if Artifacts.objects.filter(artifact_id=artifact_id).count() == 0:
#         break
# return artifact_idfrom django.core.urlresolvers import reverse


class Products(models.Model):
    description = models.CharField(max_length=200, default="", unique=False)
    active = models.IntegerField(max_length=1, default=0)
    sale_price = models.FloatField(max_length=10, default=0)
    created = models.DateTimeField(auto_now_add=True)
    dt_last_sale = models.DateTimeField(auto_now=True)
    markup_sale = models.FloatField(max_length=5, default=0)
    price_cost = models.FloatField(max_length=10, default=0)
    stock = models.FloatField(max_length=5, default=0)
    stock_min = models.FloatField(max_length=5, default=0)
    code_int = models.IntegerField(max_length=7, default=0)
    code_ean = models.CharField(max_length=14, unique=True)
