from django.db import models


class Poultry(models.Model):
    TYPE_CHOICES = (
        ('kienyeji', 'Kienyeji'),
        ('broilers', 'Broilers'),
        ('layers', 'Layers'),
    )
    CHICKS_TYPE_CHOICES = (
        ('chicks_kienyeji', 'Chicks (Kienyeji)'),
        ('chicks_broilers', 'Chicks (Broilers)'),
        ('chicks_layers', 'Chicks (Layers)'),
    )
    chicks_type = models.CharField(max_length=20, choices=CHICKS_TYPE_CHOICES, blank=True, null=True)
    poultry_house = models.ForeignKey('Farm.PoultryHouse', on_delete=models.CASCADE, to_field='pen_number')
    poultry_type = models.CharField(max_length=20, choices=TYPE_CHOICES,blank=True, null=True)
    total_quantity = models.PositiveIntegerField(default=0)
    kienyeji_grown_quantity = models.PositiveIntegerField(default=0)
    broilers_grown_quantity = models.PositiveIntegerField(default=0)
    layers_grown_quantity = models.PositiveIntegerField(default=0)
    kienyeji_chicks_quantity = models.PositiveIntegerField(default=0)
    broilers_chicks_quantity = models.PositiveIntegerField(default=0)
    layers_chicks_quantity = models.PositiveIntegerField(default=0)

    def total_chicks_quantity(self):
        chicks_quantity = 0
        if self.chicks_type:
            if self.chicks_type == 'chicks_kienyeji':
                chicks_quantity += self.kienyeji_chicks_quantity
            elif self.chicks_type == 'chicks_broilers':
                chicks_quantity += self.broilers_chicks_quantity
            elif self.chicks_type == 'chicks_layers':
                chicks_quantity += self.layers_chicks_quantity
        return chicks_quantity

    def save(self, *args, **kwargs):
        if self.poultry_type:
            if self.poultry_type == 'kienyeji':
                self.kienyeji_grown_quantity = self.total_quantity
            elif self.poultry_type == 'broilers':
                self.broilers_grown_quantity = self.total_quantity
            elif self.poultry_type == 'layers':
                self.layers_grown_quantity = self.total_quantity

        # Check if chicks_type is selected before updating chicks quantities
        if self.chicks_type:
            if self.chicks_type == 'chicks_kienyeji':
                self.kienyeji_chicks_quantity = self.total_quantity
            elif self.chicks_type == 'chicks_broilers':
                self.broilers_chicks_quantity = self.total_quantity
            elif self.chicks_type == 'chicks_layers':
                self.layers_chicks_quantity = self.total_quantity

        # Calculate the total quantity
        total_quantity = (
                self.kienyeji_grown_quantity + self.broilers_grown_quantity + self.layers_grown_quantity +
                self.kienyeji_chicks_quantity + self.broilers_chicks_quantity + self.layers_chicks_quantity
        )
        self.total_quantity = total_quantity

        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['poultry_type'], name='unique_poultry_type'),
        ]



    def __str__(self):
        if self.poultry_type:

           return f"{self.poultry_type} - {self.total_quantity} ({self.poultry_house})"

        elif self.chicks_type:
            return f"{self.poultry_type} - {self.total_quantity} ({self.poultry_house})"
        else:
            return f"Poultry - {self.total_quantity} ({self.poultry_house})"




class PoultryDeath(models.Model):
    poultry = models.ForeignKey(Poultry, on_delete=models.CASCADE, related_name='deaths')
    date = models.DateField()
    cause = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.poultry} - {self.date} - {self.cause}"