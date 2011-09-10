# -*- coding: utf-8 -*-

"""
Various project-wide utilities that don't have a place anywhere else and that
will probably be used by multiple apps.
"""

import json
import urllib

from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

log = settings.LOGGER

# Exports
__all__ = ('render_to', 'do_redirect', 'JsonResponse')

def do_redirect(view_name, **kwargs):
    """
    Construct a redirect URL with query params and then return it.

    @param view_name: The full namespace path to the view function. This will be
        reversed to the url.
    @param kwargs: Any keyword arguments you would like to pass to the view's
        template.
    """
    redir_path = reverse(view_name)
    redir_params = urllib.urlencode(kwargs)
    redir_url = '{0}?{1}'.format(redir_path, redir_params)

    return redirect(redir_url)


# Decorators
def render_to(template_name):
    """
    A decorator intended to be applied to view functions to monkey patch 
    Django's render_to_response(). Allows you to create views without 
    including the RequestContext boiler-plate.

    So this:
        def my_view(request):
            # View code here...
            return render_to_response('my_template.html', my_data_dictionary, 
                                      context_instance=RequestContext(request))
    Becomes this:

        @render_to('my_template.html')
        def my_view(request):
            # View code here...
            return some_dict

    Awesome, right?!
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if not isinstance(output, dict):
                return output
            return render_to_response(template_name, output,
                                      context_instance=RequestContext(request))
        return wrapper
    return renderer


# Classes
class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with 'application/json' mimetype.
    """
    def __init__(self, data, status=200):
        super(JsonResponse, self).__init__(content=json.dumps(data), mimetype='application/json', status=status)
