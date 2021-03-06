from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ddjjsite.views.home', name='home'),
                       # url(r'^ddjjsite/', include('ddjjsite.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ddjj/', include('ddjjapp.urls')),
                       )


if settings.DEBUG:
    urlpatterns += patterns('',
                           (r'^', include('ddjjapp.urls')),
                            ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
