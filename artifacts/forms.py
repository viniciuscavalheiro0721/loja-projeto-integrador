from django import forms

from .models import Artifacts

class artifactsForm(forms.ModelForm):

    class Meta:
        model = Artifacts
        # fields = '__all__'      
        fields = ('name', 'slug','description', 'author', 'about', 'usage', 'style', 'culture', 'ethnicity', 'age', 'inscriptions', 'fabrication_date', 'heritage_id', 'manufacture', 'decoration', 'collection', 'material', 'length', 'width', 'diameter', 'height', 'circumference', 'depth', 'weight', 'owner', 'acqusition_date', 'donor', 'last_owner', 'personality', 'post_author', 'image' )



class CountryForm(forms.Form):
  
    OPTIONS = (
        ("1", "1"),
        ("2", "Germany"),
        ("3", "Neitherlands"),
    )
    artifacts_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)