
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import artifactsForm
from .forms import CountryForm
from .models import Artifacts
from collection.models import Collection
from django.core.paginator import Paginator
from django.template import RequestContext
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



def addlogic(request):
 search = request.POST.get('search')
 some_var = request.POST.getlist('checks[]')
 
 collection = Collection.objects.all()

 if search and some_var:
    artifacts_list = Artifacts.objects.filter(collection__in=some_var, name__icontains=search )  

 elif some_var:
    artifacts_list = Artifacts.objects.filter(collection__in=some_var) 
    # data=''
    # if(len(search)>0):
    #          data=search 
    #          return HttpResponse(data)
    
        
 elif search:
   artifacts_list = Artifacts.objects.filter( name__icontains=search )  
  # if (len(artifacts_list) <= 0):
   # return HttpResponse("deu certp")

 else:
        artifacts_list_full = Artifacts.objects.all()
        paginator = Paginator(artifacts_list_full, 9)
        page = request.GET.get('page')
        artifacts_list = paginator.get_page(page)
        return render(request, 'artifacts/artifacts_list.html', {'artifacts_list':artifacts_list, 'collection':collection })




#  if some_var:

#     # data=''
#     # if(len(search)>0):
#     #          data=search 
#     #          return HttpResponse(data)
#     artifacts_list = Artifacts.objects.filter(collection__in=some_var )
        
#  if search:
#     artifacts_list = Artifacts.objects.filter(collection__in=some_var, name__icontains=search )  

 paginator = Paginator(artifacts_list, 9)
 page = request.GET.get('page')
 artifacts_list = paginator.get_page(page)
 return render(request, 'artifacts/artifacts_list.html', {'artifacts_list':artifacts_list, 'collection':collection })


def ArtifactsList(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    check = request.GET.get('checks[]')
    collection = Collection.objects.all()
    
    if search:
        artifacts_list = Artifacts.objects.filter(name__icontains=search)
    elif filter:
        artifacts_list = Artifacts.objects.filter(collection=filter )
    elif check:
         artifacts_list = Artifacts.objects.filter(collection='checks[]' )
    else:
        artifacts_list_full = Artifacts.objects.all()
        paginator = Paginator(artifacts_list_full, 9)
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

@login_required
def helloWorld(request):
    return HttpResponse('Hello World!')

