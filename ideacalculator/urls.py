from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from ideacalculator.views import getideas

urlpatterns = patterns('',
    (r'^getidea/$', getideas),
)
