from django.contrib import admin
from local.models import Zona
from local.models import Mesa
from local.models import Cliente

class ZonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')

class MesaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'capacidad', 'zona', 'disponible', 'encargado')

	def disponible(self,obj):
		return False

	def encargado(self,obj):
		return "Alguien"

admin.site.register(Zona, ZonaAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Cliente)