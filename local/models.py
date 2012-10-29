from django.db import models

class Zona(models.Model):
	nombre      = models.CharField(max_length=200,unique=True)
	descripcion = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return self.nombre

class Mesa(models.Model):
	nombre      = models.CharField(max_length=200,unique=True)
	descripcion = models.TextField(blank=True,null=True)
	capacidad   = models.IntegerField()
	zona        = models.ForeignKey(Zona)

	def __unicode__(self):
		return self.nombre

class Cliente(models.Model):
	documento = models.CharField(max_length=11,blank=True,null=True,unique=True)
	nombre    = models.CharField(max_length=200)
	email     = models.EmailField(blank=True,null=True)
	direccion = models.CharField(max_length=250,blank=True,null=True)
	telefono  = models.BigIntegerField(null=True,blank=True)

 	def __unicode__(self):
		return self.nombre