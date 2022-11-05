import json
from cgi import test
from datetime import datetime
from itertools import product
from unicodedata import decimal
from webbrowser import get

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
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

        pgto = forma_pgto.objects.all()
        pdts = Products.objects.all()
        if request.method == 'POST':
            if request.POST['btn'] == "Inserir":

                if request.POST['codigo'] == "":
                    cod_int = 0
                else:
                    cod_int = request.POST['codigo']
                prod = Products.objects.filter(code_int=cod_int)
                if prod:
                    item = item_cupom.objects.create(
                        preco=prod[0].sale_price, limite_cliente=1, qtd_item=1, codigo_cupom_id=cpn[0].codigo_cupom, codigo_int_id=prod[0].code_int, description=prod[0].description)
                    item.save()
                # alterar o total na tabela cupom campo "preco"
                cpn_up = cupom.objects.filter(fecha_cupom=False, id_pdv=pdv[0].id_pdv).update(
                    preco=request.POST['total'], codigo_pgto_id=forma_pgto(id=request.POST['pgto']), acrescimo=request.POST['acres'], desconto=request.POST['desc'])

            if request.POST['btn'] == "Finalizar":

                balance = float(pdv[0].balance_pdv) + \
                    float(request.POST['total-fin'])
                cpn_up = cupom.objects.filter(fecha_cupom=False, id_pdv=pdv[0].id_pdv).update(
                    preco=request.POST['total-fin'], codigo_pgto_id=forma_pgto(id=request.POST['pgto']), fecha_cupom=True)
                pdv_up = Pdv.objects.filter(
                    id_pdv=request.POST['id-pdv'], active_pdv=True, id_user_pdv_id=User(id=request.POST['user'])).update(
                    balance_pdv=balance
                )

            if request.POST['btn'] == "Cancelar":
                cpn_up = cupom.objects.filter(fecha_cupom=False, id_pdv=pdv[0].id_pdv).update(
                    fecha_cupom=True, cancela_cupom=True)

            return redirect('/../pdv/caixa')

        return render(request, 'pdv/frente-caixa.html', {'products': pdts, 'pdv': pdv[0], 'cupom': cpn[0], 'pgtos': pgto})

    else:
        return redirect('/../pdv/pdv/add')


@ login_required
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
            cpn = cupom.objects.filter(
                fecha_cupom=False, id_pdv=pdv[0].id_pdv)

        itens_cpn = item_cupom.objects.filter(codigo_cupom=cpn[0].codigo_cupom)

        if request.method == 'POST':
            if request.POST['valqtd'] != '0':
                up_item = item_cupom.objects.filter(
                    codigo_item=request.POST['id_item']).update(qtd_item=request.POST['valqtd'])
            else:
                del_item = item_cupom.objects.get(
                    codigo_item=request.POST['id_item'])
                del_item.delete()
            return redirect('/../pdv/caixa/itens-cupom')
        return render(request, 'pdv/itens-cupom.html', {'itens': itens_cpn, 'cupom': cpn[0]})

    else:
        return redirect('/../pdv/pdv/add')
