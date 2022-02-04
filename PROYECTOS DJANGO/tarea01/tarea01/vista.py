from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from administrador.models import Cliente
from datetime import datetime


def listaclientes(request):
    obj_clientes=Cliente.objects.all()
    return render(request,"lista_clientes.html", {"clientes":obj_clientes})