from django import forms
from .models import SalidaTerreno, DiaSemana
from core.models import Asignatura, UsersMetadata, Perfiles
from django.contrib.auth.forms import UserChangeForm
from core.models import Asignatura
from django.db import models
from core import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q


SEMESTRE_CHOICES = [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
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
            'situacion': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'numero_cuenta': forms.NumberInput(attrs={'class': 'form-control','type':'number', 'required': 'required' }),
            'semestre': forms.Select(choices=SEMESTRE_CHOICES, attrs={'class': 'form-select', 'required': 'required'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control','type':'number' , 'required': 'required'}),
            'semana': forms.NumberInput(attrs={'class': 'form-control','type':'number' , 'required': 'required'}),
            'actividad': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control','type': 'date', 'required': 'required'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control','type': 'date', 'required': 'required'}),
            'dias': forms.NumberInput(attrs={'class': 'form-control','type':'number', 'required': 'required' }),
            'noches': forms.NumberInput(attrs={'class': 'form-control','type':'number', 'required': 'required'}),
            'diasemana': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
            'lugar_ejecucion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': 'required'}),
            'asignaturas': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox', }),
            'exp_aprendizaje': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'num_alumnos': forms.NumberInput(attrs={'class': 'form-control','type':'number', 'required': 'required' }),
            'secciones': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox', }),
            'docente_titular': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'docentes_apoyo': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),
            'num_salida': forms.NumberInput(attrs={'class': 'form-control','type':'number', 'required': 'required'}),
            'asig_base': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': 'required'}),
            'semaforo': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
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
    fields = ['sexo', 'perfil', 'nacionalidad', 'semestre', 'sede', 'nom_carrera', 'jornada', 'rut', 'nombres', 'ap_paterno', 'ap_materno', 'fnacimiento', 'estado_civil', 'direccion', 'numero', 'celular', 'contacto_emergencia', 'estado', 'foto','asignaturas_inscritas']
    class Meta:
        model = UsersMetadata
        exclude = ['user', 'slug', 'correoduoc']  
        widgets = {
            'comuna': forms.Select(attrs={'class': 'select2'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Ingrese el slug', 'readonly': 'readonly'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'perfil': forms.Select(attrs={'class': 'form-select'}),
            'nacionalidad': forms.Select(attrs={'class': 'form-select'}),
            'semestre': forms.Select(choices=SEMESTRE_CHOICES, attrs={'class': 'form-select'}),
            'sede': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'nom_carrera': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'jornada': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'rut': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'nombres': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'ap_paterno': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'ap_materno': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'fnacimiento': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'estado_civil': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'numero': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'celular': forms.NumberInput(attrs={'class': 'form-control','type':'number' }),
            'contacto_emergencia': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.NumberInput(attrs={'class': 'form-control','type': 'file'}),
            'asignaturas_inscritas': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'checkbox'}),

        }
        labels = {
            'nom_carrera': 'Carrera',
            'ap_paterno': 'Apellido paterno',
            'fnacimiento': 'Fecha de nacimiento',
            # Agrega más campos y etiquetas según sea necesario
        }

from core.models import Asignatura, UsersMetadata, Perfiles

class AsignaturaForm(forms.ModelForm):
    

    class Meta:
        model = Asignatura
        fields = ['nombre', 'sigla',]



class SalidaTerrenoFormSemaforo(forms.ModelForm):

    class Meta:
        model = SalidaTerreno
        fields = ['semaforo']
        widgets = {
            'semaforo': forms.Select(attrs={'class': 'form-select'}),
        }

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['data1'].widget.attrs.update({
            'class': 'miSelect',
        })





class SalidaTerrenoImplementoForm(forms.ModelForm):
    class Meta:
        model = SalidaTerrenoImplemento
        fields = ['salida_terreno', 'implemento', 'presente']
        widgets = {
            'implemento': forms.CheckboxSelectMultiple
        }










# class SeccionForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         asignatura_id = kwargs.pop('asignatura_id', None)
#         instance = kwargs.get('instance') 
#         print(instance) # Obtener la instancia de la sección

#         super(SeccionForm, self).__init__(*args, **kwargs)

#         if asignatura_id:
#             asignatura = Asignatura.objects.get(pk=asignatura_id)
#             secciones_exist = Seccion.objects.filter(asignatura=asignatura).values_list('nombre__id', flat=True)
#             nombres_disponibles = NombreSeccion.objects.exclude(id__in=secciones_exist)

#             # Si estamos editando una instancia existente, incluir el nombre actual
#             if instance and instance.nombre:
#                 self.fields['nombre'].queryset = NombreSeccion.objects.filter(pk=instance.nombre.id) | nombres_disponibles
#                 print('dsfasdfasdfasd')
#             else:
#                 self.fields['nombre'].queryset = nombres_disponibles
#                 print('dsfasdfasdfasd')
           

#         perfil_alumno = Perfiles.objects.get(nombre='Alumno')
#         self.fields['usuarios'].queryset = UsersMetadata.objects.filter(perfil=perfil_alumno)

#     class Meta:
#         model = Seccion
#         fields = ['nombre', 'usuarios']
#         widgets = {
#             'nombre': forms.Select(attrs={'class': 'form-control'}),
#             'usuarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
#         }

class SeccionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        asignatura_id = kwargs.pop('asignatura_id', None)
        instance = kwargs.get('instance') 
        print(instance) # Obtener la instancia de la sección

        super(SeccionForm, self).__init__(*args, **kwargs)

        if asignatura_id:
            asignatura = Asignatura.objects.get(pk=asignatura_id)
            secciones_exist = Seccion.objects.filter(asignatura=asignatura).values_list('nombre__id', flat=True)
            nombres_disponibles = NombreSeccion.objects.exclude(id__in=secciones_exist)

            # Si estamos editando una instancia existente, incluir el nombre actual
            if instance and instance.nombre:
                self.fields['nombre'].queryset = NombreSeccion.objects.filter(pk=instance.nombre.id) | nombres_disponibles
            else:
                self.fields['nombre'].queryset = nombres_disponibles
          
        # Filtrar usuarios por asignaturas inscritas y perfil "Alumno"
        if asignatura_id:
            # Consulta para obtener las secciones asociadas a la asignatura
            secciones_asignatura = Seccion.objects.filter(asignatura=asignatura_id)
            
            # Consulta para obtener los IDs de las secciones asociadas a la asignatura
            secciones_asignatura_ids = secciones_asignatura.values_list('id', flat=True)
            
            # Consulta para filtrar usuarios que están inscritos en la asignatura pero no en otra sección de la misma asignatura
            perfil_alumno = Perfiles.objects.get(nombre='Alumno')
            self.fields['usuarios'].queryset = UsersMetadata.objects.filter(
                perfil=perfil_alumno, asignaturas_inscritas=asignatura_id
            ).exclude(
                Q(secciones__in=secciones_asignatura_ids) & ~Q(secciones__isnull=True)
            )

    class Meta:
        model = Seccion
        fields = ['nombre', 'usuarios']
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'usuarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }




# class EditarSeccionForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(EditarSeccionForm, self).__init__(*args, **kwargs)
        
#         instance = kwargs.get('instance')
        
#         if instance:
#             # Obtener el nombre de la sección seleccionada
#             nombre_seccion_actual = instance.nombre
            
#             # Obtener todas las secciones excepto la actual
#             secciones_excluidas = Seccion.objects.exclude(id=instance.id)
#             nombres_excluidos = [seccion.nombre.id for seccion in secciones_excluidas]
            
#             # Obtener los nombres de sección que no están siendo utilizados actualmente
#             nombres_disponibles = NombreSeccion.objects.exclude(id__in=nombres_excluidos)
            
#             # Incluir el nombre actual en el queryset del campo 'nombre'
#             self.fields['nombre'].queryset = NombreSeccion.objects.filter(pk=nombre_seccion_actual.id) | nombres_disponibles
#         else:
#             # Si no hay instancia, mostrar todos los nombres disponibles
#             nombres_disponibles = NombreSeccion.objects.all()
#             self.fields['nombre'].queryset = nombres_disponibles
        
#         # Filtrar usuarios cuyo perfil sea "Alumno" para el campo 'usuarios'
#         perfil_alumno = Perfiles.objects.get(nombre='Alumno')
#         self.fields['usuarios'].queryset = UsersMetadata.objects.filter(perfil=perfil_alumno)

#     class Meta:
#         model = Seccion
#         fields = ['nombre', 'usuarios']
#         widgets = {
#             'nombre': forms.Select(attrs={'class': 'form-control'}),
#             'usuarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
#         }
        
class EditarSeccionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        asignatura_id = instance.asignatura_id if instance else None
        print("Asignatura ID:", asignatura_id)  # Print para verificar el ID de la asignatura
        super(EditarSeccionForm, self).__init__(*args, **kwargs)
        
        # Obtener todos los nombres de sección disponibles
        nombres_disponibles = NombreSeccion.objects.all()
        print("Nombres disponibles:", nombres_disponibles)  # Print para verificar los nombres disponibles
        
        if instance:
            # Obtener el nombre de la sección seleccionada
            nombre_seccion_actual = instance.nombre
            print("Nombre de la sección actual:", nombre_seccion_actual)  # Print para verificar el nombre de la sección actual
            
            # Obtener todas las secciones excepto la actual
            secciones_excluidas = Seccion.objects.filter(asignatura=asignatura_id).exclude(id=instance.id)
            nombres_excluidos = [seccion.nombre.id for seccion in secciones_excluidas]
            
            # Excluir los nombres de sección ya asignados a otras secciones
            nombres_disponibles = nombres_disponibles.exclude(id__in=nombres_excluidos)
            print("Nombres disponibles después de la exclusión:", nombres_disponibles)  # Print para verificar los nombres disponibles
        
        # Incluir el nombre actual en el queryset del campo 'nombre'
        self.fields['nombre'].queryset = nombres_disponibles
        
        # Filtrar usuarios por asignaturas inscritas y perfil "Alumno"
        if asignatura_id:
            # Consulta para obtener las secciones asociadas a la asignatura
            secciones_asignatura = Seccion.objects.filter(asignatura=asignatura_id)
            print("Secciones de la asignatura:", secciones_asignatura)  # Print para verificar las secciones de la asignatura
            
            # Consulta para obtener los IDs de las secciones asociadas a la asignatura
            secciones_asignatura_ids = secciones_asignatura.values_list('id', flat=True)
            print("IDs de las secciones de la asignatura:", secciones_asignatura_ids)  # Print para verificar los IDs de las secciones de la asignatura
            
            # Consulta para filtrar usuarios que están inscritos en la asignatura pero no en otra sección de la misma asignatura
            perfil_alumno = Perfiles.objects.get(nombre='Alumno')
            users_queryset = UsersMetadata.objects.filter(
                perfil=perfil_alumno, asignaturas_inscritas=asignatura_id
            ).exclude(Q(secciones__in=secciones_asignatura_ids) & ~Q(secciones__id=instance.id))
            print("Usuarios queryset:", users_queryset)  # Print para verificar el queryset de usuarios

            self.fields['usuarios'].queryset = users_queryset

    class Meta:
        model = Seccion
        fields = ['nombre', 'usuarios']
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'usuarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }





class ComentarioForm(forms.Form):
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control border border-primary border border-3', 'maxlength': 500, }),
        max_length=500,
        label='Comentario'
    )




