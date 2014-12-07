from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  # Examples:
  # url(r'^blog/', include('blog.urls')),

  url(r'^backend/admin/', include(admin.site.urls)),
  url(r'^backend/api/places.json$','place.views.places_json',name='places'),
  url(r'^backend/api/(\d+).json$','place.views.place_detail_json',name='places'),
)

import os
from django.conf import settings

if settings.DEBUG:
  ng_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'ng-app')
  urlpatterns += patterns('',
    url('^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'.*', 'localvore.views.index_serve', {'document_root': ng_path}),
  )
  
  
