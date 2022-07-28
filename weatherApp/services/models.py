from django.db import models


class City(models.Model):
	name = models.CharField(max_length=100)
	weather = models.JSONField(blank=True, null=True)
	lastUpdated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "citie"
	
	def __str__(self):
		return self.name