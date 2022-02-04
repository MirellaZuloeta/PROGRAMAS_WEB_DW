from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField

# Create your models here.

class TipoDocumento(models.Model):
     tipoDocID=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=30, unique=True)
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
  sexo=models.CharField(max_length=1,null=True, blank=True) 
  fechaNacimiento=models.DateField(null=True, blank=True) 
  numeroDocumento=models.CharField(max_length=21, unique=True)
  tipoDocID=models.ForeignKey('TipoDocumento', on_delete=models.DO_NOTHING, default=0)
  foto=models.ImageField(upload_to="clientes", blank=True, null=True) 
  def __str__(self) :
          return self.nombres
