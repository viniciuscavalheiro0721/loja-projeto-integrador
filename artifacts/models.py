from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
import string, random
from django.urls import reverse_lazy

# def generateId():
#     length = 12

    # while True:
    #     artifact_id = ''.join(random.choices(string.ascii_uppercase, k=length))
    #     if Artifacts.objects.filter(artifact_id=artifact_id).count() == 0:
    #         break
    # return artifact_idfrom django.core.urlresolvers import reverse

class Artifacts(models.Model):
    #artifact_id = models.CharField(max_length=30, default="", unique=True, primary_key=True) #No de registro
    name = models.CharField(max_length=50, default="", unique=False)
    slug = models.SlugField(max_length=50, default="", unique=True)
    description = models.CharField(max_length=200, default="", unique=False)
    author = models.CharField(max_length=50, default="Desconhecido", unique=False)
    about = RichTextField(blank=True)
    usage = models.CharField(max_length=60, default="Desconhecido", unique=False)
    style = models.CharField(max_length=30, default="Desconhecido", unique=False)
    culture = models.CharField(max_length=30, default="Desconhecida", unique=False)
    ethnicity = models.CharField(max_length=30, default="Desconhecida", unique=False)
    age = models.CharField(max_length=12, default="Desconhecido", unique=False)
    inscriptions = models.CharField(max_length=200, default="Desconhecido")
    fabrication_date = models.CharField(max_length=12, default="Desconhecido", unique=False)
    heritage_id = models.CharField(max_length=30, default="", unique=True) #No de livro tombo
    manufacture = models.CharField(max_length=30, default="Desconhecida", unique=False)
    decoration = models.CharField(max_length=30, default="Desconhecida", unique=False)
    collection = models.ForeignKey('collection.collection', default="", related_name='collection', on_delete=models.CASCADE)
    material = models.ForeignKey('materials.materials', default="",related_name='material', on_delete=models.CASCADE)
    length = models.FloatField(max_length=5, default=0)
    width = models.FloatField(max_length=5, default=0)
    diameter = models.FloatField(max_length=5, default=0)
    height = models.FloatField(max_length=5, default=0)
    circumference = models.FloatField(max_length=5, default=0)
    depth = models.FloatField(max_length=5, default=0)
    weight = models.FloatField(max_length=5, default=0)
    owner = models.CharField(max_length=30, default="Desconhecido", unique=False)
    acqusition_date = models.CharField(max_length=12, default="Desconhecido", unique=False)
    donor = models.CharField(max_length=30, default="Desconhecido", unique=False)
    last_owner = models.CharField(max_length=30, default="Desconhecido", unique=False)
    personality = models.CharField(max_length=30, default="Desconhecido", unique=False)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
   
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("artifacts:detail", kwargs={"slug": self.slug})
    

   
    def get_main_edit(self):
        return reverse("artifacts:artifacts-update", kwargs={"pk": self.id})

