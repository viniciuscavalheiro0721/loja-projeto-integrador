from django.views.generic import ListView

from .models import Aboutus

class AboutusListView(ListView):
    model = Aboutus
