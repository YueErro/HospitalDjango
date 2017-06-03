from django.db import models
from django.conf import settings

class PacienteProfile(models.Model):
	usuario = models.CharField(max_length=15)
	nombre = models.CharField(max_length=15)
	pais = models.CharField(max_length=15)
	ciudad = models.CharField(max_length=15)
	domicilio = models.CharField(max_length=35)
	edad = models.IntegerField()
	sexo = models.CharField(max_length=15)
	Area_Medica = models.CharField(max_length=45)
	Reporte_Enfermedad = models.CharField(max_length=15)	
	Foto = models.URLField(default='')
	Dias_enfermo = models.IntegerField()
	Comentarios = models.CharField(max_length=125)
	Respuesta = models.CharField(default='', max_length=300)

	def __str__(self):
		return self.usuario + self.Reporte_Enfermedad
