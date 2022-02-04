from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField
from django.contrib.auth.models import User

# Create your models here.
class Estilo(models.Model):
     estiloID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=20, unique=True)
     def __str__(self) :
          return self.nombre

class Dimension(models.Model):
     dimensionID=models.AutoField(primary_key=True)
     descripcion=models.CharField(max_length=20, unique=True)
     def __str__(self) :
          return self.descripcion

class Color(models.Model):
     colorID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=20, unique=True)
     def __str__(self) :
          return self.nombre

class TipoProducto(models.Model):
     tipoProID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=30)
     imagen=models.ImageField(upload_to="tipoproductos", blank=True, null=True) 
     def __str__(self) :
          return self.nombre

class Marca(models.Model):
     marcaID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=30, unique=True)
     def __str__(self) :
          return self.nombre

class TipoDocumento(models.Model):
     tipoDocID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=30, unique=True)
     def __str__(self) :
          return self.nombre

class Producto(models.Model):
     codigoPro=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=100)
     precio=models.DecimalField(decimal_places=2,max_digits=12)
     precioMayor=models.DecimalField(decimal_places=2,max_digits=12)
     stock=models.IntegerField()
     descripcion=models.CharField(max_length=100)
     talla=models.IntegerField()
     tipoProID=models.ForeignKey('TipoProducto', on_delete=models.DO_NOTHING, default=0)
     marcaID=models.ForeignKey('Marca', on_delete=models.DO_NOTHING, default=0)
     estiloID=models.ForeignKey('Estilo', on_delete=models.DO_NOTHING, default=0)
     dimensionID=models.ForeignKey('Dimension', on_delete=models.DO_NOTHING, default=0)
     colorID=models.ForeignKey('Color', on_delete=models.DO_NOTHING, default=0)
     imagen=models.ImageField(upload_to="productos", blank=True, null=True) 
     def __str__(self) :
          return self.nombre


class Comentario(models.Model):
     comentarioID=models.AutoField(primary_key=True)
     comentario=models.CharField(max_length=300)
     usuario=models.CharField(max_length=300)
     fecha=models.DateTimeField(auto_now_add=True)
     codigoPro=models.ForeignKey('Producto', related_name="producto_comentarios",on_delete=models.DO_NOTHING, default=0)
     def __str__(self) :
          return "{} {}".format(self.comentario,self.codigoPro)

class Cliente(models.Model):
  codigoCli=models.AutoField(primary_key=True)
  nombres=models.CharField(max_length=50,null=True, blank=True)
  apellidos=models.CharField(max_length=50,null=True, blank=True)
  direccion=models.CharField(max_length=300,null=True, blank=True)
  telefono=models.CharField(max_length=12,null=True, blank=True)
  sexo=models.CharField(max_length=1,null=True, blank=True) 
  fechaNacimiento=models.DateField(null=True, blank=True)
  numeroDocumento=models.CharField(max_length=21, unique=True,null=True, blank=True)
  numeroTarjeta=models.CharField(max_length=50,null=True, blank=True)
  cvv=models.IntegerField(null=True, blank=True)
  mmaa=models.CharField(max_length=10,null=True, blank=True)
  tipoDocID=models.ForeignKey('TipoDocumento', on_delete=models.DO_NOTHING, default=1)
  foto=models.ImageField(upload_to="clientes", blank=True, null=True) 
  comentario=models.CharField(max_length=300,null=True, blank=True)
  usuario=models.ForeignKey(get_user_model(), related_name="cliente_usuario", on_delete=models.DO_NOTHING, blank=True, null=True)
  def __str__(self) :
          return self.nombres

class Venta(models.Model):
     ventaID=models.AutoField(primary_key=True)
     fecha=models.DateField(auto_now_add=True)
     hora=models.TimeField(auto_now_add=True)
     subtotal=models.DecimalField(decimal_places=2,max_digits=12, null=True, blank=True)
     costoEnvio=models.DecimalField(decimal_places=2,max_digits=12, null=True, blank=True)
     total=models.DecimalField(decimal_places=2,max_digits=12, null=True, blank=True)
     pendiente=models.BooleanField(default=True)
     direccionEnvio=models.CharField(max_length=300, blank=True, null=True)
     referenciaDireccion=models.CharField(max_length=300, blank=True, null=True)
     usuario=models.ForeignKey(get_user_model(), related_name="venta_usuario", on_delete=models.DO_NOTHING, default=0)
     def __str__(self) :
          return "{} {}".format(self.fecha,self.hora)

class CarritoCompras(models.Model):
     carritoID=models.AutoField(primary_key=True)
     precio=models.DecimalField(decimal_places=2,max_digits=12)
     producto=models.ForeignKey('Producto', related_name="producto_carrito",on_delete=models.DO_NOTHING,  default=0)
     usuario=models.ForeignKey(get_user_model(), related_name="carrito_usuario", on_delete=models.DO_NOTHING, default=0)
     cantidad=models.IntegerField(default=1)
     comprado=models.BooleanField(default=False)
     pendiente=models.BooleanField(default=False)
     ventaID=models.ForeignKey('Venta', on_delete=models.DO_NOTHING, blank=True, null=True)
     def __str__(self) :
          return "{} {}".format(self.usuario,self.producto)
   
