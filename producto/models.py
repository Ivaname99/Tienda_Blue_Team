from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(null=False, max_length=50, verbose_name="Nombre")
    descripcion = models.TextField(null=False, max_length=200, verbose_name="Descripción")
    existencias = models.IntegerField(null=False, verbose_name="Existencias")
    fechaProduccion = models.DateField(null=False, verbose_name="Fecha de producción")
    fechaCaducidad = models.DateField(null=False, verbose_name="Caducidad")
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=9, verbose_name="Precio")
    
class Contacto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    usuario = models.TextField(null=False, max_length=200, verbose_name="Usuario")
    email = models.TextField(null=False, max_length=200, verbose_name="Email")
    mensaje = models.TextField(null=False, max_length=200, verbose_name="Mensaje")
