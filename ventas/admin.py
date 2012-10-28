from django.contrib import admin
from local.models import Mesa
from carta.models import Plato
from ventas.models import Comanda
from ventas.models import Pedido
from ventas.models import Comprobante

class PedidoInline(admin.TabularInline):
	readonly_fields = ['precio']
	model = Pedido
	extra = 3

	def precio(self,obj):
		precio = obj.cantidad*obj.plato.precio
		return precio

class ComprobanteInline(admin.TabularInline):
	readonly_fields = ['subtotal', 'igv', 'total']
	model = Comprobante
	extra = 1

class ComandaAdmin(admin.ModelAdmin):
	inlines = [PedidoInline, ComprobanteInline]
	list_display = ('mesa', 'encargado', 'pedidos', 'pub_fecha', 'total')


	def total(self,obj):
		total = 0
		Pedidos = Pedido.objects.filter(comanda=obj.id)
		for item in Pedidos:
			total = total + (item.plato.precio*item.cantidad)
		return total

	def encargado(self, obj):
		return obj.mesa.encargado

	def pedidos(self, obj):
		return Pedido.objects.filter(comanda=obj.id).count()


admin.site.register(Comanda, ComandaAdmin)