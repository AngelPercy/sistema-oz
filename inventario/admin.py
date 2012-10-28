from django.contrib import admin
from compras.models import Compra
from inventario.models import Categoria
from inventario.models import Medida
from inventario.models import Producto

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'padre', 'total')

	def total(self, obj):
		return Producto.objects.filter(categoria=obj.id).count()

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'categoria', 'actual', 'unidad', 'minimo')

	def actual(self, obj):
		total = 0
		Compras = Compra.objects.filter(producto=obj.id)
		for item in Compras:
			total = total + item.cantidad
		#Ventas  = Compra.objects.filter(producto=obj.id)
		#for item in Ventas:
		#	total = total + item.cantidad
		return total


class MedidaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'unidad')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Medida, MedidaAdmin)
admin.site.register(Producto, ProductoAdmin)