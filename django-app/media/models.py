from django.db import models
from sorl.thumbnail import get_thumbnail

class Image(models.Model):
  name = models.CharField(null=True,blank=True,max_length=500)
  src = models.ImageField(upload_to='uploads/photos/%Y-%m', null=True,max_length=200)
  upload_dt = models.DateTimeField(auto_now_add=True)
  rejected = models.BooleanField(default=False)
  @property
  def as_json(self):
    return {
      'name': self.name,
      'url': self.src.url,
      'url_medium': get_thumbnail(self.src,"300x300").url,
      'url_small': get_thumbnail(self.src,"128x128", crop='center').url,
    }

  #instagramphoto = models.ForeignKey(InstagramPhoto,null=True,blank=True)
  class Meta:
    ordering = ('name',)
