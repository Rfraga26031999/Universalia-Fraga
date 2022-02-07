from django.urls import path
from Universidades.views import inicio, ProfesorListView, buscar, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView, ProfesorDetailView, EstudianteCreateView, EstudianteDeleteView, EstudianteDetailView, EstudianteListView, EstudianteUpdateView, CarreraCreateView, CarreraDeleteView, CarreraDetailView, CarreraListView, CarreraUpdateView, agregar_avatar

urlpatterns = [
    path('inicio/', inicio, name = 'inicio'),
    path('estudiantes/', EstudianteListView.as_view(), name = 'estudiantes'),
    path('carreras/', CarreraListView.as_view(), name = 'carreras'),
    path('profesores/', ProfesorListView.as_view(), name = 'profesores'),
    path('formularioestudiantes/', EstudianteCreateView.as_view(), name = 'formulario_estudiantes'),
    path('formulariocarreras/', CarreraCreateView.as_view(), name = 'formulario_carreras'),
    path('formularioprofesores/', ProfesorCreateView.as_view(), name = 'formulario_profesores'),
    path('buscar/', buscar, name = 'buscar'),
    path('borrarprofesores/<pk>', ProfesorDeleteView.as_view(), name = 'borrar_profesores'),
    path('editarprofesores/<pk>', ProfesorUpdateView.as_view(), name = 'editar_profesor'),
    path('verprofesor/<pk>', ProfesorDetailView.as_view(), name = 'ver_profesor'),
    path('borrarestudiantes/<pk>', EstudianteDeleteView.as_view(), name = 'borrar_estudiantes'),
    path('editarestudiantes/<pk>', EstudianteUpdateView.as_view(), name = 'editar_estudiantes'),
    path('verestudiante/<pk>', EstudianteDetailView.as_view(), name = 'ver_estudiante'),
    path('borrarcarreras/<pk>', CarreraDeleteView.as_view(), name = 'borrar_carreras'),
    path('editarcarreras/<pk>', CarreraUpdateView.as_view(), name = 'editar_carreras'),
    path('vercarrera/<pk>', CarreraDetailView.as_view(), name = 'ver_carrera'),
    path('agregaravatar/', agregar_avatar, name = 'agregar_avatar'),
]