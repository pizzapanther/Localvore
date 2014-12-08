from django.contrib import admin

from .models import Image

class ImageAdmin (admin.ModelAdmin):
  list_display = ('src', 'upload_dt')
  
admin.site.register(Image, ImageAdmin)
