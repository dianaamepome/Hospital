
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'patientapp.views.home'),
    url(r'^login/$', 'patientapp.views.do_login'),
    url(r'^logout/$', 'patientapp.views.do_logout'),
   # url(r'^homepage/displayhostels/(?P<id>\d+)/((?P<hostelinfo>.*)/)?/studreg/$','hostels.views.studregister'),

)
