from django.db import models


class Poultry(models.Model):
    TYPE_CHOICES = (
        ('chicks_kienyeji', 'Chicks (Kienyeji)'),
        ('chicks_broilers', 'Chicks (Broilers)'),
        ('chicks_layers', 'Chicks (Layers)'),
    )
    poultry_house = models.ForeignKey('Farm.PoultryHouse', on_delete=models.CASCADE, to_field='pen_number')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    total_quantity = models.PositiveIntegerField(default=0)
    kienyeji_quantity = models.PositiveIntegerField(default=0)
    broilers_quantity = models.PositiveIntegerField(default=0)
    layers_quantity = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.type == 'chicks_kienyeji':
            self.kienyeji_quantity = self.total_quantity
        elif self.type == 'chicks_broilers':
            self.broilers_quantity = self.total_quantity
        elif self.type == 'chicks_layers':
            self.layers_quantity = self.total_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_type_display()} - {self.total_quantity} ({self.poultry_house})"


class PoultryDeath(models.Model):
    poultry = models.ForeignKey(Poultry, on_delete=models.CASCADE, related_name='deaths')
    date = models.DateField()
    cause = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.poultry} - {self.date} - {self.cause}"