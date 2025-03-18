
"""
Task app: Views file
"""

from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from tasks.models import Task


class TaskList(ListView):
    """
    Task list Generic List View
    """
    model = Task
    ordering = ["-task_created"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"nlink": "list"})
        return context


class TaskCreate(CreateView):
    """
    Task Create View
    """
    model = Task
    fields = ["task_title", "task_description"]

    def get_success_url(self):
        return reverse("tasks:tasks_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"nlink": "new"})
        return context


class TaskDetails(DetailView):
    """
    Task Detail View
    """
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"nlink": "details"})
        return context


class TaskUpdate(UpdateView):
    """
    Task Update View
    """
    model = Task
    fields = ["task_title", "task_description"]

    def get_success_url(self):
        return reverse("tasks:tasks_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"nlink": "update"})
        return context


class TaskDelete(DeleteView):
    """
    Task Delete View
    """
    model = Task
    success_url = reverse_lazy("tasks:tasks_list")


class Custom404(TemplateView):
    """
    Custom 404 View
    """
    template_name = "tasks/404.html"


class Custom500(TemplateView):
    """
    Custom 500 View
    """
    template_name = "tasks/500.html"
