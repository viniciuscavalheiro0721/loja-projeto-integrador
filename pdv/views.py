from cgi import test
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import PDVForm
from .models import Pdv, cupom, forma_pgto


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
    pdv = Pdv.objects.filter(active_pdv=True, id_user_pdv_id=request.user.id)
    if pdv[0]:
        cpn = cupom.objects.filter(fecha_cupom=False, id_pdv=pdv[0].id_pdv)
        # verifica se existe cupom aberto
        if not cpn:
            cpn_new = cupom.objects.create(fecha_cupom=False, acrescimo=0, preco_custo=0,
                                           preco=0, cancela_cupom=False, desconto=0, id_pdv=pdv[0], dt_cupom=datetime.now(), codigo_pgto=forma_pgto(id=1))
            cpn_new.save()
            cpn = cupom.objects.filter(fecha_cupom=False, id_pdv=pdv[0].id_pdv)
            # return HttpResponse(pdv)

        pgto = forma_pgto.objects.get(id=cpn[0].codigo_pgto_id)
        return render(request, 'pdv/frente-caixa.html', {'pdv': pdv[0], 'cupom': cpn[0], 'pgto': pgto})

    else:
        return redirect('/../pdv/pdv/add')


@login_required
# Verifica se entra no cria pdv ou na frente de caixa
def itens_cupom(request):
    return render(request, 'pdv/itens-cupom.html')
