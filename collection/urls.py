from django.urls import path

from . import views

app_name = "collection"

urlpatterns = [
    path("", views.CollectionListView.as_view(), name="list"),
    path("<slug:slug>/", views.CollectionDetailView.as_view(), name="detail")
]