from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError



@python_2_unicode_compatible
class Latency(models.Model):
	city_from = models.ForeignKey('cities_light.City', 
		related_name='city_from',
		verbose_name=_('City from'),
		null=True
	)
	city_to = models.ForeignKey('cities_light.City',
		related_name='city_to',
		verbose_name=_('City to'),
		null=True
	)
	latency = models.FloatField(default=0,
		verbose_name=_('Latency'),
		null=True
	)

	class Meta:
		unique_together = (('city_from', 'city_to'),)

	def clean(self, *args, **kwargs):
		if self.city_from == self.city_to:
			raise ValidationError(_('City from and city to must not coincide!'))

		if self.latency < 0:
			raise ValidationError(_('Latency must be > 0!'))
		return super(Latency, self).clean(*args, **kwargs)

	def __str__(self):
		return str(self.pk)