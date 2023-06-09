from django.http import HttpResponse, JsonResponse
from .models import Project, Tank
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def indexw(request):
    title = 'Django Course!!'
    return render(request,'index.html',{
        'title': title
    })

def hello(request):
    # return HttpResponse("<h2>Hello World</h2>")
    return render(request,"home.html")

def about(request):
    username = 'Super Administrador'
    usernameDic = {'username':"Super Administrador"}
    return render(request,'about.html',{
        'username':username,
        'username1':usernameDic
    })
    # return HttpResponse("<h1>Hola mundo</h1>")

def string(request,username):
    print(username)
    return HttpResponse("<h1>Hola mundwewew %s</h1>"% username)

def entero(request,id):
    result = id + 10 * 2
    return HttpResponse("<h1>Hola mundwewew %s</h1>"% result)

def project(request):
    data = list(Project.objects.values())
    # return JsonResponse(data, safe=False)
    return render(request,'project/project.html',{
        'project':data
    })

def consultaProject(request,id):
    consulta = Project.objects.get(id=id)
    consula1 = get_object_or_404(Project,id=id)    
    return HttpResponse('<h1>project: %s</h1>' % consulta.name)

def tank(request):
    # return HttpResponse('<h1>tank</h1>')
    tasks = Tank.objects.all()
    return render(request,'tasks/tasks.html',{
        'task': tasks
    })

def consultaTank(request,id):
    task = get_object_or_404(Tank,id=id)
    return HttpResponse('<h1>task: %s</h1>' % task.title)

def consultaTankN(request, titl):
    task = Tank.objects.get(title=titl)   
    return HttpResponse('<h1>task: %s</h1>' % task.title)

def create_task(request):
    if request.method == 'GET':
        return render(request,'tasks/create_task.html',{
        'form' : CreateNewTask
        })
    else:
        Tank.objects.create(title=request.POST['title'],description= request.POST['description'], project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request,'project/create_project.html',{
            'form': CreateNewProject
        })   
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')
    
def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    tasks = Tank.objects.filter(project_id = id)
    print(project)
    return render(request, 'project/detail.html',{
        'project': project,
        'tasks': tasks
    })