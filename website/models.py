from django.db import models

# Create your models here.
class service(models.Model):
    service_name = models.CharField(max_length=40)
    service_desc = models.CharField(max_length=200)