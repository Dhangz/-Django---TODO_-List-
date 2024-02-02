from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(ModelForm):

  class Meta:
    model = Task
    fields = ['title', 'description', 'priority']

    labels = {
      'title': '',
      'description': '',
      'priority': ''
    }

    widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control item  bg-transparent mb-3 text-light'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-transparent mb-3 text-light', 'style': 'resize: none;', 'rows': '4', 'cols': '20',}),
            'priority': forms.Select(attrs={'class': 'form-select bg-transparent mb-3'}),
        }




