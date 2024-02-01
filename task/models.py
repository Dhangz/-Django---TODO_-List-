from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    HIGH_PRIORITY = 'high'
    MEDIUM_PRIORITY = 'medium'
    LOW_PRIORITY = 'low'

    PRIORITY_CHOICES = [
        (HIGH_PRIORITY, 'High Priority'),
        (MEDIUM_PRIORITY, 'Medium Priority'),
        (LOW_PRIORITY, 'Low Priority'),
    ]

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
