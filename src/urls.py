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

        # url(settings.STATIC_URL + r'bootstrap/(?P<path>.*)$', 'django.views.static.serve',
        #     {'document_root': settings.STATIC_ROOT.joinpath('bootstrap'), 'show_indexes': True}),
        
        # static(settings.STATIC_URL + 'less', document_root=settings.STATIC_ROOT.joinpath('less')),
        # # url(r'^static/less/(?P<path>.*)$', 'django.views.static.serve',
        # #     {'document_root': settings.STATIC_ROOT.joinpath('less'), 'show_indexes': True}),
        
        # url(settings.STATIC_URL + r'js/(?P<path>.*)$', 'django.views.static.serve',
        #     {'document_root': settings.STATIC_ROOT.joinpath('js'), 'show_indexes': True}),
        
        # url(settings.STATIC_URL + r'css/(?P<path>.*)$', 'django.views.static.serve',
        #     {'document_root': settings.STATIC_ROOT.joinpath('css'), 'show_indexes': True}),
        
        url(r'', include('django.contrib.staticfiles.urls')),

    ) + urlpatterns
    # import pdb; pdb.set_trace()