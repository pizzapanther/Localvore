from django.contrib import admin

from .models import PlaceType, Source, City, Place

class PlaceAdmin(admin.ModelAdmin):
  list_display = ('__unicode__','placetype','description')
  list_editable = ('placetype',)

admin.site.register(PlaceType)
admin.site.register(Source)
admin.site.register(City)
admin.site.register(Place,PlaceAdmin)
