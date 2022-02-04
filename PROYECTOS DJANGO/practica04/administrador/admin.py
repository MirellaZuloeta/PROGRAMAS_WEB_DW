from django.contrib import admin
from administrador.models import Usuario, Curso

class UsuariosAdmin(admin.ModelAdmin):
     list_display=("codigoUsuario","nombres","apellidos","email","password","codigoCursp","foto","numeroDocumento")
     search_fields=("nombres","numeroDocumento")
     list_filter=("nombres","numeroDocumento")

class CursosAdmin(admin.ModelAdmin):
     list_display=("codigoCurso","nombre","descripcion","imagen")
     search_fields=("codigoCurso","nombre")
     list_filter=("codigoCurso","nombre")


admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(Curso, CursosAdmin)