import random
import string
from email.policy import default
from unittest.util import _MAX_LENGTH

from ckeditor.fields import RichTextField
from django.contrib import admin
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


class Pdv(models.Model):

    id_user_pdv = models.ForeignKey(User, on_delete=models.CASCADE)
    code_pdv = models.IntegerField(max_length=3, default=0)
    balance_pdv = models.FloatField(max_length=10, default=0)
    active_pdv = models.IntegerField(max_length=1, default=0)
    created = models.DateTimeField(auto_now_add=True)
