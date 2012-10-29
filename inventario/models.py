from django.db import models

class Categoria(models.Model):
	nombre      = models.CharField(max_length=200,unique=True)
	descripcion = models.TextField(blank=True, null=True)
	padre       = models.ForeignKey('self', blank=True, null=True)

	def __unicode__(self):
		return self.nombre

class Medida(models.Model):
	nombre    = models.CharField(max_length=50,unique=True)
	unidad    = models.CharField(max_length=10,unique=True)

	def __unicode__(self):
		return self.nombre

class Articulo(models.Model):
	nombre      = models.CharField(max_length=200,unique=True)
	descripcion = models.TextField(blank=True, null=True)
	categoria   = models.ForeignKey(Categoria)
	minimo      = models.DecimalField(max_digits=5,decimal_places=3)
	unidad      = models.ForeignKey(Medida)

	def __unicode__(self):
		return self.nombre