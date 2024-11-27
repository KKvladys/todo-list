from django.urls import path

from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task_create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/task_update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),


]

app_name = "task_manager"
