from django.conf.urls import patterns, include, url
from home import views
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('facturacion.urls')),
    url(r'^$',views.index_view, name='vista_index'),
    url(r'^index/$',  views.index_view, name='vista_index'),
    url(r'^registro/$',  views.register_view, name='vista_registro'),
    url(r'^login/$',  views.login_view, name='vista_login'),
    url(r'^logout/$', views.logout_view,name='vista_logout'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
