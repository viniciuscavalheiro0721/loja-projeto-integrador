from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import string, random

# def generateId():
#     length = 12

    # while True:
    #     artifact_id = ''.join(random.choices(string.ascii_uppercase, k=length))
    #     if Artifacts.objects.filter(artifact_id=artifact_id).count() == 0:
    #         break
    # return artifact_id

class Artifacts(models.Model):
    #artifact_id = models.CharField(max_length=30, default="", unique=True, primary_key=True) #No de registro
    name = models.CharField(max_length=50, default="", unique=False)
    slug = models.SlugField(max_length=50, default="", unique=True)
    description = models.CharField(max_length=200, default="", unique=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50, default="Desconhecido", unique=False)
    about = models.CharField(max_length=60, default="Desconhecido", unique=False)
    usage = models.CharField(max_length=60, default="Desconhecido", unique=False)
    style = models.CharField(max_length=30, default="Desconhecido", unique=False)
    culture = models.CharField(max_length=30, default="Desconhecida", unique=False)
    ethnicity = models.CharField(max_length=30, default="Desconhecida", unique=False)
    fabrication_date = models.CharField(max_length=12, default="Desconhecido", unique=False)
    heritage_id = models.CharField(max_length=30, default="", unique=True) #No de livro tombo
    aditional_numbers = models.IntegerField(default="", unique=False)
    
    collection = models.ForeignKey('collection.collection', default="", related_name='collection', on_delete=models.CASCADE)
    material = models.ForeignKey('materials.materials', default="",related_name='material', on_delete=models.CASCADE)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default='')

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("artifacts:detail", kwargs={"slug": self.slug})
    