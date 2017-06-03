from django.db import models
from django.conf import settings

class Respuesta(models.Model):
	respuesta = models.CharField(max_length=300)

	def __str__(self):
		return self.usuario + self.respuesta

