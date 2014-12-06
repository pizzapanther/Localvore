from django.contrib import admin

from .models import PlaceType, Source, City, Place

admin.site.register(PlaceType)
admin.site.register(Source)
admin.site.register(City)
admin.site.register(Place)
