from django.db import models

class Image(models.Model):
  name = models.CharField(null=True,blank=True,max_length=500)
  src = models.ImageField(upload_to='uploads/photos/%Y-%m', null=True,max_length=200)
  upload_dt = models.DateTimeField(auto_now_add=True)
  rejected = models.BooleanField(default=False)

  #instagramphoto = models.ForeignKey(InstagramPhoto,null=True,blank=True)
  def save(self,*args,**kwargs):
    self.filename = self.filename or str(self.file).split('/')[-1]
    self.name = self.name or self.filename
    super(FileModel,self).save(*args,**kwargs)
  class Meta:
    ordering = ('name',)
