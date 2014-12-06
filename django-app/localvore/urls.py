from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'localvore.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
)

import os
from django.conf import settings

if settings.DEBUG:
  from django.views.static import serve
  
  ng_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'ng-app')
  urlpatterns += [url(r'^(?P<path>.*)$', serve, kwargs={'document_root': ng_path})]
  