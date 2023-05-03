from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('index/', views.indexw),
    path('about/', views.about),
    path('string/<str:username>', views.string),
    path('integer/<int:id>', views.entero),
    path('project/', views.project),
    path('cltProject/<int:id>', views.consultaProject),
    path('tank/', views.tank),
    path('clttank/<int:id>', views.consultaTank),
    path('clttanknombre/<str:titl>', views.consultaTankN),
    path('CrearTask/',views.create_task)
    
]
