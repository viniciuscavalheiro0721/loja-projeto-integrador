from django.urls import path, re_path

from . import views

app_name = "pdv"

urlpatterns = [
    re_path(r'pdv/add/$',  views.PDVCreateView.as_view(),
            name='pdv_add'),
    path('', views.index_pdv),
    path('caixa/', views.frente_caixa, name='caixa'),

    path('caixa/itens-cupom/', views.itens_cupom, name='itens-cupom'),
]
