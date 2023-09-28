from django.db import models
from django.conf import settings
from django import forms
from django.urls import reverse_lazy
from django_extensions.db.fields import AutoSlugField


class Task(models.Model):
    title = models.CharField(max_length=255)
    due_datetime = models.DateTimeField()
    slug = AutoSlugField(populate_from=["title"])

    def __str__(self):
        return f"{self.title} (due le {self.due_datetime.strftime('%d/%m/%Y à %H:%M')})"
