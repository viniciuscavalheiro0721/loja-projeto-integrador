from django.db import models
from ckeditor.fields import RichTextField
import string

class Materials(models.Model):
    #material_id = models.CharField(max_length=30, unique=True, primary_key=True) #No de registro
    name = models.CharField(max_length=30, default="Desconhecido", unique=True)
    slug = models.SlugField(max_length=50, default="", unique=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("artifacts:detail", kwargs={"slug": self.slug})