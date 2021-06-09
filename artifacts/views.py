
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import artifactsForm
from .models import Artifacts


def teste(request):
    return render(request, 'artifacts/artifacts_create_form.html')

@login_required
def editForm(request,id):
#  return render(request, 'artifacts/artifacts_create_form.html')

    artifacts = get_object_or_404(Artifacts, pk=id)
    form = artifactsForm(instance=artifacts)

    if(request.method == 'POST'):
        form = artifactsForm(request.POST, instance=artifacts)

        if(form.is_valid()):
            artifacts.save()
            return redirect('/artifacts')
        else:
            return render(request, 'artifacts/artifacts_edit_form.html', {'form': form, 'artifacts': artifacts} )
    else:
            return render(request, 'artifacts/artifacts_edit_form.html', {'form': form, 'artifacts': artifacts} )



class ArtifactsListView(ListView):
    model = Artifacts

class ArtifactsDetailView(DetailView):
    model = Artifacts

class ArtifactsCreateView(CreateView):
    model = Artifacts
    form_class = artifactsForm
    success_url = reverse_lazy('artifacts:list')

class ArtifactsUpdateView(UpdateView):
    model = Artifacts
    form_class = artifactsForm
    success_url = reverse_lazy('artifacts:list')

