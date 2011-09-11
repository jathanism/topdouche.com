from django.db import models
from django.template.defaultfilters import slugify as default_slugify
from django.utils import simplejson as json

import datetime
from decimal import Decimal
import random

# Create your models here.

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
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, blank=True)
    description = models.CharField(max_length=140, blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3, null=True,
                                 blank=True, default=Decimal('0'))
    comments = models.CharField(max_length=140, blank=True)

    @property
    def random_profile(self):
        #profile = random.choice(self.tagged_items.all())
        #return profile.url
        if not hasattr(self, '_url_list'):
            self._populate_url_list()

        if not self._url_list:
            self._populate_url_list()

        random.shuffle(self._url_list)
        url = self._url_list.pop()

        return url

    def _populate_url_list(self):
        self._url_list = [p.url for p in self.tagged_items.all()]

    def __unicode__(self):
        return u'%s' % self.name

    def __repr__(self):
        return u'<Tag: %s>' % self.name

    def natural_key(self):
        return self.name

    def slugify(self, tag, i=None):
        slug = default_slugify(tag)
        if i is not None:
            slug += "_%d" % i
        return slug

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = self.slugify(self.name)

        if not self.rating >= 0 and self.rating <= 10:
            raise ValueError('Rating must be 1-10')

        super(Tag, self).save()

class Profile(models.Model):
    url = models.URLField(verify_exists=True, unique=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3, null=True,
                                 default=Decimal('0'))
    #tags = TaggableManager(through=TaggedProfile, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tagged_items')

    @property
    def douchescore(self):
        #avg_info = self.tags.all().aggregate(models.Avg('rating'))
        #avg_score = avg_info['rating__avg']
        #return avg_score + self.rating
        sum_info = self.tags.all().aggregate(models.Sum('rating'))
        return sum_info['rating__sum'] or Decimal('0')

    @property
    def username(self):
        return u'%s' % self.url.split('/')[-1]

    def __unicode__(self):
        return u'%s' % self.url

    def __repr__(self):
        return u'<Profile: %s>' % self.url

    def save(self, *args, **kwargs):
        if not self.rating >= 0 and self.rating <= 10:
            raise ValueError('Rating must be 1-10')
        
        super(Profile, self).save()
