from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path(
        "htmx/tasks/form/display/",
        views.hx_display_form,
        name="htmx-display-form",
    ),
    path(
        "htmx/tasks/button/display/",
        views.hx_display_button,
        name="htmx-display-button",
    ),
    path(
        "htmx/tasks/button/create/",
        views.hx_create_task,
        name="htmx-task-create",
    ),
]
