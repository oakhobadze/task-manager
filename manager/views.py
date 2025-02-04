from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from manager.forms import WorkerCreationForm, WorkerUpdateForm, WorkerSearchForm, TaskSearchForm
from manager.models import Worker, Task, Position, TaskType


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

    return render(request, "home/index.html", context=context)


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    queryset = Position.objects.all()
    context_object_name = "positions"


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:positions-list")
    template_name = "manager/position-create.html"


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:positions-list")
    template_name = "manager/position-update.html"


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    success_url = reverse_lazy("manager:positions-list")
    template_name = "manager/position-delete.html"


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    queryset = TaskType.objects.all()
    context_object_name = "task_types"


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-types-list")
    template_name = "manager/task-type-create.html"


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-types-list")
    template_name = "manager/task-type-update.html"


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-types-list")
    template_name = "manager/task-type-delete.html"


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    queryset = Worker.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm()
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")
        if username:
            return Worker.objects.filter(username__icontains=username)
        return Worker.objects.all()


class WorkerDetailListView(LoginRequiredMixin, DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("manager:workers-list")
    template_name = "manager/worker_create.html"


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("manager:workers-list")
    template_name = "manager/worker_update.html"


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:workers-list")
    template_name = "manager/worker_delete.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    queryset = Task.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        queryset = Task.objects.filter(is_completed=False)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class TaskDetailListView(LoginRequiredMixin, DetailView):
    model = Task
    queryset = Task.objects.all()


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:tasks-list")
    template_name = "manager/task_create.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:tasks-list")
    template_name = "manager/task_update.html"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("manager:tasks-list")
    template_name = "manager/task_delete.html"
