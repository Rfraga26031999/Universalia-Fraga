from django.contrib import admin

from Universidades.models import Carrera, Estudiante, Profesor

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Profesor)