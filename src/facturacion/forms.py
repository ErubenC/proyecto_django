from django import forms
from facturacion.models import Marca, GrupoItem, Unidad, Bodega

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
    marca = forms.ModelChoiceField(queryset=Marca.objects.order_by('nombre'))
    grupo = forms.ModelChoiceField(queryset=GrupoItem.objects.order_by('nombre'))
    unidad = forms.ModelChoiceField(queryset=Unidad.objects.order_by('nombre'))
    bodega = forms.ModelChoiceField(queryset=Bodega.objects.order_by('nombre'),required=False)
    
'''   def clean_marca(self):
        if "(" in self.cleaned_data['marca']:
            marca = self.cleaned_data['marca'].split("(")[1]
            if ")" in marca:
                marca = marca.split(")")[0]                
                try:
                    Marca.objects.get(codigo_propio=marca)
                except Marca.DoesNotExist:
                    raise forms.ValidationError('Marca no existe')
                return marca
        raise forms.ValidationError('Marca no existe')
    
    def clean_unidad(self):
        if "(" in self.cleaned_data['unidad']:
            unidad = self.cleaned_data['unidad'].split("(")[1]
            if ")" in unidad:
                unidad = unidad.split(")")[0]                
                try:
                    Unidad.objects.get(codigo_propio=unidad)
                except Unidad.DoesNotExist:
                    raise forms.ValidationError('Unidad no existe')
                print unidad
                return unidad
        raise forms.ValidationError('Unidad no existe')
    
    def clean_grupo(self):
        if "(" in self.cleaned_data['grupo']:
            grupo = self.cleaned_data['grupo'].split("(")[1]
            if ")" in grupo:
                grupo = grupo.split(")")[0]                
                try:
                    GrupoItem.objects.get(codigo_propio=grupo)
                except GrupoItem.DoesNotExist:
                    raise forms.ValidationError('Grupo no existe')
                return grupo
        raise forms.ValidationError('Grupo no existe')
    
    def clean_bodega(self):
        if "(" in self.cleaned_data['bodega']:
            bodega = self.cleaned_data['bodega'].split("(")[1]
            if ")" in bodega:
                bodega = bodega.split(")")[0]                
                try:
                    Bodega.objects.get(codigo_propio=bodega)
                except Bodega.DoesNotExist:
                    raise forms.ValidationError('Bodega no existe')
                return bodega
        raise forms.ValidationError('Bodega no existe')
    
'''   