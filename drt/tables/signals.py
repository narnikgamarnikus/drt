
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Latency
from channels import Group
from django.db.models import Q
import json




@receiver(post_save, sender=Latency)
def create_or_update_latency(sender, instance, created, *args, **kwargs):

	cities_from = [i for i in set([i.city_from.name for i in Latency.objects.all()])]
	cities_to = [i for i in set([i.city_to.name for i in Latency.objects.all()])]
	cities = cities_from + cities_to

	matrix = {cf: {ct: Latency.objects.filter(
		Q(city_to__name=cf, city_from__name=ct) | 
		Q(city_to__name=ct, city_from__name=cf))[0].latency if Latency.objects.filter(
		Q(city_to__name=cf, city_from__name=ct) | 
		Q(city_to__name=ct, city_from__name=cf)).count() > 0 else 0 for ct in cities} 
		for cf in cities}

	print(matrix)

	Group("tables").send({
		"text": json.dumps({
            'matrix': matrix
            })
        }, immediately=True)