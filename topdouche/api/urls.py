# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('api.views',
    # API
    #(r'^$', 'help_index'),
    (r'^profile/add/$', 'create_profile'),
    (r'^profile/(?P<url>[^/]+)?$', 'get_profile'),
)
