from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "index"

urlpatterns = [
    path("", login_required(views.IndexListView.as_view()), name="list"),
    path('logout/', views.logoutnlogin, name='logout'),

]
