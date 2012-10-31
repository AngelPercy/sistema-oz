# Requerido
from django.db import models
# Referencia
from inventario.models import Articulo
from local.models import Cliente

class Comprobante(models.Model):
	TIPO_OPCIONES = (
		('00', 'Ninguno'),
		('01', 'Factura'),
		('03', 'Boleta'),
		('12', 'Ticket'),
		('16', 'Pasajes Terrestres'),
		('15', 'Pasajes Aereos'),
		('02', 'Recibo de Honorarios'),
		('07', 'Nota de Credito'),
		('08', 'Nota de Debito'),
	)
	MONEDAS_OPCIONES = (
		('PEN', 'Nuevos Soles'),
		('USD', 'Dolares Americanos'),
	)
	fecha   = models.DateField()
	tipo    = models.CharField(max_length=2,choices=TIPO_OPCIONES,default='01')
	serie   = models.CharField(max_length=5,blank=True,null=True)
	numero  = models.CharField(max_length=8,blank=True,null=True)
	cliente = models.ForeignKey(Cliente)
	moneda  = models.CharField(max_length=3,choices=MONEDAS_OPCIONES,default='PEN')

	def __unicode__(self):
		return 'Comprobante'

class Elemento(models.Model):
	articulo    = models.ForeignKey(Articulo)
	cantidad    = models.DecimalField(max_digits=5,decimal_places=3,default=1)
	detalle     = models.CharField(max_length=250,blank=True,null=True)
	precio      = models.DecimalField(max_digits=5,decimal_places=2)
	comprobante = models.ForeignKey(Comprobante)

	def __unicode__(self):
		return ('%d de %s') % (self.cantidad, self.articulo)