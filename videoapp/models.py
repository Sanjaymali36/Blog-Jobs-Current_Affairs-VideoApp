from django.db import models

# Create your models here.
# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    #description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='topics1')
    Publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='topics1')

    def __str__(self):
        return self.subject


class Video_Content(models.Model):
    Video_Content= models.TextField(max_length=4000)
    title = models.CharField(max_length=200,blank=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name='posts1')
    #created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts1',null=True,default="BodhiAI")
    #updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='+')
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.Video_Content



class Entry(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=4000, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    start_publication = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=255,null=True,default="bodhiai1")
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    link1 = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

class Video(models.Model):
    #slug = models.SlugField(max_length=255, null=True, blank=True)
    content= models.TextField(max_length=4000)
    video_category= models.CharField(max_length=200,blank=True)
    video_topic = models.CharField(max_length=200,blank=True)
    video_title = models.CharField(max_length=200,blank=True)
    upload_date = models.DateTimeField(null=True,blank=True)
    #publisher = models.ForeignKey(User,on_delete=models.CASCADE, related_name='video',null=True,default="BodhiAI")
    publisher=models.CharField(max_length=200,default="BodhiAI",null=True,blank=True)
    #updat:xed_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='+')
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.video_title

