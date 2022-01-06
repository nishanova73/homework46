from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task, STATUS_CHOICES


def main_view(request):
    return render(request, 'main.html')


def tasks_view(request):
    tasks = Task.objects.order_by("status")
    return render(request, 'tasks.html', {'tasks':tasks})


def create_task_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create_task.html', {"status_choices":STATUS_CHOICES, "form":form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            create_until = form.cleaned_data.get('create_until')
            detailed_description = form.cleaned_data.get('detailed_description')
            new_task = Task.objects.create(description=description,
                                           status=status,
                                           create_until=create_until,
                                           detailed_description=detailed_description,)
            return redirect("task_view", pk=new_task.pk)
        return render(request, "create_task.html", {"form":form})


def task_view(request, pk):
   task = get_object_or_404(Task, pk=pk)
   context = {"task": task}
   return render(request, 'task_view.html', context)

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
                        'description': task.description,
                        'detailed_description': task.detailed_description,
                        'status': task.status,
                        'create_until': task.create_until} )
        return render(request, 'task_update.html', {"task":task, "form":form})
    else:
        if task.create_until == '':
            task.create_until = None
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            task.create_until = request.POST.get('create_until')
            task.detailed_description = request.POST.get('detailed_description')
            task.save()
            return redirect("task_view", pk=task.pk)
        return render(request, 'task_update.html', {"task": task, "form": form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, "task_delete.html", {"task":task})
    else:
        task.delete()
        return redirect("home")
