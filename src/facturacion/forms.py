from django import forms
from facturacion.models import Marca, GrupoItem, Unidad, Bodega, Canton,\
    Provincia

class MarcaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    codigo_propio = forms.CharField(widget=forms.TextInput())
    
class GrupoForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    codigo_propio = forms.CharField(widget=forms.TextInput())
    
class BodegaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    codigo_propio = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    
class UnidadForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    codigo_propio = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.TextInput())
    

BIEN_SERVICIO = (('Bien', 'Bien'), ('Servicio', 'Servicio'))    

class ItemForm(forms.Form):
    codigo_propio = forms.CharField(widget=forms.TextInput())
    codigo_barras = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.TextInput())
    #Bien_o_Servicio = forms.ChoiceField(choices=BIEN_SERVICIO, widget=forms.RadioSelect)
    Bien_o_Servicio = forms.CharField(max_length=30,widget=forms.Select(choices=BIEN_SERVICIO))
    iva = forms.BooleanField(required=False)
    ubicacion = forms.CharField(widget=forms.TextInput())
    marca = forms.ModelChoiceField(queryset=Marca.objects.all())
    grupo = forms.ModelChoiceField(queryset=GrupoItem.objects.all())
    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all())
    bodega = forms.ModelChoiceField(queryset=Bodega.objects.all(),required=False)
    

class ProveedoresForm(forms.Form):
    nombre_comercial = forms.CharField(widget=forms.TextInput())
    codigo_propio = forms.CharField(widget=forms.TextInput())
    razon_social = forms.CharField(widget=forms.TextInput())
    ruc = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.all())
    canton = forms.ModelChoiceField(queryset=Canton.objects.all())
    email = forms.EmailField(label='Correo',widget=forms.TextInput(),required=False)
    telefono = forms.CharField(widget=forms.TextInput(),required=False)
    fax = forms.CharField(widget=forms.TextInput(),required=False)
    
class ClientesForm(forms.Form):
    nombre_comercial = forms.CharField(widget=forms.TextInput())
    codigo_propio = forms.CharField(widget=forms.TextInput())
    razon_social = forms.CharField(widget=forms.TextInput())
    ruc = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.all())
    canton = forms.ModelChoiceField(queryset=Canton.objects.all())
    email = forms.EmailField(label='Correo',widget=forms.TextInput(),required=False)
    telefono = forms.CharField(widget=forms.TextInput(),required=False)
    fax = forms.CharField(widget=forms.TextInput(),required=False)
    
