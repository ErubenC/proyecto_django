from django.conf.urls import patterns, url
from facturacion import views
from django.views.generic import ListView
from facturacion.models import Proveedor, Marca, Unidad, GrupoItem, Bodega, Item
from facturacion.views import Pag_ListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^facturacion/$',  views.facturacion_view, name='vista_facturacion'),
    url(r'^marca/$',  views.marca_view, name='vista_marca'),
    url(r'^bodega/$',  views.bodega_view, name='vista_bodega'),
    url(r'^grupo/$',  views.grupo_view, name='vista_grupo'),
    url(r'^unidad/$',  views.unidad_view, name='vista_unidad'),
    url(r'^item/$',  views.item_view, name='vista_item'),
    url(r'^proveedores/$',  views.proveedores_view, name='vista_proveedores'),
    url(r'^clientes/$',  views.clientes_view, name='vista_clientes'),
    url(r'^carga_cantones/$',  views.carga_cantones_view, name='vista_carga_cantones'),
    (r'^lista_proveedores/$', ListView.as_view(model=Proveedor,)),
    #(r'^lista_marcas/$', ListView.as_view(model=Marca,)),
    (r'^lista_marcas/$', Pag_ListView.as_view(model=Marca,)),
    (r'^lista_grupos/$', Pag_ListView.as_view(model=GrupoItem,)),
    (r'^lista_unidades/$', Pag_ListView.as_view(model=Unidad,)),
    (r'^lista_bodegas/$', Pag_ListView.as_view(model=Bodega,)),
    (r'^lista_items/$', Pag_ListView.as_view(model=Item,)),
    url(r'^editar_unidad/$',  views.editar_unidad_view, name='vista_editar_unidad'),
    url(r'^editar_grupo/$',  views.editar_grupo_view, name='vista_editar_grupo'),
    url(r'^editar_marca/$',  views.editar_marca_view, name='vista_editar_marca'),
    url(r'^editar_bodega/$',  views.editar_bodega_view, name='vista_editar_bodega'),
    url(r'^editar_item/$',  views.editar_item_view, name='vista_editar_item'),
    
)
