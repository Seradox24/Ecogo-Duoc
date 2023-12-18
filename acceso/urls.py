from django.urls import path
from .views import *



urlpatterns = [
	path('', acceso_login, name="acceso_login"),

]