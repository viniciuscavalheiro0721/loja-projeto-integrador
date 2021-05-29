from django.views.generic import DetailView, ListView

from .models import Materials

class MaterialsListView(ListView):
    model = Materials

class MaterialsDetailView(DetailView):
    model = Materials