from django.views.generic import DetailView, ListView

from .models import Collection

class CollectionListView(ListView):
    model = Collection

class CollectionDetailView(DetailView):
    model = Collection