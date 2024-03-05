from django.db import models

# Create your models here.
class Gallery(models.Model):

  category = models.CharField(max_length=100)
  image = models.ImageField(upload_to='image', null=True)

  def __str__(self):
    return f'{self.category}'
  
class Pictures(models.Model):
  category = models.ForeignKey(Gallery, on_delete = models.CASCADE)
  image = models.ImageField(upload_to='images')

  def __str__(self):
    return f'{self.image}'
  
class Music(models.Model):
  category = models.ForeignKey(Gallery, on_delete = models.CASCADE)
  music_title = models.CharField(max_length = 100)
  image= models.ImageField(upload_to='music_picture')
  audio_file = models.FileField(blank=True,null=True, upload_to='music')
  audio_link = models.CharField(max_length=200,blank=True,null=True)
  duration=models.CharField(max_length=20)

  def __str__(self):
    return f'{self.music_title}'
  
class Video(models.Model):
  category = models.ForeignKey(Gallery, on_delete = models.CASCADE)
  video_title = models.CharField(max_length = 100)
  video_file = models.FileField(upload_to='video')


  def __str__(self):
    return f'{self.video_title}'




