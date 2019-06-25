
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.template.defaultfilters import slugify
from tinymce.widgets import TinyMCE
from django.db import models

from .models import *
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["Blog_Text","title","topic","created_by","link1","link2","link3"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class latestAdmin(admin.ModelAdmin):
    fieldsets = [
           ("Content", {"fields": ['content','slug','category','title','topic', 'status','creater', 'edited_by','link1','link2','link3']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
            obj.save()
        else:
            obj.edited_by = request.user
        slug_str = "%s %s" % (obj.title.lower(),obj.pk)
        obj.slug = slugify(slug_str)
        obj.save()



    
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(latest,latestAdmin)

