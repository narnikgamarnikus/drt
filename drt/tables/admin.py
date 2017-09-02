from django.contrib import admin
from .models import Latency
from .forms import LatencyForm


@admin.register(Latency)
class LatencyAdmin(admin.ModelAdmin):
    form = LatencyForm
    list_display = ('city_from', 'city_to', 'latency')
    search_fields = ['city_from', 'city_to',]

