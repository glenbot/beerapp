from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('home.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# Local url patterns for development
try:
    from local_urls import MEDIA_PATTERNS
    urlpatterns += MEDIA_PATTERNS
except ImportError:
    from django.conf import settings
    from os.path import join
    # serve static files
    if settings.DEBUG:
        urlpatterns += patterns('',
            (r'^site_media/(?P<path>.*)$', 
            'django.views.static.serve',
            {'document_root': join(settings.PROJECT_ROOT,'site_media')}),         
        )