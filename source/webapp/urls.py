from django.urls import path
from webapp.views import main_view, tasks_view, create_task_view, task_view

urlpatterns = [
    path('', main_view),
    path('task/', tasks_view),
    path('task/create_task/', create_task_view),
    path('task_view/<int:pk>/', task_view),
]