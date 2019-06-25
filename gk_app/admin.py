
from django.contrib import admin

from tinymce.widgets import TinyMCE
from django.db import models

from .models import *
class DateWiseGKAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["GK_Text","title","topic","created_by","updated_at","link1",]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class CategoryWiseGKAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["GK_Text","title","topic","created_by","link1","link2","link3"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
admin.site.register(Date_Category)
admin.site.register(DateWiseGK,DateWiseGKAdmin)
admin.site.register(Topic)
admin.site.register(CategoryWise)
admin.site.register(CategoryWiseGK,CategoryWiseGKAdmin)
admin.site.register(TopicWise)



