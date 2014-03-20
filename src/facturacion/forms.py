from django import forms
from facturacion.models import Marca, GrupoItem, Unidad, Canton, Provincia, \
Bodega, Transaccion, Grupo_doc, Rubro_cancelacion


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
    iva = forms.BooleanField(label='Autorizar facturacion',initial=False,required=False)
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
    

class CrearDocumentoForm(forms.Form):
    codigo_propio = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.TextInput())
    tabs = forms.CharField(widget=forms.TextInput())
    iva = forms.BooleanField(label='Lleva IVA',initial=False,required=False)
    con_precio = forms.BooleanField(label='Lleva precio',initial=False,required=False)
    con_items = forms.BooleanField(label='Lleva items',initial=False,required=False)
    transaccion = forms.ModelChoiceField(queryset=Transaccion.objects.order_by('descripcion'))
    grupo_doc = forms.ModelChoiceField(label='Grupo de documento',queryset=Grupo_doc.objects.order_by('descripcion'))
    rubro_canc = forms.ModelChoiceField(label='Rubro de cancelacion',queryset=Rubro_cancelacion.objects.order_by('descripcion'))
   
class TransaccionForm(forms.Form):
    codigo = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.TextInput())
    tabs = forms.CharField(widget=forms.TextInput())
    
class GrupoDocForm(forms.Form):
    codigo = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.TextInput())
    tabs = forms.CharField(widget=forms.TextInput())
    
class RubroCancelacionForm(forms.Form):
    codigo = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.TextInput())
    tabs = forms.CharField(widget=forms.TextInput())
    

