from django.contrib import admin
from .models import Aboutus

@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
    list_display = ("title","text", "textImg")