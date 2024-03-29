from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/florian/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT}),
    url(r'^csm/export/plot/', 'csm.views.plot'),
    url(r'^csm/export/', 'csm.views.export'),
    url(r'^csm/internal/.*', 'csm.views.internal'),
    url(r'^csm/stuff/.*', 'csm.views.stuff'),
    url(r'^csm/', 'csm.views.index'),

)
