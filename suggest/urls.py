from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
   (r'^home/', 'autosuggest.example.views.home'),
)
