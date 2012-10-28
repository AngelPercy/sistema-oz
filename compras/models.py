# Requerido
from django.db import models
# Referencia
from inventario.models import Producto

class Comprobante(models.Model):
	TIPO_OPCIONES = (
		('BOL', 'Boleta'),
		('FAC', 'Factura'),
		('NAN', 'Ninguno'),
	)
	MONEDAS_OPCIONES = (
		('PEN', 'Nuevos Soles'),
		('USD', 'Dolares Americanos'),
	)
	tipo    = models.CharField(max_length=100,choices=TIPO_OPCIONES,default='FAC')
	numero  = models.CharField(max_length=20,blank=True,null=True)
	fecha   = models.DateField()
	moneda  = models.CharField(max_length=3,choices=MONEDAS_OPCIONES,default='PEN')

class Insumo(models.Model):
	producto    = models.ForeignKey(Producto)
	cantidad    = models.DecimalField(max_digits=5,decimal_places=3,default=1)
	detalle     = models.CharField(max_length=250,blank=True,null=True)
	precio      = models.DecimalField(max_digits=5,decimal_places=2)
	fecha       = models.DateTimeField(auto_now=True,auto_now_add=True)
	comprobante = models.ForeignKey(Comprobante)