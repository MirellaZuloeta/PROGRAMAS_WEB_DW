from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from gestion.models import Articulo
from datetime import datetime

def saludo(request):
  return HttpResponse("Mi primera web con DJango")

class Persona(object):
  def __init__(self,nombre,apellido) :
      self.nombre=nombre
      self.apellido=apellido

def uso_plantilla(request):
  persona1=Persona("Jaime","Torres")
  universidad="USAT"
  ahora=datetime.now()
  cursos=["BASE DE DATOS","REDES","IA"]
  archivo_html=open("C:/Users/USER/OneDrive - Catholic University Santo Toribio de Mogrovejo/Desktop/PROGRAMAS_WEB_DW/PROYECTOS DJANGO/proyecto01/proyecto01/plantillas/plantilla1.html")
  templ=Template(archivo_html.read())
  archivo_html.close()
  contx=Context({"nombre_universidad":universidad,"fechahora" :ahora,"nombre_persona":persona1.nombre,"apellido_persona":persona1.apellido,"cursos":cursos})
  documento=templ.render(contx)
  return HttpResponse(documento)
  

def listaarticulos(request):
    obj_articulos=Articulo.objects.all()
    return render(request,"lista_articulos.html", {"articulos":obj_articulos})