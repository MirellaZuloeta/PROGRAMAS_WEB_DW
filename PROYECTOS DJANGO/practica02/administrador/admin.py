from django.contrib import admin
from administrador.models import TipoProducto,Producto
# Register your models here.
class TipoProductosAdmin(admin.ModelAdmin):
  list_display=("tipoProId","nombre","descripcion")
  search_fields=("nombre",)
  list_filter=("nombre","descripcion")

class ProductosAdmin(admin.ModelAdmin):
     list_display=("idProducto","nombre","precio","stock","marca","descripcion","talla","tipoPro")
     search_fields=("nombre","precio","marca")
     list_filter=("marca","talla","tipoPro")

admin.site.register(TipoProducto,TipoProductosAdmin)
admin.site.register(Producto, ProductosAdmin)
