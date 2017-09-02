from dal import autocomplete

from django import forms
from .models import Latency

class LatencyForm(forms.ModelForm):
    class Meta:
        model = Latency
        fields = ('__all__')
        widgets = {
            'city_from': autocomplete.ModelSelect2(url='tables:city-autocomplete'),
            'city_to': autocomplete.ModelSelect2(url='tables:city-autocomplete')
        }