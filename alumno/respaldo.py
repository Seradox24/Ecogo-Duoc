

@login_required
@Alumno_required
def home_alumno(request,baja_estudiante_id=None):
    user = request.user
    
    now = timezone.now()
    now_chile = now.astimezone(timezone.get_default_timezone())
    print(now_chile)

    # Obtén el objeto UsersMetadata asociado al usuario
    user_metadata = UsersMetadata.objects.get(user=user)

    # Filtra las salidas de terreno según la sección, asignatura, situacion del usuario
    # y excluye las salidas de terreno cuya fecha de ingreso ha pasado y cuya fecha de termino ha pasado
    # salidas_terreno = SalidaTerreno.objects.filter(
    #     Q(situacion=6),
    #     Q(fecha_ingreso__gte=timezone.now()) | Q(fecha_termino__gt=timezone.now())
    # ).order_by('fecha_ingreso')

        # Obtén las asignaturas inscritas por el alumno
    asignaturas_inscritas = user_metadata.asignaturas_inscritas.all()

    print(asignaturas_inscritas)

    # Obtén las secciones en las que está el usuario
    secciones_usuario = user_metadata.secciones.all()

    print(secciones_usuario)

    # Filtra las salidas de terreno según la sección, asignatura, situación del usuario
    # y excluye las salidas de terreno cuya fecha de ingreso ha pasado y cuya fecha de termino ha pasado
    salidas_terreno = SalidaTerreno.objects.filter(
        Q(situacion=6),
        Q(fecha_ingreso__gte=timezone.now()) | Q(fecha_termino__gt=timezone.now()),
        Q(asignaturas__in=asignaturas_inscritas) | Q(secciones__in=secciones_usuario)
    ).order_by('fecha_ingreso')

    # Toma la primera salida de terreno después de ordenar
    primera_salida_cercana = salidas_terreno.first()
      
    if not primera_salida_cercana:
        print("No hay salidas de terreno próximas disponibles para mostrar..")
        return render(request, 'db_alumno/db_home.html', {'data': None})
    
    print(primera_salida_cercana)

    name = primera_salida_cercana.lugar_ejecucion
    name = name.replace(" ", "%20")
    print(name)
    

    # Llamar a la función obtener_clima salida_terreno_id, name, region)
    pronosticos_guardados = obtener_clima(primera_salida_cercana, name)
    current_clima = obtener_current_clima(primera_salida_cercana, name)
    print(pronosticos_guardados)
    print('-----------------')
    print(current_clima)

    

# Suponiendo que tienes una instancia de SalidaTerreno llamada 'salida_terreno'

# Consulta para obtener los pronósticos climáticos asociados a la salida de terreno
    pronosticos = PronosticoClima.objects.filter(salida_terreno=primera_salida_cercana).order_by('-fecha')[:2]


# Invertir el orden de los pronósticos
    pronosticos = reversed(pronosticos)
    print(pronosticos)

# Consulta para obtener el clima actual asociado a la salida de terreno
    clima_actual = CurrentClima.objects.get(salida_terreno=primera_salida_cercana)
    print(clima_actual.ubicacion)

# #seccion de bajada del estudiante 
#     estudiante = user_metadata
#     salida_terreno = primera_salida_cercana

#     # Buscamos una BajaEstudiante existente que coincida con el estudiante y la salida a terreno
#     baja_estudiante = BajaEstudiante.objects.filter(estudiante=estudiante, salida_terreno=salida_terreno).first() if estudiante and salida_terreno else None

#     # Si no encontramos una BajaEstudiante existente, creamos una nueva
#     if not baja_estudiante:
#         baja_estudiante = BajaEstudiante(estudiante=estudiante, salida_terreno=salida_terreno)

#     if request.method == 'POST':
#         form = BajaEstudianteForm(request.POST, instance=baja_estudiante)
#         if form.is_valid():
#             form.save()
#             return redirect('home_alumno')
#     else:
#         form = BajaEstudianteForm(instance=baja_estudiante)

# #implementos
        

#     implementos_asociados = []
#     if primera_salida_cercana:
#         try:
#             # Intentar obtener los implementos asociados a la primera salida de terreno cercana
#             implementos_asociados = primera_salida_cercana.salidaterrenoimplemento_set.first().implemento.all()
#         except SalidaTerrenoImplemento.DoesNotExist:
#             print("No hay implementos asociados a la salida de terreno.")
#         except Exception as e:
#             print(f"Error al obtener los implementos asociados: {e}")    
    





    context = {
        #'form': form,
        'data': primera_salida_cercana,
        'pronostico': pronosticos,
        'current_clima': clima_actual,
        #'baja_estudiante':baja_estudiante,
        #'implementos': implementos_asociados,
    }

    # Renderización de la plantilla con los datos
    return render(request, 'db_alumno/db_home.html', context)