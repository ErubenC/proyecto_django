from django.conf.urls import patterns, include, url
from home.views import index_view, login_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',  index_view, name='vista_index'),
    url(r'^login/$',  login_view, name='vista_login'),
)
