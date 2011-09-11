# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods, require_POST
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.core.serializers import serialize
#from django.db.models.query import QuerySet

from models import Profile, Tag
from utils import JsonResponse
import forms

log = settings.LOGGER

def handle_bad_request(err=None):
    """Returns a 400 with the message of your choice!"""
    if err is None:
        msg = 'bad request'
    else:
        msg = str(err)

    log.critical( 'Got bad request with error: ' + msg )

    return JsonResponse({'exception': msg}, 400)


@require_POST
def create_profile(request):
    form = forms.ProfileForm(request.POST)

    if form.is_valid():
        log.debug('Profile form is valid.')
        new_profile = form.save()
        cd = form.cleand_data

    else:
        log.debug('Profile form is NOT valid.')
        return handle_bad_request(dict(form.errors))

    return HttpResponse(serialize('json', new_profile))

def get_profile(request, url=None):
    if url is None:
        url = request.REQUEST.get('url', '')
    profile = get_object_or_404(Profile.objects.get(url=url))

    #return HttpResponse(serialize('json', profile))
    return HttpResponse('Got profile: ' + profile.url)
