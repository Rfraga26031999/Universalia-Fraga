from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, EmailField, PositiveIntegerField, PositiveBigIntegerField, DecimalField

class Carrera(Model):
  carrera = CharField(max_length=100)
  duracion = DecimalField(decimal_places=1, max_digits=2)
  facultad = CharField(max_length=40)
  cantidad_materias = IntegerField(verbose_name='Materias')

  def __str__(self):
      return f'{self.carrera}'

class Estudiante(Model):
  nombre = CharField(max_length=40)
  apellido = CharField(max_length=40)
  email = EmailField()
  carrera = CharField(max_length=40)
  edad = PositiveIntegerField()
  dni = PositiveBigIntegerField(verbose_name='DNI')
  legajo = PositiveBigIntegerField()

  def __str__(self):
    return f'{self.nombre} {self.apellido}'

class Profesor(Model):
  nombre = CharField(max_length=40)
  apellido = CharField(max_length=40)
  email = EmailField()
  catedra = CharField(max_length=40)
  materia_dictada = CharField(max_length=50)
  edad = PositiveIntegerField()
  dni = PositiveBigIntegerField(verbose_name='DNI')

  def __str__(self):
      return f'{self.nombre} {self.apellido}'