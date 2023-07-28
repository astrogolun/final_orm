from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio')
    list_filter = ('laboratorio',)
    search_fields = ('nombre', 'laboratorio__nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('laboratorio', 'f_fabricacion')
    search_fields = ('nombre', 'laboratorio__nombre')
