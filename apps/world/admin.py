from django.contrib import admin

from django.contrib.gis import admin as gis_admin

from .models import Country

admin.site.register(Country)