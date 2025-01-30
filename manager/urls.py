from django.urls import path

from manager.views import (index, WorkerListView, TaskListView,
                           TaskDetailListView, WorkerDetailListView, WorkerCreateView,
                           WorkerUpdateView, WorkerDeleteView, TaskCreateView,
                           TaskUpdateView, TaskDeleteView, TaskTypeListView, PositionListView, TaskTypeCreateView,
                           TaskTypeUpdateView, TaskTypeDeleteView, PositionCreateView, PositionUpdateView,
                           PositionDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("tasktypes/", TaskTypeListView.as_view(), name="task-types-list"),
    path("tasktypes/create/", TaskTypeCreateView.as_view(), name="task-types-create"),
    path("tasktypes/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-types-update"),
    path("tasktypes/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-types-delete"),
    path("positions/", PositionListView.as_view(), name="positions-list"),
    path("positions/create/", PositionCreateView.as_view(), name="positions-create"),
    path("positions/<int:pk>/update", PositionUpdateView.as_view(), name="positions-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="positions-delete"),
    path("workers/", WorkerListView.as_view(), name="workers-list"),
    path("workers/<int:pk>/", WorkerDetailListView.as_view(), name="workers-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="workers-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="workers-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="workers-delete"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskDetailListView.as_view(), name="tasks-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="tasks-delete"),
]

app_name = "manager"
