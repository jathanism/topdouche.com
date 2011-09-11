# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods, require_POST
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.utils import simplejson as json
from django.core.serializers import serialize
#from django.db.models.query import QuerySet

from decimal import Decimal
import random

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

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def object_to_dict(obj):
    """Take an object, return only the fields attribute, plus special sauce?"""
    json_data = serialize('json', [obj], use_natural_keys=True)
    data = json.loads(json_data)
    fields = data[0]['fields']
    fields['id'] = data[0]['pk']

    if hasattr(obj, 'douchescore'):
        fields['douchescore'] = float(obj.douchescore)
    if hasattr(obj, 'username'):
        fields['username'] = obj.username
    if hasattr(obj, 'random_profile'):
        fields['random_profile'] = obj.random_profile
    
    return fields

@require_POST
def create_profile(request):
    json_data = request.raw_post_data
    log.debug('Got raw post data: %s' % json_data)
    print 'Got raw post data: %s' % json_data
    try:
        data = json.loads(json_data)
    except ValueError:
        return handle_bad_request('%s is not valid JSON' % json_data)

    form = forms.ProfileForm(data)

    if form.is_valid():
        log.debug('Profile form is valid.')
        new_profile = form.save()
    else:
        log.debug('Profile form is NOT valid.')
        return handle_bad_request(dict(form.errors))

    return JsonResponse(new_profile.id)

def get_profile(request, url=None, profile_id=None):
    if url is None:
        url = request.REQUEST.get('url', '')
    if profile_id is None:
        profile_id = request.REQUEST.get('id', '')

    profile = get_or_none(Profile, url=url) or get_or_none(Profile, pk=profile_id)
    if profile is None:
        return handle_bad_request('Profile matching query does not exist.')

    data = object_to_dict(profile)

    return JsonResponse(data)

def get_profiles_by_tag(request, tag=None, count=10):
    if tag is None:
        tag = request.REQUEST.get('tag', '')

    count = request.REQUEST.get('count') or count
    try:
        count = int(count)
    except (ValueError, TypeError):
        count = 10

    print 'count is: %s' % count

    #profiles = Profile.objects.filter(tags__in=Tag.objects.filter(name=tag))
    profiles = Profile.objects.filter(tags__in=Tag.objects.filter(name=tag))[:count]
    data = [object_to_dict(p) for p in profiles]

    return JsonResponse(data)

def get_profiles_by_rating(request, count=10, tag=None):
    count = request.REQUEST.get('count') or count
    try:
        count = int(count)
    except (ValueError, TypeError):
        count = 10

    tag = tag or request.REQUEST.get('tag')
    if tag is None:
        profiles = reversed(sorted(Profile.objects.all()[:count], key=lambda p: 
                                   p.douchescore))
    else:
        profiles = Profile.objects.filter(tags__in=Tag.objects.filter(name=tag))[:count]

    data = [object_to_dict(p) for p in profiles]

    return JsonResponse(data)

def get_tags_by_rating(request, count=10):
    count = request.REQUEST.get('count') or count
    try:
        count = int(count)
    except (ValueError, TypeError):
        count = 10

    #tags = reversed(sorted(Tag.objects.all(), key=lambda t: t.rating))
    tags = reversed(sorted(Tag.objects.all()[:count], key=lambda t: t.rating))
    data = [object_to_dict(t) for t in tags]

    return JsonResponse(data)

@require_POST
def tag_profile(request, profile_id=None, url=None, tag=None):
    json_data = request.raw_post_data
    #log.debug('Got raw post data: %s' % json_data)
    try:
        data = json.loads(json_data)
    except ValueError:
        return handle_bad_request('%s is not valid JSON' % json_data)

    url = data.get('url', '')
    profile_id = data.get('profile_id', '')
    tag = data.get('tag', '')

    print 'data is: %s' % data
    profile = get_or_none(Profile, url=url) or get_or_none(Profile, pk=profile_id)
    if profile is None:
        return handle_bad_request('Profile matching query does not exist.')

    tag = get_or_none(Tag, name=tag)
    if tag is None:
        return handle_bad_request('Tag matching query does not exist.')

    profile.tags.add(tag)
    profile.save()

    return HttpResponse()

@require_POST
def create_tag(request):
    json_data = request.raw_post_data
    log.debug('Got raw post data: %s' % json_data)
    print 'Got raw post data: %s' % json_data
    try:
        data = json.loads(json_data)
    except ValueError:
        return handle_bad_request('%s is not valid JSON' % json_data)

    form = forms.TagForm(data)

    if form.is_valid():
        log.debug('Tag form is valid.')
        new_tag = form.save()
    else:
        log.debug('Tag form is NOT valid.')
        return handle_bad_request(dict(form.errors))

    return JsonResponse(new_tag.id)

def get_tag(request, name=None):
    if name is None:
        name = request.REQUEST.get('name', '')

    tag = get_or_none(Tag, name=name)
    if tag is None:
        return handle_bad_request('Tag matching query does not exist.')

    data = object_to_dict(tag)

    return JsonResponse(data)

@require_POST
def rate_profile(request):
    json_data = request.raw_post_data
    log.debug('Got raw post data: %s' % json_data)
    print 'Got raw post data: %s' % json_data
    try:
        data = json.loads(json_data)
    except ValueError:
        return handle_bad_request('%s is not valid JSON' % json_data)

    profile_id = data.get('profile_id', '')
    value = data.get('value', '')

    profile = get_or_none(Profile, url=url) or get_or_none(Profile, pk=profile_id)
    if profile is None:
        return handle_bad_request('Profile matching query does not exist.')

    old_rating = profile.rating
    profile.rating += value
    profile.save()

    data = dict(old=old_rating, new=profile.rating)

    return JsonResponse(data)

@require_POST
def rate_tag(request):
    json_data = request.raw_post_data
    log.debug('Got raw post data: %s' % json_data)
    print 'Got raw post data: %s' % json_data
    try:
        data = json.loads(json_data)
    except ValueError:
        return handle_bad_request('%s is not valid JSON' % json_data)

    name = data.get('name', '')
    value = data.get('value', '')

    tag = get_or_none(Tag, name=name)
    if tag is None:
        return handle_bad_request('Tag matching query does not exist.')

    old_rating = tag.rating
    tag.rating += Decimal(value)
    tag.save()

    data = dict(old=str(old_rating), new=str(tag.rating))

    return JsonResponse(data)
