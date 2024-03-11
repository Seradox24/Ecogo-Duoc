from django import forms
from core.models import Asignatura


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'sigla',]