from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import Truncator
import datetime
class News(models.Model):
    news_text = models.TextField(blank=True)
    hindi_news=models.TextField(blank=True)
    title = models.CharField(max_length=200,blank=True)
    title_hindi = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200,blank=True,default="Editorial")
    source = models.CharField(max_length=200, blank=True,default="The Hindu")
    date=models.DateField(default=datetime.date.today,null=True, blank=True)
    link1 = models.URLField(null=True, blank=True)
    language=models.CharField(max_length=200,blank=True,default="English")
    def __str__(self):
        return self.title