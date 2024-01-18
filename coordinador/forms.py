from django import forms
from .models import SalidaTerreno, DiaSemana
from core.models import Asignatura, UsersMetadata, Perfiles

SEMESTRE_CHOICES = [
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),
    ('VI', 'VI'),
    ('VII', 'VII'),
    ('VIII', 'VIII'),
]

class SalidaTerrenoForm(forms.ModelForm):
    try:
        # Intenta obtener el perfil de profesor
        perfil_profesor = Perfiles.objects.get(nombre='Docente')

        # Filtra los usuarios que tienen el perfil de profesor
        docente_titular = forms.ModelChoiceField(
            queryset=UsersMetadata.objects.filter(perfil=perfil_profesor),
            widget=forms.Select(attrs={'class': 'form-select'}),
        )
        docentes_apoyo = forms.ModelMultipleChoiceField(
            queryset=UsersMetadata.objects.filter(perfil=perfil_profesor),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
        )
    except Perfiles.DoesNotExist:
        # Si el perfil de profesor no existe, deja el queryset vacío
        docente_titular = forms.ModelChoiceField(
            queryset=UsersMetadata.objects.none(),
            widget=forms.Select(attrs={'class': 'form-select'}),
        )
        docentes_apoyo = forms.ModelMultipleChoiceField(
            queryset=UsersMetadata.objects.none(),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
        )
    
    

    class Meta:
        model = SalidaTerreno
        fields = '__all__'
        widgets = {
            'situacion': forms.Select(attrs={'class': 'form-select'}),
            'numero_cuenta': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'semestre': forms.Select(choices=SEMESTRE_CHOICES, attrs={'class': 'form-select'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'semana': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'actividad': forms.Select(attrs={'class': 'form-select'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'dias': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'noches': forms.NumberInput(attrs={'class': 'form-control','type':'number'}),
            'diasemana': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
            'lugar_ejecucion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'asignatura': forms.Select(attrs={'class': 'form-select'}),
            'exp_aprendizaje': forms.Select(attrs={'class': 'form-select'}),
            'num_alumnos': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'seccion': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
            'docente_titular': forms.Select(attrs={'class': 'form-select'}),
            'docentes_apoyo': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
            'num_salida': forms.NumberInput(attrs={'class': 'form-control','type':'number'}),
            'asig_comp_terreno': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
        




class AsignaturaForm(forms.ModelForm):
    try:
        # Intenta obtener el perfil de profesor
        perfil_profesor = Perfiles.objects.get(nombre='Docente')

        # Filtra los usuarios que tienen el perfil de profesor
        docentes = forms.ModelMultipleChoiceField(
            queryset=UsersMetadata.objects.filter(perfil=perfil_profesor),
            widget=forms.CheckboxSelectMultiple,
        )
    except Perfiles.DoesNotExist:
        # Si el perfil de profesor no existe, deja el queryset vacío
        docentes = forms.ModelMultipleChoiceField(
            queryset=UsersMetadata.objects.none(),
            widget=forms.CheckboxSelectMultiple,
        )

    class Meta:
        model = Asignatura
        fields = ['nombre', 'sigla', 'docentes', 'secciones']