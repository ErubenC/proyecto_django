from django.conf.urls import patterns, include, url
from home import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('facturacion.urls')),
    url(r'^$',index_view, name='vista_index'),
    url(r'^index/$',  index_view, name='vista_index'),
    url(r'^login/$',  login_view, name='vista_login'),
    url(r'^logout/$', views.logout_view,name='vista_logout'),
)
