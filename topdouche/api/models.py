from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.utils import simplejson as json


import datetime

# Create your models here.

RATING_CHOICES = (
    ('tag', 'Tag'),
    ('profile', 'Profile'),
    ('url', 'URL'),
)

"""
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, GenericTaggedItemBase, TagBase
class Tag(TagBase):
    description = models.CharField(max_length=140, blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=4, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class TaggedProfile(GenericTaggedItemBase):
    tag = models.ForeignKey(Tag, related_name='tagged_items')
"""

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=140, blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=4, blank=True)
    comments = models.CharField(max_length=140, blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    def __repr__(self):
        return u'<Tag: %s>' % self.name

    def slugify(self, tag, i=None):
        slug = default_slugify(tag)
        if i is not None:
            slug += "_%d" % i
        return slug

class Profile(models.Model):
    url = models.URLField(verify_exists=True)
    rating = models.DecimalField(decimal_places=2, max_digits=4, blank=True)
    #tags = TaggableManager(through=TaggedProfile, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tagged_items')

    def __unicode__(self):
        return u'%s' % self.url

    def __repr__(self):
        return u'<Profile: %s>' % self.url
