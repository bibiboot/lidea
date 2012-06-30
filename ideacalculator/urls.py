from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from ideacalculator.views import getideas

urlpatterns = patterns('',
    (r'^getidea/$', getideas),
)
