from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from gestion.models import Articulo
from datetime import datetime

def saludo(request):
	return HttpResponse("Mi primera web con DJango")

class Persona(object):
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido 

def uso_plantilla(request):
	persona1 = Persona("Jaime","Torres")
	universidad = "USAT"
	ahora = datetime.now()
	cursos = ["Base de Datos","Redes de computadoras","Inteligencia Artificial"]
	archivo_html = open("D:/Oscar/USAT/python/ProyectosDjango/proyecto001/proyecto001/plantillas/plantilla1.html")
	templ = Template(archivo_html.read())
	archivo_html.close()
	contx = Context({"nombre_universidad":universidad, "fechahora":ahora, "nombre_persona":persona1.nombre, "apellido_persona": persona1.apellido, "cursos": cursos} )
	documento = templ.render(contx)
	return HttpResponse(documento)

def listaarticulos(request):
	obj_articulos = Articulo.objects.all()
	return render(request, "lista_articulos.html",{"articulos":obj_articulos})

def formulario(request):
	return render(request, "formulario.html")

def buscar_articulo(request):
	texto_busca = request.GET['dato']
	articulos = Articulo.objects.filter(nombre__icontains=texto_busca)
	return render(request, "formulario.html",{"articulo":texto_busca, "articulos":articulos})
	#return render(request, "resultado_busqueda.html",{"articulo":texto_busca, "articulos":articulos})