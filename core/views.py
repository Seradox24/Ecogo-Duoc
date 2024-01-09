from pyexpat.errors import messages
from django.shortcuts import redirect, render

from core.models import Asignatura

# def guardar_asignatura(request):
#     if request.method == 'POST':
#         nombre = request.POST.get('nombre')
#         sigla = request.POST.get('sigla')
#         docentes_ids = request.POST.getlist('docentes')
#         secciones_ids = request.POST.getlist('secciones')

#         # Crea una nueva instancia de Asignatura
#         nueva_asignatura = Asignatura(nombre=nombre, sigla=sigla)
#         nueva_asignatura.save()

#         # Asigna los docentes seleccionados a la asignatura
#         nueva_asignatura.docentes.add(*docentes_ids)

#         # Asigna las secciones seleccionadas a la asignatura
#         nueva_asignatura.secciones.add(*secciones_ids)

#         # Redirige a una página de confirmación o a donde sea necesario
#         return redirect('pagina_confirmacion')

#     return render(request, 'template.html')
