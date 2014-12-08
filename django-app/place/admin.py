from django import forms
from django.contrib import admin
from django.contrib.gis.db import models

from .models import PlaceType, Source, City, Place

class PlaceAdmin(admin.ModelAdmin):
  list_display = ('name','placetype','desc')
  list_editable = ('placetype',)
  list_filter = ('placetype',)
  search_fields = ('name',)
  save_as = True
  
  raw_id_fields = ('image', 'images')
  
  formfield_overrides = {
    models.PointField: {'widget': forms.TextInput(attrs={'style': 'width: 400px;'})},
  }
  
class CityAdmin (admin.ModelAdmin):
  formfield_overrides = {
    models.PointField: {'widget': forms.TextInput(attrs={'style': 'width: 400px;'})},
  }
  
admin.site.register(PlaceType)
admin.site.register(Source)
admin.site.register(City, CityAdmin)
admin.site.register(Place,PlaceAdmin)
