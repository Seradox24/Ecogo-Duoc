from django.urls import path
from .views import *

urlpatterns = [
	path('', home_alumno, name="home_alumno"),
]