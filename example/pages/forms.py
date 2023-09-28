from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Task


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class TaskCreationFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "due_datetime")
        widgets = {
            "due_datetime": DateTimeInput,
        }

    def clean_due_datetime(self):
        """Valide que la date et l'heure saisie dans le formulaire sont dans le
        futur."""
        due_datetime = self.cleaned_data["due_datetime"]
        now = timezone.now()
        if due_datetime < now:
            raise ValidationError(
                "La date et l'heure due pour la tâche "
                "doivent être dans le futur !"
            )
        return due_datetime
