

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponse

def home(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if (request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form, 'tasks':tasks}

    return render(request, 'index.html', context)

def update_tasks(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'form': form}
    return render(request, 'update_tasks.html',context)

def delete_tasks(request, pk):
    if request.method == "POST":
        item = Task.objects.get(id=pk)
        item.delete()

        return redirect('/')

    return HttpResponse('Something went wrong')
