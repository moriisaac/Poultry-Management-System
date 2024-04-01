# In feed/models.py

from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    expiry_date = models.DateField()
    administration_method = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=100)
    feeding_time = models.DateTimeField()
    quantity_bought = models.DecimalField(max_digits=10, decimal_places=2,default=10)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    @property
    def total_quantity_remaining(self):
        return self.quantity_bought - self.quantity_used

    @property
    def is_quantity_below_threshold(self):
        if self.total_quantity_remaining < 0.2 * self.quantity_bought:
            return True
        return False
