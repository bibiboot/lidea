import settings
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

PROJECT_PATH = settings.PROJECT_PATH
STATIC_PATH = settings.PROJECT_PATH + "/"

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #(r'^home/', include('autosuggest.example.urls')),
   (r'^home/', 'lidea.suggest.views.home'), 
   (r'^search/', 'lidea.suggest.views.autosuggest'),
   (r'^loveideaz/', include('ideac.urls')),

   (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH +'html/css/'}),
   (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH + 'html/js/'}),
   (r'^html/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH + 'html/templates/'}),
   (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH + 'html/images/'}),

)
