from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from ideacalculator.models import Place
from ideacalculator.views import homepage, getideas

urlpatterns = patterns('',
    (r'^home/$', homepage),
    (r'^getidea/$', getideas),
)