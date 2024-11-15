from functools import wraps
from django.shortcuts import render, redirect
from core.models import UsersMetadata
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from core.models import UsersMetadata

# def Alumno_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         user_metadata = UsersMetadata.objects.get(user=request.user)
#         if user_metadata.perfil.nombre == 'Alumno':
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('no_access')  # Redirige a una vista que indica que no tiene acceso
#     return _wrapped_view

def Alumno_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        try:
            user_metadata = UsersMetadata.objects.get(user=request.user)
            if user_metadata.perfil.nombre == 'Alumno':
                return view_func(request, *args, **kwargs)
            else:
                return redirect('no_access')  # Redirige a una vista que indica que no tiene acceso
        except UsersMetadata.DoesNotExist:
            raise Http404("No se encontraron metadatos para este usuario")
    return _wrapped_view

def Docente_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_metadata = UsersMetadata.objects.get(user=request.user)
        if user_metadata.perfil.nombre == 'Docente':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_access')  # Redirige a una vista que indica que no tiene acceso
    return _wrapped_view

def Coordinador_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_metadata = UsersMetadata.objects.get(user=request.user)
        if user_metadata.perfil.nombre == 'Coordinador':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_access')  # Redirige a una vista que indica que no tiene acceso
    return _wrapped_view

def Pañol_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_metadata = UsersMetadata.objects.get(user=request.user)
        if user_metadata.perfil.nombre == 'Pañol':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_access')  # Redirige a una vista que indica que no tiene acceso
    return _wrapped_view
