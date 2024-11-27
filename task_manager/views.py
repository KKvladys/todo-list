from django.shortcuts import render
from django.views import generic

from task_manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_manager/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TagListView(generic.ListView):
    model = Tag