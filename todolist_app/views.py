from django.shortcuts import render, redirect 
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from random import choice
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

def index(request):
    context  = {'welcome_text': 'Welcome to the index Page'}
    return render(request, 'index.html', context)

@login_required
def todolist(request):
    # list of all the object of the class from the db
    if request.method == "POST":
        form =  TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage =  request.user
            form.save()
        messages.success(request, "Task Added Successfully")
        return redirect("todolist")
    else:            
        all_tasks = TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 5)
        page  = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def randomFunc():
    
    for number in range(1, 25):
        obj = TaskList()
        obj.task = "Random Task " + str(number)
        obj.done  =  choice(['True', 'False'])
        obj.save()
        
# for editing a task
@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        task  =  TaskList.objects.get(id = task_id)
        form =  TaskForm(request.POST or None, instance = task)
        if task.manage == request.user:
            if form.is_valid():
                form.save()
            
            messages.success(request, "Task Edited Successfully")
        else:
            messages.error(request, "Access Denied!")
        return redirect("todolist")
    else:
        task_obj = TaskList.objects.get(pk =  task_id)
        if task_obj.manage == request.user:
            return render(request, 'edit.html', {'task_obj': task_obj})
        else:
            messages.error(request, "Access Denied!")
            return redirect('todolist')
    
# for marking a task a completed
@login_required
def complete_task(request, task_id): # can also use 'pk' for primary key 
    task  =  TaskList.objects.get(id = task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, "Access Denied!")
    return redirect('todolist')

# for marking a task as pending
@login_required
def pending_task(request, task_id): # can also use 'pk' for primary key 
    task  =  TaskList.objects.get(id = task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, "Access Denied!")
    return redirect('todolist')

# for deletion of a task
@login_required
def delete_task(request, task_id): # can also use 'pk' for primary key 
    task  =  TaskList.objects.get(id = task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, "Access Denied!")
    return redirect('todolist')


def about(request):
    context  = {'welcome_text': 'Welcome to the About Page'}
    return render(request, 'about.html', context)

def contact(request):
    context  = {'welcome_text': 'Welcome to the contact page' }
    return render(request, 'contact.html', context)
    

def random_task(request, id):
    s =  SessionStore()
    s.create()
    s.set_expiry(300)
    task = s.get_expiry_age()
    return render(request, 'random.html', {'task': task})
    