from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Carrera, Estudiante, Profesor
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# def formulario_estudiantes(request):
#   if request.method == 'POST':
#     formulario = FormularioEstudiantes(request.POST)
#     if formulario.is_valid():
#       data = formulario.cleaned_data
#       Estudiante.objects.create(nombre = data['nombre'], apellido = data['apellido'], email = data['email'], carrera = data['carrera'], edad = data['edad'], dni = data['dni'], legajo = data['legajo'])
#       return redirect('estudiantes')
#   else:
#     formulario = FormularioEstudiantes()
#   return render(request, 'formulario_estudiantes.html', {'formulario_estudiantes': formulario})

# def formulario_carreras(request):
#   if request.method == 'POST':
#     formulario = FormularioCarreras(request.POST)
#     if formulario.is_valid():
#       data = formulario.cleaned_data
#       Carrera.objects.create(carrera = data['carrera'], duracion = data['duracion'], facultad = data['facultad'], cantidad_materias = data['cantidad_materias'])
#       return redirect('carreras')
#   else:
#     formulario = FormularioCarreras()
#   return render(request, 'formulario_carreras.html', {'formulario_carreras': formulario})

# def formulario_profesores(request):
#   if request.method == 'POST':
#     formulario = FormularioProfesores(request.POST)
#     if formulario.is_valid():
#       data = formulario.cleaned_data
#     Profesor.objects.create(nombre = data['nombre'], apellido = data['apellido'], email = data['email'], catedra = data['catedra'], materia_dictada = data['materia_dictada'], edad = data['edad'], dni = data['dni'])
#     return redirect('profesores')
#   else:
#     formulario = FormularioProfesores()
#   return render(request, 'formulario_profesores.html', {'formulario_profesores': formulario})

# def borrar_profesores(request, id_profesor):
#     profesor = Profesor.objects.get(id = id_profesor)
#     profesor.delete()
#     return redirect('profesores')

# def actualizar_profesores(request, id_profesor):
#   profesor = Profesor.objects.get(id = id_profesor)
#   if request.method == 'POST':
#     formulario = FormularioProfesores(request.POST)
#     if formulario.is_valid():
#       data = formulario.cleaned_data
#       profesor.nombre = data['nombre']
#       profesor.apellido = data['apellido']
#       profesor.email = data['email']
#       profesor.catedra = data['catedra']
#       profesor.materia_dictada = data['materia_dictada']
#       profesor.edad = data['edad']
#       profesor.dni = data['dni']
#       profesor.save()
#       return redirect('profesores')
#   else:
#     formulario = FormularioProfesores(model_to_dict(profesor))
#   return render(request, 'formulario_profesores.html', {'formulario_profesores': formulario})

def inicio(request):
  return render(request, 'inicio.html')

def estudiantes(request):
  return render(request, 'estudiantes.html', {'estudiantes': Estudiante.objects.all()})

def carreras(request):
  return render(request, 'carreras.html', {'carreras': Carrera.objects.all()})

def profesores(request):
  return render(request, 'profesores.html', {'profesores': Profesor.objects.all()})

def busqueda_carrera(request):
  return render(request, 'busqueda_carrera.html')

def buscar(request):
  carrera = request.GET.get("carrera")
  if carrera:
    estudiantes = Estudiante.objects.filter(carrera = carrera)
    return render(request, 'buscar.html', {'carrera': carrera, 'estudiantes': estudiantes})
  else:
    return HttpResponse('No se envió una carrera registrada.')

# PROFESORES
class ProfesorListView(ListView):
  model = Profesor
  template_name = 'profesores.html'
  context_object_name = 'profesores'
class ProfesorDetailView(DetailView):
  model = Profesor
  template_name = 'ver_profesor.html'
class ProfesorCreateView(CreateView):
  model = Profesor
  success_url = reverse_lazy('profesores')
  fields = ['nombre', 'apellido', 'email', 'catedra', 'materia_dictada', 'edad', 'dni']
  template_name = "formulario_profesores.html"
class ProfesorUpdateView(UpdateView):
  model = Profesor
  success_url = reverse_lazy('profesores')
  fields = ['nombre', 'apellido', 'email', 'catedra', 'materia_dictada', 'edad', 'dni']
  template_name = "formulario_profesores.html"
class ProfesorDeleteView(DeleteView):
  model = Profesor
  success_url = reverse_lazy('profesores')
  template_name = 'borrar_profesor.html'

# ESTUDIANTES
class EstudianteListView(ListView):
  model = Estudiante
  template_name = 'estudiantes.html'
  context_object_name = 'estudiantes'
class EstudianteDetailView(DetailView):
  model = Estudiante
  template_name = 'ver_estudiante.html'
class EstudianteCreateView(CreateView):
  model = Estudiante
  success_url = reverse_lazy('estudiantes')
  fields = ['nombre', 'apellido', 'email', 'carrera', 'edad', 'dni', 'legajo']
  template_name = "formulario_estudiantes.html"
class EstudianteUpdateView(UpdateView):
  model = Estudiante
  success_url = reverse_lazy('estudiantes')
  fields = ['nombre', 'apellido', 'email', 'carrera', 'edad', 'dni', 'legajo']
  template_name = "formulario_estudiantes.html"
class EstudianteDeleteView(DeleteView):
  model = Estudiante
  success_url = reverse_lazy('estudiantes')
  template_name = 'borrar_estudiante.html'

# CARRERAS
class CarreraListView(ListView):
  model = Carrera
  template_name = 'carreras.html'
  context_object_name = 'carreras'
class CarreraDetailView(DetailView):
  model = Carrera
  template_name = 'ver_carrera.html'
class CarreraCreateView(CreateView):
  model = Carrera
  success_url = reverse_lazy('carreras')
  fields = ['carrera', 'duracion', 'facultad', 'cantidad_materias']
  template_name = "formulario_carreras.html"
class CarreraUpdateView(UpdateView):
  model = Carrera
  success_url = reverse_lazy('carreras')
  fields = ['carrera', 'duracion', 'facultad', 'cantidad_materias']
  template_name = "formulario_carreras.html"
class CarreraDeleteView(DeleteView):
  model = Carrera
  success_url = reverse_lazy('carreras')
  template_name = 'borrar_carrera.html'