import django
django.setup()
from django.conf import settings

from place.models import Place
from unicode_sucks import latin1_to_ascii as _

import yelp,time

yelp_api = yelp.Api(
  consumer_key=settings.YELP_KEY,
  consumer_secret=settings.YELP_SECRET,
  access_token_key=settings.YELP_TOKEN,
  access_token_secret=settings.YELP_TOKEN_SECRET)

def _p(s):
  try:
    print _(s)
  except UnicodeError:
    pass

Place.objects.all().update(yelp_url=None)

cutoff = 0.01
print "cutoff is %s"%cutoff
print "%s remain"%Place.objects.filter(yelp_url=None).count()
for place in Place.objects.filter(yelp_url=None):
  search_results = yelp_api.Search(term=_(place.name),location=_("%s, Houston, TX"%place.address))
  for business in search_results.businesses:
    ll = business.location.coordinate
    error = ((ll['latitude'] - place.geopoint.y)**2 + (ll['longitude'] - place.geopoint.x)**2)**0.5
    if error > cutoff:
      #_p("%s failed with error of %s"%(place,error))
      #_p("found: %s"%business.name)
      pass
    else:
      place.yelp_url = business.url
      place.save()
      _p("Success: %s as %s"%(_(place.name),_(business.name)))
      break
