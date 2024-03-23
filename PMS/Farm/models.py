from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Farm(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class PoultryHouse(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    pen_no = models.CharField(max_length=100)

    mortality_rate = models.FloatField()
    production_rate = models.FloatField()
    capacity = models.PositiveIntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"{self.farm.name}'s Poultry House"