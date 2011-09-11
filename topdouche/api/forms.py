# -*- coding: utf-8 -*-
from django.conf import settings
from django import forms
from django.forms import ValidationError as FormValidationError

from models import Profile, Tag

log = settings.LOGGER

class ProfileForm(forms.ModelForm):

    """
    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        taglist = tags.split(',')
        print 'Got tags: %s' % repr(tagslist)
        log.debug('Got tags: %s' % repr(tagslist))
        tags = [Tag.objects.get_or_create(name=t) for t in taglist]
        #try:
        #    tags = [Tag.objects.get_or_create(name=t) for t in taglist]
        #except Exception as err:
        #    raise FormValidationError('Could not parse tags: %s' % repr(tags))

        return tags
    """

    class Meta:
        model = Profile
        fields = ('url',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
