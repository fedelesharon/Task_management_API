from django.db import models

# Create your models here.
from django.db import models
class Task(models.Model):
    # Fields for the Task model
    title = models.CharField(max_length=255)  # Task title
    description = models.TextField(blank=True, null=True)  # Task description
    due_date = models.DateField()  # Due date for the task
    completed = models.BooleanField(default=False)  # Task completion status
    priority = models.CharField(
        max_length=10,
        choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')],
        default='Medium',
    )

    def __str__(self):
        return self.title

