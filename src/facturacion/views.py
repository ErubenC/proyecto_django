from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from facturacion.forms import MarcaForm,BodegaForm,UnidadForm,GrupoForm,\
    ItemForm, ProveedoresForm
from facturacion.models import Marca, GrupoItem, Bodega, Unidad, Item, Proveedor
from django.contrib.auth.decorators import login_required, user_passes_test
from pcardext import cp

def facturacion_view(request):
    return render_to_response("facturacion/base.html", context_instance=RequestContext(request))


def marca_view(request):
    mensaje = ""
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            m = Marca()
            m.nombre = form.cleaned_data['nombre']
            m.codigo_propio = form.cleaned_data['codigo_propio']
            m.save()
            mensaje = "Se agrego satisfactoriamente."
        else:
            mensaje = "Llene correctamente los campos."
        form = MarcaForm()
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/marca.html",ctx,context_instance=RequestContext(request))
    else:
        form = MarcaForm()
        ctx = {"form":form}
        return render_to_response("facturacion/marca.html",ctx,context_instance=RequestContext(request))
   
def grupo_view(request):
    mensaje = ""
    if request.method == "POST":
        form = GrupoForm(request.POST)
        if form.is_valid():
            g = GrupoItem()
            g.nombre = form.cleaned_data['nombre']
            g.codigo_propio = form.cleaned_data['codigo_propio']
            g.save()
            mensaje = "Se agrego satisfactoriamente."
        else:
            mensaje = "Llene correctamente los campos."
        form = GrupoForm()
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/grupo.html",ctx,context_instance=RequestContext(request))
    else:
        form = GrupoForm()
        ctx = {"form":form}
        return render_to_response("facturacion/grupo.html",ctx,context_instance=RequestContext(request))
   
def bodega_view(request):
    mensaje = ""
    if request.method == "POST":
        form = BodegaForm(request.POST)
        if form.is_valid():
            b = Bodega()
            b.nombre = form.cleaned_data['nombre']
            b.codigo_propio = form.cleaned_data['codigo_propio']
            b.direccion = form.cleaned_data['direccion']
            b.save()
            mensaje = "Se agrego satisfactoriamente."
        else:
            mensaje = "Llene correctamente los campos."
        form = BodegaForm()
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/bodega.html",ctx,context_instance=RequestContext(request))
    else:
        form = BodegaForm()
        ctx = {"form":form}
        return render_to_response("facturacion/bodega.html",ctx,context_instance=RequestContext(request))
   
def unidad_view(request):
    mensaje = ""
    if request.method == "POST":
        form = UnidadForm(request.POST)
        if form.is_valid():
            u = Unidad()
            u.nombre = form.cleaned_data['nombre']
            u.codigo_propio = form.cleaned_data['codigo_propio']
            u.descripcion = form.cleaned_data['descripcion']
            u.save()
            mensaje = "Se agrego satisfactoriamente."
        else:
            mensaje = "Llene correctamente los campos."
        form = UnidadForm()
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/unidad.html",ctx,context_instance=RequestContext(request))
    else:
        form = UnidadForm()
        ctx = {"form":form}
        return render_to_response("facturacion/unidad.html",ctx,context_instance=RequestContext(request))
   
def item_view(request):
    mensaje = ""
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            u = Item()
            u.codigo_propio = form.cleaned_data['codigo_propio']
            u.codigo_barras = form.cleaned_data['codigo_barras']
            u.descripcion = form.cleaned_data['descripcion']
            if form.cleaned_data['Bien_o_Servicio'] == "Bien":
                u.es_bien = True
                u.es_servicio = False
            else:
                u.es_bien = False
                u.es_servicio = True
            u.iva = form.cleaned_data['iva']
            u.ubicacion = form.cleaned_data['ubicacion']
            u.id_marca =form.cleaned_data['marca']
            u.id_unidad = form.cleaned_data['unidad']
            u.id_grupo = form.cleaned_data['grupo']
            
            u.save()
            
            if(form.cleaned_data['bodega']!=""):
                bod = form.cleaned_data['bodega']
                u.item_bodega.add(bod)
            
            mensaje = "Se agrego satisfactoriamente."
            form = ItemForm()
        else:
            mensaje = "Llene correctamente los campos."
        
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/item.html",ctx,context_instance=RequestContext(request))
    else:
        form = ItemForm()
        ctx = {"form":form}
        return render_to_response("facturacion/item.html",ctx,context_instance=RequestContext(request))
   
def proveedores_view(request):
    
    mensaje = ""
    if request.method == "POST":
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            u = Proveedor()
            u.nombre_comercial = form.cleaned_data['nombre_comercial']
            u.codigo_propio = form.cleaned_data['codigo_propio']
            u.razon_social = form.cleaned_data['razon_social']
            u.ruc = form.cleaned_data['ruc']
            u.direccion = form.cleaned_data['direccion']
            u.canton = form.cleaned_data['canton']
            u.mail = form.cleaned_data['email']
            u.telefono = form.cleaned_data['telefono']
            u.fax = form.cleaned_data['fax']
            u.save()
            
            mensaje = "Se agrego satisfactoriamente."
            form = ProveedoresForm()
        else:
            mensaje = "Llene correctamente los campos."
        
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/proveedores.html",ctx,context_instance=RequestContext(request))
    else:
        form = ProveedoresForm()
        ctx = {"form":form}
        return render_to_response("facturacion/proveedores.html",ctx,context_instance=RequestContext(request))
    
    
    