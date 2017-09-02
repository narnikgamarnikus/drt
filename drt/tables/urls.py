from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.LatencyListView.as_view(),
        name='list'
    ),
    url(
        r'^city-autocomplete/$',
        views.CityAutocomplete.as_view(),
        name='city-autocomplete',
    ),
]
