from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
import string, random

class Collection(models.Model):
    #collection_id = models.CharField(max_length=30, unique=True, primary_key=True) #No de registro
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=50, default="", unique=True)
    description = RichTextField(blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default=0)

    def __str__(self):
        return self.name

    def __strid__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("collection:detail", kwargs={"slug": self.slug})

        