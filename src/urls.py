from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('cms.urls'))
)

if settings.DEBUG:
    urlpatterns = patterns(
        '',

        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

        url(r'', include('django.contrib.staticfiles.urls')),

    ) + urlpatterns
