import folium
from django.shortcuts import render
from folium.plugins import FastMarkerCluster

from apps.gis.models import EVChargingLocation
from django.db.models import Avg


def home_page(request):
    avg_lat = EVChargingLocation.objects.aggregate(avg=Avg('latitude'))['avg']
    print(avg_lat)
    stations = EVChargingLocation.objects.exclude(latitude__gt=avg_lat)

    m = folium.Map(location=[41.3775, 64.5853], zoom_start=6)

    latitudes = [station.latitude for station in stations]
    longitudes = [station.longitude for station in stations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)

    context = {
        'map': m._repr_html_()
    }

    return render(request, "gis/index.html", context)
