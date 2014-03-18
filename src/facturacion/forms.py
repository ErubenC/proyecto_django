from django import forms
from facturacion.models import Marca, GrupoItem, Unidad

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
    #bien = forms.BooleanField()
    #servicio = forms.BooleanField()
    iva = forms.BooleanField(required=False)
    ubicacion = forms.CharField(widget=forms.TextInput())
    marca = forms.ModelChoiceField(queryset=Marca.objects.all())
    grupo = forms.ModelChoiceField(queryset=GrupoItem.objects.all())
    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all())
    #marca = forms.CharField(widget=forms.TextInput())
    #grupo = forms.CharField(widget=forms.TextInput())
    #unidad = forms.CharField(widget=forms.TextInput())
    
