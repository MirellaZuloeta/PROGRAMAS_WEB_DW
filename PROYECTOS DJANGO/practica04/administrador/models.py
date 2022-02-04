from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField
from django.contrib.auth.models import User



class Curso(models.Model):
     codigoCurso=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=100)
     descripcion=models.CharField(max_length=100)
     imagen=models.ImageField(upload_to="imgcursos", blank=True, null=True) 
     def __str__(self) :
          return self.nombre

class Usuario(models.Model):
  codigoUsuario=models.AutoField(primary_key=True)
  nombres=models.CharField(max_length=50)
  apellidos=models.CharField(max_length=50)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=30)
  nomUsuario=models.CharField(max_length=30, unique=True)
  direccion=models.CharField(max_length=300)
  telefono=models.CharField(max_length=12)
  sexo=models.CharField(max_length=1,null=True, blank=True) #####################
  fechaNacimiento=models.DateField(null=True, blank=True) ######################
  numeroDocumento=models.CharField(max_length=21, unique=True)
  foto=models.ImageField(upload_to="fotousers", blank=True, null=True) 
  comentario=models.CharField(max_length=300,null=True, blank=True)
  codigoCursp=models.ForeignKey('Curso', on_delete=models.DO_NOTHING, default=0)
  def __str__(self) :
          return self.nombres