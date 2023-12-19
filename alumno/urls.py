from django.urls import path, include
from .views import *

urlpatterns = [
	path('home/', home_alumno, name="home_alumno"),
]