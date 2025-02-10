import json
import os
from linecache import cache

import folium
from django.shortcuts import render
from django.views.generic import TemplateView
from folium.plugins import MousePosition
from shapely.geometry import shape
from django.views.decorators.cache import cache_page

from apps.world.models import Country
from core.settings import GEOJSON_URL


class CountryIndexView(TemplateView):
    template_name = 'gis/countries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["countries"] = Country.objects.all()
        return context


class CountryDetailView(TemplateView):
    template_name = 'gis/country.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["country"] = Country.objects.get(sov_a3=self.kwargs.get('iso_code'))
        return context




@cache_page(60 * 15)
def home_page(request):
    # Define the path to your GeoJSON file
    geojson_file_path = os.path.join('data', GEOJSON_URL)
    print(geojson_file_path)

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
        highlight_function=lambda x: {'weight': 2, 'color': 'blue'},
        tooltip=folium.GeoJsonTooltip(
            fields=["region_name", "district", "parent_code"],
            aliases=["Region Name", "District", "OKPO"],
            localize=True,
        )
    ).add_to(m)

    MousePosition().add_to(m)

    context = {
        'area': area,
        'map': m._repr_html_(),
    }

    return render(request, "gis/index.html", context)


class GeoMapIndex(TemplateView):
    template_name = "gis/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["geojson_url"] = GEOJSON_URL
        return context

    def get(self, request, *args, **kwargs):
        geojson_file_path = os.path.join('data', GEOJSON_URL)
        print(geojson_file_path)

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
            highlight_function=lambda x: {'weight': 2, 'color': 'blue'},
            tooltip=folium.GeoJsonTooltip(
                fields=["region_name", "district", "parent_code"],
                aliases=["Region Name", "District", "OKPO"],
                localize=True,
            )
        ).add_to(m)

        MousePosition().add_to(m)

        context = {
            'area': area,
            'map': m._repr_html_(),
        }

        return render(request, self.template_name, context)


GeoMapIndex = cache_page(60 * 15)(GeoMapIndex.as_view())
