from django.db import models
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
	numero  = models.CharField(max_length=20)
	fecha   = models.DateField()
	moneda  = models.CharField(max_length=3,choices=MONEDAS_OPCIONES, default='PEN')

class Insumo(models.Model):
	producto    = models.ForeignKey(Producto)
	cantidad    = models.DecimalField(max_digits=5,decimal_places=3,default=1)
	detalle     = models.TextField(blank=True,null=True)
	precio_uni  = models.DecimalField(max_digits=5,decimal_places=2)
	fecha_pub   = models.DateTimeField(auto_now=True,auto_now_add=True)
	comprobante = models.ForeignKey(Comprobante)