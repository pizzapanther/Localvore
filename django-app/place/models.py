from django.contrib.gis.db import models
from django.conf import settings
from media.models import Image

import yelp

class PlaceType(models.Model):
  name = models.CharField(max_length=64)
  slug = models.CharField(max_length=64)
  __unicode__ = lambda self: self.name
  @property
  def as_json(self):
    return {k: getattr(self,k) for k in ['name','slug','id'] }

class Source(models.Model):
  name = models.CharField(max_length=64)
  __unicode__ = lambda self: self.name

class GeoModel(models.Model):
  name = models.CharField(max_length=128)
  geopoint = models.PointField()
  __unicode__ = lambda self: self.name

class City(GeoModel):
  objects = models.GeoManager()

class Place(GeoModel):
  address = models.CharField(max_length=128)
  city = models.ForeignKey(City)
  zipcode = models.CharField(max_length=16)
  url = models.URLField(null=True,blank=True)
  description = models.TextField(null=True,blank=True)
  placetypes = models.ManyToManyField(PlaceType)
  images = models.ManyToManyField(Image)
  image = models.ForeignKey(Image,related_name="+",null=True,blank=True)
  source = models.ManyToManyField(Source)
  source_url = models.URLField(null=True,blank=True)
  yelp_url = models.URLField(null=True,blank=True)

  objects = models.GeoManager()
  def get_yelp(self):
    if not self.yelp_url:
      return None
    yelp_api = yelp.Api(
      consumer_key=settings.YELP_KEY,
      consumer_secret=settings.YELP_SECRET,
      access_token_key=settings.YELP_TOKEN,
      access_token_secret=settings.YELP_TOKEN_SECRET)
    business = yelp_api.GetBusiness(self.yelp_url.split('/')[-1])
    if not business.reviews:
      return
    out = []
    for review in business.reviews:
      _d = {k:getattr(review,k) for k in ['rating', 'rating_image_small_url', 'time_created', 'excerpt']}
      _d['user'] = {k:getattr(review.user,k) for k in ['id', 'image_url', 'name']}
      out.append(_d)
    return out
  @property
  def as_json(self):
    _d = {k: getattr(self,k) for k in ['name','id','address','zipcode','url','description','source_url']}
    _d['geopoint'] = self.geopoint.tuple
    _d['city'] = str(self.city)
    _d['placetypes'] = [pt.as_json for pt in self.placetypes.all()]
    _d['images'] = [i.as_json for i in self.images.all()]
    if self.image:
      _d['image'] = self.image.as_json
    return _d
  @property
  def full_json(self):
    _d = self.as_json
    _d['yelp'] = self.get_yelp()
    return _d
