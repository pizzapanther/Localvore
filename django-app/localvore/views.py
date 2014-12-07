from django.http import HttpResponse
from django.views.static import serve

from place.models import Place

from simplejson import dumps

def index_serve (request, document_root=None):
  if request.path.startswith(('/favicon.ico', '/components/', '/css/', '/img/', '/js/', '/tpl/')):
    return serve(request, request.path[1:], document_root=document_root)
    
  return serve(request, 'index.html', document_root=document_root)
  
def places_json (request):
  places = Place.objects.all()
  if 'placetype' in request.GET:
    places = places.filter(placetypes__slug=placetype)
  return HttpResponse(dumps([p.as_json for p in places]))
