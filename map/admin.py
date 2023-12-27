from django.contrib.gis import admin

from .models import PropertyGIS


@admin.register(PropertyGIS)
class PropertyGISAdmin(admin.GISModelAdmin):
    list_display = ("name", "GEOMETRY")