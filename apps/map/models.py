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
