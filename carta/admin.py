from inventario.models import Producto
from carta.models import Categoria
from carta.models import Plato
from carta.models import Insumo
from django.contrib import admin

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'superior', 'total')

	def total(sef, obj):
		return Plato.objects.filter(categoria=obj.id).count()

class InsumoInline(admin.TabularInline):
	readonly_fields = ['unidad']
	model = Insumo
	extra = 5

	def unidad(self,obj):
		return obj.producto.unidad

class PlatoAdmin(admin.ModelAdmin):
	inlines = [InsumoInline]
	list_display = ('nombre', 'categoria', 'descripcion', 'precio')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Plato, PlatoAdmin)