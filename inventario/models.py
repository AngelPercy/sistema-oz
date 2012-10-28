from django.db import models

class Categoria(models.Model):
	nombre      = models.CharField(max_length=200)
	descripcion = models.TextField(blank=True, null=True)
	padre       = models.ForeignKey('self', blank=True, null=True)
	fecha_pub   = models.DateField(auto_now=True, auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class Medida(models.Model):
	nombre    = models.CharField(max_length=50)
	unidad    = models.CharField(max_length=10)
	fecha_pub = models.DateField(auto_now=True,auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class Insumo(models.Model):
	nombre      = models.CharField(max_length=200)
	descripcion = models.TextField(blank=True, null=True)
	categoria   = models.ForeignKey(Categoria)
	unidad      = models.ForeignKey(Medida)
	fecha       = models.DateField(auto_now=True,auto_now_add=True)
	minimo      = models.DecimalField(max_digits=5,decimal_places=3,blank=True,null=True)

	def __unicode__(self):
		return self.nombre