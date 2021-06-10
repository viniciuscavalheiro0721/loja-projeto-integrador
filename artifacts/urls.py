from django.urls import path
from django.conf.urls import url



from . import views

app_name = "artifacts"

urlpatterns = [
#    path("", views.ArtifactsListView.as_view(), name="list"),
    path("<slug:slug>/", views.ArtifactsDetailView.as_view(), name="detail"),
    url(r'artifacts/add/$',  views.ArtifactsCreateView.as_view(), name='artifacts_add'),
    path('artifacts/<pk>', views.ArtifactsUpdateView.as_view(), name='artifacts-update'),
    path('', views.ArtifactsList, name='list'),
]


