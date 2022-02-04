from django.contrib import admin
from administrador.models import TipoDocumento,Cliente
# Register your models here.

# Register your models here.
class TipoDocumentosAdmin(admin.ModelAdmin):
     list_display=("tipoDocID","nombre")
     search_fields=("nombre",)
     list_filter=("nombre",)


class ClientesAdmin(admin.ModelAdmin):
     list_display=("codigoCli","nombres","apellidos","email","password","nomUsuario","direccion","telefono","sexo","fechaNacimiento","numeroDocumento","tipoDocID","foto")
     search_fields=("nombres","numeroDocumento")
     list_filter=("nombres","numeroDocumento")

admin.site.register(TipoDocumento, TipoDocumentosAdmin)
admin.site.register(Cliente, ClientesAdmin)