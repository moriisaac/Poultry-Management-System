from django.db import models

class OtherSupply(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
