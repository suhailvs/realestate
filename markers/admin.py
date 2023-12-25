from django.contrib.gis import admin

from markers.models import * #Marker, PlacePoint, MultilineStrings



@admin.register(Lines)
class LinesAdmin(admin.GISModelAdmin):
    list_display = ("ogc_fid", "name",)
@admin.register(MultilineStrings)
class MultilineAdmin(admin.GISModelAdmin):
    list_display = ("ogc_fid", "name",)

@admin.register(MultiPolygons)
class MultiPolygonsAdmin(admin.GISModelAdmin):
    list_display = ("ogc_fid", "name",)

@admin.register(OtherRelations)
class OtherRelationsAdmin(admin.GISModelAdmin):
    list_display = ("ogc_fid", "name",)

@admin.register(PlacePoint)
class PlacePointAdmin(admin.GISModelAdmin):
    list_display = ("ogc_fid", "name",)

