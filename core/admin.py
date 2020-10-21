from django.contrib import admin
from core.models import Tienda, TiendaHorario, TiendaCategoria
from django.contrib.gis.db import models
from django.contrib.gis.forms import OSMWidget
from core.forms import CategoriaForm

class TiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    formfield_overrides = {
        models.PolygonField: {'widget': OSMWidget},
    }

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tienda', 'es_categoria_padre', 'activa')
    list_filter = ('tienda','activa')
    search_fields = ('nombre',)
    form = CategoriaForm


admin.site.register(Tienda, TiendaAdmin)
admin.site.register(TiendaHorario)
admin.site.register(TiendaCategoria, CategoriasAdmin)
admin.site.site_header = "Entregas BackOffice"