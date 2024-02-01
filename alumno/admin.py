# admin.py
from django.contrib import admin
from .models import Estado, Documento_inasis
from core.models import UsersMetadata

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Documento_inasis)
class DocumentoInasisAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'users_metadata', 'salida_terreno', 'estado']
    search_fields = ['nombre', 'users_metadata__user__username']
    list_filter = ['estado']

    # Excluye 'fecha_creacion' del formulario, ya que es un campo no editable
    exclude = ['fecha_creacion']

    def save_model(self, request, obj, form, change):
        # Asigna el usuario actual al campo users_metadata antes de guardar
        obj.users_metadata = UsersMetadata.objects.get(user=request.user)
        obj.save()
