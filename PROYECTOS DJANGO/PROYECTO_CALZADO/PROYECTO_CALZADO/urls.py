"""PROYECTO_CALZADO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from PROYECTO_CALZADO.vista import buscar_voz,registrar,perfil,producto,carrito,RegistrarVenta,RegistrarCliente,Paso04, Paso02,Paso03,RegistroUsuario,ListarCarrito,CambiarPerfil,index,carrito,Ingresar ,ListarCarritoFinalizadas,EliminarCarrito,AniadirCarrito,cyber,contacto,ubicacion,DetalleProducto,buscar_articulos,about, ComentarioProducto,login, Ingresar, Salir


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path("cyber/",cyber, name='cyber'),
    path("base/",cyber, name='base'),
    path('ubicacion/', ubicacion, name='ubicacion'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login , name='login'),
    path('ingresar/', Ingresar.as_view(), name='ingresar'),
    path('registrar/', RegistroUsuario.as_view(), name='registrar'),
    path('cambiar_perfil/', CambiarPerfil.as_view(), name='cambiar_perfil'),
    path('salir/', Salir.as_view() , name='salir'),
    path('detalle_producto/<int:pk>/', DetalleProducto.as_view(),name='detalle_producto'),
    path('crear_comentario/' ,ComentarioProducto.as_view(), name='crear_comentario'),
    path('aniadir_carrito/', AniadirCarrito.as_view() , name='aniadir_carrito'),
    path('listar_carrito/', ListarCarrito.as_view() , name='listar_carrito'),
    path('listar_finalizado/', ListarCarritoFinalizadas.as_view() , name='listar_finalizado'),
    path('eliminar_carrito/<int:pk>/', EliminarCarrito.as_view(),name='eliminar_carrito'),
    path('carrito/', carrito , name='carrito'),
    path("buscar/",buscar_articulos, name='buscar'),
    path('paso04/', Paso04.as_view() , name='paso04'),
    path('paso02/', Paso02.as_view() , name='paso02'),
    path('paso03/', Paso03.as_view() , name='paso03'),
    path('registrarCliente/', RegistrarCliente.as_view() , name='registrarCliente'),
    path('registrarVenta/', RegistrarVenta.as_view() , name='registrarVenta'),
    path('producto/', producto , name='producto'),
    path('perfil/', perfil , name='perfil'),
    path('registro/', registrar , name='registro'),
    path("buscar2/",buscar_voz, name='buscar2'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)