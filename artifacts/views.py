
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import artifactsForm
from .models import Artifacts
from collection.models import Collection
from django.core.paginator import Paginator
@login_required
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

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
# from django.http import HttpResponse
# from .forms import TaskForm
# from django.contrib import messages
# import datetime

# from .models import Task


@login_required
def ArtifactsList(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    collection = Collection.objects.all()
    
    if search:
        artifacts_list = Artifacts.objects.filter(name__icontains=search)
    elif filter:
        artifacts_list = Artifacts.objects.filter(collection=filter)
    else:
        artifacts_list_full = Artifacts.objects.all()
        paginator = Paginator(artifacts_list_full, 3)
        page = request.GET.get('page')
        artifacts_list = paginator.get_page(page)

    return render(request, 'artifacts/artifacts_list.html', {'artifacts_list':artifacts_list, 'collection':collection })

class ArtifactsListView(ListView):
    model = Artifacts
   
class ArtifactsDetailView(DetailView):
    model = Artifacts

class ArtifactsCreateView(LoginRequiredMixin, CreateView):
    model = Artifacts
    form_class = artifactsForm
    success_url = reverse_lazy('artifacts:list')

class ArtifactsUpdateView(LoginRequiredMixin, UpdateView):
    model = Artifacts
    form_class = artifactsForm
    success_url = reverse_lazy('artifacts:list')

