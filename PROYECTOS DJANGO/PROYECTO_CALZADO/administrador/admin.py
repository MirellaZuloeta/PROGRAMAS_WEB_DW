from django.contrib import admin
from administrador.models import TipoProducto,Marca,Venta ,CarritoCompras,TipoDocumento,Cliente,Producto, Estilo, Dimension, Color, Comentario
# Register your models here.

class EstilosAdmin(admin.ModelAdmin):
     list_display=("estiloID","nombre")
     search_fields=("nombre",)
     list_filter=("nombre",)

class DimensionesAdmin(admin.ModelAdmin):
     list_display=("dimensionID","descripcion")
     search_fields=("descripcion",)
     list_filter=("descripcion",)

class ColoresAdmin(admin.ModelAdmin):
     list_display=("colorID","nombre")
     search_fields=("nombre",)
     list_filter=("nombre",)

class CarritoComprasAdmin(admin.ModelAdmin):
     list_display=("carritoID","precio","producto","usuario","cantidad","comprado","ventaID")
     search_fields=("producto","usuario")
     list_filter=("producto","usuario")

class VentasAdmin(admin.ModelAdmin):
     list_display=("ventaID","fecha","hora","subtotal","costoEnvio","total","pendiente","direccionEnvio","referenciaDireccion","usuario")
     search_fields=("fecha","hora")
     list_filter=("fecha","hora")


class TipoProductosAdmin(admin.ModelAdmin):
     list_display=("tipoProID","nombre","imagen")
     search_fields=("nombre",)
     list_filter=("nombre",)

class MarcasAdmin(admin.ModelAdmin):
     list_display=("marcaID","nombre")
     search_fields=("nombre",)
     list_filter=("nombre",)

class TipoDocumentosAdmin(admin.ModelAdmin):
     list_display=("tipoDocID","nombre")
     search_fields=("nombre",)
     list_filter=("nombre",)

class ProductosAdmin(admin.ModelAdmin):
     list_display=("codigoPro","nombre","precio","precioMayor","stock","descripcion","talla","tipoProID","marcaID","estiloID","dimensionID","colorID","imagen")
     search_fields=("nombre","talla")
     list_filter=("nombre","talla")

class ClientesAdmin(admin.ModelAdmin):
     list_display=("codigoCli","nombres","apellidos","direccion","telefono","sexo","fechaNacimiento","numeroDocumento","numeroTarjeta","cvv","mmaa","tipoDocID","foto","comentario","usuario")
     search_fields=("nombres","numeroDocumento")
     list_filter=("nombres","numeroDocumento")

class ComentariosAdmin(admin.ModelAdmin):
     list_display=("comentarioID","comentario","usuario","fecha","codigoPro")
     search_fields=("usuario","codigoPro")
     list_filter=("usuario","codigoPro")

admin.site.register(Estilo, EstilosAdmin)
admin.site.register(Color, ColoresAdmin)
admin.site.register(Dimension, DimensionesAdmin)
admin.site.register(TipoProducto,TipoProductosAdmin)
admin.site.register(Marca,MarcasAdmin)
admin.site.register(TipoDocumento, TipoDocumentosAdmin)
admin.site.register(Venta, VentasAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Comentario,ComentariosAdmin)
admin.site.register(CarritoCompras,CarritoComprasAdmin)