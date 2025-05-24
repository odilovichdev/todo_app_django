from django.http import HttpResponseNotFound
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse, render, redirect

from apps.todo.models import Todo, SubTask


class TodoListView(ListView):
    model = Todo

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['debug_context'] = context.copy()
        return context


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "description"]
    template_name = "todo/todo_update.html"

    def get_success_url(self):
        return reverse("todo:todo_list")


class TodoDeleteView(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse("todo:todo_list")


class TodoDetailView(DetailView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['debug_context'] = context
        return context


class SubtaskCompleteView(View):
    def post(self, request, todo_id, subtask_id):
        try:
            subtask = SubTask.objects.get(id=subtask_id)
            subtask.completed = True
            subtask.save()
        except SubTask.DoesNotExist:
            return HttpResponseNotFound("Subtask Not Found.")
        return redirect("todo:todo_detail", pk=todo_id)


class SubtaskUpdateView(UpdateView):
    model = SubTask
    fields = ['title', 'description']
    template_name = "todo/subtask_update.html"

    def get_success_url(self):
        todo_id = self.object.todo.id
        return reverse("todo:todo_detail", kwargs={"pk": todo_id})

    def get_object(self, queryset=None):
        subtask_id = self.kwargs.get("subtask_id")
        return SubTask.objects.get(id=subtask_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo_id = self.kwargs.get("todo_id")
        context['todo'] = Todo.objects.get(id=todo_id)
        return context

class SubtaskDeleteView(DeleteView):
    model = SubTask
    template_name = "todo/subtask_delete.html"

    def get_success_url(self):
        todo_id = self.kwargs.get("todo_id")
        return reverse("todo:todo_detail", kwargs={"pk": todo_id})

    def get_object(self, queryset=None):
        subtask_id = self.kwargs.get("subtask_id")
        return SubTask.objects.get(id=subtask_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo_id = self.kwargs.get("todo_id")
        context["todo"] = Todo.objects.get(id=todo_id)
        return context










