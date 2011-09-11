# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('api.views',
    # Profile
    (r'^profile/add/$', 'create_profile'),
    (r'^profile/tag/$', 'tag_profile'),
    (r'^profile/(?P<profile_id>[^/]+)?$', 'get_profile'),
    (r'^profiles/(?P<tag>[^/]+)?$', 'get_profiles_by_tag'),

    # Tag
    (r'^tag/add/$', 'create_tag'),
    (r'^tag/(?P<name>[^/]+)?$', 'get_tag'),

    # Rating
    (r'^rating/profile/$', 'rate_profile'),
    (r'^rating/tag/$', 'rate_tag'),

)
