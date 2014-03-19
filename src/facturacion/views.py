from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from facturacion.forms import MarcaForm,BodegaForm,UnidadForm,GrupoForm,\
    ItemForm
from facturacion.models import Marca, GrupoItem, Bodega, Unidad, Item
from django.contrib.auth.decorators import login_required, user_passes_test
from pcardext import cp


def not_in_facturacion_group(user):
    if user:
        x = user.groups.filter(name='facturacion').count() == 1
        print x
        return x
    return False

@login_required
@user_passes_test(not_in_facturacion_group, login_url='/login')
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
    marca = Marca.objects.all()
    marcas = ""
    for m in marca:
        marcas = marcas+''+m.__getattribute__('nombre')+" ("+m.__getattribute__('codigo_propio')+'),'
      
    unidad = Unidad.objects.all()
    unidades = ""
    for u in unidad:
        unidades = unidades+''+u.__getattribute__('nombre')+" ("+u.__getattribute__('codigo_propio')+'),'
    
    grupo = GrupoItem.objects.all()
    grupos = ""
    for g in grupo:
        grupos = grupos+''+g.__getattribute__('nombre')+" ("+g.__getattribute__('codigo_propio')+'),'
   
    bodega = Bodega.objects.all()
    bodegas = ""
    for bo in bodega:
        bodegas = bodegas+''+bo.__getattribute__('nombre')+" ("+bo.__getattribute__('codigo_propio')+'),'
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
        
        ctx = {"form":form,"mensaje":mensaje,"marcas":marcas,"unidades":unidades,"grupos":grupos,"bodegas":bodegas}
        return render_to_response("facturacion/item.html",ctx,context_instance=RequestContext(request))
    else:
        form = ItemForm()
        ctx = {"form":form,"marcas":marcas,"unidades":unidades,"grupos":grupos,"bodegas":bodegas}
        return render_to_response("facturacion/item.html",ctx,context_instance=RequestContext(request))
   
