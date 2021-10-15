from django.contrib import admin
from gestion.models import Cliente, Articulo, Seccion
# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
  list_display=("nombre","direccion","email","telefono")
  search_fields=("nombre","email")

class ArticulosAdmin(admin.ModelAdmin):
     list_display=("nombre","seccion","precio")
     search_fields=("nombre","precio")
     list_filter=("seccion",)

class SeccionAdmin(admin.ModelAdmin):
     list_display=("nombre",)

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Seccion, SeccionAdmin)