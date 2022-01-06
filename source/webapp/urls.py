from django.urls import path
from webapp.views import (main_view,
                          tasks_view,
                          create_task_view,
                          task_view,
                          task_update_view,
                          task_delete_view,)

urlpatterns = [
    path('', main_view, name="main"),
    path('task/', tasks_view, name="home"),
    path('task/create_task/', create_task_view, name="task_add"),
    path('task_view/<int:pk>/', task_view, name="task_view"),
    path('task_view/<int:pk>/update/', task_update_view, name="task_update_view"),
    path('task_view/<int:pk>/delete/', task_delete_view, name="task_delete_view"),
]