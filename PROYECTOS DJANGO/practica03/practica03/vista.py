from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from administrador.models import Cliente, TipoDocumento
from datetime import datetime
from django import forms
from .forms import RegistrarDocumento

def listaclientes(request):
    obj_clientes=Cliente.objects.all()
    return render(request,"lista_clientes.html", {"clientes":obj_clientes})

def formulario(request):
	return render(request, "buscar_clientes.html")


def buscar_cliente(request):
	texto_busca = request.GET['dato']
	clientes = Cliente.objects.filter(nombres__icontains=texto_busca)
	return render(request, "buscar_clientes.html",{"cliente":texto_busca, "clientes":clientes})

def registrarDoc(request):
    register_form = RegistrarDocumento()
    return render(request, 'registrar_documento.html', {'register_form': register_form})

def registrar(self):
        nuevo_usuario = TipoDocumento(nombre=self.data['nombre'])
        nuevo_usuario.save()
        return 'Registro exitoso'

