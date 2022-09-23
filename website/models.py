from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_desc = models.CharField(max_length=5000)
    service_icon = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.service_name