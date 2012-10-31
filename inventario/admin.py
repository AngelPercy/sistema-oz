# Requerido
from django.contrib import admin
# Si mismo
from inventario.models import Categoria
from inventario.models import Medida
from inventario.models import Articulo
# Referencia
from compras.models import Elemento

class ArticuloInline(admin.TabularInline):
	model = Articulo
	extra = 0

class CategoriaAdmin(admin.ModelAdmin):
	inlines = [ArticuloInline]
	list_display = ('nombre', 'descripcion', 'padre', 'total')

	def total(self, obj):
		return Articulo.objects.filter(categoria=obj.id).count()

class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'categoria', 'actual', 'unidad', 'minimo')

	def actual(self, obj):
		suma = 0
		Insumos = Elemento.objects.filter(producto=obj.id)
		for item in Insumos:
			suma = suma + item.cantidad
		resta = 0
		total = suma - resta
		return total


class MedidaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'unidad')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Medida, MedidaAdmin)
admin.site.register(Articulo, ArticuloAdmin)