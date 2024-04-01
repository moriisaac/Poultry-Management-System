from django.db import models

# Create your models here.
from django.db import models

class Medicine(models.Model):
    MEDICINE_TYPES = (
        ('Chicks', 'Chicks'),
        ('Broilers', 'Broilers'),
        ('Layers', 'Layers'),
        ('Other', 'Other')
    )

    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=100)
    medicine_type = models.CharField(max_length=100, choices=MEDICINE_TYPES)

    def __str__(self):
        return self.name