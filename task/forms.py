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
            'title': forms.TextInput(attrs={'class': 'form-control bg-transparent mb-3', 'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-transparent mb-3', 'placeholder': 'Decription'}),
            'priority': forms.Select(attrs={'class': 'form-select bg-transparent mb-3', 'placeholder': 'Priority'}),
        }




