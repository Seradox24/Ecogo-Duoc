from django.shortcuts import render, redirect, get_object_or_404
from core.models import UsersMetadata, Perfiles
from core.decorators import Alumno_required
from django.contrib.auth.decorators import login_required
from coordinador.models import SalidaTerreno
from django.db.models import Q
from django.utils import timezone
# views.py
from django.contrib import messages
from .models import Documento_inasis, Estado
# Ajusta según la estructura de tus modelos


@login_required
@Alumno_required
def home_alumno(request):
    user = request.user

    # Obtén el objeto UsersMetadata asociado al usuario
    user_metadata = UsersMetadata.objects.get(user=user)

    # Filtra las salidas de terreno según la sección, asignatura, situacion del usuario
    # y excluye las salidas de terreno cuya fecha de ingreso ha pasado y cuya fecha de termino ha pasado
    salidas_terreno = SalidaTerreno.objects.filter(
        Q(seccion__alumnos=user_metadata) | Q(asignatura__docentes=user_metadata),
        Q(situacion=6),
        Q(fecha_ingreso__gte=timezone.now()) | Q(fecha_termino__gt=timezone.now())
    ).order_by('fecha_ingreso')

    # Toma la primera salida de terreno después de ordenar
    primera_salida_cercana = salidas_terreno.first()
    print(primera_salida_cercana)

    return render(request, 'db_alumno/db_home.html', {'data': primera_salida_cercana})











@login_required
@Alumno_required
def ji_alumno(request):
    user = request.user
    user_metadata = UsersMetadata.objects.get(user=user)
    salidas_terreno = SalidaTerreno.objects.filter(
    Q(seccion__alumnos=user_metadata) | Q(asignatura__docentes=user_metadata),
    Q(situacion__in=[5, 6]),  # Aquí agregamos la condición para situaciones 5 o 6
    Q(fecha_ingreso__gte=timezone.now()) | Q(fecha_termino__gt=timezone.now())
    ).order_by('fecha_ingreso')
    for salida in salidas_terreno:
        documentos = Documento_inasis.objects.filter(users_metadata=user_metadata, salida_terreno=salida)
        print(documentos)  # Imprime los documentos obtenidos
        salida.documentos = documentos

    


    # Toma la primera salida de terreno después de ordenar primera_salida_cercana = salidas_terreno.first()
    
    print(salidas_terreno)

    return render(request, 'db_alumno/db_alumno_asis.html',{'data': salidas_terreno})














@login_required
@Alumno_required
def msalida_alumno(request):
    return render(request, 'db_alumno/db_alumno_mysali.html')

@login_required
def aperfil(request):
    return render(request, 'db_alumno/db_alumno_perfil.html')

# Create your views here.












@login_required
def subir_documento(request, salida_terreno_id):
    print(salida_terreno_id)
    user = request.user
    salida_terreno = get_object_or_404(SalidaTerreno, id=salida_terreno_id)

    # Verificar si el usuario ya ha subido un documento para esta salida de terreno
    # Cambia "alumno" por "user_metadata" en la siguiente línea
    user_metadata = UsersMetadata.objects.get(user=user)
    documento_existente = Documento_inasis.objects.filter(users_metadata=user_metadata, salida_terreno=salida_terreno).exists()

    if documento_existente:
        print('Ya has subido un documento para esta salida de terreno.')
        return redirect('ji_alumno')

    if request.method == 'POST':
        # Procesar el formulario para subir documentos
        # ...

        # Crear y guardar el documento en la base de datos
        documento = Documento_inasis(
            nombre='gfds',  # Ajusta según los campos de tu formulario
            descripcion='gfds',  # Ajusta según los campos de tu formulario
            archivo=request.FILES['archivo'],  # Ajusta según los campos de tu formulario
            users_metadata=user_metadata,
            salida_terreno=salida_terreno
        )
        documento.save()

        print('Documento subido exitosamente.')
        return redirect('ji_alumno')

    return render(request, 'nombre_de_la_plantilla_para_subir_documento.html', {'salida_terreno': salida_terreno})
   




# Vista para evaluar documentos
@login_required
def evaluar_documento(request, documento_id):
    user = request.user
    documento = get_object_or_404(Documento_inasis, id=documento_id)

    if documento.users_metadata != user:
        print('No tienes permisos para evaluar este documento.')
        return redirect('nombre_de_la_vista_donde_redirigir')

    if request.method == 'POST':
        # Procesar el formulario para evaluar documentos (aceptado o no aceptado)
        # ...

        # Actualizar el estado del documento en la base de datos
        documento.estado = Estado.objects.get(nombre=request.POST['estado'])  # Ajusta según los campos de tu formulario
        documento.save()

        print('Documento evaluado exitosamente.')
        return redirect('nombre_de_la_vista_donde_redirigir')

    return render(request, 'nombre_de_la_plantilla_para_evaluar_documento.html', {'documento': documento})