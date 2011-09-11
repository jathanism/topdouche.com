# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import Profile, Tag

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('url', 'rating',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'rating',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag, TagAdmin)
