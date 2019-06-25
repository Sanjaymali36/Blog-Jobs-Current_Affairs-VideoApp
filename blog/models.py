# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.text import Truncator
from django.db import models



# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import Truncator
import datetime

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='topics')
    Publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='topics')

    def __str__(self):
        return self.subject


class Blog(models.Model):
    Blog_Text = models.TextField()
    title = models.CharField(max_length=200,blank=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name='posts')
    #created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts',null=True,default="BodhiAI")
    #updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='+')
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)
    def __str__(self):
        truncated_title = Truncator(self.title)
        return truncated_title.chars(100)

class Comment(models.Model):

    user= models.ForeignKey(User,on_delete=models.CASCADE)

    comment= models.CharField(max_length=140, null=False)

    updated= models.DateTimeField(auto_now=True)

    timestamp= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.comment)

class latest(models.Model):
    id = models.AutoField(primary_key=True)
    DRAFT = 'D'
    HIDDEN = 'H'
    PUBLISHED = 'P'
    ENTRY_STATUS = (
        (DRAFT, 'Draft'),
        (HIDDEN, 'Hidden'),
        (PUBLISHED, 'Published'),
    )
    category = models.CharField(max_length=4000, null=True, blank=True)
    topic = models.CharField(null=True, blank=True,max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=ENTRY_STATUS)
    start_publication = models.DateTimeField(null=True, blank=True)
    creater = models.ForeignKey(User,on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True,null=True, blank=True)
    edited_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name="+")
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.topic
"""
    class Meta:
        verbose_name = "latest"
        verbose_name_plural = ""

    def __unicode__(self):
        return self.topic

"""        
