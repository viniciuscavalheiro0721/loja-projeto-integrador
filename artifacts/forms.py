from django import forms

from .models import Artifacts

class artifactsForm(forms.ModelForm):

    class Meta:
        model = Artifacts
        fields = ('name', 'slug','description', 'author', 'about', 'usage', 'style', 'culture', 'ethnicity', 'age', 'inscriptions', 'fabrication_date', 'heritage_id', 'manufacture', 'decoration', 'collection', 'material', 'length', 'width', 'diameter', 'height', 'circumference', 'depth', 'weight', 'owner', 'acqusition_date', 'donor', 'last_owner', 'personality', 'post_author', 'image' )