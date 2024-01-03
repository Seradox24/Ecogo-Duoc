from django import forms
from .models import SalidaTerreno

class SalidaTerrenoForm(forms.ModelForm):
    class Meta:
        model = SalidaTerreno
        fields = '__all__'
