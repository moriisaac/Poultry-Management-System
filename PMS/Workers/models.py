# In workers/models.py

from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    date_employed = models.DateField()
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
