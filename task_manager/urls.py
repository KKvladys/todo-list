from django.urls import path

from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateView,
    TaskDeleteView,
    change_task_status
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task_create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/task_update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/task_delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("/<int:pk>/change-status/", change_task_status, name="task-change-status"),
]

app_name = "task_manager"
