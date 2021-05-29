from django.views.generic import DetailView, ListView

from .models import Artifacts

class ArtifactsListView(ListView):
    model = Artifacts

class ArtifactsDetailView(DetailView):
    model = Artifacts