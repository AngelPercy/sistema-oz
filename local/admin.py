from django.contrib import admin
from local.models import Zona
from local.models import Mesa
from local.models import Cliente
from ventas.models import Comanda

class ZonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')

class MesaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'capacidad', 'zona', 'disponible', 'encargado')

	def disponible(self,obj):
		Comandas = Comanda.objects.filter(mesa=obj.id,activa=True).count()
		if Comandas > 0:
			return 'Ocupada'
		else:
			return 'Disponible'


	def encargado(self,obj):
		return "Alguien"

admin.site.register(Zona, ZonaAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Cliente)