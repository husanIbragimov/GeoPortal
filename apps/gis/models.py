from django.db import models

from apps.common.models import BaseModel


class EVChargingLocation(BaseModel):
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # altitude = models.FloatField() # optional

    def __str__(self):
        return self.name
