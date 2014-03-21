from django.shortcuts import render_to_response
from django.template import RequestContext
from facturacion.forms import MarcaForm,BodegaForm,UnidadForm,GrupoForm,\
    ItemForm, ProveedoresForm, ClientesForm
from facturacion.models import Marca, GrupoItem, Bodega, Unidad, Item, Proveedor,\
    Cliente, Canton
from django.views.generic.list import ListView

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
            '''
            if(form.cleaned_data['bodega']!=""):
                bod = form.cleaned_data['bodega']
                u.item_bodega.add(bod)
            '''
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
    
class Pag_ListView(ListView):
    paginate_by = 8
    
def editar_unidad_view(request):
    if request.method == "GET":
        pk = request.GET['pk']
        unidad = Unidad.objects.filter(pk=pk).first()
        form = UnidadForm({"nombre":unidad.nombre,"descripcion":unidad.descripcion,"codigo_propio":unidad.codigo_propio});
        ctx = {"form":form,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx, context_instance=RequestContext(request))
    if request.method == "POST":
        pk = request.POST['cod']
        unidad = Unidad.objects.filter(pk=pk).first()
        form = UnidadForm(request.POST)
        if form.is_valid():
            unidad.nombre = form.cleaned_data['nombre']
            unidad.codigo_propio = form.cleaned_data['codigo_propio']
            unidad.descripcion = form.cleaned_data['descripcion']
            unidad.save()
            mensaje = "Correcto"
            form = UnidadForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx,context_instance=RequestContext(request))

def editar_grupo_view(request):
    if request.method == "GET":
        pk = request.GET['pk']
        grupo = GrupoItem.objects.filter(pk=pk).first()
        form = GrupoForm({"nombre":grupo.nombre,"codigo_propio":grupo.codigo_propio});
        ctx = {"form":form,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx, context_instance=RequestContext(request))
    if request.method == "POST":
        pk = request.POST['cod']
        grupo = GrupoItem.objects.filter(pk=pk).first()
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo.nombre = form.cleaned_data['nombre']
            grupo.codigo_propio = form.cleaned_data['codigo_propio']
            grupo.save()
            mensaje = "Correcto"
            form = GrupoForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx,context_instance=RequestContext(request))

def editar_bodega_view(request):
    if request.method == "GET":
        pk = request.GET['pk']
        bodega = Bodega.objects.filter(pk=pk).first()
        form = BodegaForm({"nombre":bodega.nombre,"direccion":bodega.direccion,"codigo_propio":bodega.codigo_propio});
        ctx = {"form":form,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx, context_instance=RequestContext(request))
    if request.method == "POST":
        pk = request.POST['cod']
        bodega = Bodega.objects.filter(pk=pk).first()
        form = BodegaForm(request.POST)
        if form.is_valid():
            bodega.nombre = form.cleaned_data['nombre']
            bodega.codigo_propio = form.cleaned_data['codigo_propio']
            bodega.descripcion = form.cleaned_data['direccion']
            bodega.save()
            mensaje = "Correcto"
            form = BodegaForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx,context_instance=RequestContext(request))

def editar_marca_view(request):
    if request.method == "GET":
        pk = request.GET['pk']
        marca = Marca.objects.filter(pk=pk).first()
        form = MarcaForm({"nombre":marca.nombre,"codigo_propio":marca.codigo_propio});
        ctx = {"form":form,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx, context_instance=RequestContext(request))
    if request.method == "POST":
        pk = request.POST['cod']
        marca = Marca.objects.filter(pk=pk).first()
        form = MarcaForm(request.POST)
        if form.is_valid():
            marca.nombre = form.cleaned_data['nombre']
            marca.codigo_propio = form.cleaned_data['codigo_propio']
            marca.save()
            mensaje = "Correcto"
            form = MarcaForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx,context_instance=RequestContext(request))
   
  
def editar_item_view(request):
    if request.method == "GET":
        pk = request.GET['pk']
        item = Item.objects.filter(pk=pk).first()
        if item.es_bien:
            bos = "Bien"
        else:
            bos= "Servicio"
        
        form = ItemForm({"codigo_barras":item.codigo_barras,"codigo_propio":item.codigo_propio,
                         "descripcion":item.descripcion,"Bien_o_Servicio":bos,
                         "iva":item.iva,"ubicacion":item.ubicacion,
                         "marca":item.id_marca.pk,"grupo":item.id_grupo.pk,"unidad":item.id_unidad.pk});
        ctx = {"form":form,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx, context_instance=RequestContext(request))
    if request.method == "POST":
        pk = request.POST['cod']
        item = Item.objects.filter(pk=pk).first()
        form = ItemForm(request.POST)
        if form.is_valid():
            item.codigo_barras = form.cleaned_data['codigo_barras']
            item.codigo_propio = form.cleaned_data['codigo_propio']
            item.descripcion = form.cleaned_data['descripcion']
            if form.cleaned_data['Bien_o_Servicio'] =="Bien":
                item.es_bien = True
                item.es_servicio = False
            else:
                item.es_bien = False
                item.es_servicio=True
            item.ubicacion = form.cleaned_data['ubicacion']
            item.iva = form.cleaned_data['iva']
            item.id_marca = form.cleaned_data['marca']
            item.id_grupo = form.cleaned_data['grupo']
            item.id_unidad = form.cleaned_data['unidad']
            item.save()
            mensaje = "Correcto"
            form = ItemForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx,context_instance=RequestContext(request))
   
    
  
def editar_proveedor_view(request):
    if request.method == "GET":
        pk = request.GET['pk']
        proveedor = Proveedor.objects.filter(pk=pk).first()
        form = ProveedoresForm({"nombre_comercial":proveedor.nombre_comercial,"codigo_propio":proveedor.codigo_propio,
                         "razon_social":proveedor.razon_social,
                         "ruc":proveedor.ruc,"direccion":proveedor.direccion,
                         "provincia":proveedor.canton.provincia.pk,"canton":proveedor.canton.pk,
                         "email":proveedor.mail,"telefono":proveedor.telefono,"fax":proveedor.fax});
        ctx = {"form":form,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx, context_instance=RequestContext(request))
    if request.method == "POST":
        pk = request.POST['cod']
        proveedor = Proveedor.objects.filter(pk=pk).first()
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            proveedor.nombre_comercial = form.cleaned_data['nombre_comercial']
            proveedor.codigo_propio = form.cleaned_data['codigo_propio']
            proveedor.razon_social = form.cleaned_data['razon_social']
            proveedor.ruc = form.cleaned_data['ruc']
            proveedor.direccion = form.cleaned_data['direccion']
            proveedor.canton = form.cleaned_data['canton']
            proveedor.mail = form.cleaned_data['email']
            proveedor.telefono = form.cleaned_data['telefono']
            proveedor.fax = form.cleaned_data['fax']
            proveedor.save()
            mensaje = "Correcto"
            form = ProveedoresForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx,context_instance=RequestContext(request))
   
  
def editar_cliente_view(request):
    if request.method == "GET":
        pk = request.GET['pk']
        cliente = Cliente.objects.filter(pk=pk).first()
        form = ClientesForm({"nombre_comercial":cliente.nombre_comercial,"codigo_propio":cliente.codigo_propio,
                         "razon_social":cliente.razon_social,
                         "ruc":cliente.ruc,"direccion":cliente.direccion,
                         "provincia":cliente.canton.provincia.pk,"canton":cliente.canton.pk,
                         "email":cliente.mail,"telefono":cliente.telefono,"fax":cliente.fax});
        ctx = {"form":form,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx, context_instance=RequestContext(request))
    if request.method == "POST":
        pk = request.POST['cod']
        cliente = Cliente.objects.filter(pk=pk).first()
        form = ClientesForm(request.POST)
        if form.is_valid():
            cliente.nombre_comercial = form.cleaned_data['nombre_comercial']
            cliente.codigo_propio = form.cleaned_data['codigo_propio']
            cliente.razon_social = form.cleaned_data['razon_social']
            cliente.ruc = form.cleaned_data['ruc']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.canton = form.cleaned_data['canton']
            cliente.mail = form.cleaned_data['email']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.fax = form.cleaned_data['fax']
            cliente.save()
            mensaje = "Correcto"
            form = ClientesForm()
        else:
            mensaje = "Llene correctamente los campos."
        ctx = {"form":form,"mensaje":mensaje,"pk":pk}
        return render_to_response("facturacion/editar.html",ctx,context_instance=RequestContext(request))
 