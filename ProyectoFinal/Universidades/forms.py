import email
from django.forms import Form, CharField, IntegerField, EmailField, DecimalField

class FormularioEstudiantes(Form):
  nombre = CharField(max_length=40)
  apellido = CharField(max_length=40)
  email = EmailField()
  carrera = CharField(max_length=40)
  edad = IntegerField()
  dni = IntegerField()
  legajo = IntegerField()

class FormularioCarreras(Form):
  carrera = CharField(max_length=100)
  duracion = DecimalField(decimal_places=1, max_digits=2)
  facultad = CharField(max_length=40)
  cantidad_materias = IntegerField()

class FormularioProfesores(Form):
  nombre = CharField(max_length=40)
  apellido = CharField(max_length=40)
  email = EmailField()
  catedra = CharField(max_length=40)
  materia_dictada = CharField(max_length=50)
  edad = IntegerField()
  dni = IntegerField()