from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField

# Create your models here.
class TipoProducto(models.Model):
     tipoProID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=30)
     def __str__(self) :
          return self.nombre

class Marca(models.Model):
     marcaID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=30, unique=True)
     def __str__(self) :
          return self.nombre

class TipoDocumento(models.Model):
     tipoDocID=models.IntegerField(primary_key=True)
     nombre=models.CharField(max_length=30, unique=True)
     def __str__(self) :
          return self.nombre

class Estado(models.Model):
     estadoID=models.IntegerField(primary_key=True)
     descripcion=models.CharField(max_length=20, unique=True)
     def __str__(self) :
          return self.descripcion

class TipoTarjeta(models.Model):
     tipoTarID=models.IntegerField(primary_key=True)
     descripcion=models.CharField(max_length=30, unique=True)
     def __str__(self) :
          return self.descripcion

class MetodoPago(models.Model):
     metodoID=models.IntegerField(primary_key=True)
     descripcion=models.CharField(max_length=20, unique=True)
     def __str__(self) :
          return self.descripcion

class Inventario(models.Model):
     inventarioID=models.AutoField(primary_key=True)
     fecha=models.DateField()
     descripcion=models.CharField(max_length=200)
     def __str__(self) :
          return self.descripcion

class Producto(models.Model):
     codigoPro=models.IntegerField(primary_key=True)
     nombre=models.CharField(max_length=100)
     precio=models.DecimalField(decimal_places=2,max_digits=12)
     precioMayor=models.DecimalField(decimal_places=2,max_digits=12)
     stock=models.IntegerField()
     descripcion=models.CharField(max_length=100)
     talla=models.IntegerField()
     tipoProID=models.ForeignKey('TipoProducto', on_delete=models.DO_NOTHING, default=0)
     marcaID=models.ForeignKey('Marca', on_delete=models.DO_NOTHING, default=0)
     def __str__(self) :
          return self.nombre

class Cliente(models.Model):
  codigoCli=models.AutoField(primary_key=True)
  nombres=models.CharField(max_length=50)
  apellidos=models.CharField(max_length=50)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=30)
  nomUsuario=models.CharField(max_length=30, unique=True)
  direccion=models.CharField(max_length=100)
  telefono=models.CharField(max_length=12)
  sexo=models.CharField(max_length=1, null=True)
  fechaNacimiento=models.DateField(null=True)
  numeroDocumento=models.CharField(max_length=21, unique=True)
  tipoDocID=models.ForeignKey('TipoDocumento', on_delete=models.DO_NOTHING, default=0)
  def __str__(self) :
          return self.nombres

class Tarjeta(models.Model):
     tarjetaID=models.AutoField(primary_key=True)
     numeroTarjeta=models.CharField(max_length=50)
     cvv=models.IntegerField()
     mmaa=models.CharField(max_length=10)
     codigoCli=models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=0)
     tipoTarID=models.ForeignKey('TipoTarjeta', on_delete=models.DO_NOTHING, default=0)
     def __str__(self) :
          return self.numeroTarjeta

class Venta(models.Model):
     ventaID=models.AutoField(primary_key=True)
     fecha=models.DateField()
     hora=models.TimeField()
     monto=models.DecimalField(decimal_places=2,max_digits=12)
     igv=models.DecimalField(decimal_places=2,max_digits=12)
     descuento=models.DecimalField(decimal_places=2,max_digits=12, null=True)#default
     tarjetaID=models.ForeignKey('Tarjeta', on_delete=models.DO_NOTHING, default=0)
     metodoID=models.ForeignKey('MetodoPago', on_delete=models.DO_NOTHING, default=0)
     def __str__(self) :
          return str(self.tarjetaID)

class DetalleVenta(models.Model):
     detalleVentaID=models.AutoField(primary_key=True)
     precio=models.DecimalField(decimal_places=2,max_digits=12)
     cantidad=models.IntegerField()
     codigoPro=models.ForeignKey('Producto', on_delete=models.DO_NOTHING, default=0)
     ventaID=models.ForeignKey('Venta', on_delete=models.DO_NOTHING, default=0)

class DetalleInventario(models.Model):
     detalleInventarioID=models.AutoField(primary_key=True)
     precio=models.DecimalField(decimal_places=2,max_digits=12)
     cantidad=models.IntegerField()
     cantidad_reposicion=models.IntegerField(null=True)
     cantidad_defectuoso=models.IntegerField(null=True)#default
     motivo=models.CharField(max_length=150, null=True)  
     estadoID=models.ForeignKey('Estado', on_delete=models.DO_NOTHING, default=0)
     codigoPro=models.ForeignKey('Producto', on_delete=models.DO_NOTHING, default=0)
     inventarioID=models.ForeignKey('Inventario', on_delete=models.DO_NOTHING, default=0)
    











