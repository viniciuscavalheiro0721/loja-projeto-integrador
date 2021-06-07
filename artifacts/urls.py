from django.urls import path


from . import views

app_name = "artifacts"

urlpatterns = [
    path("", views.ArtifactsListView.as_view(), name="list"),
    path("<slug:slug>/", views.ArtifactsDetailView.as_view(), name="detail"),
    path("artifacts/add/", views.ArtifactsCreateView.as_view(), name="create_form"),
    path('artifacts/<int:pk>/', views.ArtifactsUpdateView.as_view(), name='form-update'),
    path('az', views.teste, name='task-list'),
    path('edit/<int:id>/', views.editForm, name='edit-form'),
]


