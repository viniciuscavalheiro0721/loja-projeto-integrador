from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductsListView.as_view(), name="list"),

]
