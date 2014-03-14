
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'healthprovider.views.home'),
    url(r'^login/$', 'healthprovider.views.do_login'),
    url(r'^logout/$', 'healthprovider.views.do_logout'),

)
