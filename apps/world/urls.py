from django.urls import path

from .views import GeoMapIndex, CountryIndexView, CountryDetailView

urlpatterns = [
    path('', GeoMapIndex, name='home'),
    path('country/', CountryIndexView.as_view(), name='index'),
    path('country/<str:iso_code>/', CountryDetailView.as_view(), name='index'),
]
