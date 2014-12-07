import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'localvore.settings'

from django.conf import settings
import django

django.setup()

from media.models import Image
from place.models import Place, City, Source
import json, requests, time
from geopy.geocoders import GoogleV3

f = open('localvore/settings/private/export-376.json','r')
places = json.loads(f.read())
f.close()

_dir = settings.MEDIA_ROOT

for dirname in ['','uploads','photos','culturemap']:
  _dir = os.path.join(_dir,dirname)
  if not os.path.exists(_dir):
    os.mkdir(_dir)
    print "made directory: %s"%_dir

def pull_image(url):
  fname = url.split('/')[-1]
  rel_path = os.path.join('uploads/photos/culturemap',fname)
  fpath = os.path.join(settings.MEDIA_ROOT,rel_path)
  if not os.path.exists(fpath):
    data = requests.get(url,stream=True).raw.read()
    with open(fpath,'wb') as f:
      f.write(data)
    print "new image: %s"%rel_path
  return rel_path

if __name__ == "__main__":
  Place.objects.all().delete()
  geolocator = GoogleV3()
  def reverse_geocode(value):
    google_address = geolocator.geocode(value)
    if not google_address:
      msg = 'Unable to find anything at that address, please try again.'
      raise ValueError('Google could not find the address: %s'%value)
    address, (latitude, longitude) = google_address
    return {
      'address': address,
      'lat': latitude,
      'lon': longitude
    }

  _cities = ('West University Place','Houston','Sugar Land','Pearland','The Woodlands','Humble')
  cities = {}
  for name in _cities:
    try:
      cities[name] = City.objects.get(name=name)
    except City.DoesNotExist:
      _g = reverse_geocode(name+', TX')
      cities[name] = City(name=name,geopoint='POINT(%s %s)'%(_g['lon'],_g['lat']))
      cities[name].save()
      print "New city: %s"%name
  
  found = 0
  created = 0
  for json in places:
    try:
      place = Place.objects.get(geopoint='POINT(%s %s)'%tuple(json['geopoint'][::-1]))
      found += 1
    except Place.DoesNotExist:
      time.sleep(0.1)
      _g = reverse_geocode('%s,%s'%tuple(json['geopoint']))
      city = None
      for key,value in cities.items():
        if key in _g['address']:
          city = value
          break
      address = _g['address'].split(city.name)
      image = None
      if 'image' in json:
        image,new = Image.objects.get_or_create(src=pull_image(json['image']))
      place = Place(
        name = json['title'],
        address = _g['address'].split(', '+city.name)[0],
        geopoint = 'POINT(%s %s)'%tuple(json['geopoint'][::-1]),
        image = image,
        city=city,
        zipcode = _g['address'].split('TX ')[-1].split(',')[0],
        description = json['desc'],
        source_url = json['link']
      )
      place.save()
      place.source.add(Source.objects.get_or_create(name="CultureMap")[0])
      place.save()
      created += 1
      print "Place Created: %s"%place
  print "%s created and %s found"%(created,found)
      
    #place = Place.objects.get_or_create
  
