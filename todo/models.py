from django.db import models
from datetime import date

class Todo(models.Model):
    
    name = models.CharField(max_length = 100, blank = False, null = False)
    description = models.TextField(blank = False, null = False)
    is_done = models.BooleanField(default = False)
    date = models.DateField(default = date.today())
    estimated_end = models.DateField(blank = True, null = True)
    priority = models.IntegerField(default = 3)

    def __str__(self) -> str:
        return self.name