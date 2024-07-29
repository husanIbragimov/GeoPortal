import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.map.models import EVChargingLocation


class Command(BaseCommand):
    help = 'Load data from EV Station file'

    # def handle(self, *args, **kwargs):
    #     data_file = os.path.join(settings.BASE_DIR, 'data', 'regions.json')
    #     keys = ("regions",)
    #
    #     with open(data_file) as f:
    #         data = json.load(f)
    #         regions = data['regions']
    #
    #         EVChargingLocation.objects.bulk_create(
    #             [EVChargingLocation(**station) for station in regions]
    #         )

    def handle(self, *args, **kwargs):
        data_file = os.path.join(settings.BASE_DIR, 'data', 'Tuman_27_03_2024.geojson')
        """
        generate json file from geojson file
        """
        data_path = "data.json"
        with open(data_file, 'r', encoding='utf-8') as f1:
            data = json.load(f1)
            with open(data_path, 'w', encoding='utf-8') as f2:
                json.dump(data, f2, ensure_ascii=False, indent=4)


