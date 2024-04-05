from django.db import models

class ManureRemoval(models.Model):
    date_of_removal = models.DateField()
    destination = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Manure removed on {self.date_of_removal}"