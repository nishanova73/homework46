from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

# Create your views here.
from webapp.models import Task, STATUS_CHOICES

def main_view(request):
    return render(request, 'main.html')

def tasks_view(request):
    tasks = Task.objects.order_by("status")
    return render(request, 'tasks.html', {'tasks':tasks})

def create_task_view(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {"status_choices":STATUS_CHOICES})
    else:
        description = request.POST.get('description')
        status = request.POST.get('status')
        create_until = request.POST.get('create_until')
        detailed_description = request.POST.get('detailed_description')
        if create_until == '':
            create_until = None
        new_task = Task.objects.create(description=description,
                                       detailed_description = detailed_description,
                                       status=status,
                                       create_until=create_until)
        return redirect("task_view", pk=new_task.pk)

def task_view(request, pk):
   task = get_object_or_404(Task, pk=pk)
   context = {"task": task}
   return render(request, 'task_view.html', context)

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html', {"task":task})
    else:
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.create_until = request.POST.get('create_until')
        task.detailed_description = request.POST.get('detailed_description')
        if task.create_until == '':
            task.create_until = None
        task.save()
        return redirect("task_view", pk=task.pk)
