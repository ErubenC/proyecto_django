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
    url(r'^cofig_documentos/$',  views.transaccion_view, name='vista_config_documentos'),
    
)
