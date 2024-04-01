# models.py

from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('worker', 'Worker'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    is_staff = models.BooleanField(default=False)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_users'  # Add a different related name here
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_users'  # Add a different related name here
    )

    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
    #     permissions_related_name = 'custom_user_permissions'
    #     groups_related_name = 'custom_user_groups'



class Worker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_employed = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username
