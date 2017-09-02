from django.core.urlresolvers import reverse
from django.views.generic import ListView
from .models import Latency
from dal import autocomplete
from cities_light.models import City
from django.db.models import Q

class LatencyListView(ListView):
    model = Latency

    def get_context_data(self):
        context = super(LatencyListView, self).get_context_data()
        latency = Latency.objects.all() 

        cities_from = [i for i in set([i.city_from.name for i in Latency.objects.all()])]
        cities_to = [i for i in set([i.city_to.name for i in Latency.objects.all()])]
        cities = cities_from + cities_to

        context['matrix'] = {cf: {ct: Latency.objects.filter(
            Q(city_to__name=cf, city_from__name=ct) | 
            Q(city_to__name=ct, city_from__name=cf))[0].latency if Latency.objects.filter(
            Q(city_to__name=cf, city_from__name=ct) | 
            Q(city_to__name=ct, city_from__name=cf)).count() > 0 else 0 for ct in cities} 
            for cf in cities}

        return context


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith = self.q)

        return qs
