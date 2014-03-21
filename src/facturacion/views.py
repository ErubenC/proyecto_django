from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from facturacion.forms import MarcaForm,BodegaForm,UnidadForm,GrupoForm,\
   TransaccionForm, ItemForm, ProveedoresForm, ClientesForm, GrupoDocForm,\
    RubroCancelacionForm, CrearDocumentoForm
from facturacion.models import Marca, GrupoItem, Bodega, Unidad, Item, Proveedor,\
    Cliente, Canton, Transaccion, Grupo_doc, Rubro_cancelacion, Documento

from django.views.generic.list import ListView
from django.utils.datastructures import MultiValueDictKeyError

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
            print 'el id es:'
            print form.cleaned_data['marca']
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
    

def clientes_view(request):
    
    mensaje = ""
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            u = Cliente()
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
            form = ClientesForm()
        else:
            mensaje = "Llene correctamente los campos."
        
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/cliente.html",ctx,context_instance=RequestContext(request))
    else:
        form = ClientesForm()
        ctx = {"form":form}
        return render_to_response("facturacion/cliente.html",ctx,context_instance=RequestContext(request))
    
    
    
       
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
        return render_to_response("facturacion/proveedor.html",ctx,context_instance=RequestContext(request))
    else:
        form = ProveedoresForm()
        ctx = {"form":form}
        return render_to_response("facturacion/proveedor.html",ctx,context_instance=RequestContext(request))
    
    
def carga_cantones_view(request):
    if request.method == "GET":
        provincia = request.GET['value']
        if provincia == "":
            return render_to_response("facturacion/carga_cantones.html",context_instance=RequestContext(request))
        cantones = Canton.objects.filter(provincia=provincia)
        ctx = {"cantones":cantones}
        return render_to_response("facturacion/carga_cantones.html",ctx,context_instance=RequestContext(request))
    
    
class IndexView(ListView):
    model = Marca
    paginate_by = 5
    queryset = Marca.objects.all()
    
def config_doc_view(request):
    return render_to_response("facturacion/base_config_doc.html",context_instance=RequestContext(request))
    
def grupo_doc_view(request):
    mensaje = ""
    if request.method == "POST":
        form = GrupoDocForm(request.POST)
        if form.is_valid():
            gd = Grupo_doc()
            gd.codigo = form.cleaned_data['codigo']
            gd.descripcion = form.cleaned_data['descripcion']
            gd.tabs = form.cleaned_data['tabs']
            gd.save()
            mensaje = "Se agrego satisfactoriamente."
            form = GrupoDocForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    else:
        form = GrupoDocForm()
        ctx = {"form":form}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    
    
def rubros_canc_view(request):
    mensaje = ""
    if request.method == "POST":
        form = RubroCancelacionForm(request.POST)
        if form.is_valid():
            rc = Rubro_cancelacion()
            rc.codigo = form.cleaned_data['codigo']
            rc.descripcion = form.cleaned_data['descripcion']
            rc.tabs = form.cleaned_data['tabs']
            rc.save()
            mensaje = "Se agrego satisfactoriamente."
            form = RubroCancelacionForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"title":'Rubros de cancelacion',"titulo_pagina":'Agregar rubros de cancelacion'}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    else:
        form = GrupoDocForm()
        ctx = {"form":form,"title":'Rubros de cancelacion',"titulo_pagina":'Agregar rubros de cancelacion'}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    
def tipo_transaccion_view(request):
    mensaje = ""
    if request.method == "POST":
        form = TransaccionForm(request.POST)
        if form.is_valid():
            t = Transaccion()
            t.codigo = form.cleaned_data['codigo']
            t.descripcion = form.cleaned_data['descripcion']
            t.tabs = form.cleaned_data['tabs']
            t.save()
            mensaje = "Se agrego satisfactoriamente."
            form = TransaccionForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"title":'Tipos de transaccion',"titulo_pagina":'Agregar tipos de transaccion'}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    else:
        form = GrupoDocForm()
        ctx = {"form":form,"title":'Tipos de transaccion',"titulo_pagina":'Agregar tipos de transaccion'}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    
def tipo_documento_view(request):
    mensaje = ""
    if request.method == "POST":
        form = CrearDocumentoForm(request.POST)
        if form.is_valid():
            d = Documento()
            d.codigo = form.cleaned_data['codigo']
            d.descripcion = form.cleaned_data['descripcion']
            d.tabs = form.cleaned_data['tabs']
            d.iva = form.cleaned_data['iva']
            d.con_precio = form.cleaned_data['con_precio']
            d.con_items = form.cleaned_data['con_items']
            d.transaccion = form.cleaned_data['transaccion']
            d.grupo_doc = form.cleaned_data['grupo_doc']
            d.rubro_cancelacion = form.cleaned_data['rubro_canc']
            d.save()
            mensaje = "Se agrego satisfactoriamente."
            form = CrearDocumentoForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"title":'Tipos de documentos',"titulo_pagina":'Agregar nuevo tipo de documento'}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    else:
        form = CrearDocumentoForm()
        ctx = {"form":form,"title":'Tipos de documentos',"titulo_pagina":'Agregar nuevo tipo de documento'}
        return render_to_response("facturacion/config_doc.html",ctx,context_instance=RequestContext(request))
    
    
    '''
    La vista documento_view genera dinamicamente un formato de documento que depende
    de las caracteristicas antes definidas
    '''
def documento_view(request):
    try:
        tipo = request.GET['tipo']
        print tipo
    except MultiValueDictKeyError:
        print "no envio un parametro get"
    return render_to_response("facturacion/documento.html",context_instance=RequestContext(request))
     

    

    
    
