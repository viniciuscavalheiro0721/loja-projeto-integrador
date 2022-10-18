
from django.contrib.auth.models import User
from django.db import models


class Pdv(models.Model):

    id_user_pdv = models.ForeignKey(User, on_delete=models.CASCADE)
    code_pdv = models.IntegerField(max_length=3, default=0)
    balance_pdv = models.FloatField(max_length=10, default=0)
    active_pdv = models.IntegerField(max_length=1, default=0)
    created = models.DateTimeField(auto_now_add=True)
