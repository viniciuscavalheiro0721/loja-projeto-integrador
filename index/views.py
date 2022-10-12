from django.contrib.auth.views import logout_then_login
from django.views.generic import ListView

from .models import Index


class IndexListView(ListView):
    model = Index


def logoutnlogin(request):
    return logout_then_login(request, login_url="/")
