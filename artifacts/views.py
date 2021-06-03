
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView




from .models import Artifacts

class ArtifactsListView(ListView):
    model = Artifacts

class ArtifactsDetailView(DetailView):
    model = Artifacts

class ArtifactsCreateView(CreateView):
    model = Artifacts
    fields = ['slug']

class ArtifactsUpdateView(UpdateView):
    model = Artifacts
    fields = ['slug']

