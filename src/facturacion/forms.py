from django import forms
from facturacion.models import Marca, GrupoItem, Unidad, Bodega, Transaccion, Grupo_doc, Rubro_cancelacion

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

BIEN_SERVICIO = (('Bien', 'Bien'), ('Servicio', 'Servicio'))  

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
    