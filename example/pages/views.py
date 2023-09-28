from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET, require_POST
from django.utils import timezone
from django.contrib import messages

from .models import Task
from .forms import TaskCreationFrom


@require_GET
def home_view(request):
    tasks = Task.objects.filter(due_datetime__gt=timezone.now()).order_by(
        "due_datetime"
    )
    return TemplateResponse(request, "pages/home/home.html", {"tasks": tasks})


@require_GET
def hx_display_button(request):
    return TemplateResponse(request, "pages/home/hx/display-button.html")


@require_GET
def hx_display_form(request):
    form = TaskCreationFrom()
    return TemplateResponse(
        request, "pages/home/hx/display-form.html", {"form": form}
    )


@require_POST
def hx_create_task(request):
    form = TaskCreationFrom(request.POST)
    if not form.is_valid():
        messages.error(
            request, "Une erreur a été détectée dans le formulaire !"
        )
        return TemplateResponse(
            request,
            "pages/home/hx/create-task--error.html",
            {"form": form},
            headers={"HX-Swap": "none"},
        )

    form.save()
    tasks = Task.objects.filter(due_datetime__gt=timezone.now()).order_by(
        "due_datetime"
    )
    messages.success(request, "Votre nouvelle tâche a été créée !")
    return TemplateResponse(
        request, "pages/home/hx/create-task--success.html", {"tasks": tasks}
    )
