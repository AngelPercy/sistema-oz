# Requerido
from django.contrib import admin
# Si mismo
from inventario.models import Categoria
from inventario.models import Medida
from inventario.models import Producto
# Referencia
from compras.models import Cosa

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'padre', 'total')

	def total(self, obj):
		return Producto.objects.filter(categoria=obj.id).count()

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'categoria', 'actual', 'unidad', 'minimo')

	def actual(self, obj):
		suma = 0
		Insumos = Cosa.objects.filter(producto=obj.id)
		for item in Insumos:
			suma = suma + item.cantidad
		resta = 0
		total = suma - resta
		return total


class MedidaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'unidad')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Medida, MedidaAdmin)
admin.site.register(Producto, ProductoAdmin)