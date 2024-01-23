from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SalidaTerrenoForm, UserCreationWithMetadataForm, UserEditForm, UsersMetadataForm
from .models import SalidaTerreno
from core.decorators import Coordinador_required
from django.contrib.auth.decorators import login_required
from core.models import UsersMetadata
from django.contrib.auth.decorators import login_required
from .forms import UserCreationWithMetadataForm, UsersMetadataForm
from django.contrib import messages
from .forms import AsignaturaForm
import pandas as pd
from django.http import HttpResponseBadRequest
from .utils import store_data_frame_in_session, retrieve_data_frame_from_session, clear_data_frame_from_session
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import Http404



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
    mensaje = ""
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
def gest_usuarios(request):
    if request.method == 'POST':
        form = UsersMetadataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_tu_vista')
    else:
        form = UsersMetadataForm()

    return render(request, 'db_coordinador/db_gest_usuarios.html', {'form': form})


def agreg_usuarios(request):
    if request.method == 'POST':
        user_form = UserCreationWithMetadataForm(request.POST)
        metadata_form = UsersMetadataForm(request.POST)

        if user_form.is_valid() and metadata_form.is_valid():
            user = user_form.save()
            metadata = metadata_form.save(commit=False)
            metadata.user = user
            metadata.username_field = user.username
            metadata.save()
            return redirect('gest-usuarios') 
    else:
        user_form = UserCreationWithMetadataForm()
        metadata_form = UsersMetadataForm()

    return render(request, 'db_coordinador/db_agreg_usuarios.html', {'user_form': user_form, 'metadata_form': metadata_form})


def gest_usuarios(request):
    usuarios = UsersMetadata.objects.all()
    return render(request, 'db_coordinador/db_gest_usuarios.html', {'usuarios': usuarios})


def edit_usuarios(request, id):
    usuario = get_object_or_404(UsersMetadata, id=id)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario.user)
        metadata_form = UsersMetadataForm(request.POST, instance=usuario)

        if user_form.is_valid() and metadata_form.is_valid():
            user_form.save()
            metadata_form.save()

            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('gest-usuarios')

    else:
        user_form = UserEditForm(instance=usuario.user)
        metadata_form = UsersMetadataForm(instance=usuario)

    return render(request, 'db_coordinador/db_edit_usuarios.html', {'user_form': user_form, 'metadata_form': metadata_form, 'usuario': usuario})

def eliminar_usuarios(request, id):
    # Obtén la instancia del usuario que deseas eliminar
    usuario = get_object_or_404(UsersMetadata, id=id)

    if request.method == 'POST':
        # Elimina el usuario
        usuario.user.delete()
        usuario.delete()
        
        # Redirige a la página de lista de usuarios u otra página según tus necesidades
        return redirect('gest-usuarios')

    return render(request, 'ruta_de_la_plantilla_para_confirmar_eliminar.html', {'usuario': usuario})

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

# @login_required
# @Coordinador_required
# def cargar_datos(request):
#     if request.method == 'POST':
#         # Recupera el DataFrame de la sesión del usuario
#         data_frame_dict = request.session.get('data_frame')
#         if data_frame_dict is not None:
#             df = pd.DataFrame.from_dict(data_frame_dict)
            
#             # Aquí puedes procesar el DataFrame y cargar los datos en tu modelo
#             print(df)



#             # Elimina el DataFrame de la sesión del usuario
#             del request.session['data_frame']

#         return redirect('home_coordinador')

#     return HttpResponseBadRequest("Bad Request: Se esperaba una solicitud POST.")


from django.contrib.auth.models import User
from core.models import UsersMetadata, Perfiles  # Asegúrate de ajustar esto con la ruta correcta de tu modelo




# @login_required
# @Coordinador_required
# def cargar_datos(request):
#     if request.method == 'POST':
       
#         data_frame_dict = request.session.get('data_frame')
#         if data_frame_dict is not None:
#             df = pd.DataFrame.from_dict(data_frame_dict)

           
#             for index, row in df.iterrows():
                
#                 rut = row['RUT']
#                 userito=row['CORREO DUOC']
#                 jornada = row['JORNADA']
#                 nombre = row['NOMBRES'].replace(" ", "")  # Elimina espacios del nombre
#                 apellido_paterno = row['AP.PATERNO'].replace(" ", "")  # Elimina espacios del apellido
#                 print(f"-{rut}- {userito} - - {jornada} - - {nombre} - - {apellido_paterno}  - {userito}")
#                 print(f"contraseña = {rut}{jornada}{nombre[:3]}{apellido_paterno[-2:]}")
               
#                 user = User.objects.filter(username=userito).first()

#                 if user:
                    
#                     user.set_password(f"{rut}{jornada}{nombre[:3]}{apellido_paterno[-2:]}")
                    
#                     print(user)
#                     print(user.username)
#                     print(user.password)
#                     user.save()
                    
#                 else:
                    
#                     user = User.objects.create_user(username=userito, password=f"{rut}{jornada}{nombre[:3]}{apellido_paterno[-2:]}")
                    
#                     print(user)
#                     print(user.username)
#                     print(user.password)

               

#             # Elimina el DataFrame de la sesión del usuario
#             del request.session['data_frame']

#         return redirect('home_coordinador')

#     return HttpResponseBadRequest("Bad Request: Se esperaba una solicitud POST.")




@login_required
@Coordinador_required
def cargar_datos(request):
    if request.method == 'POST':
        data_frame_dict = request.session.get('data_frame')
        if data_frame_dict is not None:
            df = pd.DataFrame.from_dict(data_frame_dict)
            # Intenta obtener el objeto Perfil para 'Alumno', o crea uno si no existe
            perfil_alumno, created = Perfiles.objects.get_or_create(id=1, nombre="Alumno")

            for index, row in df.iterrows():
                rut = str(row['RUT']).replace(" ", "") if isinstance(row['RUT'], str) else str(row['RUT'])
                userito = row['CORREO DUOC'].replace(" ", "") 
                jornada = row['JORNADA'].replace(" ", "") 
                nombre = row['NOMBRES'].replace(" ", "")  # Elimina espacios del nombre
                apellido_paterno = row['AP.PATERNO'].replace(" ", "")
                apellido_materno = row['AP.MATERNO'].replace(" ", "")  # Elimina espacios del apellido
                print(f"-{rut}- {userito} - - {jornada} - - {nombre} - - {apellido_paterno}  - {userito}")
                print(f"contraseña = {rut}{jornada}{nombre[:3]}{apellido_paterno[-2:]}")
               
                user = User.objects.filter(username=userito).first()
                

                if user:
                    print(user)
                    print(user.username)
                    print(user.password)
                    print(perfil_alumno)
                    user.save()
                    users_metadata, created = UsersMetadata.objects.get_or_create(user=user)
                    if not created:
                        users_metadata.sexo_id = 1
                        users_metadata.nombres = nombre
                        users_metadata.ap_paterno = apellido_paterno
                        users_metadata.ap_materno = apellido_materno
                        users_metadata.perfil_id = 1
                        users_metadata.save()

    # Si ya existe, actualiza los campos necesarios
    
        
                    
                    # Obtiene o crea el objeto UsersMetadata asociado al usuario
                    
                    # ... y otros campos ...

                    
                    
                else:
                    user = User.objects.create_user(username=userito, password=f"{rut}{jornada}{nombre[:3]}{apellido_paterno[-2:]}")
                    print(user)
                    print(user.username)
                    print(user.password)
                    
                    print(perfil_alumno.id)
                   


                    # Crea el objeto UsersMetadata asociado al nuevo usuario
                    UsersMetadata.objects.create(sexo_id=1,nombres=nombre,ap_paterno=apellido_paterno,ap_materno =apellido_materno, perfil_id=1, user_id=user.id,)

            # Elimina el DataFrame de la sesión del usuario
            del request.session['data_frame']

        return redirect('home_coordinador')

    return HttpResponseBadRequest("Bad Request: Se esperaba una solicitud POST.")