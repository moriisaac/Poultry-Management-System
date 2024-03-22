# from django.db import models
# from django.contrib.auth.models import User
#
# class Farm(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#
# class Flock(models.Model):
#     name = models.CharField(max_length=200)
#     farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
#     number_of_birds = models.IntegerField()
#     type_of_birds = models.CharField(max_length=200)
#
# class Egg(models.Model):
#     flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
#     date_laid = models.DateField()
#     quantity = models.IntegerField()
#
#
# class Feed(models.Model):
#     flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
#     date_given = models.DateField()
#     quantity = models.IntegerField()
#
# class Medication(models.Model):
#     flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
#     date_given = models.DateField()
#     quantity = models.IntegerField()
#     name = models.CharField(max_length=200)
#     dosage = models.CharField(max_length=200)
#     notes = models.TextField()

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Farm(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PoultryHouse(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"{self.farm.name}'s Poultry House"

class Chicken(models.Model):
    poultry_house = models.ForeignKey(PoultryHouse, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    health_status = models.CharField(max_length=20)
    weight = models.FloatField()

    def __str__(self):
        return f"{self.breed} in {self.poultry_house}"