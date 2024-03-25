from django import forms
from .models import *
from coordinador.models import SalidaTerreno
from django.db import models



class BajaEstudianteForm(forms.ModelForm):
    # Sobrescribimos el método __init__ para personalizar el formulario
    def __init__(self, *args, **kwargs):
        # Extraemos el id de la salida a terreno si se proporciona
        salida_terreno_id = kwargs.pop('salida_terreno_id', None)
        # Llamamos al __init__ original de ModelForm
        super(BajaEstudianteForm, self).__init__(*args, **kwargs)
        # Si se proporcionó un id de salida a terreno
        if salida_terreno_id:
            # Filtramos las bajadas que no tienen salida a terreno o que tienen la salida a terreno especificada
            self.fields['bajada'].queryset = Bajada.objects.filter(
                models.Q(salida_terreno__isnull=True) | 
                models.Q(salida_terreno__id=salida_terreno_id)
            )
        else:
            # Si no se proporcionó un id de salida a terreno, mostramos solo las bajadas que no tienen salida a terreno
            self.fields['bajada'].queryset = Bajada.objects.filter(salida_terreno__isnull=True)

    class Meta:
        model = BajaEstudiante
        fields = ['bajada']



class DocumentoCerMedicoForm(forms.ModelForm):
    class Meta:
        model = DocumentoCerMedico
        fields = ['archivo']  # Solo mostramos el campo de archivo
        widgets = {
            'archivo': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpeg,.jpg,.png,.doc,.docx'}),
        }