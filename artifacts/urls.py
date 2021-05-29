from django.urls import path

from . import views

app_name = "artifacts"

urlpatterns = [
    path("", views.ArtifactsListView.as_view(), name="list"),
    path("<slug:slug>/", views.ArtifactsDetailView.as_view(), name="detail"),
]