# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import Profile, Tag

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('url', 'rating',)
    search_fields = ('url',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'rating',)
    search_fields = ('name', 'rating',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag, TagAdmin)
