from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
)

from markers.models import MultilineStrings



class MarkerSerializer(
    GeoFeatureModelSerializer
):
    class Meta:
        fields = ("ogc_fid", "name")
        geo_field = "GEOMETRY"
        model = MultilineStrings