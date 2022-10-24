from django import forms
from django.contrib.auth.models import User

from .models import Pdv


class PDVForm(forms.ModelForm):

    class Meta:
        model = Pdv
        fields = ('id_user_pdv', 'balance_pdv', 'active_pdv')
