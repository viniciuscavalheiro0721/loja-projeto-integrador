from django.contrib import admin
from .models import Materials

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}