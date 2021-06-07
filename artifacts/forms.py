from django import forms

from .models import Artifacts

class artifactsForm(forms.ModelForm):

    class Meta:
        model = Artifacts
        fields = ('name', 'slug','description')