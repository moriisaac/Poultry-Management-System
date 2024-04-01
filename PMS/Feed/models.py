from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    expiry_date = models.DateField()
    administration_method = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=100)
    feeding_time = models.DateTimeField()
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name