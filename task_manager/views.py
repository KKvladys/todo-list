from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import TaskForm
from task_manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_manager/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_manager:tag-list")
