from inventario.models import Producto
from compras.models import Compra
from compras.models import Documento
from django.contrib import admin

class DocumentoInline(admin.TabularInline):
	model = Documento
	extra = 1

class CompraAdmin(admin.ModelAdmin):
	inlines = [DocumentoInline]
	list_display = ('producto', 'cantidad', 'unidad', 'total')

	def unidad(self, obj):
		return obj.producto.unidad

	def total(self, obj):
		total = 0
		Documentos = Documento.objects.filter(compra=obj.producto)
		for item in Documentos:
			total = item.monto+total
		return total

admin.site.register(Compra, CompraAdmin)