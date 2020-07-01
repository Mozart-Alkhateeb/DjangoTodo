from django.conf import settings
from django.db import models

class Task(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description =  models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.description