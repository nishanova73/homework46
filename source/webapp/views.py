from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from webapp.models import Task, STATUS_CHOICES
from webapp.utils import article_validate


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
        new_task = Task(description=description,
                        status=status,
                        create_until=create_until,
                        detailed_description=detailed_description,)
        errors = article_validate(description, create_until, detailed_description, status)
        if errors:
            return render(request, "create_task.html", {"errors":errors,"task":new_task})
        new_task.save()
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
        errors = article_validate(task.description, task.status, task.create_until, task.detailed_description)
        if errors:
            return render(request, 'task_update.html', {"status_choices": STATUS_CHOICES}, {"errors": errors, "task": task})
        task.save()
        return redirect("task_view" , pk=task.pk)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, "task_delete.html", {"task":task})
    else:
        task.delete()
        return redirect("home")
