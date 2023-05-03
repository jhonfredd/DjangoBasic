# DjangoBasic
1.) Revisar en la consola si tenemos python:
    python --version
2.) Revisamos la version del pip:
    pip --version
3.) Si no estan vamos a instalar python url de descarga
    https://www.python.org/downloads/
4.) Despues de instalado python instalamos el ambiente virtual de django
    pip install virtualenv
5.) Revisamos si esta instalado correctamente
    virtualenv --version
6.) Colocamos el nombre en virtualenv 
    virtualenv venv
7.) Activamos el script activate
    .\venv\script\activate
8.) Vamos a F1 y buscamos 
    select interprete
9.) Vamos a F1 y creamos la consola
    create new terminal
10.) Debe se aparecer asi
      (venv) C:\Users\USUARIO\django>
11.) Consultamos si python esta bien instalado 
      python --version
12.) Cnsultamos si pip esta bien instalado en la misma consola
      pip --version
13.) Instalamos Django 
      pip install django
14.) Limpiamos consola 
      cls
15.) Comandos basicos de cmd
      cls -> Limpiar consola
      cd .. -> Salir de una carpeta
      cd nombre -> Entramos a una carpte
      dir -> Listamos las carpertas y archivo
16.) Ejecutamos para ver si esta instalado Django
      django-admin --version
17.) Vemos la version de Django
      python -m django --version
18.) Vemos todos los comandos disponibles
      python -m django help 
19.) Abrir terminar 
      python
20.) Ejecutamos una suma para saber si estamos en la consola de python
      2 + 2
21.) Ejecutamos la importacion de django
       import django
22.) Ejecutamos comando para ver la version de la importacion
      django.get_version()
      '4.2'
      >>> 
23.) Salimos de la consola de python
      exit()
24.) Creamos un proyecto en Django
      django-admin startProject mysite
25.) Ejecutamos ahora el manage.py del venv
      python manage.py runserver 3000 el 3000 es el puerto que ustedes quieran
26.) Creamos una aplicacion 
      python manage.py startapp  nombre del proyecto
27.) Creamos migracion siempre que cambiemos o creemos modelos siempre se ejecuta
      python manage.py makemigrations
28.) Ejecutamos la creacion de la migracion
      python manage.py migrate
30.) Ejecutamos de nuevo la consola del interprete de python
      python manage.py shell
31.) Ejecutamos consultas desde python
      from myapp.models import Project, Tank
32.) Guardamos en una variable para depues usarla
      p = project(name="aplicacion web")
      
