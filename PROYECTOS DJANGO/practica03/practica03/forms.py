from django import forms
from administrador.models import TipoDocumento

class RegistrarDocumento(forms.Form):
 nombre = forms.CharField(label='Nombre',max_length=30)

