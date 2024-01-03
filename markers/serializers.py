from rest_framework_gis.serializers import GeoFeatureModelSerializer
from markers.models import Lines, MultiPolygons, OtherRelations, PlacePoint, MultilineStrings

class MarkerSerializer(GeoFeatureModelSerializer):
    class Meta:
        fields = ("ogc_fid", "name")
        geo_field = "GEOMETRY"
        model = MultiPolygons