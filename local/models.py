from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Zona(models.Model):
	nombre      = models.CharField(max_length=200)
	descripcion = models.TextField(blank=True,null=True)
	fecha_pub   = models.DateField(auto_now=True,auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class Mesa(models.Model):
	nombre      = models.CharField(max_length=200)
	descripcion = models.TextField(blank=True,null=True)
	capacidad   = models.IntegerField()
	zona        = models.ForeignKey(Zona)
	fecha_pub   = models.DateField(auto_now=True,auto_now_add=True)
	encargado   = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre