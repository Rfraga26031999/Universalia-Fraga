from django.urls import path
from Universidades.views import inicio, estudiantes, carreras, profesores, formulario_estudiantes, formulario_carreras, formulario_profesores, busqueda_carrera, buscar

urlpatterns = [
    path('inicio/', inicio, name = 'inicio'),
    path('estudiantes/', estudiantes, name = 'estudiantes'),
    path('carreras/', carreras, name = 'carreras'),
    path('profesores/', profesores, name = 'profesores'),
    path('formularioestudiantes/', formulario_estudiantes, name = 'formulario_estudiantes'),
    path('formulariocarreras/', formulario_carreras, name = 'formulario_carreras'),
    path('formularioprofesores/', formulario_profesores, name = 'formulario_profesores'),
    path('busquedacarrera/', busqueda_carrera, name = 'busqueda_carrera'),
    path('buscar', buscar, name = 'buscar'),
]