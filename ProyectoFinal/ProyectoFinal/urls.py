"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from ProyectoFinal.views import login_request, UserCreateView, UserChangeView, cambiar_contraseña, aboutme
from django.contrib.auth.views import LogoutView
from Universidades.views import inicio, Error404, Error500
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Universidades/', include('Universidades.urls')),
    path('login/', login_request, name = 'login'),
    path('registro/', UserCreateView.as_view(), name = 'registro'),
    path('logout/', LogoutView.as_view(template_name = 'usuario/logout.html'), name = 'logout'),
    path('', inicio, name = 'inicio'),
    path('miperfil/', UserChangeView.as_view(), name="miperfil"),
    path('cambiarcontraseña/', cambiar_contraseña, name="cambiar_contraseña"),
    path('aboutme/', aboutme, name="aboutme"),
]

handler404 = Error404.as_view()
handler500 = Error500.as_error_view()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)