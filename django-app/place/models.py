from django.contrib.gis.db import models
from media.models import Image

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
  objects = models.GeoManager()
  @property
  def as_json(self):
    _d = {k: getattr(self,k) for k in ['name','id','address','zipcode','url','description','source_url']}
    _d['geopoint'] = self.geopoint.tuple
    _d['city'] = str(self.city)
    _d['placetypes'] = [pt.as_json for pt in self.placetypes.all()]
    _d['images'] = [i.url for i in self.images.all()]
    return _d
