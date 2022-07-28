from django.db import models


class City(models.Model):
	#name of the city
	name = models.CharField(max_length=100)
	#weather data
	weather = models.JSONField(blank=True, null=True)
	#when it is last updated
	lastUpdated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "citie"
	
	def __str__(self):
		return self.name