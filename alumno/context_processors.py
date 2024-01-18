from django.contrib.auth.models import AnonymousUser
from core.models import UsersMetadata
from django.core.exceptions import ObjectDoesNotExist

def urls_processor(request):
    user = request.user

    # Verificar si el usuario está autenticado
    if not isinstance(user, AnonymousUser):
        try:
            user_metadata = UsersMetadata.objects.get(user=user)
        except ObjectDoesNotExist:
            user_metadata = None

        if user_metadata and hasattr(user_metadata, 'perfil') and hasattr(user_metadata.perfil, 'nombre'):
            perfil_nombre = user_metadata.perfil.nombre

            if perfil_nombre == 'Alumno':
                urls = [
                    {'url': 'home_alumno', 'nombre': 'Home', 'icon': 'fs-5 fa fa-house'},
                    {'url': 'ji_alumno', 'nombre': 'Justificación de Inasistencia', 'icon': 'txt fa fa-heart-circle-plus'},
                    {'url': 'msalida_alumno', 'nombre': 'Mis Salidas', 'icon': 'txt fa fa-person-walking-luggage'},
                    # Añade más URLs para el perfil de alumno aquí
                ]
            elif perfil_nombre == 'Docente':
                urls = [
                    {'url': 'home_docente', 'nombre': 'Home', 'icon': 'fs-5 fa fa-house'},
                    {'url': 'gest_asig', 'nombre': 'Gestionar Asignatura', 'icon': 'txt fa fa-book-bookmark'},

                    # Añade las URLs para el perfil de docente aquí
                ]
            elif perfil_nombre == 'Coordinador':
                urls = [
                    {'url': 'home_coordinador', 'nombre': 'Home', 'icon': 'fs-5 fa fa-house'},
                    {'url': 'listar_salida', 'nombre': 'Gestionar salida a terreno', 'icon': 'txt fa fa-book-bookmark'},
                    
                    {'url': 'gest-usuarios', 'nombre': 'Gestión Usuarios', 'icon': 'txt fa fa-solid fa-users'},
                    {'url': 'carga_masiva_alumno', 'nombre': 'Carga Masiva Estudiantes', 'icon': 'txt fa fa-book-bookmark'},

                    # Añade las URLs para el perfil de coordinador aquí
                ]
            elif perfil_nombre == 'Pañol':
                urls = [
                    # Añade las URLs para el perfil de pañol aquí
                ]
            else:
                urls = []  # Si el usuario no tiene un rol reconocido, no proporcionamos ninguna URL
        else:
            urls = []  # Si el usuario no tiene UsersMetadata, perfil o nombre, no proporcionamos ninguna URL
    else:
        urls = []  # Si el usuario no está autenticado, no proporcionamos ninguna URL

    return {'urls': urls}
