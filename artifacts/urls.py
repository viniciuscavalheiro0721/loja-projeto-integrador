from django.urls import include, path, re_path

from . import views

app_name = "artifacts"

urlpatterns = [
    #    path("", views.ArtifactsListView.as_view(), name="list"),
    path("<slug:slug>/", views.ArtifactsDetailView.as_view(), name="detail"),
    re_path(r'artifacts/add/$',  views.ArtifactsCreateView.as_view(),
            name='artifacts_add'),
    path('artifacts/<pk>', views.ArtifactsUpdateView.as_view(),
         name='artifacts-update'),
    path('', views.ArtifactsList, name='list'),
    path('addlogic', views.addlogic, name='add'),
    # path('', views.countries_view, name='list'),
    path('helloworld/', views.helloWorld),

]
