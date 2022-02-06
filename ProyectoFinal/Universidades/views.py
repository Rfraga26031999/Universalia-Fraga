from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from Universidades.forms import AvatarFormulario, FormularioProfesores, FormularioEstudiantes, FormularioCarreras
from .models import Carrera, Estudiante, Profesor, Avatar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def inicio(request):
  if request.user.is_authenticated:
    avatares = Avatar.objects.filter(user = request.user)
  else:
    avatares = ''
  if avatares:
    avatar_url = avatares.last().imagen.url
  else:
    avatar_url = ''
  return render(request, 'inicio.html', {'avatar_url': avatar_url})

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
  estudiantes = Estudiante.objects.filter(carrera = carrera)
  if carrera:
    estudiantes = Estudiante.objects.filter(Q(titulo__icontains = carrera), Q(descripcion__icontains = carrera)).distinct()
  return render(request, 'buscar.html', {'carrera': carrera, 'estudiantes': estudiantes})

class AvatarView:
  def get_context_data(self, **kwargs):
    contexto = super().get_context_data(**kwargs)
    contexto['avatar_url'] = Avatar.objects.filter(user = self.request.user).last().imagen.url
    return contexto

# PROFESORES
class ProfesorListView(LoginRequiredMixin, AvatarView, ListView):
  model = Profesor
  template_name = 'profesor/profesores.html'
  context_object_name = 'profesores'
class ProfesorDetailView(AvatarView, DetailView):
  model = Profesor
  template_name = 'profesor/ver_profesor.html'
class ProfesorCreateView(AvatarView, CreateView):
  model = Profesor
  success_url = reverse_lazy('profesores')
  template_name = "profesor/formulario_profesores.html"
  form_class = FormularioProfesores
class ProfesorUpdateView(AvatarView, UpdateView):
  model = Profesor
  success_url = reverse_lazy('profesores')
  fields = ['nombre', 'apellido', 'email', 'catedra', 'materia_dictada', 'edad', 'dni']
  template_name = "profesor/editar_profesor.html"
class ProfesorDeleteView(AvatarView, DeleteView):
  model = Profesor
  success_url = reverse_lazy('profesores')
  template_name = 'profesor/borrar_profesor.html'

# ESTUDIANTES
class EstudianteListView(AvatarView, ListView):
  model = Estudiante
  template_name = 'estudiante/estudiantes.html'
  context_object_name = 'estudiantes'
class EstudianteDetailView(AvatarView, DetailView):
  model = Estudiante
  template_name = 'estudiante/ver_estudiante.html'
class EstudianteCreateView(AvatarView, CreateView):
  model = Estudiante
  success_url = reverse_lazy('estudiantes')
  template_name = "estudiante/formulario_estudiantes.html"
  form_class = FormularioEstudiantes
class EstudianteUpdateView(AvatarView, UpdateView):
  model = Estudiante
  success_url = reverse_lazy('estudiantes')
  fields = ['nombre', 'apellido', 'email', 'carrera', 'edad', 'dni', 'legajo']
  template_name = "estudiante/editar_estudiante.html"
class EstudianteDeleteView(AvatarView, DeleteView):
  model = Estudiante
  success_url = reverse_lazy('estudiantes')
  template_name = 'estudiante/borrar_estudiante.html'

# CARRERAS
class CarreraListView(AvatarView, ListView):
  model = Carrera
  template_name = 'carrera/carreras.html'
  context_object_name = 'carreras'
class CarreraDetailView(AvatarView, DetailView):
  model = Carrera
  template_name = 'carrera/ver_carrera.html'
class CarreraCreateView(AvatarView, CreateView):
  model = Carrera
  success_url = reverse_lazy('carreras')
  template_name = "carrera/formulario_carreras.html"
  form_class = FormularioCarreras
class CarreraUpdateView(AvatarView, UpdateView):
  model = Carrera
  success_url = reverse_lazy('carreras')
  fields = ['carrera', 'duracion', 'facultad', 'cantidad_materias']
  template_name = "carrera/editar_carreras.html"
class CarreraDeleteView(AvatarView, DeleteView):
  model = Carrera
  success_url = reverse_lazy('carreras')
  template_name = 'carrera/borrar_carrera.html'

@login_required
def agregar_avatar(request):
  if request.method == 'POST':
    formulario = AvatarFormulario(request.POST, request.FILES)
    if formulario.is_valid():
      avatar = Avatar(user = request.user, imagen = formulario.cleaned_data['imagen'])
      avatar.save()
      return redirect('inicio')
  else:
    formulario = AvatarFormulario()
  return render(request, 'usuario/crear_avatar.html', {'form': formulario})

class Error404(TemplateView):
  template_name = 'errores/404.html'

class Error500(TemplateView):
  template_name = 'errores/500.html'

  @classmethod
  def as_error_view(cls):

    v = cls.as_view()
    def view(request):
      r = v(request)
      r.render()
      return r
    return view