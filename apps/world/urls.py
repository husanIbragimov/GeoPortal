from django.urls import path

from .views import GeoMapIndex

urlpatterns = [
    path('', GeoMapIndex, name='home'),
]
