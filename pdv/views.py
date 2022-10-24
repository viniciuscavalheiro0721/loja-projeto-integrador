from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import PDVForm
from .models import Pdv


class PDVCreateView(LoginRequiredMixin, CreateView):
    model = Pdv
    form_class = PDVForm
    success_url = reverse_lazy('pdv:caixa')


@login_required
# Verifica se entra no cria pdv ou na frente de caixa
def index_pdv(request):
    value = Pdv.objects.filter(active_pdv=True, id_user_pdv_id=request.user.id)
    if value:
        return redirect('caixa/')
    else:
        return redirect('pdv/add')


@login_required
# Verifica se entra no cria pdv ou na frente de caixa
def frente_caixa(request):
    value = Pdv.objects.filter(active_pdv=True, id_user_pdv_id=request.user.id)
    if value:
        return render(request, 'pdv/frente-caixa.html')

    else:
        return redirect('/../pdv/pdv/add')
