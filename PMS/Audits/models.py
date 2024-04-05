from django.db import models

class EggReport(models.Model):
    app_name = models.CharField(max_length=100)
    report_type = models.CharField(max_length=50)
    criteria = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)