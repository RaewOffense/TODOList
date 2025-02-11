from django.db import models

# Create your models here.

class TodoList(models.Model):
    task = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.task