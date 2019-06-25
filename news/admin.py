

from django.contrib import admin

from tinymce.widgets import TinyMCE
from django.db import models

from .models import *
class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["title","title_hindi","news_text","hindi_news","category","source","date","link1","language"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(News,NewsAdmin)