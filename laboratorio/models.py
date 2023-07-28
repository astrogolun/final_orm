from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100) 
    pais = models.CharField(max_length=100, default='')  
    director_general = models.OneToOneField('DirectorGeneral', on_delete=models.SET_NULL, null=True, blank=True, related_name='laboratorio_asignado')
    
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, default='--') 
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.SET_NULL, null=True, blank=True, related_name='director_general_asignado')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(verbose_name='Fecha de fabricación')
    p_costo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

