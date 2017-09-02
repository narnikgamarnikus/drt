from channels import Group
from .models import Latency
from django.db.models import Q
import json


def tables_connect(message):
    message.reply_channel.send({"accept": True})
    Group("tables").add(message.reply_channel)


def tables_message(message):
	print(message.content['text'])
	cities_from = [i for i in set([i.city_from.name for i in Latency.objects.all()])]
	cities_to = [i for i in set([i.city_to.name for i in Latency.objects.all()])]
	cities = cities_from + cities_to

	matrix = {cf: {ct: Latency.objects.filter(
		Q(city_to__name=cf, city_from__name=ct) | 
		Q(city_to__name=ct, city_from__name=cf))[0].latency if Latency.objects.filter(
		Q(city_to__name=cf, city_from__name=ct) | 
		Q(city_to__name=ct, city_from__name=cf)).count() > 0 else 0 for ct in cities} 
		for cf in cities}

	Group("tables").send({
		"text": json.dumps({
            'matrix': matrix
            })
        }, immediately=True)


def tables_disconnect(message):
    Group("tables").discard(message.reply_channel)
