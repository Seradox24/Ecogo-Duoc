from django.urls import include, path
from .views import *



urlpatterns = [
	path('', acceso_login, name="acceso_login"),
	
]