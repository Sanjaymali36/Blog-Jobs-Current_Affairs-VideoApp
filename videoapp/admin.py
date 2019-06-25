from django.contrib import admin

# Register your models here.
# coding: utf-8

from django.contrib import admin
from django.template.defaultfilters import slugify
from tinymce.widgets import TinyMCE
from videoapp.models import *
from django.db import models


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["content","video_category","video_title","video_topic","upload_date","publisher","link1","link2","link3"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}, 
    }

    def save_model(self, request, obj, form, change):
        slug_str = "%s %s" % (obj.pk, obj.video_title.lower())
        obj.slug = slugify(slug_str)
        obj.save()


class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Content", {"fields": ['title', 'summary', 'slug', 'link1']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def save_model(self, request, obj, form, change):
        slug_str = "%s %s" % (obj.pk, obj.title.lower())
        obj.slug = slugify(slug_str)
        obj.save()

    """
    list_display = ['title', 'status', 'summary', 'creation_date', 'last_update', 'created_by', 'edited_by']
    list_filter = ['status',]
    search_fields = ['title', 'content', 'created_by__username']
    date_hierarchy = 'start_publication'
  
    fields = ['title', 'content', 'summary', 'status', 'start_publication']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
            obj.save()
        else:
            obj.edited_by = request.user
        slug_str = "%s %s" % (obj.pk, obj.title.lower())
        obj.slug = slugify(slug_str)
        obj.save()

"""
admin.site.register(Category)
admin.site.register(Video,VideoAdmin)
admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)







