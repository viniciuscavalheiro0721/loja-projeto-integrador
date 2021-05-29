from django.contrib import admin
from .models import Artifacts

@admin.register(Artifacts)
class ArtifactsAdmin(admin.ModelAdmin):
    list_display = ("name","description", "post_author", "collection", "material", "heritage_id", "created", "updated")
    prepopulated_fields = {"slug": ("name",)}