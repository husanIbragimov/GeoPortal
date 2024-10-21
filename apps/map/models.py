from django.db import models

# from django.contrib.gis.db import models as gis_models

from apps.common.models import BaseModel


class EVChargingLocation(BaseModel):
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # point = gis_models.PointField(null=True)

    def __str__(self):
        return self.name


class GeoFeature(BaseModel):
    TYPE = (
        ('Feature', 'Feature'),
        ('FeatureCollection', 'FeatureCollection'),
        ('Point', 'Point'),
        ('Polygon', 'Polygon'),
        ('MultiPolygon', 'MultiPolygon'),
    )
    type = models.CharField(max_length=20, default='Feature')
    properties = models.JSONField()
    geometry = models.JSONField()

    class Meta:
        db_table = 'geo_features'
        verbose_name = 'Geo Feature'
        verbose_name_plural = 'Geo Features'

    def __str__(self):
        return self.properties.get('region_name')
