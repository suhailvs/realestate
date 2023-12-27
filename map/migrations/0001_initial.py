# Generated by Django 4.1.5 on 2023-12-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("latlngs", models.JSONField(default=list)),
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
            ],
        ),
    ]