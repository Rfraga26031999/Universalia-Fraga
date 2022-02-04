from django.forms import Form, CharField, IntegerField, EmailField, DecimalField, ImageField, ModelForm
from Universidades.models import Profesor, Carrera, Estudiante
class FormularioEstudiantes(ModelForm):
  nombre = CharField(max_length=40, min_length=3)
  apellido = CharField(max_length=40, min_length=3)
  email = EmailField()
  carrera = CharField(max_length=40, min_length=3)
  edad = IntegerField(min_value=1, max_value=100)
  dni = IntegerField(min_value=5000000, max_value=60000000)
  legajo = IntegerField(min_value=1, max_value=150000)
  class Meta:
    model = Estudiante
    fields = ['nombre', 'apellido', 'email', 'carrera', 'edad', 'dni', 'legajo']

class FormularioCarreras(ModelForm):
  carrera = CharField(max_length=100, min_length = 3)
  duracion = DecimalField(decimal_places= 1, max_digits = 2)
  facultad = CharField(max_length = 40, min_length = 3)
  cantidad_materias = IntegerField(min_value = 1, max_value = 60)
  class Meta:
    model = Carrera
    fields = ['carrera', 'duracion', 'facultad', 'cantidad_materias']

class FormularioProfesores(ModelForm):
  nombre = CharField(max_length = 40, min_length = 3)
  apellido = CharField(max_length = 40, min_length = 3)
  email = EmailField()
  catedra = CharField(max_length = 40, min_length = 3)
  materia_dictada = CharField(max_length = 50, min_length = 3)
  edad = IntegerField(min_value = 1, max_value = 100)
  dni = IntegerField(min_value = 5000000, max_value = 60000000)
  class Meta:
    model = Profesor
    fields = ['nombre', 'apellido', 'email', 'catedra', 'materia_dictada', 'edad', 'dni']

class AvatarFormulario(Form):
  imagen = ImageField(required=True)