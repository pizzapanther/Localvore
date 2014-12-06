from django.contrib.gis.db import models
from media.models import Image

class PlaceType(models.Model):
  name = models.CharField(max_length=64)
  __unicode__ = lambda self: self.name

class Source(models.Model):
  name = models.CharField(max_length=64)
  __unicode__ = lambda self: self.name

class GeoModel(models.Model):
  name = models.CharField(max_length=128)
  geopoint = models.PointField()
  __unicode__ = lambda self: self.name

class City(GeoModel):
  pass

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