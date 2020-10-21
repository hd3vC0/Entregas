from builtins import map
from django.contrib.gis.db import models

class Tienda(models.Model):
    codigo_interno = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    direccion = models.CharField(max_length=200)
    localizacion = models.PolygonField()
    estado = models.BooleanField(verbose_name='Activo')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tienda"


class TiendaHorario(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=[
        (0, "Lunes"),
        (1, "Martes"),
        (2, "Miercoles"),
        (3, "Jueves"),
        (4, "Viernes"),
        (5, "Sabado"),
        (6, "Domingo")
    ], verbose_name="Día de la semana")
    dia_especifico = models.DateField(verbose_name='Día específico', blank=True, default=None)
    hora_inicio = models.TimeField(verbose_name="Hora de inicio")
    hora_fin = models.TimeField(verbose_name="Hora de fin")
    activo = models.BooleanField(verbose_name="Activo", default=True)

    class Meta:
        verbose_name = "Horario"

class TiendaCategoria(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, verbose_name="Nombre de categoría")
    icono = models.ImageField(blank=True)
    banner = models.ImageField(blank=True)
    activa = models.BooleanField()
    categoriaPadre = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoría padre')

    def es_categoria_padre(obj):
        return True if obj.categoriaPadre==None else False

    es_categoria_padre.boolean = True
    es_categoria_padre.short_description = "Categoría Padre"

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"







