# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import Profile #, Rating 

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

"""
class RatingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rating, RatingAdmin)
"""
