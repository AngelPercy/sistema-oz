from inventario.models import Producto
from compras.models import Insumo
from compras.models import Comprobante
from django.contrib import admin

class InsumoInline(admin.TabularInline):
	readonly_fields = ['unidad','total']
	model = Insumo
	extra = 1

	def total(self, obj):
		total = obj.precio_uni * obj.cantidad
		return total

	def unidad(self, obj):
		return obj.producto.unidad

class ComprobanteAdmin(admin.ModelAdmin):
	inlines = [InsumoInline]
	list_display = ('tipo', 'numero', 'fecha', 'moneda')

admin.site.register(Comprobante, ComprobanteAdmin)