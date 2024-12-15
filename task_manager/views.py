from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from task_manager.forms import TaskForm
from task_manager.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("status","-created")


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
    fields = ["name"]
    success_url = reverse_lazy("task_manager:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_manager:tag-list")


def change_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return redirect(reverse("task_manager:task-list"))
