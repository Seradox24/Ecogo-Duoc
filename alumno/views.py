from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from core.models import UsersMetadata, Perfiles
from core.decorators import Alumno_required
from django.contrib.auth.decorators import login_required
from coordinador.models import SalidaTerreno, PronosticoClima, CurrentClima,SalidaTerrenoImplemento
from django.db.models import Q,F
from django.utils import timezone
from django.contrib import messages
import requests
import json
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from pytz import timezone as pytz_timezone
from .forms import *
from django.http import Http404, HttpResponseBadRequest
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages


def obtener_clima(salida_terreno, name):
    # Verificar si existe información actualizada en los últimos 15 minutos
    try:
        ultima_actualizacion = PronosticoClima.objects.filter(salida_terreno=salida_terreno).latest('ultima_actualizacion').ultima_actualizacion
    except PronosticoClima.DoesNotExist:
        ultima_actualizacion = None

    if ultima_actualizacion is not None:
        tiempo_transcurrido = timezone.now() - ultima_actualizacion
        # Si la última actualización es menor a 15 minutos, no se realiza la actualización
        if tiempo_transcurrido < timedelta(hours=5):
            print('Si la última actualización es menor a 5 horas, no se realiza la actualización')
            return []

    # Si no hay información actualizada o han pasado más de 15 minutos, se consulta la API
    
    api_key = '10e980c96dbf46c6991205607240702'
    ubicacion = f'{name},%20Chile'
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={ubicacion}&days=3&aqi=yes&alerts=yes&lang=es'
    response = requests.get(url)
    data = response.json()
    PronosticoClima.objects.filter(salida_terreno=salida_terreno).delete()

    current_clima_data = data['current']
    ultima_actualizacion_api_str = current_clima_data['last_updated']
    print(ultima_actualizacion_api_str)
    ultima_actualizacion_api = datetime.strptime(ultima_actualizacion_api_str, '%Y-%m-%d %H:%M')
    print(ultima_actualizacion_api)
    ultima_actualizacion_api = timezone.make_aware(ultima_actualizacion_api, timezone=timezone.utc)
    print(ultima_actualizacion_api)

    # Extraer la información para los tres días del pronóstico
    pronosticos_guardados = []
    for dia in data['forecast']['forecastday']:
        fecha_str = dia['date']  # Obtener la cadena de fecha
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')  # Convertir la cadena a un objeto datetime
        fecha = timezone.make_aware(fecha, timezone=timezone.utc)

        # Convertir la fecha a la zona horaria de Chile continental
        chile_tz = pytz_timezone('America/Santiago')
        fecha_chile = fecha.astimezone(chile_tz)


        # Verificar si ya existe un pronóstico para esta fecha y salida de terreno
        pronostico_existente = PronosticoClima.objects.filter(salida_terreno=salida_terreno, fecha=fecha_chile).first()
        if pronostico_existente:
            # Actualizar el pronóstico existente con la nueva información
            pronostico_existente.ubicacion = data['location']['name']
            pronostico_existente.region = data['location']['region']
            pronostico_existente.pais = data['location']['country']
            pronostico_existente.temperatura_max = dia['day']['maxtemp_c']
            pronostico_existente.temperatura_min = dia['day']['mintemp_c']
            pronostico_existente.uv_index = dia['day']['uv']
            pronostico_existente.probabilidad_lluvia = dia['day']['daily_chance_of_rain']
            pronostico_existente.condiciones = dia['day']['condition']['text']
            pronostico_existente.icono = dia['day']['condition']['icon']
            pronostico_existente.ultima_actualizacion_api = ultima_actualizacion_api
            pronostico_existente.save()
            pronosticos_guardados.append(pronostico_existente)
        else:
            # Si no existe un pronóstico para esta fecha y salida de terreno, crear uno nuevo
            pronostico = PronosticoClima.objects.create(
                salida_terreno=salida_terreno,
                ubicacion=data['location']['name'],
                region=data['location']['region'],
                pais=data['location']['country'],
                fecha=fecha_chile,
                temperatura_max=dia['day']['maxtemp_c'],
                temperatura_min=dia['day']['mintemp_c'],
                uv_index=dia['day']['uv'],
                probabilidad_lluvia=dia['day']['daily_chance_of_rain'],
                condiciones=dia['day']['condition']['text'],
                icono=dia['day']['condition']['icon'],
                ultima_actualizacion_api=ultima_actualizacion_api
            )
            pronosticos_guardados.append(pronostico)

    return pronosticos_guardados


def obtener_current_clima(salida_terreno, name):
    # Verificar si existe información actualizada en los últimos 15 minutos
    try:
        ultima_actualizacion_servidor = CurrentClima.objects.filter(salida_terreno=salida_terreno).latest('ultima_actualizacion_servidor').ultima_actualizacion_servidor
    except CurrentClima.DoesNotExist:
        ultima_actualizacion_servidor = None

    if ultima_actualizacion_servidor is not None:
        tiempo_transcurrido = timezone.now() - ultima_actualizacion_servidor
        # Si la última actualización es menor a 15 minutos, no se realiza la actualización
        if tiempo_transcurrido < timedelta(minutes=15):
            print('Si la última actualización es menor a 15 minutos, no se realiza la actualización')
            return []

    # Si no hay información actualizada o han pasado más de 15 minutos, se consulta la API
    api_key = '10e980c96dbf46c6991205607240702'
    ubicacion = f'{name},%20Chile'
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={ubicacion}&days=3&aqi=yes&alerts=yes&lang=es'
    response = requests.get(url)
    data = response.json()

    # Extraer la información del clima actual
    current_clima_data = data['current']
    ultima_actualizacion_api_str = current_clima_data['last_updated']
    print(ultima_actualizacion_api_str)
    ultima_actualizacion_api = datetime.strptime(ultima_actualizacion_api_str, '%Y-%m-%d %H:%M')
    print(ultima_actualizacion_api)
    ultima_actualizacion_api = timezone.make_aware(ultima_actualizacion_api, timezone=timezone.utc)
    print(ultima_actualizacion_api)

    # Convertir la fecha a la zona horaria de Chile continental
    chile_tz = pytz_timezone('America/Santiago')
    ultima_actualizacion_servidor = timezone.now().astimezone(chile_tz)

    # Verificar si ya existe un registro para esta salida de terreno
    current_clima_existente = CurrentClima.objects.filter(salida_terreno=salida_terreno).first()
    if current_clima_existente:
        # Actualizar el registro existente con la nueva información
        current_clima_existente.ubicacion = data['location']['name']
        current_clima_existente.region = data['location']['region']
        current_clima_existente.pais = data['location']['country']
        current_clima_existente.temperatura_actual = current_clima_data['temp_c']
        current_clima_existente.condicion_text = current_clima_data['condition']['text']
        current_clima_existente.condicion_icono = current_clima_data['condition']['icon']
        current_clima_existente.ultima_actualizacion_servidor = ultima_actualizacion_servidor
        current_clima_existente.ultima_actualizacion_api = ultima_actualizacion_api
        current_clima_existente.save()
        return [current_clima_existente]
    else:
        # Si no existe un registro, crear uno nuevo
        current_clima = CurrentClima.objects.create(
            salida_terreno=salida_terreno,
            ubicacion=data['location']['name'],
            region=data['location']['region'],
            pais=data['location']['country'],
            temperatura_actual=current_clima_data['temp_c'],
            condicion_text=current_clima_data['condition']['text'],
            condicion_icono=current_clima_data['condition']['icon'],
            ultima_actualizacion_servidor=ultima_actualizacion_servidor,
            ultima_actualizacion_api=ultima_actualizacion_api
        )
        return [current_clima]



@login_required
@Alumno_required
def home_alumno(request, baja_estudiante_id=None):
    # Obtener el usuario que está realizando la solicitud
    user = request.user
    
    # Obtener la hora actual en la zona horaria predeterminada
    now = timezone.now()
    now_chile = now.astimezone(timezone.get_default_timezone())
    print(now_chile)

    try:
        # Obtener los metadatos del usuario
        user_metadata = UsersMetadata.objects.get(user=user)
    except UsersMetadata.DoesNotExist:
        # Manejar el caso en que no se encuentren metadatos para el usuario
        print("No se encontraron metadatos para el usuario.")
        return render(request, 'error.html', {'message': 'No se encontraron metadatos para el usuario.'})

    # Obtener las asignaturas inscritas por el alumno
    asignaturas_inscritas = user_metadata.asignaturas_inscritas.all()
    print(asignaturas_inscritas)

    # Obtener las secciones en las que está el usuario
    secciones_usuario = user_metadata.secciones.all()
    print(secciones_usuario)

    try:
        # Filtrar las salidas de terreno según las condiciones especificadas
        salidas_terreno = SalidaTerreno.objects.filter(
            Q(situacion=6),
            Q(fecha_ingreso__gte=timezone.now()) | Q(fecha_termino__gt=timezone.now()),
            Q(asignaturas__in=asignaturas_inscritas) | Q(secciones__in=secciones_usuario)
        ).order_by('fecha_ingreso')
    except SalidaTerreno.DoesNotExist:
        # Manejar el caso en que no se encuentren salidas de terreno que cumplan con los criterios
        print("No se encontraron salidas de terreno que cumplan con los criterios especificados.")
        return render(request, 'error.html', {'message': 'No se encontraron salidas de terreno que cumplan con los criterios especificados.'})

    # Obtener la primera salida de terreno cercana
    primera_salida_cercana = salidas_terreno.first()
    
    if not primera_salida_cercana:
        # Manejar el caso en que no haya salidas de terreno disponibles
        print("No hay salidas de terreno próximas disponibles para mostrar..")
        return render(request, 'db_alumno/db_home.html', {'data': None})
    
    print(primera_salida_cercana)

    # Reemplazar espacios en blanco en el nombre del lugar de ejecución para usar en la URL de consulta de clima
    name = primera_salida_cercana.lugar_ejecucion
    name = name.replace(" ", "%20")

    # Obtener pronósticos de clima para la salida de terreno
    pronosticos_guardados = obtener_clima(primera_salida_cercana, name)
    current_clima = obtener_current_clima(primera_salida_cercana, name)

    # Obtener los dos últimos pronósticos de clima asociados a la salida de terreno
    pronosticos = PronosticoClima.objects.filter(salida_terreno=primera_salida_cercana).order_by('-fecha')[:2]

    # Invertir el orden de los pronósticos
    pronosticos = reversed(pronosticos)
    print(pronosticos)

    try:
        # Obtener el clima actual asociado a la salida de terreno
        clima_actual = CurrentClima.objects.get(salida_terreno=primera_salida_cercana)
        print(clima_actual.ubicacion)
    except CurrentClima.DoesNotExist:
        # Manejar el caso en que no se encuentre el clima actual
        print("No se encontró el clima actual asociado a la salida de terreno.")
        return render(request, 'error.html', {'message': 'No se encontró el clima actual asociado a la salida de terreno.'})

    # Construir el contexto para pasar a la plantilla
    context = {
        'data': primera_salida_cercana,
        'pronostico': pronosticos,
        'current_clima': clima_actual,
    }

    # Renderizar la plantilla con el contexto
    return render(request, 'db_alumno/db_home.html', context)

    






@login_required
@Alumno_required
def ji_alumno(request):


    
    
    
    



    


    # Toma la primera salida de terreno después de ordenar primera_salida_cercana = salidas_terreno.first()
    
    

    return render(request, 'db_alumno/db_alumno_asis.html',{})














@login_required
@Alumno_required
def msalida_alumno(request):
    salidas = SalidaTerreno.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(salidas, 5)
        salidas = paginator.page(page)
    except:
        raise Http404


    data = {
        'salidas': salidas,
        'paginator': paginator
    }

    return render(request, 'db_alumno/db_alumno_mysali.html',data)

@login_required
def aperfil(request):
    if request.method == 'POST':
        form = DocumentoCerMedicoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            # Obtener el nombre de usuario
            nombre_usuario = request.user.username
            # Concatenar los datos y guardarlos en el documento
            documento.nombre = f"Ficha médica alumno {nombre_usuario}"
            documento.descripcion = f"Documento subido el día {timezone.now().strftime('%d %b %Y')}"
            documento.users_metadata = request.user.usersmetadata
            documento.save()
            messages.success(request, 'Documento subido exitosamente.')
            return redirect('aperfil')
    else:
        form = DocumentoCerMedicoForm()
    documentos = DocumentoCerMedico.objects.filter(users_metadata=request.user.usersmetadata)
    return render(request, 'db_alumno/db_alumno_asis.html', {'form': form, 'documentos': documentos})

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