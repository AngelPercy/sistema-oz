from django.contrib import admin
from local.models import Zona
from local.models import Mesa

class ZonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')

class MesaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'capacidad', 'zona', 'disponible', 'encargado')

	def disponible(self,obj):
		return False

admin.site.register(Zona, ZonaAdmin)
admin.site.register(Mesa, MesaAdmin)