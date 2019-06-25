from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import Truncator
import datetime

class Jobs(models.Model):
    jobs_info = models.TextField(max_length=40000)
    job_title = models.CharField(max_length=200,blank=True)
    job_department = models.CharField(max_length=200,blank=True)
    job_location=models.CharField(max_length=200,blank=True)
    notification=models.CharField(max_length=200,blank=True)
    qualification=models.CharField(max_length=200,blank=True)
    syllabus=models.TextField(max_length=40000,blank=True)
    last_date = models.DateTimeField(null=True,blank=True)
    admit_card=models.URLField(null=True, blank=True)
    result=models.URLField(null=True, blank=True)
    #updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='+')
    apply_link= models.URLField(null=True, blank=True)
    more_detail= models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.job_title





















class Location(models.Model):
    name = models.CharField(max_length=30, unique=True)
    #description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location_Category(models.Model):
    subject = models.CharField(max_length=255)
    notification = models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    last_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='topics8')
    Publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='topics8')
    Apply_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.subject


class LoctionWiseJobs(models.Model):
    job_details= models.TextField(max_length=40000)
    title = models.CharField(max_length=200,blank=True)
    topic = models.ForeignKey(Location_Category,on_delete=models.CASCADE, related_name='posts8')
    #created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts8',null=True,default="BodhiAI")
    #updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='+')
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.job_details



class Departments(models.Model):
    name = models.CharField(max_length=30, unique=True)
    #description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department_sub_Category(models.Model):
    subject = models.CharField(max_length=255)
    notification = models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    last_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Departments,on_delete=models.CASCADE, related_name='topics9')
    Publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='topics9')
    Apply_link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.subject


class DepartmentWiseJobs(models.Model):
    jobs_details = models.TextField(max_length=40000)
    title = models.CharField(max_length=200,blank=True)
    topic = models.ForeignKey(Department_sub_Category,on_delete=models.CASCADE, related_name='posts9')
    #created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts9',null=True,default="BodhiAI")
    #updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='+')
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)
    link3 = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.jobs_details


