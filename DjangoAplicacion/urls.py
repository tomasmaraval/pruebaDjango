from django.shortcuts import render
from django.urls import path
from DjangoAplicacion.views import *

urlpatterns = [
    path('', index),
    path('inicio/', inicio, name='inicio'),
    path('curso/', curso, name='curso'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profes'),
    path('estudiantes/', estudiantes, name='alumnos'),
    path('entregables/', entregables, name='entregables'),
    path('cursos_form/', cursos_form, name='cursos_form')
]