# Requerido
from django.contrib import admin
# Si mismo
from carta.models import Categoria
from carta.models import Plato
from carta.models import Insumo

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'superior', 'conteo')

	def conteo(sef, obj):
		return Plato.objects.filter(categoria=obj.id).count()

class InsumoInline(admin.TabularInline):
	readonly_fields = ['medida']
	model = Insumo
	extra = 5

	def medida(self,obj):
		return obj.articulo.unidad

class PlatoAdmin(admin.ModelAdmin):
	inlines = [InsumoInline]
	list_display = ('nombre', 'categoria', 'descripcion', 'precio')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Plato, PlatoAdmin)