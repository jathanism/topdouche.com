from django.db import models
from django.utils import simplejson as json

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, GenericTaggedItemBase, TagBase

import datetime

# Create your models here.

RATING_CHOICES = (
    ('tag', 'Tag'),
    ('profile', 'Profile'),
    ('url', 'URL'),
)

"""
class Rating(models.Model):
    score = models.DecimalField(decimal_places=2, max_digits=4)

    def __unicode__(self):
        return u'%s' % self.score

    def __repr__(self):
        return u'<Rating: %s>' % self.score

    class Meta:
        ordering = ('score',)
"""

class Tag(TagBase):
    description = models.CharField(max_length=140, blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=4, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class TaggedProfile(GenericTaggedItemBase):
    tag = models.ForeignKey(Tag, related_name='tagged_items')

"""
class TaggedProfile(TaggedItemBase):
    content_object = models.ForeignKey('Profile')
    score = models.DecimalField(decimal_places=2, max_digits=4)
"""

class Profile(models.Model):
    url = models.URLField(verify_exists=True)
    rating = models.DecimalField(decimal_places=2, max_digits=4, blank=True)
    #rating = models.ForeignKey(Rating)
    #tags = TaggableManager()
    tags = TaggableManager(through=TaggedProfile)

    def __unicode__(self):
        return u'%s' % self.url

    def __repr__(self):
        return u'<Profile: %s>' % self.url
