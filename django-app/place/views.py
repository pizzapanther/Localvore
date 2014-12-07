from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from place.models import Place, PlaceType

from json import dumps
from geopy.geocoders import GoogleV3
import random

def places_json (request):
  places = Place.objects.all()
  
  placetype = request.GET.get('placetype', '')
  if placetype:
    places = places.filter(placetype__slug=placetype)
    
  lat = request.GET.get('lat',29.7604267) #y
  lon = request.GET.get('lon',-95.3698028) #x
  geopoint = fromstr('POINT(%s %s)'%(lon,lat))
  #miles = request.GET.get('miles', 10)
  #places = places.filter(geopoint__distance_lte=(geopoint,D(mi=miles))).distance(geopoint).order_by('distance')
  places = places.distance(geopoint).order_by('distance')[:200]
  geolocator = GoogleV3()
  return HttpResponse(dumps([p.as_json for p in places]))

def place_detail_json (request,pk):
  place = get_object_or_404(Place,pk=pk)
  json = place.full_json
  lat = request.GET.get('lat',29.7604267) #y
  lon = request.GET.get('lon',-95.3698028) #x
  geopoint = fromstr('POINT(%s %s)'%(lon,lat))
  json['distance'] = place.geopoint.distance(geopoint)*0.00062137119223733
  return HttpResponse(dumps(place.full_json))

def featured_places (request):
  out = {}
  for placetype in PlaceType.objects.all():
    jsons = [p.as_json for p in Place.objects.filter(placetype=placetype).order_by('-yelp_rating')[:10]]
    random.shuffle(jsons)
    out[placetype.name] = jsons
  return HttpResponse(dumps(out))
