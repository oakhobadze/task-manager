from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from manager.models import Worker, Task


@login_required
def index(request):
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "manager/index.html", context=context)


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    queryset = Worker.objects.all()


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    queryset = Task.objects.all()


class WorkerDetailListView(LoginRequiredMixin, DetailView):
    model = Worker


class TaskDetailListView(LoginRequiredMixin, DetailView):
    model = Task
    queryset = Task.objects.all()
