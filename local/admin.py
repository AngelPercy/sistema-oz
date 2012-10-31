from django.contrib import admin
from local.models import Zona
from local.models import Mesa
from local.models import Cliente
from ventas.models import Comanda

class ZonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')

class ComandaInline(admin.TabularInline):
	model = Comanda
	extra = 0

class MesaAdmin(admin.ModelAdmin):
	inlines = [ComandaInline]	
	list_display = ('nombre', 'capacidad', 'zona', 'disponible', 'encargado')

	def disponible(self,obj):
		Comandas = Comanda.objects.filter(mesa=obj.id,activa=True).count()
		if Comandas > 0:
			return 'Ocupada'
		else:
			return 'Disponible'


	def encargado(self,obj):
		Conteo = Comanda.objects.filter(mesa=obj.id,activa=True).count()
		if Conteo > 0:
			Comandas = Comanda.objects.filter(mesa=obj.id,activa=True)
			for item in Comandas:
				return item.encargado
		else:
			return '(Nada)'

admin.site.register(Zona, ZonaAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Cliente)