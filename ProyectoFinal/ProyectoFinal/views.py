from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserChangePasswordForm, UserProfileForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from Universidades.views import AvatarView
from django.contrib.auth.mixins import LoginRequiredMixin

def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      usuario = form.cleaned_data['username']
      contraseña = form.cleaned_data['password']
      user = authenticate(username = usuario, password = contraseña)
      if user is not None:
        login(request, user)
        return redirect('inicio')
      else:
        return render(request, 'usuario/login.html', {'form': form, 'error': 'No es valido el usuario y contraseña.'})
    else:
      return render(request, 'usuario/login.html', {'form': form})  
  else:
    form = AuthenticationForm()
    return render(request, 'usuario/login.html', {'form': form})

class UserCreateView(CreateView):
  model = User
  success_url = reverse_lazy('login')
  template_name = 'usuario/registro.html'
  form_class = UserRegisterForm

class UserChangeView(LoginRequiredMixin, AvatarView, UpdateView):
  form_class = UserProfileForm
  template_name = 'usuario/miperfil.html'
  success_url = reverse_lazy('inicio')

  def get_object(self):
      return self.request.user

class UserLoginView(LoginView):
  template_name = 'usuario/login.html'
  next_page = reverse_lazy('inicio')

@login_required
def cambiar_contraseña(request):
  usuario = request.user
  if request.method == 'POST':
    formulario = UserChangePasswordForm(request.POST)
    if formulario.is_valid():
      data = formulario.cleaned_data
      usuario.set_password(data['password1'])
      usuario.save()
      return redirect('inicio')
  else:
    formulario = UserChangePasswordForm({'email': usuario.email})
  return render(request, 'usuario/cambiar_contraseña.html', {'form': formulario})

def aboutme(request):
  return render(request, 'aboutme.html')