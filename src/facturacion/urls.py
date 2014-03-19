from django.conf.urls import patterns, url
from facturacion import views

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
    
)
