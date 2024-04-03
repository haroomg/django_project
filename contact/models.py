from django.db import models
from datetime import date


class Contact(models.Model):
    
    name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    emil = models.EmailField(max_length = 100, blank = True, null = True, unique = True)
    phone = models.CharField(max_length = 15, blank = True, null = True, unique = True)
    mibile = models.CharField(max_length = 15, blank = True, null = True, unique = True)
    notes = models.TextField(blank = True, null = True)
    company_name = models.CharField(max_length = 50, blank = False, null = False)
    date = models.DateField(default = date.today())
    
    def __str__(self) -> str:
        return self.name + ' ' + self.last_name
