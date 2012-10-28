from django.db import models
from inventario.models import Producto

class Categoria(models.Model):
	nombre      = models.CharField(max_length=200)
	descripcion = models.TextField(null=True,blank=True)
	superior    = models.ForeignKey('self',blank=True,null=True)
	fecha_pub   = models.DateField(auto_now=True,auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class Plato(models.Model):
	nombre      = models.CharField(max_length=200)
	categoria   = models.ForeignKey(Categoria)
	descripcion = models.TextField(null=True,blank=True)
	precio      = models.DecimalField(max_digits=5,decimal_places=2)
	fecha_pub   = models.DateField(auto_now=True,auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class Insumo(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.DecimalField(max_digits=5,decimal_places=2)
	opcional = models.BooleanField()
	plato    = models.ForeignKey(Plato)