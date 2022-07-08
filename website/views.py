from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task

# Create your views here.


def index(request):
    tasks = reversed(Task.objects.all())
    return render(request, 'website/index.html', {'tasks': tasks})


def task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except:
        return render(request, 'website/pagenotfound.html', {})
    return render(request, 'website/task.html', {'task': task})


def add(request):
    if request.method == "POST":
        try:
            form = Task(name=request.POST.get('name'),
                        description=request.POST.get('description'))
            form.save()
            return HttpResponseRedirect(".")
        except:
            return render(request, 'website/somethingwentwrong.html', {})
    return render(request, 'website/add.html', {})


def about(request):
    return render(request, 'website/about.html', {})


def update(request, id):
    if request.method == "POST":
        try:
            task = Task.objects.get(pk=id)
            name = request.POST.get("name")
            description = request.POST.get("description")
            task.name = name
            task.description = description
            task.save()
            return HttpResponseRedirect(reverse('website:task', args=[id]))
        except:
            return render(request, 'website/somethingwentwrong.html', {})
    try:
        task = Task.objects.get(pk=id)
    except:
        return render(request, 'website/somethingwentwrong.html', {})
    return render(request, 'website/update.html', {'task': task})


def delete(request, id):
    if request.method == "POST":
        try:
            task = Task.objects.get(pk=id)
            task.delete()
            return HttpResponseRedirect(reverse('website:index'))
        except:
            return render(request, 'website/somethingwentwrong.html', {})
