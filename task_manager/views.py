from django.shortcuts import render
from django.views import generic

from task_manager.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_list.html"
    queryset = Task.objects.prefetch_related("tags")