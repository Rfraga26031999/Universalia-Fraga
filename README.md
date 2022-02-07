# Universalia

Universalia es un proyecto en desarrollo que busca generar un ambiente de administración y control para las Universidades que lo utilicen y a su vez ser un portal de ayuda para los estudiantes a la hora de buscar una Universidad para estudiar lo que ellos deseen. El usuario podrá buscar por Carrera y ver que estudiantes están inscriptos en la misma para, en caso de querer, poder contactarse con ellos para realizar consultas o pedir opiniones.


## Comenzando 🚀

Para inicializar el proyecto deberás ir al repositorio de GitHub, ir al botón desplegable de _Code_ y descargarlo como .zip. Luego, descomprimirlo donde gustes.

## Pre-requisitos 📋

Dentro de la carpeta _Universalia-Fraga-master_ encontraran un archivo llamado _requirements.txt_ donde verán los programas necesarios para el funcionamiento de Universalia, si no los poseen el proyecto no correrá correctamente.

#### Recomendación
Sugiero realizar las instalaciones dentro del entorno virtual ya generado en el proyecto para no tener problemas en el futuro debido a una instalación global, para ello deberán activarlo con el siguiente comando:
_source env/Scripts/activate_

Podrás comprobar si se activó correctamente si arriba de la ruta donde estas posicionado aparece _(env)_

En caso de querer desactivarlo deberás correr el comando _deactivate_ desde la carpeta _Proyecto final Python_ donde está localizado el entorno virtual.

A continuación, dejo los comandos necesarios para instalar desde la consola lo requerido:

- _pip install Pillow_ (es necesario instalar Pillow para el funcionamiento de las imágenes del Avatar y el correcto correr del servidor)
- _pip install Django_ (con este comando además de instalar _Django_ también instalaremos _tzdata, sqlparse y asgiref_)

## Puesta en marcha 🔧

Al descomprimirlo, tendrás que abrir tu consola de preferencia _(PowerShell, Bash, cmd, etc.)_, posicionarte en la carpeta _Universalia-Fraga-master_ y digitar los siguientes comandos:

- _source env/Scripts/activate_ (este comando es necesario para activar el entorno virtual donde fue desarrollado).

- _cd ProyectoFinal_ (para movernos a la carpeta que posee en manage.py).

- _python manage.py runserver_ (necesario para levantar el servidor y que comience a funcionar).

Una vez realizado todo esto podrás ver el proyecto en funcionamiento desde tu navegador de preferencia escribiendo en la barra de navegación _localhost:8000_ o _http://127.0.0.1:8000/_

#### Aclaración importante antes de continuar.
Estos comandos fueron probados en Windows 10 y 11, en otros sistemas operativos podrían no funcionar.

## Funcionalidades del proyecto ⚙️


## Construido con 🛠️

* [Django](https://www.djangoproject.com/) - Framework basado en Python utilizado para el armado de la aplicación.
* [HTML](https://developer.mozilla.org/es/docs/Web/HTML) - Lenguaje de marcado utilizado para estructurar el proyecto.
* [CSS](https://developer.mozilla.org/es/docs/Web/CSS) - Lenguaje de diseño gráfico utilizado para la parte visual.
* [Bootstrap](https://getbootstrap.com/) - Framework front-end utilizado para estilizar lo visual.

## Autores ✒️
* **Rogelio Fraga** - [Rfraga26031999](https://github.com/Rfraga26031999)

## Expresiones de Gratitud 🎁

* **Martín Gotelli Ferenaz** - *El profe, un genio que nos enseñó un montón 😄* - [MartinGotelli](https://github.com/MartinGotelli)

* **Adam Ezequiel Tolosa** - *Mi tutor, que estuvo desde el inicio del curso apoyándome 😉* - []()

* **Andrés Villanueva** - *Por brindar a la comunidad este modelo de ReadMe tan claro y útil 😊* - [villanuevand](https://github.com/villanuevand)

⌨️ con ❤️ por [Rfraga26031999](https://github.com/Rfraga26031999) 😉👋
