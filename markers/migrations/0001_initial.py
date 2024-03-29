# Generated by Django 4.2.8 on 2023-12-27 01:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lines",
            fields=[
                (
                    "ogc_fid",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("osm_id", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("highway", models.CharField(max_length=255)),
                ("waterway", models.CharField(max_length=255)),
                ("aerialway", models.CharField(max_length=255)),
                ("barrier", models.CharField(max_length=255)),
                ("man_made", models.CharField(max_length=255)),
                ("z_order", models.IntegerField()),
                ("other_tags", models.CharField(max_length=255)),
                (
                    "GEOMETRY",
                    django.contrib.gis.db.models.fields.LineStringField(srid=4326),
                ),
            ],
            options={
                "db_table": "lines",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MultilineStrings",
            fields=[
                (
                    "ogc_fid",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("osm_id", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("other_tags", models.CharField(max_length=255)),
                (
                    "GEOMETRY",
                    django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
                ),
            ],
            options={
                "db_table": "multilinestrings",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MultiPolygons",
            fields=[
                (
                    "ogc_fid",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("osm_id", models.CharField(max_length=255)),
                ("osm_way_id", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("aeroway", models.CharField(max_length=255)),
                ("amenity", models.CharField(max_length=255)),
                ("admin_level", models.CharField(max_length=255)),
                ("barrier", models.CharField(max_length=255)),
                ("boundary", models.CharField(max_length=255)),
                ("building", models.CharField(max_length=255)),
                ("craft", models.CharField(max_length=255)),
                ("geological", models.CharField(max_length=255)),
                ("historic", models.CharField(max_length=255)),
                ("land_area", models.CharField(max_length=255)),
                ("landuse", models.CharField(max_length=255)),
                ("leisure", models.CharField(max_length=255)),
                ("man_made", models.CharField(max_length=255)),
                ("military", models.CharField(max_length=255)),
                ("natural", models.CharField(max_length=255)),
                ("office", models.CharField(max_length=255)),
                ("place", models.CharField(max_length=255)),
                ("shop", models.CharField(max_length=255)),
                ("sport", models.CharField(max_length=255)),
                ("tourism", models.CharField(max_length=255)),
                ("other_tags", models.CharField(max_length=255)),
                (
                    "GEOMETRY",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "db_table": "multipolygons",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="OtherRelations",
            fields=[
                (
                    "ogc_fid",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("osm_id", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("other_tags", models.CharField(max_length=255)),
                (
                    "GEOMETRY",
                    django.contrib.gis.db.models.fields.GeometryCollectionField(
                        srid=4326
                    ),
                ),
            ],
            options={
                "db_table": "other_relations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PlacePoint",
            fields=[
                (
                    "ogc_fid",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("osm_id", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("barrier", models.CharField(max_length=255)),
                ("highway", models.CharField(max_length=255)),
                ("ref", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("is_in", models.CharField(max_length=255)),
                ("place", models.CharField(max_length=255)),
                ("man_made", models.CharField(max_length=255)),
                ("other_tags", models.CharField(max_length=255)),
                ("GEOMETRY", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                "db_table": "points",
                "managed": False,
            },
        ),
    ]
