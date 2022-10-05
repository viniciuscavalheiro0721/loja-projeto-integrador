from django.views.generic import DetailView, ListView

from .models import Products


class ProductsListView(ListView):
    model = Products


class ProductsDetailView(DetailView):
    model = Products
