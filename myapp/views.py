from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import createNewTask, createNewProject

# Create your views here.
def index(request):
    title = "Index Page!!"
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return render(request, 'about.html')
    
def hello(request, username):
    return HttpResponse('hello %s' % username)



def Tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('task : %s'%task.tittle)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    
def Create_task(request):
    if request.method == 'POST':
        form = createNewTask(request.POST)
        Task.objects.create(
            tittle = request.POST['tittle'],
            description = request.POST['description'],
            project_id = '1'
        )
        if form.is_valid():
            messages.info(request, 'Tarea creada!')
            return HttpResponseRedirect('/tasks/')            
    else:
        form = createNewTask()
    
    
    return render(request, 'projects/create_project.html', {
        'form': form
    })
    
def Projects(request):
    # products = list(Project.objects.values())
    # return JsonResponse(products, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def Create_project(request):
    
    if request.method == 'POST':
        form = createNewProject(request.POST)
        Project.objects.create(
            name = request.POST['name']
        )
        if form.is_valid():
            messages.info(request, 'Projecto creado!')
            return HttpResponseRedirect('/projects/')            
    else:
        form = createNewProject()
    
    
    return render(request, 'projects/create_project.html', {
        'form': form
    })