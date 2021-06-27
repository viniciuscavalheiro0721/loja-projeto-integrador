from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
import string, random

class Aboutus(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField(blank=True)
    textImg = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)