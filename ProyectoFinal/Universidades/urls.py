from django.urls import path
from Universidades.views import inicio, ProfesorListView, busqueda_carrera, buscar, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView, ProfesorDetailView, EstudianteCreateView, EstudianteDeleteView, EstudianteDetailView, EstudianteListView, EstudianteUpdateView, CarreraCreateView, CarreraDeleteView, CarreraDetailView, CarreraListView, CarreraUpdateView

urlpatterns = [
    path('inicio/', inicio, name = 'inicio'),
    path('estudiantes/', EstudianteListView.as_view(), name = 'estudiantes'),
    path('carreras/', CarreraListView.as_view(), name = 'carreras'),
    path('profesores/', ProfesorListView.as_view(), name = 'profesores'),
    path('formularioestudiantes/', EstudianteCreateView.as_view(), name = 'formulario_estudiantes'),
    path('formulariocarreras/', CarreraCreateView.as_view(), name = 'formulario_carreras'),
    path('formularioprofesores/', ProfesorCreateView.as_view(), name = 'formulario_profesores'),
    path('busquedacarrera/', busqueda_carrera, name = 'busqueda_carrera'),
    path('buscar/', buscar, name = 'buscar'),
    path('borrarprofesores/<pk>', ProfesorDeleteView.as_view(), name = 'borrar_profesores'),
    path('actualizarprofesores/<pk>', ProfesorUpdateView.as_view(), name = 'actualizar_profesores'),
    path('verprofesor/<pk>', ProfesorDetailView.as_view(), name = 'ver_profesor'),
    path('borrarestudiantes/<pk>', EstudianteDeleteView.as_view(), name = 'borrar_estudiantes'),
    path('actualizarestudiantes/<pk>', EstudianteUpdateView.as_view(), name = 'actualizar_estudiantes'),
    path('verestudiante/<pk>', EstudianteDetailView.as_view(), name = 'ver_estudiante'),
    path('borrarcarreras/<pk>', CarreraDeleteView.as_view(), name = 'borrar_carreras'),
    path('actualizarcarreras/<pk>', CarreraUpdateView.as_view(), name = 'actualizar_carreras'),
    path('vercarrera/<pk>', CarreraDetailView.as_view(), name = 'ver_carrera'),
]