from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tareas", max_length=200)
    description  = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)