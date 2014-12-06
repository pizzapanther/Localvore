from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  # Examples:
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
)

import os
from django.conf import settings

if settings.DEBUG:
  ng_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'ng-app')
  urlpatterns += patterns('',
    url(r'.*', 'localvore.views.index_serve', kwargs={'document_root': ng_path})
  )
  
  