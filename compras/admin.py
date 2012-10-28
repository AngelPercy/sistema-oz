# Requeridos
from django.contrib import admin
# Si mismo
from compras.models import Comprobante
from compras.models import Insumo
# Referencia
from inventario.models import Producto

class CosaInline(admin.TabularInline):
	readonly_fields = ['unidad', 'precio_unitario']
	fields = ('producto', 'cantidad', 'unidad', 'detalle', 'precio_unitario', 'precio')
	model = Cosa
	extra = 3

	def precio_unitario(self,obj):
		precio = obj.precio/obj.cantidad
		return precio

	def unidad(self,obj):
		return obj.producto.unidad

class ComprobanteAdmin(admin.ModelAdmin):
	inlines = [CosaInline]
	list_display = ('tipo', 'numero', 'fecha', 'moneda')

admin.site.register(Comprobante, ComprobanteAdmin)