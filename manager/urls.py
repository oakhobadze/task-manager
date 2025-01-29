from django.urls import path

from manager.views import index, WorkerListView, TaskListView, TaskDetailListView, WorkerDetailListView

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="workers-list"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskDetailListView.as_view(), name="tasks-detail"),
    path("workers/<int:pk>/", WorkerDetailListView.as_view(), name="workers-detail"),
]

app_name = "manager"
