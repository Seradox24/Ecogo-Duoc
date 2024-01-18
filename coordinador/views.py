from django.shortcuts import render, redirect, get_object_or_404
from .forms import SalidaTerrenoForm
from .models import SalidaTerreno
from core.decorators import Coordinador_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from .forms import AsignaturaForm
import pandas as pd
from django.http import HttpResponseBadRequest
from .utils import store_data_frame_in_session, retrieve_data_frame_from_session, clear_data_frame_from_session
from django.http import HttpResponse


@login_required
@Coordinador_required
def home_coordinador(request):
    form = AsignaturaForm()

    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'db_coordinador/db_home_c.html', {'form': form})


@login_required
@Coordinador_required
def gest_users(request):
    return render(request, 'db_coordinador/db_coordinador_gest_users.html')


@login_required
@Coordinador_required
def crear_salida(request):
    mensaje = ""  # Inicializa la variable con un valor predeterminado
    if request.method == 'POST':
        form = SalidaTerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Salida creada correctamente!")
            return redirect(to="listar_salida")
    else:
        form = SalidaTerrenoForm()
    return render(request, 'db_coordinador/db_coordinador_crear_sl.html', {'form': form, 'mensaje': mensaje})


@login_required
@Coordinador_required
def listar_salida(request):
    salidas = SalidaTerreno.objects.all()

    data = {
        'salidas': salidas
    }

    return render(request, 'db_coordinador/db_listar_salida.html', data)


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import SalidaTerrenoForm
from .models import SalidaTerreno

@login_required
@Coordinador_required
def editar_salida(request, id):
    print(id)
    salida = get_object_or_404(SalidaTerreno, id=id)

    if request.method == 'POST':
        form = SalidaTerrenoForm(request.POST, instance=salida, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect('listar_salida')
        else:
            print(form.errors)
    else:
        form = SalidaTerrenoForm(instance=salida)

    return render(request, 'db_coordinador/db_editar_salida.html', {'form': form, 'instance': salida})



@login_required
@Coordinador_required
def eliminar_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)
    salida.delete()
    messages.success(request, "Eliminado correctamente!")
    return redirect(to="listar_salida")



@login_required
@Coordinador_required
def listar_alumnos_sl(request):
    return render(request, 'db_coordinador/db_coordinador_listar_alumnos_sl.html')


@login_required
@Coordinador_required
def carga_masiva_alumno(request):
    if request.method == 'POST':
        file = request.FILES.get('archivo')
        if file is None:
            # Devuelve un mensaje de error si no se ha cargado ningún archivo
            return HttpResponse('<h1>Por favor, cargue un archivo.</h1>')
        
        try:
            df = pd.read_excel(file)
            
            # Almacena el DataFrame en la sesión del usuario
            request.session['data_frame'] = df.to_dict()

            return render(request, 'db_coordinador/vista_previa_carga.html', {'data_frame': df})
        except Exception as e:
            # Devuelve una respuesta HTTP con el mensaje de error
            return HttpResponse('<h1>' + str(e) + '</h1>')
            
    return render(request, 'db_coordinador/db_carga_masiva_alumno.html')


# ...

@login_required
@Coordinador_required
def cargar_datos(request):
    if request.method == 'POST':
        # Recupera el DataFrame de la sesión del usuario
        data_frame_dict = request.session.get('data_frame')
        if data_frame_dict is not None:
            df = pd.DataFrame.from_dict(data_frame_dict)
            
            # Aquí puedes procesar el DataFrame y cargar los datos en tu modelo
            print(df)

            # Elimina el DataFrame de la sesión del usuario
            del request.session['data_frame']

        return redirect('home_coordinador')

    return HttpResponseBadRequest("Bad Request: Se esperaba una solicitud POST.")
