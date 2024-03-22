from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# # from django.contrib.auth.models import User
# #
# # class Farm(models.Model):
# #     name = models.CharField(max_length=200)
# #     location = models.CharField(max_length=200)
# #     owner = models.ForeignKey(User, on_delete=models.CASCADE)
# #
# # class Flock(models.Model):
# #     name = models.CharField(max_length=200)
# #     farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
# #     number_of_birds = models.IntegerField()
# #     type_of_birds = models.CharField(max_length=200)
# #
# # class Egg(models.Model):
# #     flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
# #     date_laid = models.DateField()
# #     quantity = models.IntegerField()
# #
# #
# # class Feed(models.Model):
# #     flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
# #     date_given = models.DateField()
# #     quantity = models.IntegerField()
# #
# # class Medication(models.Model):
# #     flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
# #     date_given = models.DateField()
# #     quantity = models.IntegerField()
# #     name = models.CharField(max_length=200)
# #     dosage = models.CharField(max_length=200)
# #     notes = models.TextField()
# from django.contrib.auth.models import User
# # Create your models here.
# # from django.db import models
# # from django.contrib.auth.models import User
# #
class Farm(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class EggProduction(models.Model):
    DATE_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly')
    )
    frequency = models.CharField(max_length=10, choices=DATE_CHOICES)
    date_of_production = models.DateField()
    quantity = models.IntegerField()
class PoultryHouse(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"{self.farm.name}'s Poultry House"

class Chicken(models.Model):
    STAGE_CHOICES = (
        ('chicks', 'Chicks'),
        ('layers', 'Layers'),
        ('broilers', 'Broilers'),
        ('others', 'Others')
    )
    stage = models.CharField(max_length=10, choices=STAGE_CHOICES)
    poultry_house = models.ForeignKey(PoultryHouse, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    health_status = models.CharField(max_length=20)

    weight = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} in {self.poultry_house}"

class BrokenEggs(models.Model):

    egg_production = models.ForeignKey(EggProduction, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()

class Feed(models.Model):
    poultry_house = models.ForeignKey(PoultryHouse, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    expiry_date = models.DateField()
    administration_method = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=100)

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=100)

class OtherSupplies(models.Model):
    poultry_house = models.ForeignKey(PoultryHouse, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    expiry_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=100)

class Purchase(models.Model):
    buyer_name = models.CharField(max_length=100)
    buyer_contact = models.CharField(max_length=100)
    buyer_address = models.TextField()
    frequency_choices = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    )
    frequency = models.CharField(max_length=10, choices=frequency_choices)
    quantity = models.IntegerField()
    bird = models.ForeignKey(Chicken, on_delete=models.CASCADE)
# from django.db import models
# from django.conf import settings
# from django.urls import reverse
#
# # User = settings.AUTH_USER_MODEL
#
#
class AuditableModel(models.Model):
    """
    Abstract base model with common fields for audit trail.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    auth_user = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        abstract = True


class FinanceModel(AuditableModel):
    """
    Model for recording sales and purchases with permissions and URL retrieval method.
    """
    category_choices = (('Sale', 'Sale'), ('Purchase', 'Purchase'))
    supplier_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=35)
    is_default = models.BooleanField(default=False)
    category = models.CharField(max_length=10, choices=category_choices)
    invoice_no = models.CharField(max_length=35, unique=True)

    class Meta:
        permissions = (
            ('finance_add_new', 'Can create custom'),
            ('finance_update', 'Can update custom'),
            ('finance_delete', 'Can delete custom'),
            ('finance_report', 'Can view report custom'),
            ('finance_audit_trail', 'Can view audit trail custom')
        )
        verbose_name = 'Sale / Purchase'
        verbose_name_plural = 'Sales / Purchases'
        db_table = 'finance_model'

    def get_absolute_url(self):
        return reverse('finance:update', args=[str(self.id)])


# class ItemDetail(models.Model):
#     """
#     Model for item details associated with a finance model.
#     """
#     invoice_no = models.ForeignKey(FinanceModel, on_delete=models.CASCADE, related_name='item_details')
#     quantity = models.FloatField()
#     unit_price = models.FloatField()
#     amount = models.FloatField()
#     description = models.CharField(max_length=255)
#
#     class Meta:
#         verbose_name = 'Item Detail'
#         verbose_name_plural = 'Item Details'
#         db_table = 'item_detail_model'
#
#



class FinanceModelAudit(models.Model):
    """
    Model for auditing changes to finance models.
    """
    ACTION_CHOICES = (
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted')
    )
    invoice_no = models.CharField(max_length=35)
    item_id = models.IntegerField()
    quantity = models.FloatField(null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    auth_user = models.CharField(max_length=35)
    action_flag = models.CharField(max_length=20, choices=ACTION_CHOICES)

    class Meta:
        verbose_name = 'Sale / Purchase Audit'
        verbose_name_plural = 'Sales / Purchases Audit'
        db_table = 'finance_model_audit'

#
class EggsModel(AuditableModel):
    """
    Model for recording egg production with permissions.
    """
    pen = models.ForeignKey('birds.PenHouse', on_delete=models.RESTRICT, to_field='pen_number')
    date_created = models.DateField(auto_now_add=True)
    time = models.TimeField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.pen}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Egg'
        verbose_name_plural = 'Eggs'
        db_table = 'eggs_model'
        permissions = (
            ('manage_eggs', 'Can manage eggs custom'),
        )


class EggsModelAudit(models.Model):
    """
    Model for auditing changes to egg production.
    """
    pen = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    time = models.TimeField()
    egg_id = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()
    action_flag = models.CharField(max_length=15)
    auth_user = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.pen}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Egg Audit'
        verbose_name_plural = 'Eggs Audit'
        db_table = 'eggs_audit_model'
        permissions = (
            ('manage_eggs_audit', 'Can manage eggs audit custom'),
        )


# class PenHouse(AuditableModel):
#     """
#     Model for recording pen houses with permissions.
#     """
#     pen_number = models.IntegerField(unique=True)
#     pen_name = models.CharField(max_length=60)
#
#     def __str__(self):
#         return f'#{self.pen_number} - {self.pen_name}'
#
#     class Meta:
#         ordering = ['id']
#         verbose_name = 'Penhouse'
#         verbose_name_plural = 'Penhouses'
#         db_table = 'penhouse_model'
#         permissions = (
#             ('birds_manage_pen_house', 'Can manage pen house custom'),
#         )
#
#
# class BirdsStock(AuditableModel):
#     """
#     Model for recording bird stock with permissions.
#     """
#     pen_house = models.ForeignKey(PenHouse, on_delete=models.RESTRICT, related_name='bird_stocks')
#     invoice_no = models.ForeignKey(FinanceModel, on_delete=models.RESTRICT, related_name='bird_stocks')
#     quantity = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.pen_house} - {self.invoice_no}'
#
#     class Meta:
#         verbose_name = 'birds Stock'
#         verbose_name_plural = 'birds Stocks'
#         db_table = 'birds_stock_model'
#         permissions = (
#             ('birds_manage_birds_stock', 'Can manage bird stock custom'),
#         )
#
#
# class MedicineFeed(AuditableModel):
#     """
#     Model for recording medicine and feed with permissions.
#     """
#     CATEGORY_CHOICES = (
#         ('Medicine', 'Medicine'),
#         ('Feed', 'Feed')
#     )
#     category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
#     quantity = models.CharField(max_length=10)
#     description = models.TextField(null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Medicine/Feed'
#         verbose_name_plural = 'Medicines/Feeds'
#         db_table = 'medicine_feed_model'
#         permissions = (
#             ('birds_manage_medicine_feed', 'Can manage medicine/feeds custom'),
#         )
#
#
# class MortalityCull(AuditableModel):
#     """
#     Model for recording mortality and cull with permissions.
#     """
#     CATEGORY_CHOICES = (
#         ('Mortality', 'Mortality'),
#         ('Cull', 'Cull')
#     )
#     category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
#     quantity = models.IntegerField()
#     description = models.TextField(null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Mortality/Cull'
#         verbose_name_plural = 'Mortality/Culls'
#         db_table = 'mortality_cull_model'
#         permissions = (
#             ('birds_can_manage_mortality_cull', 'Can manage mortality/culls custom'),
#         )
