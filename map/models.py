from django.db import models

# Create your models here.
class Property(models.Model):
    latlngs = models.JSONField(default = list)
    name = models.CharField(max_length=255)
    address = models.TextField()