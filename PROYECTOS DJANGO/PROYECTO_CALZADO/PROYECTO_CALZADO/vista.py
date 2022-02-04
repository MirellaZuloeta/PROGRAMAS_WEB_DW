import pyttsx3
from django import template
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import NullBooleanField
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import Template,Context, context
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView
from stripe.api_resources.checkout import session
from administrador.models import Cliente, Comentario, Marca,  Producto, CarritoCompras, TipoProducto, Venta
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView, CreateView
from django.db.models import Q, Max, Min, query
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
import smtplib
from decouple import config
from django. contrib.auth.models import User
from django.conf import settings
import speech_recognition as sr



def talk(text):
    voice=pyttsx3.init()
    voices=voice.getProperty('voices')
    voice.setProperty('voice',voices[-1].id)
    voice.setProperty('rate',140)
    voice.say(text)
    voice.runAndWait()


def buscar_voz(request):
     tipoproductos=TipoProducto.objects.all()
     if 'busqueda' in request.POST:
          r = sr.Recognizer()  
          with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source)
               audio = r.listen(source) 
               try:
                         producto = r.recognize_google(audio, language="es-ES")
                         talk('El producto buscado es '+producto)
                         productos=Producto.objects.filter(nombre__icontains=producto)
               except:
                         producto='' 
                         productos=Producto.objects.all()
               contexto={
                    "producto":producto,
                    "productos":productos,
                    "tipoproductos":tipoproductos
               }
          return render(request,"cyber.html",contexto)
    


def about(request):
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          return render(request,"about.html",{"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"about.html",{"tipoproductos":tipoproductos})

def index(request):
     tipoproductos=TipoProducto.objects.all()  
     clientes= Cliente.objects.filter(foto__icontains='c')
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          return render(request,"index.html",{"tipoproductos":tipoproductos ,"clientes":clientes,"carritos":carritos,"precio":valor})   
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"index.html",{"tipoproductos":tipoproductos ,"clientes":clientes})

def carrito(request):
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          return render(request,"carrito.html",{"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"carrito.html",{"tipoproductos":tipoproductos})


def producto(request):
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          return render(request,"carrito.html",{"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"producto.html",{"tipoproductos":tipoproductos})


def perfil(request):
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          return render(request,"carrito.html",{"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"perfil.html",{"tipoproductos":tipoproductos})

def ubicacion(request):
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          return render(request,"ubicacion.html",{"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"ubicacion.html",{"tipoproductos":tipoproductos})


def registrar(request):
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          return render(request,"ubicacion.html",{"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"registrar.html",{"tipoproductos":tipoproductos})

def contacto(request):
     tipoproductos=TipoProducto.objects.all()
     if 'enviar' in request.GET:
          remitente=request.GET['remitente']
          message=request.GET['mensaje']
          subject=request.GET['asunto']
          correo=request.GET['correo']   
          clave=request.GET['password']
          destinatario='fabiana.sandoval82@gmail.com'
          message='Subject: {}\n\n{}'.format(subject, message)
          server=smtplib.SMTP('smtp.gmail.com', 587)
          server.starttls()
          server.login(correo,clave)
          server.sendmail(correo, destinatario,message)
          server.quit()
          return render(request,"contact.html",{"remitente":remitente,"tipoproductos":tipoproductos})

     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          return render(request,"contact.html",{"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"contact.html",{"tipoproductos":tipoproductos})

def login(request):
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          return render(request,"login.html",{"tipoproductos":tipoproductos ,"carritos":carritos})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"login.html",{"tipoproductos":tipoproductos})

def cyber(request):
     productos=Producto.objects.all()
     tipoproductos=TipoProducto.objects.all()
     if 'carrito' in request.GET:
          usuario=request.GET['usuario']
          carritos=CarritoCompras.objects.filter(comprado=False, pendiente=False, usuario=usuario)
          valor=0
          for carrito in carritos:
               valor=valor+carrito.precio
          return render(request,"cyber.html",{"productos":productos,"tipoproductos":tipoproductos ,"carritos":carritos,"precio":valor})
     if 'filtro1' in request.GET:
          tipo=request.GET['dato1']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro2' in request.GET:
          tipo=request.GET['dato2']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro3' in request.GET:
          tipo=request.GET['dato3']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro4' in request.GET:
          tipo=request.GET['dato4']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     if 'filtro5' in request.GET:
          tipo=request.GET['dato5']
          tipofin=TipoProducto.objects.filter(tipoProID=tipo).get(tipoProID=tipo)       
          productos=Producto.objects.filter(tipoProID=tipofin)
          return render(request,"cyber.html",{"productos":productos, "tipoproductos":tipoproductos})
     return render(request,"cyber.html",{"productos":productos,"tipoproductos":tipoproductos })


def buscar_articulos(request):
     tipoproductos=TipoProducto.objects.all()
     if  request.GET['nombre'] == "":
          obj_productos=Producto.objects.all()
          return render(request,"cyber.html",{"productos":obj_productos, "tipoproductos":tipoproductos})
     else:
          texto_busca= request.GET['nombre']
          productos=Producto.objects.filter(nombre__icontains=texto_busca)
          return render(request,"cyber.html",{"producto":texto_busca,"productos":productos, "tipoproductos":tipoproductos})





class ListadoProductos(ListView):
     template_name ="C:/Users/USER/OneDrive - Catholic University Santo Toribio de Mogrovejo/Desktop/PROYECTO_CALZADO/PROYECTO_CALZADO/plantillas/cyber.html"
     model=Producto
     paginate_by =1

     def get_queryset(self):
          query = None
          if ('nombre' in self.request.GET) and self.request.GET['nombre'] != "":
               query = Q(nombre=self.request.GET["nombre"])

          if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
               try:
                    if query == None:
                         query=Q(precio__lte=int(float(self.request.GET['maximo'])))
                    else:
                          query= query & Q(precio__lte=int(float(self.request.GET['maximo'])))
               except:
                    pass

          if ('minimo' in self.request.GET) and self.request.GET['minimo'] != "":
               try:
                    if query == None:
                         query=Q(precio__gte=int(float(self.request.GET['minimo'])))
                    else:
                          query= query & Q(precio__gte=int(float(self.request.GET['minimo'])))
               except:
                    pass

          if query is not None:
               productos=Producto.objects.filter(query)
          else:
               productos=Producto.objects.all()
          return productos

     def get_context_data(self, **kwargs):
          context =super(ListadoProductos,self).get_context_data(**kwargs)
          context['maximo'] =Producto.objects.all().aggregate(Max('precio'))['precio__max']
          context['minimo'] =Producto.objects.all().aggregate(Min('precio'))['precio__min']
          return context




class Paso02(ListView,LoginRequiredMixin):
     template_name='carrito.html'
     login_url='/ingresar/'
     model=CarritoCompras
     queryset=CarritoCompras.objects.filter(comprado=False, pendiente=False)
     def get_context_data(self, **kwargs):
          context =super(Paso02,self).get_context_data(**kwargs)
          context['tab'] ='paso02'
          return context

class Paso03(ListView,LoginRequiredMixin):
     template_name='carrito.html'
     login_url='/ingresar/'
     model=CarritoCompras
     queryset=CarritoCompras.objects.filter(comprado=False, pendiente=False)
     def get_context_data(self, **kwargs):
          context =super(Paso03,self).get_context_data(**kwargs)
          context['tab'] ='paso03'
          return context

class Paso04(TemplateView,LoginRequiredMixin):
     template_name='carrito.html'
     login_url='/ingresar/'

     def get_context_data(self, **kwargs):
          context =super(Paso04,self).get_context_data(**kwargs)
          context['tab'] ='paso04'
          return context


class DetalleProducto(DetailView):
     template_name='producto.html'
     model =Producto

class Salir(LogoutView):
     next_page= reverse_lazy('index')

class Ingresar(LoginView):
     template_name='login.html'
     def get(self, request, *args, **kwargs):
          if request.user.is_authenticated:
               return HttpResponseRedirect(reverse('index'))
          else:
               context=self.get_context_data(**kwargs)
               return self.render_to_response(context)
     def get_success_url(self):
          return reverse('index')

class CambiarPerfil(LoginRequiredMixin, UpdateView):
     model=User
     fields = ('first_name','last_name','email')
     success_url='/index/'
     template_name='perfil.html'

     def get_object(self, queryset=None) :
         return self.request.user

class ComentarioProducto(CreateView):
     template_name='producto.html'
     model=Comentario
     fields=('comentario','usuario','codigoPro',)

     def get_success_url(self):
          return "/detalle_producto/{}/".format(self.object.codigoPro.pk)

class RegistroUsuario(CreateView):
     template_name="registrar.html"
     model=User
     success_url='/registrar/'
     fields = ('password','username','email',)  
     def get_success_url(self):
          return "/ingresar/"

class RegistrarCliente(CreateView, LoginRequiredMixin):
     template_name='carrito.html'
     model=Cliente
     fields=('telefono','numeroTarjeta','cvv','mmaa','comentario','usuario')
     success_url=reverse_lazy('paso03')

class RegistrarVenta(CreateView, LoginRequiredMixin):
     template_name='carrito.html'
     model=Venta
     valor=Venta.objects.aggregate(Max('ventaID')) 
     dato=valor.get('ventaID__max')
     fields=('subtotal','costoEnvio','total','direccionEnvio','referenciaDireccion','usuario')
     CarritoCompras.objects.filter(comprado=False).update(comprado=True, ventaID=dato)  
     success_url=reverse_lazy('index')

class AniadirCarrito(CreateView, LoginRequiredMixin):
     template_name='producto.html'
     model=CarritoCompras
     fields=('precio','producto','usuario',)
     success_url=reverse_lazy('listar_carrito')
    # login_url='/ingresar/'


class EliminarCarrito(DeleteView,LoginRequiredMixin):
     template_name='carrito.html'
     queryset=CarritoCompras.objects.filter(comprado=False)
     model=CarritoCompras
     success_url=reverse_lazy('listar_carrito')
     login_url='/ingresar/'

class ListarCarrito(ListView,LoginRequiredMixin):
     template_name='carrito.html'
     model=CarritoCompras
     queryset=CarritoCompras.objects.filter(comprado=False)
     login_url='/ingresar/'
     def get_context_data(self, **kwargs):
          context =super(ListarCarrito,self).get_context_data(**kwargs)
          context['tab'] ='sincomprar'
          return context

class ListarCarritoFinalizadas(ListView,LoginRequiredMixin):
     template_name='carrito.html'
     model=CarritoCompras
     queryset=CarritoCompras.objects.filter(comprado=True)
     login_url='/ingresar/'

     def get_context_data(self, **kwargs):
          context =super(ListarCarritoFinalizadas,self).get_context_data(**kwargs)
          context['tab'] ='finalizadas'
          return context




