from django.urls import path

from . import views

app_name = "materials"

urlpatterns = [
    path("", views.MaterialsListView.as_view(), name="list"),
    path("<slug:slug>/", views.MaterialsDetailView.as_view(), name="detail")
]