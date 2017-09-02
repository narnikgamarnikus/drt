from django.apps import AppConfig


class TablesConfig(AppConfig):
    name = 'drt.tables'
    verbose_name = "Tables"

    def ready(self):
    	import drt.tables.signals
