from django.db import models
from django.contrib.gis.db import models as gismodels
# Create your models here.
class Property(models.Model):
    latlngs = models.JSONField(default = list)
    name = models.CharField(max_length=255)
    address = models.TextField()


class PropertyGIS(gismodels.Model):
    name = gismodels.CharField(max_length=255)
    GEOMETRY = gismodels.MultiPolygonField()