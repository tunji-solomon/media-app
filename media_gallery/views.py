from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse



def index(request):
  data = Gallery.objects.all()
  context = {
    'datas' : data
  }
  return render (request,'media_gallery/index.html',context)

def music(request):
  data = Music.objects.all()
  context = {
    'datas': data
  }
  return render(request,'media_gallery/music.html',context )

def movies(request):
  data = Video.objects.all()
  context = {
    'datas' : data
  }
  return render(request, 'media_gallery/video.html', context)
   
def pictures(request):
  data = Pictures.objects.all()

  context = {
    'datas': data
  }
  return render(request,'media_gallery/pictures.html',context )


