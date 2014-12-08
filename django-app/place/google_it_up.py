from googleplaces import GooglePlaces, types, lang
from django.conf import settings
import django; django.setup()

from place.models import Place
from unicode_sucks import latin1_to_ascii as _

def _p(s):
  try:
    print _(s)
  except UnicodeError:
    pass

google_places = GooglePlaces(settings.GOOGLE_SERVER_KEY)

for place in Place.objects.filter(google_rating__isnull=True):
  lng, lat = place.geopoint.tuple
  query_result = google_places.nearby_search(lat_lng={'lat':lat,'lng':lng}, name=place.name,rankby="distance")
  if not query_result.places:
    _p("nothing found for %s"%place.name)
    continue
  business = query_result.places[0]
  location = query_result.places[0].geo_location
  cutoff = 0.005
  error = ((location['lat'] - place.geopoint.y)**2 + (location['lng'] - place.geopoint.x)**2)**0.5
  if error > cutoff:
    _p("%s failed with error of %s"%(place,error))
    _p("%s found \n"%business.name)
  else:
    business.get_details()
    print business.rating
    place.google_rating = business.rating or None
    place.save()
    _p("Success: %s as %s"%(_(place.name),_(business.name)))
