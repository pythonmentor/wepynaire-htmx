from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils import timezone
from django.contrib import messages

from .models import Task
from .forms import TaskCreationForm


def home_view(request):
    tasks = Task.objects.filter(due_datetime__gt=timezone.now()).order_by(
        "due_datetime"
    )
    return TemplateResponse(request, "pages/home/home.html", {"tasks": tasks})


def task_create_view(request):
    tasks = Task.objects.filter(due_datetime__gt=timezone.now()).order_by(
        "due_datetime"
    )
    form = TaskCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, "Votre nouvelle tâche a bien été crée")
            return redirect("home")
        else:
            messages.error(
                request,
                "Une erreur a été rencontrée avec la création de votre tâche",
            )
    return TemplateResponse(
        request, "pages/tasks/create.html", {"tasks": tasks, "form": form}
    )
