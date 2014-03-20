from django.conf.urls import patterns, url
from facturacion import views
from django.views.generic import ListView
from facturacion.models import Proveedor, Marca, Unidad, GrupoItem, Bodega
from facturacion.views import IndexView

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
    (r'^lista_marcas(?P<pagina>.*)/$', IndexView.as_view()),
    (r'^lista_grupos/$', ListView.as_view(model=GrupoItem,)),
    (r'^lista_unidades/$', ListView.as_view(model=Unidad,)),
    (r'^lista_bodegas/$', ListView.as_view(model=Bodega,)),
    
)
