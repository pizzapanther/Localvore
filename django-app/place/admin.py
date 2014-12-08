from django.contrib import admin

from .models import PlaceType, Source, City, Place

class PlaceAdmin(admin.ModelAdmin):
  list_display = ('name','placetype','desc')
  list_editable = ('placetype',)
  list_filter = ('placetype',)
  search_fields = ('name',)
  
admin.site.register(PlaceType)
admin.site.register(Source)
admin.site.register(City)
admin.site.register(Place,PlaceAdmin)
