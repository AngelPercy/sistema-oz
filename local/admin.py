from local.models import Zona
from local.models import Mesa
from django.contrib import admin

class ZonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')

class MesaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'capacidad', 'zona', 'disponible', 'encargado')

admin.site.register(Zona, ZonaAdmin)
admin.site.register(Mesa, MesaAdmin)