from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import FormularioCarreras, FormularioEstudiantes, FormularioProfesores
from .models import Carrera, Estudiante, Profesor


def inicio(request):
  return render(request, 'inicio.html')

def estudiantes(request):
  return render(request, 'estudiantes.html', {'estudiantes': Estudiante.objects.all()})

def carreras(request):
  return render(request, 'carreras.html', {'carreras': Carrera.objects.all()})

def profesores(request):
  return render(request, 'profesores.html', {'profesores': Profesor.objects.all()})

def formulario_estudiantes(request):
  if request.method == 'POST':
    formulario = FormularioEstudiantes(request.POST)
    if formulario.is_valid():
      data = formulario.cleaned_data
      Estudiante.objects.create(nombre = data['nombre'], apellido = data['apellido'], email = data['email'], carrera = data['carrera'], edad = data['edad'], dni = data['dni'], legajo = data['legajo'])
      return redirect('estudiantes')
  else:
    formulario = FormularioEstudiantes()
  return render(request, 'formulario_estudiantes.html', {'formulario_estudiantes': formulario})


def formulario_carreras(request):
  if request.method == 'POST':
    formulario = FormularioCarreras(request.POST)
    if formulario.is_valid():
      data = formulario.cleaned_data
      Carrera.objects.create(carrera = data['carrera'], duracion = data['duracion'], facultad = data['facultad'], cantidad_materias = data['cantidad_materias'])
      return redirect('carreras')
  else:
    formulario = FormularioCarreras()
  return render(request, 'formulario_carreras.html', {'formulario_carreras': formulario})


def formulario_profesores(request):
  if request.method == 'POST':
    formulario = FormularioProfesores(request.POST)
    if formulario.is_valid():
      data = formulario.cleaned_data
    Profesor.objects.create(nombre = data['nombre'], apellido = data['apellido'], email = data['email'], catedra = data['catedra'], materia_dictada = data['materia_dictada'], edad = data['edad'], dni = data['dni'])
    return redirect('profesores')
  else:
    formulario = FormularioProfesores()
  return render(request, 'formulario_profesores.html', {'formulario_profesores': formulario})

def busqueda_carrera(request):
  return render(request, 'busqueda_carrera.html')

def buscar(request):
  carrera = request.GET.get("carrera")
  if carrera:
    estudiantes = Estudiante.objects.filter(carrera = carrera)
    return render(request, 'buscar.html', {'carrera': carrera, 'estudiantes': estudiantes})
  else:
    return HttpResponse('No se envió una carrera registrada.')