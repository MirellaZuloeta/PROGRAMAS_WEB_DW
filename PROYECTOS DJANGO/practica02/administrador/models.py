from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class TipoProducto(models.Model):
     tipoProId=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=30)
     descripcion=models.CharField(max_length=50)
     def __str__(self) :
          return self.nombre
          
class Producto(models.Model):
     idProducto=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=100)
     precio=models.DecimalField(decimal_places=2,max_digits=12)
     stock=models.IntegerField()
     marca=models.CharField(max_length=30)
     descripcion=models.CharField(max_length=100)
     talla=models.IntegerField()
     tipoPro=models.ForeignKey('TipoProducto', on_delete=models.DO_NOTHING, default=0)
    
