from django.contrib.gis.db import models


class Lines(models.Model):
    ogc_fid = models.AutoField(primary_key=True, editable=False)
    osm_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    highway = models.CharField(max_length=255)
    waterway = models.CharField(max_length=255)
    aerialway = models.CharField(max_length=255)
    barrier = models.CharField(max_length=255)
    man_made = models.CharField(max_length=255)
    z_order = models.IntegerField()
    other_tags = models.CharField(max_length=255)
    GEOMETRY = models.LineStringField()
    class Meta:
        db_table = 'lines'
        managed = False

class MultilineStrings(models.Model):
    ogc_fid = models.AutoField(primary_key=True, editable=False)
    osm_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    other_tags = models.CharField(max_length=255)
    GEOMETRY = models.MultiLineStringField()

    class Meta:
        db_table = 'multilinestrings'
        managed = False


class MultiPolygons(models.Model):
    ogc_fid = models.AutoField(primary_key=True, editable=False)
    osm_id = models.CharField(max_length=255)
    osm_way_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    aeroway = models.CharField(max_length=255)
    amenity = models.CharField(max_length=255)
    admin_level = models.CharField(max_length=255)
    barrier = models.CharField(max_length=255)
    boundary = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    craft = models.CharField(max_length=255)
    geological = models.CharField(max_length=255)
    historic = models.CharField(max_length=255)
    land_area = models.CharField(max_length=255)
    landuse = models.CharField(max_length=255)
    leisure = models.CharField(max_length=255)
    man_made = models.CharField(max_length=255)
    military = models.CharField(max_length=255)
    natural = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    shop = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    tourism = models.CharField(max_length=255)
    other_tags = models.CharField(max_length=255)
    GEOMETRY = models.MultiPolygonField()

    class Meta:
        db_table = 'multipolygons'
        managed = False

class OtherRelations(models.Model):
    ogc_fid = models.AutoField(primary_key=True, editable=False)
    osm_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    other_tags = models.CharField(max_length=255)
    GEOMETRY = models.GeometryCollectionField()

    class Meta:
        db_table = 'other_relations'
        managed = False

class PlacePoint(models.Model):
    ogc_fid = models.AutoField(primary_key=True, editable=False)
    osm_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    barrier = models.CharField(max_length=255)
    highway = models.CharField(max_length=255)
    ref = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_in = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    man_made = models.CharField(max_length=255)
    other_tags = models.CharField(max_length=255)
    GEOMETRY = models.PointField()

    class Meta:
        db_table = 'points'
        managed = False


