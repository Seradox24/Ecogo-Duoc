from django.apps import AppConfig

default_app_config = 'core.apps.CoreConfig'

def ready(self):
    import core.signals  # Importa el módulo de señales cuando la aplicación está lista
