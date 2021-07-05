from django.views.generic import DetailView, ListView, UpdateView
from django.core.paginator import Paginator
from .models import Collection
from django.shortcuts import render, get_object_or_404, redirect

from artifacts.models import Artifacts

class CollectionListView(ListView):
    model = Collection

class CollectionDetailView(DetailView):
    model = Collection




def CollectionList(request,pk):

    # Primeiro, buscamos os funcionarios
    artifacts=Artifacts.objects.filter(collection__in=pk) 
    collection=Collection.objects.filter(id__in=pk) 
    # Incluímos no contexto
    # contexto = {
    #   'collection': 1
    # }
  


    return render(request, 'collection/collection_detail.html',{'artifacts':artifacts, 'collection':collection })


