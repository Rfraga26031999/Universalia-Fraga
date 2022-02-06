from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import EmailField, CharField, PasswordInput, EmailInput, TextInput
from django.contrib.auth.models import User
from Universidades.views import AvatarView

class UserRegisterForm(UserCreationForm):
  email = EmailField()
  password1 = CharField(label = 'Contraseña', widget = PasswordInput)
  password2 = CharField(label = 'Repetir contraseña.', widget = PasswordInput)
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts = {k:'' for k in fields}

class UserEditForm(AvatarView, UserCreationForm):
  email = EmailField()
  password1 = CharField(label = 'Contraseña', widget = PasswordInput)
  password2 = CharField(label = 'Repetir contraseña.', widget = PasswordInput)
  first_name = CharField()
  last_name = CharField()
  class Meta:
    model = User
    fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
    help_texts = {k:'' for k in fields}

class UserProfileForm(AvatarView, UserChangeForm):
  password = None
  email = EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
  first_name = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
  last_name = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
  username = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name', 'username']

class UserChangePasswordForm(AvatarView, UserCreationForm):
  password1 = CharField(label = 'Contraseña', widget = PasswordInput, required=False)
  password2 = CharField(label = 'Repetir contraseña.', widget = PasswordInput, required=False)
  class Meta:
    model = User
    fields = ['password1', 'password2']
    help_texts = {k:'' for k in fields}