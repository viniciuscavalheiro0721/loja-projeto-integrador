from django.views.generic import ListView

from .models import Index

class IndexListView(ListView):
    model = Index
