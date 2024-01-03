import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from markers.models import Lines, MultiPolygons, OtherRelations, PlacePoint, MultilineStrings


from rest_framework import viewsets
from rest_framework_gis import filters

from markers.serializers import MarkerSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "GEOMETRY"
    filter_backends = (filters.InBBoxFilter,)
    queryset = MultiPolygons.objects.all()
    serializer_class = MarkerSerializer

class MarkersMapView(TemplateView):
    template_name = "map.html"

# class MarkersMapView(TemplateView):
#     template_name = "map.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["markers"] = json.loads(
#             serialize(
#                 "geojson",
#                 MultilineStrings.objects.all(),
#             )
#         )
#         return context
