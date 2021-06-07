
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Artifacts

@login_required
def teste(request):
    return render(request, 'artifacts/artifacts_create_form.html')

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



