from django import forms
from django.db import models
from core import models
from .models import SalidaTerreno
from core.models import UsersMetadata
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from core.models import UsersMetadata


class SalidaTerrenoForm(forms.ModelForm):
    class Meta:
        model = SalidaTerreno
        fields = '__all__'


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


class UsersMetadataForm(forms.ModelForm):
    username_field = forms.CharField(required=False, widget=forms.HiddenInput())  # Campo adicional para capturar el nombre de usuario

    class Meta:
        model = UsersMetadata
        exclude = ['user', 'slug', 'correo']  
        widgets = {
            'comuna': forms.Select(attrs={'class': 'select2'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Ingrese el slug', 'readonly': 'readonly'}),
        }
