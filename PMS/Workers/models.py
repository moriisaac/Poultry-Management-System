

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('worker', 'Worker'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    is_staff = models.BooleanField(default=False)
    date_employed = models.DateField()
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)

    # Only workers with certain roles will have this set to True

    def __str__(self):
        return self.username



