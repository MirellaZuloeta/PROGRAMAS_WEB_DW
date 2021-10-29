from django.contrib import admin
from administrador.models import TipoProducto,Marca, TipoDocumento,Tarjeta,Estado,Inventario,Cliente,Producto, Venta,DetalleVenta,DetalleInventario, Estilo, Dimension, Color
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

class EstadosAdmin(admin.ModelAdmin):
     list_display=("estadoID","descripcion")
     search_fields=("descripcion",)
     list_filter=("descripcion",)

class InventariosAdmin(admin.ModelAdmin):
     list_display=("inventarioID","fecha","descripcion")
     search_fields=("fecha",)
     list_filter=("fecha",)

class ProductosAdmin(admin.ModelAdmin):
     list_display=("codigoPro","nombre","precio","precioMayor","stock","descripcion","talla","tipoProID","marcaID","estiloID","dimensionID","colorID","imagen")
     search_fields=("nombre","talla")
     list_filter=("nombre","talla")

class ClientesAdmin(admin.ModelAdmin):
     list_display=("codigoCli","nombres","apellidos","email","password","nomUsuario","direccion","telefono","sexo","fechaNacimiento","numeroDocumento","tipoDocID","foto")
     search_fields=("nombres","numeroDocumento")
     list_filter=("nombres","numeroDocumento")

class TarjetasAdmin(admin.ModelAdmin):
     list_display=("tarjetaID","numeroTarjeta","cvv","mmaa","codigoCli")
     search_fields=("codigoCli",)
     list_filter=("codigoCli",)

class VentasAdmin(admin.ModelAdmin):
     list_display=("ventaID","fecha","hora","monto","igv","descuento","tarjetaID")
     search_fields=("fecha",)
     list_filter=("fecha",)

class DetalleVentasAdmin(admin.ModelAdmin):
     list_display=("detalleVentaID","precio","cantidad","codigoPro","ventaID")
     search_fields=("codigoPro","ventaID")
     list_filter=("codigoPro","ventaID")

class DetalleInventariosAdmin(admin.ModelAdmin):
     list_display=("detalleInventarioID","precio","cantidad","cantidad_reposicion","cantidad_defectuoso","motivo","estadoID","codigoPro","inventarioID")
     search_fields=("codigoPro","inventarioID")
     list_filter=("codigoPro","inventarioID")


admin.site.register(Estilo, EstilosAdmin)
admin.site.register(Color, ColoresAdmin)
admin.site.register(Dimension, DimensionesAdmin)
admin.site.register(TipoProducto,TipoProductosAdmin)
admin.site.register(Marca,MarcasAdmin)
admin.site.register(TipoDocumento, TipoDocumentosAdmin)
admin.site.register(Estado, EstadosAdmin)
admin.site.register(Inventario, InventariosAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Tarjeta, TarjetasAdmin)
admin.site.register(Venta, VentasAdmin)
admin.site.register(DetalleVenta, DetalleVentasAdmin)
admin.site.register(DetalleInventario, DetalleInventariosAdmin)