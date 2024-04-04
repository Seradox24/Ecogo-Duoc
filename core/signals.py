from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

from .models import UsersMetadata

@receiver(pre_delete, sender=UsersMetadata)
def eliminar_archivo_adjunto(sender, instance, **kwargs):
    print("Señal pre_delete activada para UsersMetadata")

    # Verificar si la instancia tiene una imagen adjunta
    if instance.foto:
        print("Foto encontrada:", instance.foto)

        # Eliminar el archivo del servidor
        if os.path.isfile(instance.foto.path):
            print("Eliminando archivo:", instance.foto.path)
            os.remove(instance.foto.path)
        else:
            print("No se pudo encontrar el archivo:", instance.foto.path)
    else:
        print("No se encontró ninguna foto adjunta en la instancia")

