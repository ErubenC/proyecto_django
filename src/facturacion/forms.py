from django import forms

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
    nombre = forms.CharField(widget=forms.TextInput())
    codigo_propio = forms.CharField(widget=forms.TextInput())
    codigo_barras = forms.CharField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.TextInput())
    bien = forms.CharField(widget=forms.TextInput())
    servicio = forms.CharField(widget=forms.TextInput())
    iva = forms.CharField(widget=forms.TextInput())
    ubicacion = forms.CharField(widget=forms.TextInput())
    marca = forms.CharField(widget=forms.TextInput())
    grupo = forms.CharField(widget=forms.TextInput())
    unidad = forms.CharField(widget=forms.TextInput())
    item_bodega = forms.CharField(widget=forms.TextInput())
    
