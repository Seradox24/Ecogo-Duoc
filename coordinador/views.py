from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import SalidaTerreno
from core.decorators import Coordinador_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .forms import UserCreationWithMetadataForm, UsersMetadataForm
from django.contrib import messages
from .forms import AsignaturaForm
import pandas as pd
from django.http import Http404, HttpResponseBadRequest
from .utils import store_data_frame_in_session, retrieve_data_frame_from_session, clear_data_frame_from_session
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import Http404
from coordinador.forms import AsignaturaForm
from core.models import Asignatura
from django.db.models import Q
from django.contrib.auth.models import User
from core.models import UsersMetadata, Perfiles  
from .models import *
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import SalidaTerrenoForm
from .models import SalidaTerreno
from azure.communication.email import EmailClient
from azure.core.credentials import AzureKeyCredential
import uuid





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

from django.http import JsonResponse



def obtener_secciones(request):
    asignaturas_seleccionadas = request.GET.getlist('asignaturas[]')
    secciones = Seccion.objects.filter(asignatura__id__in=asignaturas_seleccionadas)
    
    # Crear una lista de diccionarios con el nombre de la asignatura y el nombre de la sección
    secciones_dict = [{'id': seccion.id, 'asignatura': seccion.asignatura.nombre, 'seccion': seccion.nombre.nombre} for seccion in secciones]
    
    # Imprimir las secciones por consola para verificar
    #for seccion in secciones_dict:
    #    print(seccion)
    
    # Devolver las secciones como una respuesta JSON
    return JsonResponse(secciones_dict, safe=False)

def obtener_asig_base(request):
    asignaturas_seleccionadas = request.GET.getlist('asignaturas[]')
    # Lógica para obtener las opciones de asignatura base basadas en las asignaturas seleccionadas
    opciones_asig_base = ...
    return JsonResponse({'opciones_asig_base': opciones_asig_base})

@login_required
@Coordinador_required
def listar_salida(request):
    salidas = SalidaTerreno.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(salidas, 2)
        salidas = paginator.page(page)
    except:
        raise Http404


    data = {
        'salidas': salidas,
        'paginator': paginator
    }

    return render(request, 'db_coordinador/db_listar_salida.html', data)




@login_required
@Coordinador_required
def editar_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)

    if request.method == 'POST':
        form = SalidaTerrenoForm(request.POST, instance=salida, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect('listar_salida')
        else:
            print('Errores del formulario:')
            print(form.errors)
            print('Errores específicos de docentes_apoyo:')
            print(form.errors.get('docentes_apoyo'))
            print(request.POST)
    else:
        form = SalidaTerrenoForm(instance=salida)
        # Obtener las asignaturas seleccionadas y pasarlas a la plantilla
        asignaturas_seleccionadas = salida.asignaturas.all()
        asignaturas_seleccionadas_ids = [asignatura.id for asignatura in asignaturas_seleccionadas]
        print("Asignaturas seleccionadas:", asignaturas_seleccionadas)

        # Obtener las secciones seleccionadas y pasarlas a la plantilla
        secciones_seleccionadas = salida.secciones.all()
        secciones_seleccionadas_ids = [seccion.id for seccion in secciones_seleccionadas]
        print("Secciones seleccionadas:", secciones_seleccionadas)

    return render(request, 'db_coordinador/db_editar_salida.html', {'form': form, 'instance': salida, 'asignaturas_seleccionadas_ids': asignaturas_seleccionadas_ids, 'secciones_seleccionadas_ids': secciones_seleccionadas_ids,'secciones_seleccionadas': secciones_seleccionadas,})







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
            messages.success(request, "Usuario agregado correctamente!")
            return redirect('gest-usuarios') 
    else:
        user_form = UserCreationWithMetadataForm()
        metadata_form = UsersMetadataForm()

    return render(request, 'db_coordinador/db_agreg_usuarios.html', {'user_form': user_form, 'metadata_form': metadata_form})


def gest_usuarios(request):
    usuarios = UsersMetadata.objects.all().order_by('-id')
    page = request.GET.get('page', 1)



    try:
        paginator = Paginator(usuarios, 5)
        usuarios = paginator.page(page)
    except:
        raise Http404


    data = {
        'usuarios': usuarios,
        'paginator': paginator
    }

    return render(request, 'db_coordinador/db_gest_usuarios.html', data)


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
                nombrecarga = row['NOMBRES']
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
                        users_metadata.nombres = nombrecarga
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
                    UsersMetadata.objects.create(sexo_id=1,nombres=nombrecarga,ap_paterno=apellido_paterno,ap_materno =apellido_materno, perfil_id=1, user_id=user.id,)

            # Elimina el DataFrame de la sesión del usuario
            del request.session['data_frame']

        return redirect('home_coordinador')

    return HttpResponseBadRequest("Bad Request: Se esperaba una solicitud POST.")



def eliminar_usuarios_mv(request):
    # Intenta obtener el DataFrame de la sesión
    data_frame_dict = request.session.get('data_frame')
    
    # Verifica si el DataFrame existe y tiene la columna 'CORREO DUOC'
    if data_frame_dict is not None and 'CORREO DUOC' in data_frame_dict:
        # Crea el DataFrame
        df = pd.DataFrame.from_dict(data_frame_dict)

        # Itera sobre el DataFrame y obtén la lista de correos
        lista_correos = df['CORREO DUOC'].str.replace(" ", "").tolist()

        # Filtra los usuarios que tienen correos en la lista
        users_to_delete = User.objects.filter(username__in=lista_correos)

        # Itera sobre los usuarios y elimínalos junto con sus UsersMetadata asociados
        for user in users_to_delete:
            try:
                user_metadata = UsersMetadata.objects.get(user=user)
                user_metadata.delete()
            except UsersMetadata.DoesNotExist:
                # Maneja la excepción si no se encuentra UsersMetadata para el usuario
                pass
            user.delete()

        # Puedes redirigir a alguna página después de eliminar los usuarios si es necesario
        return redirect('home_coordinador')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista correspondiente

    # Lógica para el caso en que no se encuentre el DataFrame o la columna 'CORREO DUOC'
    return render(request, 'error.html', {'mensaje': 'Error en la sesión de datos o estructura incorrecta del DataFrame'})


@login_required
@Coordinador_required
def agreg_asig(request):
    mensaje = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')[:100]
        sigla = request.POST.get('sigla')[:10]
        nueva_asignatura = Asignatura(nombre=nombre, sigla=sigla)
        nueva_asignatura.save()
        messages.success(request, "Asignatura agregada correctamente!")
        return redirect('gest_asig')

    return render(request, 'db_coordinador/db_coordinador_agreg_asig.html', {'mensaje': mensaje})



@login_required
@Coordinador_required
def gest_asig(request):
    asignaturas = Asignatura.objects.all().order_by('-id')
    asignaturas = reversed(asignaturas) 
    return render(request, 'db_coordinador/db_coordinador_gest_asig.html', {'asignaturas': asignaturas})
    



# @login_required
# @Coordinador_required
# def editar_asignatura(request, asignatura_id):
#     asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    
#     if request.method == 'POST':
#         form = AsignaturaForm(request.POST, instance=asignatura)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Asignatura modificada correctamente!")
#             return redirect('gest_asig')  
#     else:
#         form = AsignaturaForm(instance=asignatura)
    
#     return render(request, 'db_coordinador/db_edit_asig.html', {'form': form, 'asignatura': asignatura})

@login_required
@Coordinador_required
def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    asignatura_form = AsignaturaForm(instance=asignatura)
    seccion_form = SeccionForm(asignatura_id=asignatura_id)
    
    print("Request method:", request.method)

    secciones = Seccion.objects.filter(asignatura=asignatura)


    if request.method == 'POST':
        print("POST request detected")
        
        if 'guardar_asignatura' in request.POST:
            print("Formulario de asignatura enviado")
            asignatura_form = AsignaturaForm(request.POST, instance=asignatura)
            if asignatura_form.is_valid():
                print("Formulario de asignatura válido")
                asignatura_form.save()
                messages.success(request, "Asignatura modificada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de asignatura inválido")
                print("Errores de validación:", asignatura_form.errors)
        elif 'guardar_seccion' in request.POST:
            print("Formulario de sección enviado")
            seccion_form = SeccionForm(request.POST, asignatura_id=asignatura_id)
            if seccion_form.is_valid():
                print("Formulario de sección válido")
                seccion = seccion_form.save(commit=False)
                seccion.asignatura = asignatura
                seccion.save()
                
                # Imprimir los usuarios seleccionados
                print("Usuarios seleccionados:", request.POST.getlist('usuarios'))
                
                # Asignar los usuarios seleccionados al objeto de sección
                seccion.usuarios.set(request.POST.getlist('usuarios'))
                
                messages.success(request, "Sección creada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de sección inválido")
                print("Errores de validación:", seccion_form.errors)
        

        elif 'eliminar_seccion' in request.POST:
            seccion_id = request.POST.get('eliminar_seccion')
            try:
                seccion = Seccion.objects.get(id=seccion_id, asignatura=asignatura)
                seccion.delete()
                messages.success(request, "Sección eliminada correctamente!")
            except Seccion.DoesNotExist:
                 messages.error(request, "La sección que intentas eliminar no existe o no está asociada a esta asignatura.")
            return redirect(reverse('editar_asignatura', kwargs={'asignatura_id': asignatura_id}))
        
@login_required
@Coordinador_required
def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    asignatura_form = AsignaturaForm(instance=asignatura)
    seccion_form = SeccionForm(asignatura_id=asignatura_id)
    
    print("Request method:", request.method)

    secciones = Seccion.objects.filter(asignatura=asignatura)


    if request.method == 'POST':
        print("POST request detected")
        
        if 'guardar_asignatura' in request.POST:
            print("Formulario de asignatura enviado")
            asignatura_form = AsignaturaForm(request.POST, instance=asignatura)
            if asignatura_form.is_valid():
                print("Formulario de asignatura válido")
                asignatura_form.save()
                messages.success(request, "Asignatura modificada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de asignatura inválido")
                print("Errores de validación:", asignatura_form.errors)
        elif 'guardar_seccion' in request.POST:
            print("Formulario de sección enviado")
            seccion_form = SeccionForm(request.POST, asignatura_id=asignatura_id)
            if seccion_form.is_valid():
                print("Formulario de sección válido")
                seccion = seccion_form.save(commit=False)
                seccion.asignatura = asignatura
                seccion.save()
                
                # Imprimir los usuarios seleccionados
                print("Usuarios seleccionados:", request.POST.getlist('usuarios'))
                
                # Asignar los usuarios seleccionados al objeto de sección
                seccion.usuarios.set(request.POST.getlist('usuarios'))
                
                messages.success(request, "Sección creada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de sección inválido")
                print("Errores de validación:", seccion_form.errors)
        

        elif 'eliminar_seccion' in request.POST:
            seccion_id = request.POST.get('eliminar_seccion')
            try:
                seccion = Seccion.objects.get(id=seccion_id, asignatura=asignatura)
                seccion.delete()
                messages.success(request, "Sección eliminada correctamente!")
            except Seccion.DoesNotExist:
                 messages.error(request, "La sección que intentas eliminar no existe o no está asociada a esta asignatura.")
            return redirect(reverse('editar_asignatura', kwargs={'asignatura_id': asignatura_id}))
        
        elif 'editar_seccion' in request.POST:
            seccion_id = request.POST.get('editar_seccion_id')
            seccion_nombre_id = request.POST.get('nombre')  # Obtén el ID del nombre de la sección desde el formulario

            try:
                seccion = Seccion.objects.get(id=seccion_id, asignatura=asignatura)
                nombre_seccion = get_object_or_404(NombreSeccion, id=seccion_nombre_id)  # Recupera la instancia de NombreSeccion
                seccion.nombre = nombre_seccion  # Asigna la instancia de NombreSeccion al campo nombre

                seccion.save()  # Intenta guardar la instancia de Seccion
                messages.success(request, "Sección editada correctamente")
            except Seccion.DoesNotExist:
                messages.error(request, "La sección que intentas editar no existe o no está asociada a esta asignatura.")
            except NombreSeccion.DoesNotExist:
                messages.error(request, "El nombre de la sección proporcionado no es válido.")

            return redirect(reverse('editar_asignatura', kwargs={'asignatura_id': asignatura_id}))

    
    return render(request, 'db_coordinador/db_edit_asig.html', {'asignatura_form': asignatura_form, 'seccion_form': seccion_form, 'asignatura': asignatura,'secciones': secciones})


@login_required
@Coordinador_required
def editar_seccion(request, seccion_id):
    seccion = get_object_or_404(Seccion, id=seccion_id)
    if request.method == 'POST':
        form = EditarSeccionForm(request.POST, instance=seccion)
        if form.is_valid():
            form.save()
            messages.success(request, "Sección editada correctamente")
            return redirect('gest_asig')
    else:
        form = EditarSeccionForm(instance=seccion)
    return render(request, 'db_coordinador/db_edit_seccion.html', {'edi_seccion_form': form, 'seccion': seccion})




@login_required
@Coordinador_required
def eliminar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('gest_asig') 
    return render(request, 'db_coordinador/db_coordinador_gest_asig.html', {'asignatura': asignatura})


@login_required
@Coordinador_required
def semaforo_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)

    if request.method == 'POST':
        form = SalidaTerrenoFormSemaforo(request.POST, instance=salida, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente!")
            return redirect('listar_salida')
    else:
        form = SalidaTerrenoFormSemaforo(instance=salida)

    return render(request, 'db_coordinador/db_semaforo.html', {'form': form, 'instance': salida})



def lista_usuarios(request):
    # Obtener el valor de búsqueda del parámetro GET
    search_query = request.GET.get('search', '')

    # Filtrar los usuarios según el valor de búsqueda
    usuarios = UsersMetadata.objects.filter(
        Q(user__username__icontains=search_query) |
        Q(user__email__icontains=search_query) |
        Q(perfil__nombre__icontains=search_query) |
        Q(sexo__nombre__icontains=search_query) |
        Q(estado__icontains=search_query)
    ).distinct()

    perfil_seleccionado = request.GET.get('perfil', '')
    sexo_seleccionado = request.GET.get('sexo', '')
    print("Usuarios después de la búsqueda: ", usuarios)

    # Aplicar filtros adicionales
    if perfil_seleccionado:
        usuarios_filtrados = usuarios.filter(perfil__nombre=perfil_seleccionado)
        print("Usuarios después del filtro de perfil: ", usuarios_filtrados)
        usuarios = usuarios_filtrados

    if sexo_seleccionado:
        usuarios_filtrados = usuarios.filter(sexo__nombre=sexo_seleccionado)
        print("Usuarios después del filtro de sexo: ", usuarios_filtrados)
        usuarios = usuarios_filtrados

    return render(request, 'db_coordinador/db_gest_usuarios.html', {'usuarios': usuarios})

def ver_perfil_usuario(request, usuario_id):
    usuario = get_object_or_404(usuario, id=usuario_id)
    return render(request, 'db_coordinador/db_gest_usuarios.html', {'usuario': usuario})



@login_required
@Coordinador_required
def manual_coordinador(request):
    return render(request, 'db_coordinador/db_menu_coordinador.html')


#generar pdf para salida 


import io
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from alumno.models import SalidaTerreno, BajaEstudiante
from reportlab.lib.styles import getSampleStyleSheet

def generar_pdf(request, salida_id):
    try:
        salida = SalidaTerreno.objects.get(id=salida_id)
        secciones = salida.seccion.all()

        # Datos para la tabla
        data = []
        # Encabezados de la tabla
        headers = ["Sección", "Estudiante", "Bajada"]

        for seccion in secciones:
            try:
                # Filtrar los estudiantes que pertenecen a la sección
                estudiantes = seccion.alumnos.all()
                for estudiante in estudiantes:
                    bajada = BajaEstudiante.objects.filter(estudiante=estudiante, salida_terreno=salida).first()
                    bajada_nombre = bajada.bajada.nombre if bajada and bajada.bajada else "Sede Valparaíso"
                    data.append([seccion.nombre, str(estudiante), bajada_nombre])
            except BajaEstudiante.DoesNotExist:
                pass  # No hay estudiantes asociados a esta sección

        # Configurar estilos de la tabla
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # Encabezados en color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Texto de encabezado en blanco
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación central
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente en negrita para encabezados
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espacio inferior para encabezados
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Color de fondo para filas de datos
        ])

        # Configurar la tabla
        table = Table([headers] + data)
        table.setStyle(style)

        # Definir estilo para el título
        styles = getSampleStyleSheet()
        style_title = styles["Title"]

        # Crear el documento PDF
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        elements.append(Paragraph("Lista de Estudiantes", style=style_title))
        elements.append(table)

        # Construir el PDF
        doc.build(elements)

        # Devolver el PDF como respuesta
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f'estudiantes_{salida_id}.pdf')

    except SalidaTerreno.DoesNotExist:
        return HttpResponse("La salida a terreno especificada no existe.")




def lista_implementos_salida(request, salida_terreno_id):
    salida_terreno = get_object_or_404(SalidaTerreno, pk=salida_terreno_id)
    implementos = Implemento.objects.all()

    if request.method == 'POST':
        implementos_seleccionados = request.POST.getlist('implementos')
        if salida_terreno.salidaterrenoimplemento_set.exists():
            salida_terreno.salidaterrenoimplemento_set.first().implemento.clear()
        else:
            salida_terreno.salidaterrenoimplemento_set.create(salida_terreno=salida_terreno)
        for implemento_id in implementos_seleccionados:
            implemento = Implemento.objects.get(pk=implemento_id)
            salida_terreno.salidaterrenoimplemento_set.first().implemento.add(implemento)

        # Recuperar los implementos asociados actualizados después de guardar
        implementos_asociados = salida_terreno.salidaterrenoimplemento_set.first().implemento.all()
        return render(request, 'db_coordinador/lista_implementos_salida.html', {'salida_terreno': salida_terreno, 'implementos': implementos, 'implementos_asociados': implementos_asociados})

    # Obtener los implementos asociados si existen
    implementos_asociados = salida_terreno.salidaterrenoimplemento_set.first().implemento.all() if salida_terreno.salidaterrenoimplemento_set.exists() else []

    return render(request, 'db_coordinador/lista_implementos_salida.html', {'salida_terreno': salida_terreno, 'implementos': implementos, 'implementos_asociados': implementos_asociados})




# from django.shortcuts import render, get_object_or_404
# from .models import SalidaTerreno, Seccion

# def enviar_correos(request, salida_id):
#     # Obtener la salida de terreno o devolver un error 404 si no existe
#     salida_terreno = get_object_or_404(SalidaTerreno, pk=salida_id)

#     # Inicializar una lista para almacenar los correos electrónicos
#     correos_electronicos = []

#     # Recorrer todas las secciones asociadas a la salida a terreno
#     for seccion in salida_terreno.secciones.all():
#         # Verificar si hay usuarios asociados a esta sección
#         if seccion.usuarios.exists():
#             # Recorrer todos los usuarios en la sección y obtener su correo electrónico
#             for usuario_metadata in seccion.usuarios.all():
#                 # Verificar si el usuario tiene un correo electrónico registrado
#                 if usuario_metadata.correoduoc:
#                     # Añadir el correo electrónico a la lista de correos electrónicos
#                     correos_electronicos.append(usuario_metadata.correoduoc)
#                 else:
#                     # Enviar un mensaje de advertencia si un usuario no tiene un correo electrónico registrado
#                     print(f"Usuario {usuario_metadata} en la sección {seccion} no tiene correo electrónico registrado.")
#         else:
#             # Enviar un mensaje de advertencia si no hay usuarios asociados a la sección
#             print(f"No hay usuarios en la sección {seccion}")

#     # Imprimir la lista completa de correos electrónicos
#     print(f"Total de correos electrónicos: {len(correos_electronicos)}")
#     print(correos_electronicos)

#     # Renderizar el template con la lista de correos electrónicos
#     return render(request, 'db_coordinador/correos_salida.html', {'correos_electronicos': correos_electronicos})



def enviar_correos(request, salida_id):
    salida_terreno = get_object_or_404(SalidaTerreno, pk=salida_id)
    correos_electronicos = obtener_correos_electronicos(salida_terreno)
    print(correos_electronicos)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            enviar_correo(correos_electronicos, comentario,salida_terreno)
            # Aquí puedes agregar lógica adicional, como redirigir a una página de confirmación.
            return redirect('listar_salida')
    else:
        form = ComentarioForm()

    return render(request, 'db_coordinador/correos_salida.html', {'form': form})

def obtener_correos_electronicos(salida_terreno):
    correos_electronicos = []
    for seccion in salida_terreno.secciones.all():
        for usuario_metadata in seccion.usuarios.all():
            if usuario_metadata.correoduoc:
                correos_electronicos.append(usuario_metadata.correoduoc)
    return correos_electronicos

def generar_id_fecha():
    now = datetime.now()
    # Formato: #DDMMHHMM
    return f"#{now.strftime('%d%m%H%M')}"

import os

def enviar_correo(correos, comentario,salidav):
    try:
        # Configura tu conexión con Azure (como lo estás haciendo en tu ejemplo)
        connection_string = "endpoint=https://eco-comuni.unitedstates.communication.azure.com/;accesskey=T7AYjoP8mjm2MA6UWb3A/qgjsx6EUsOJwK+/awi6s+rwJZaDvrQ04Z4QJmE0iRg35Vy53Fb5ntVs/vXo5VPLdg=="
        client = EmailClient.from_connection_string(connection_string)

        # Carga el contenido HTML desde el archivo
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_html = os.path.join(directorio_actual, "correo.html")
        with open(ruta_html, "r") as file:
            html_content = file.read()

        # Reemplaza las variables en el HTML con los datos dinámicos
        id_fecha = generar_id_fecha()
        salida= salidav
        semaforo_str = str(salida.semaforo)
        lugar_ejecucion_str = str(salida.lugar_ejecucion)

        situacion_str = str(salida.situacion)
        actividad_str = str(salida.actividad)
        # Convierte la fecha en una cadena con el formato "dd/mm/yyyy"
        fecha_ingreso_str = salida.fecha_ingreso.strftime("%d/%m/%Y")
        fecha_fecha_termino_str = salida.fecha_termino.strftime("%d/%m/%Y")
        # Reemplaza la variable en el HTML con la fecha convertida a cadena
        html_content = html_content.replace("{{ f_ingre }}", fecha_ingreso_str)
        #html_content = html_content.format(comentario=comentario, id_fecha=id_fecha)
        html_content = html_content.replace("{{ comentario }}", comentario)
        html_content = html_content.replace("{{ f_term }}", fecha_fecha_termino_str)
        html_content = html_content.replace("{{ lugar_ejecucion }}", lugar_ejecucion_str)
        html_content = html_content.replace("{{ semaforo }}", semaforo_str)
        html_content = html_content.replace("{{ situacion }}", situacion_str)
        html_content = html_content.replace("{{ actividad }}", actividad_str)
        

        # Crea el mensaje y envíalo
        message = {
            "senderAddress": "DoNotReply@ecogo.cloud",
            "recipients": {"to": [{"address": correo} for correo in correos]},
            "content": {
                "messageId": f"unique-{uuid.uuid4()}",
                "subject": f"Salida a terreno: Actualización {id_fecha}",
                "plainText": f"{comentario}\nHola mundo por correo electrónico.",
                "html": html_content
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

        # Verifica si el envío fue exitoso
        if result.successful:
            print("Correo enviado correctamente")
        else:
            print("Error al enviar el correo:", result.error_message)

    except Exception as ex:
        print("Error general:", ex)