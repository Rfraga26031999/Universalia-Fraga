import email
from django.forms import Form, CharField, IntegerField, EmailField, DecimalField

class FormularioEstudiantes(Form):
  nombre = CharField()
  apellido = CharField()
  email = EmailField()
  carrera = CharField()
  edad = IntegerField()
  dni = IntegerField()
  legajo = IntegerField()

class FormularioCarreras(Form):
  carrera = CharField()
  duracion = DecimalField()
  facultad = CharField()
  cantidad_materias = IntegerField()

class FormularioProfesores(Form):
  nombre = CharField()
  apellido = CharField()
  email = EmailField()
  catedra = CharField()
  materia_dictada = CharField()
  edad = IntegerField()
  dni = IntegerField()