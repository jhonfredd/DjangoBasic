from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('index/', views.indexw, name="index"),
    path('about/', views.about, name="acerca"),
    path('string/<str:username>', views.string, name="string"),
    path('integer/<int:id>', views.entero, name="entero"),
    path('project/', views.project, name="project"),
    path('project/<int:id>', views.project_detail, name="project_detail"),
    path('cltProject/<int:id>', views.consultaProject, name="consultaProject"),
    path('tank/', views.tank, name="tasks"),
    # path('clttank/<int:id>', views.consultaTank, name="consultaltaskpo"),
    # path('clttanknombre/<str:titl>', views.consultaTankN, name="consultartask"),
    path('CrearTask/',views.create_task, name="crate_task"),
    path('CreateProject/',views.create_project, name="create_project")
]
