from django import forms
from .models import SalidaTerreno, DiaSemana
from core.models import Asignatura, UsersMetadata, Perfiles
from django.contrib.auth.forms import UserChangeForm
from core.models import Asignatura
from django.db import models
from core import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
            queryset=UsersMetadata.objects.filter(perfil=perfil_profesor),blank=True,
            widget=forms.Select(attrs={'class': 'form-select'}),
        )
        docentes_apoyo = forms.ModelMultipleChoiceField(
            queryset=UsersMetadata.objects.filter(perfil=perfil_profesor),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),blank=True,
        )
    except Perfiles.DoesNotExist:
        # Si el perfil de profesor no existe, deja el queryset vacío
        docente_titular = forms.ModelChoiceField(
            queryset=UsersMetadata.objects.none(),
            widget=forms.Select(attrs={'class': 'form-select'}),blank=True,
        )
        docentes_apoyo = forms.ModelMultipleChoiceField(
            queryset=UsersMetadata.objects.none(),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),blank=True,
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['docentes_apoyo'].required = False


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
            'semaforo': forms.Select(attrs={'class': 'form-select'}),
        }

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['data1'].widget.attrs.update({
            'class': 'miSelect',
        })  
        



class UsersMetadataForm(forms.ModelForm):
    class Meta:
        model = UsersMetadata
        fields = '__all__'
        widgets = {
            'comuna': forms.Select(attrs={'class': 'select2'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Ingrese el slug'}),
        }

    
class UserCreationWithMetadataForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingresa una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'email': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }
        

#class UsersMetadataForm(forms.ModelForm):
 #   class Meta:
  #      model = UsersMetadata
   #     exclude = ['user']  # Puedes excluir campos adicionales si es necesario

class UsersMetadataForm(forms.ModelForm):
    username_field = forms.CharField(required=False, widget=forms.HiddenInput())  # Campo adicional para capturar el nombre de usuario
    fields = ['sexo', 'perfil', 'nacionalidad', 'semestre', 'sede', 'nom_carrera', 'jornada', 'rut', 'nombres', 'ap_paterno', 'ap_materno', 'fnacimiento', 'estado_civil', 'direccion', 'numero', 'celular', 'contacto_emergencia', 'estado', 'foto', ]
    class Meta:
        model = UsersMetadata
        exclude = ['user', 'slug', 'correoduoc']  
        widgets = {
            'comuna': forms.Select(attrs={'class': 'select2'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Ingrese el slug', 'readonly': 'readonly'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'perfil': forms.Select(attrs={'class': 'form-select'}),
            'nacionalidad': forms.Select(attrs={'class': 'form-select'}),
            'semestre': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'sede': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'nom_carrera': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'jornada': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'rut': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'nombres': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'ap_paterno': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'ap_materno': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'fnacimiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'estado_civil': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'numero': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'celular': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'contacto_emergencia': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.NumberInput(attrs={'class': 'form-control','type': 'file'}),

        }
        labels = {
            'nom_carrera': 'Carrera',
            'ap_paterno': 'Apellido paterno',
            'fnacimiento': 'Fecha de nacimiento',
            # Agrega más campos y etiquetas según sea necesario
        }

from core.models import Asignatura, UsersMetadata, Perfiles

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



