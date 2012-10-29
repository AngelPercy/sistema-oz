# Requerido
from django.db import models
# Referencia
from inventario.models import Articulo

class Categoria(models.Model):
	nombre      = models.CharField(max_length=200,unique=True)
	descripcion = models.TextField(null=True,blank=True)
	superior    = models.ForeignKey('self',blank=True,null=True)

	def __unicode__(self):
		return self.nombre

class Plato(models.Model):
	nombre      = models.CharField(max_length=200,unique=True)
	categoria   = models.ForeignKey(Categoria)
	descripcion = models.TextField(null=True,blank=True)
	precio      = models.DecimalField(max_digits=5,decimal_places=2)
	fecha       = models.DateField(auto_now=True,auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class Insumo(models.Model):
	articulo = models.ForeignKey(Articulo)
	cantidad = models.DecimalField(max_digits=5,decimal_places=3)
	opcional = models.BooleanField()
	plato    = models.ForeignKey(Plato)

	def __unicode__(self):
		return ('%d de %s') % (self.cantidad, self.articulo)