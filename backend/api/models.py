from django.db import models

# Create your models here.
class Event(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	title = models.TextField()
	description = models.TextField()

	class Meta:
		ordering = ['start']