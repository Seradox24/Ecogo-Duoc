from django import forms
from .models import SalidaTerreno

class SalidaTerrenoForm(forms.ModelForm):
    class Meta:
        model = SalidaTerreno
        fields = '__all__'



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