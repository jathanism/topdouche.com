# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import Profile, Tag

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)
class TagAdmin(admin.ModelAdmin):
        pass
admin.site.register(Tag, TagAdmin)
