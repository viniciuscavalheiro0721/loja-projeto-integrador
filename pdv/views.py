import json
from cgi import test
from datetime import datetime
from itertools import product
from webbrowser import get

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from products.models import Products

from .forms import PDVForm
from .models import Pdv, cupom, forma_pgto, item_cupom


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
        pdts = Products.objects.all()
        if request.method == 'POST':

            prod = Products.objects.filter(code_int=request.POST['codigo'])
            if prod:
                item = item_cupom.objects.create(
                    preco=prod[0].sale_price, limite_cliente=1, qtd_item=1, codigo_cupom_id=10, codigo_int_id=prod[0].code_int, description=prod[0].description)

            # alterar o total na tabela cupom campo "preco"
            # request.POST['total']

            item.save()

        return render(request, 'pdv/frente-caixa.html', {'products': pdts, 'pdv': pdv[0], 'cupom': cpn[0], 'pgto': pgto})

    else:
        return redirect('/../pdv/pdv/add')


@login_required
# Verifica se entra no cria pdv ou na frente de caixa
def itens_cupom(request):
    pdv = Pdv.objects.filter(active_pdv=True, id_user_pdv_id=request.user.id)
    if pdv[0]:
        cpn = cupom.objects.filter(fecha_cupom=False, id_pdv=pdv[0].id_pdv)
        # verifica se existe cupom aberto
        if not cpn:
            cpn_new = cupom.objects.create(fecha_cupom=False, acrescimo=0, preco_custo=0,
                                           preco=0, cancela_cupom=False, desconto=0, id_pdv=pdv[0], dt_cupom=datetime.now(), codigo_pgto=forma_pgto(id=1))
            cpn_new.save()
            cpn = cupom.objects.filter(fecha_cupom=False, id_pdv=pdv[0].id_pdv)

        itens_cpn = item_cupom.objects.filter(codigo_cupom=cpn[0].codigo_cupom)
        return render(request, 'pdv/itens-cupom.html', {'itens': itens_cpn, 'cupom': cpn[0]})

    else:
        return redirect('/../pdv/pdv/add')
