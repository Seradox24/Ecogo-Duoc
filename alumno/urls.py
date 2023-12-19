from django.urls import path
from .views import *

urlpatterns = [
	path('alumno/', home_alumno, name="home_alumno"),
]