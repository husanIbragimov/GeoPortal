import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.gis.models import EVChargingLocation


class Command(BaseCommand):
    help = 'Load data from EV Station file'

    def handle(self, *args, **kwargs):
        data_file = os.path.join(settings.BASE_DIR, 'data', 'regions.json')
        keys = ("regions",)

        with open(data_file) as f:
            data = json.load(f)
            regions = data['regions']

            EVChargingLocation.objects.bulk_create(
                [EVChargingLocation(**station) for station in regions]
            )

    def handle_old(self, *args, **kwargs):
        data_file = os.path.join(settings.BASE_DIR, 'data', 'Tuman_27_03_2024.geojson')
        keys = ("properties",)

        regions = []
        with open(data_file) as f:
            data = json.load(f)

            for feature in range(len(data['features'])):
                properties = data['features'][feature]['properties']
                station = {
                    'name': properties['region_name'],
                    'latitude': properties['Shape_Length'],
                    'longitude': properties['Shape_Area'],
                }
                regions.append(station)

        EVChargingLocation.objects.bulk_create(
            [EVChargingLocation(**station) for station in regions]
        )
