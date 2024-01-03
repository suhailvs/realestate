from django.contrib.gis import admin

from django.contrib.gis.forms.widgets import OSMWidget
from .models import PropertyGIS

class CustomGeoWidget(OSMWidget):
    template_name = 'gis/custom_layers.html'

@admin.register(PropertyGIS)
class PropertyGISAdmin(admin.GISModelAdmin):
    gis_widget = CustomGeoWidget
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 14,
            'default_lon': 3.4825,
            'default_lat': 50.1906,
        },
    }
    list_display = ("name", "GEOMETRY")

