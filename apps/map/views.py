import json
import os

import folium
from django.shortcuts import render
from shapely.geometry import shape

from core.settings import GEOJSON_URL, LEAFLET_CONFIG


def home_page(request):
    # Define the path to your GeoJSON file
    geojson_file_path = os.path.join('data', GEOJSON_URL)

    # Read and parse the GeoJSON file
    with open(geojson_file_path, 'r', encoding="utf-8") as geojson_file:
        geojson_data = json.load(geojson_file)

    # Parse GeoJSON to get the polygon
    polygon = shape(geojson_data['features'][0]['geometry'])

    # Calculate the area
    area = polygon.area

    # Your existing code to render the map
    map_center = [41.3775, 64.5853]
    m = folium.Map(location=map_center, zoom_start=6, max_zoom=14, min_zoom=6)

    # Define a list of colors
    colors = ['#ffaf00', '#00ffaf', '#af00ff', '#ff0000', '#00ff00', '#0000ff']

    # Add the polygon to the map
    folium.GeoJson(
        geojson_data,
        style_function=lambda x: {
            'fillColor': colors[geojson_data['features'].index(x) % len(colors)],  # Fill color (hex color code)
            'color': '#D3D3D3',  # Border color (hex color code)
            'weight': 0.5,  # Border width in pixels
            'fillOpacity': 0.3  # Fill opacity
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["region_name", "district", "parent_code"],
            aliases=["Region Name", "District", "OKPO"],
            localize=True
        )
    ).add_to(m)

    # m.save('polygon_map.html')

    context = {
        'area': area,
        'map': m._repr_html_(),
    }

    return render(request, "gis/index.html", context)
